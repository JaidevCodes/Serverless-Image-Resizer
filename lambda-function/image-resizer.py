import json
import boto3
from PIL import Image
import io
import urllib.parse

s3 = boto3.client('s3')

OUTPUT_BUCKET = "image-upload-output-jaidev"

def lambda_handler(event, context):
    try:
        # Get bucket and object key
        bucket = event['Records'][0]['s3']['bucket']['name']
        key = urllib.parse.unquote_plus(
            event['Records'][0]['s3']['object']['key']
        )

        print(f"Processing file: {key} from bucket: {bucket}")

        # Get image from S3
        response = s3.get_object(Bucket=bucket, Key=key)
        image_content = response['Body'].read()

        # Open image
        image = Image.open(io.BytesIO(image_content))

        # Resize (keep aspect ratio)
        image.thumbnail((300, 300))

        # Convert to JPEG (optional standardization)
        buffer = io.BytesIO()
        image.convert("RGB").save(buffer, "JPEG")
        buffer.seek(0)

        # Output file name
        output_key = f"resized-{key.split('/')[-1]}"

        # Upload to output bucket
        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=output_key,
            Body=buffer,
            ContentType='image/jpeg'
        )

        print("Image resized and uploaded successfully!")

        return {
            'statusCode': 200,
            'body': json.dumps('Success')
        }

    except Exception as e:
        print("Error:", str(e))
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
