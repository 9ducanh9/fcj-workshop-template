---
title : "Create EC2, IAM Role, and S3 Storage"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.3.1. </b> "
---

# Create EC2, IAM Role, and S3 Storage

## Step 1: Launch an EC2 Instance

Create one EC2 instance for the backend.

Recommended MVP configuration:

| Setting | Value |
| --- | --- |
| AMI | Amazon Linux 2023 or Ubuntu 22.04 LTS |
| Instance type | `t3.small` or larger |
| Storage | 8 GB gp3 minimum |
| Inbound SSH | Port `22` from your IP only |
| Inbound HTTPS/WSS | Port `443` from `0.0.0.0/0` |

Do not expose Uvicorn directly to the internet. Uvicorn should listen on `127.0.0.1:8000`, and Nginx should be the public entry point.

## Step 2: Create the Transcript S3 Bucket

Create an S3 bucket for exported TXT transcript files:

```bash
aws s3 mb s3://livecap-transcripts --region us-east-1
```

Recommended bucket settings:

- Block all public access: enabled.
- Server-side encryption: enabled.
- Object prefix for transcript exports: `transcripts/`.

## Step 3: Create the EC2 IAM Role

Create an IAM role such as `livecap-ec2-role` and attach it to the EC2 instance.

Required permissions:

| Permission area | Purpose |
| --- | --- |
| Amazon Transcribe Streaming | Stream microphone audio for speech-to-text |
| Amazon Translate | Translate finalized segments between Vietnamese and English |
| Amazon S3 | Upload transcript TXT files and generate pre-signed URLs |
| Amazon CloudWatch Logs | Write structured backend logs |

Use scoped inline policies where possible. For S3, the backend only needs object access under the transcript prefix:

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

## Validation

- EC2 is running.
- Security group allows SSH only from your IP.
- Security group allows HTTPS/WSS on port `443`.
- S3 bucket is private.
- EC2 has the `livecap-ec2-role` attached.

