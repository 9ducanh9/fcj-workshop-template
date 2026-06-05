---
title : "Tạo EC2, IAM role và S3 storage"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.3.1. </b> "
---

# Tạo EC2, IAM role và S3 storage

## Bước 1: Launch EC2 instance

Tạo một EC2 instance cho backend.

Cấu hình MVP khuyến nghị:

| Cấu hình | Giá trị |
| --- | --- |
| AMI | Amazon Linux 2023 hoặc Ubuntu 22.04 LTS |
| Instance type | `t3.small` hoặc lớn hơn |
| Storage | Tối thiểu 8 GB gp3 |
| Inbound SSH | Port `22` chỉ từ IP của bạn |
| Inbound HTTPS/WSS | Port `443` từ `0.0.0.0/0` |

Không public Uvicorn trực tiếp ra internet. Uvicorn nên listen ở `127.0.0.1:8000`, còn Nginx là public entry point.

## Bước 2: Tạo S3 bucket lưu transcript

Tạo S3 bucket để lưu file TXT transcript export:

```bash
aws s3 mb s3://livecap-transcripts --region us-east-1
```

Cấu hình bucket khuyến nghị:

- Block all public access: bật.
- Server-side encryption: bật.
- Object prefix cho transcript export: `transcripts/`.

## Bước 3: Tạo IAM role cho EC2

Tạo IAM role như `livecap-ec2-role` và gắn vào EC2 instance.

Các quyền cần có:

| Nhóm quyền | Mục đích |
| --- | --- |
| Amazon Transcribe Streaming | Stream microphone audio để speech-to-text |
| Amazon Translate | Dịch finalized segment giữa tiếng Việt và tiếng Anh |
| Amazon S3 | Upload TXT transcript và tạo pre-signed URL |
| Amazon CloudWatch Logs | Ghi structured backend logs |

Nên dùng scoped inline policy nếu có thể. Với S3, backend chỉ cần object access dưới transcript prefix:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject"
      ],
      "Resource": "arn:aws:s3:::livecap-transcripts/transcripts/*"
    }
  ]
}
```

## Kiểm tra

- EC2 đang chạy.
- Security group chỉ cho SSH từ IP của bạn.
- Security group cho HTTPS/WSS ở port `443`.
- S3 bucket private.
- EC2 đã gắn `livecap-ec2-role`.

