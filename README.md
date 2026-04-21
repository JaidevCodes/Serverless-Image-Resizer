# 📸 Serverless Image Resizer (AWS Free Tier Project)

## 🚀 Project Overview

The **Serverless Image Resizer** is an event-driven cloud application that automatically resizes images when they are uploaded. It uses AWS serverless services to process and deliver optimized images without managing any servers.

When a user uploads an image, it is automatically resized and stored in a separate bucket. The processed image is then served globally using a CDN for fast access.

---

## 🎯 Key Features

* Automatic image resizing on upload
* Fully serverless architecture
* Scalable and cost-efficient (AWS Free Tier compatible)
* Global image delivery using CDN
* No manual processing required

---

## 🧱 Architecture

```

![Architecture]("architecture.png")
```

---

## 🛠️ Technologies Used

* **Amazon S3** – Storage for input and output images
* **AWS Lambda** – Serverless compute for resizing images
* **Pillow (Python Library)** – Image processing
* **Amazon CloudFront** – Content Delivery Network (CDN)
* **IAM Roles** – Secure permissions management

---

## ⚙️ Workflow

1. User uploads an image to the **S3 Input Bucket**
2. S3 triggers a **Lambda function**
3. Lambda:

   * Downloads the image
   * Resizes it (e.g., 300x300)
   * Optimizes the format
4. Resized image is saved to **S3 Output Bucket**
5. CloudFront serves the image globally

---

# 🧩 Why We Use a Lambda Layer (Pillow)

AWS Lambda provides a **minimal runtime environment** and does **not include image processing libraries** like Pillow by default.

Since this project requires:

* Image resizing
* Image format conversion
* Image optimization

👉 We must include an external library (**Pillow**).

### ✅ Why Lambda Layer?

* Keeps Lambda deployment package small
* Reusable across multiple functions
* Cleaner architecture
* Follows AWS best practices

---

# ⚠️ Important Note

Pillow contains compiled components (`_imaging`) which must match:

* **Linux environment (Amazon Linux)**
* **Correct Python runtime (3.10 in this project)**

👉 That’s why we use **CloudShell** to build the layer.

---

# 🚀 Create Pillow Layer Using CloudShell (Recommended)

## Step 1: Open CloudShell

Go to AWS Console → Click **CloudShell (>_)**

---

## Step 2: Run Commands

```bash
# Clean setup
rm -rf pillow-layer
mkdir pillow-layer
cd pillow-layer
mkdir python

# Install Pillow compatible with Lambda (Python 3.10)
pip3 install pillow --platform manylinux2014_x86_64 \
--target=python/ \
--implementation cp \
--python-version 3.10 \
--only-binary=:all: \
--upgrade

# Zip the layer
zip -r pillow-layer.zip python
```

---

## Step 3: Download ZIP

* Click **Actions → Download file**
* Enter:

```bash
pillow-layer.zip
```

---

## Step 4: Upload Layer to AWS Lambda

1. Go to Lambda → **Layers → Create layer**
2. Name: `pillow-layer`
3. Upload: `pillow-layer.zip`
4. Runtime: Python 3.10
5. Create

---

## Step 5: Attach Layer to Function

* Open Lambda function
* Scroll → Layers
* Remove old layer (if any)
* Add `pillow-layer`

---

# 🧪 Example

### Input:

```
Stack_Output.png (79.3 KB)
```

### Output:

```
resized-Stack_Output.png (10.8 KB)
```

👉 Significant size reduction improves performance.

---

## 🔗 Sample Output (CloudFront URL)

```
https://<your-cloudfront-domain>/resized-image.png
```

---

## 🔐 Security

* S3 buckets are **not public**
* Access is restricted via **CloudFront Origin Access Control (OAC)**
* IAM roles follow least privilege principle

---

## 💡 Use Cases

* Social media apps (profile pictures)
* E-commerce platforms (product thumbnails)
* Portfolio websites (image optimization)
* Blogging platforms (faster load times)

---

## 📈 Advantages

* No server management
* Automatically scales with usage
* Low cost (pay-per-use)
* Faster content delivery worldwide

---

## 🔥 Future Enhancements

* Multiple image sizes (thumbnail, medium, large)
* Convert images to WebP format
* Add watermarking
* API-based upload using API Gateway
* Frontend UI for uploading images
* Logging and monitoring with CloudWatch

---

## 🎓 Learning Outcomes

* Understanding of serverless architecture
* Hands-on experience with AWS services
* Event-driven system design
* CDN integration for performance optimization

---

## 🏁 Conclusion

This project demonstrates how modern cloud applications can be built using serverless technologies. It showcases scalability, automation, and performance optimization using AWS services.

---

## 👨‍💻 Author

**Jai Dev**
B.Tech CSE | Cloud Computing Enthusiast | Cloud Engineering | DevOps

---

