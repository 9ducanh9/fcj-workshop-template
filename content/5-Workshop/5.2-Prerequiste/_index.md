---
title: "Prerequisites"
date: 2026-05-12
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

# Prerequisites

## Required Tools

| Tool | Recommended version | Purpose |
| --- | --- | --- |
| Python | 3.11 or later | Run the FastAPI backend |
| Node.js | 18 LTS or later | Build the React + Vite frontend |
| npm | 9 or later | Install frontend dependencies |
| AWS CLI | v2 | Create and verify AWS resources |
| Git | Latest stable | Clone and update source code |
| Nginx | OS package version | Reverse proxy and WSS forwarding on EC2 |

## AWS Account Requirements

The AWS account needs access to:

- Amazon EC2
- Amazon S3
- Amazon CloudFront
- AWS IAM
- Amazon Transcribe Streaming
- Amazon Translate
- Amazon CloudWatch Logs

Use one AWS Region consistently for backend integrations. The LiveCap reference configuration uses `us-east-1` for Transcribe, Translate, S3, and CloudWatch.

## Backend Environment Variables

Copy `backend/.env.example` to `backend/.env` and configure these values:

| Variable | Example | Purpose |
| --- | --- | --- |
| `AWS_REGION` | `us-east-1` | Region for AWS service calls |
| `S3_BUCKET` | `livecap-transcripts` | Bucket for exported TXT transcripts |
| `DOWNLOAD_LINK_EXPIRATION` | `86400` | Pre-signed URL lifetime in seconds |
| `SESSION_TIMEOUT` | `1800` | Maximum streaming session duration |
| `MAX_SPEAKERS` | `5` | Speaker diarization limit |
| `TRANSCRIBE_LANGUAGE_CODE` | `vi-VN` | Fallback fixed Transcribe language |
| `BILINGUAL_DUAL_STREAM` | `true` | Enable Vietnamese-English bilingual mode |
| `ALLOWED_ORIGIN` | CloudFront URL | Frontend origin allowed by CORS |
| `CLOUDWATCH_LOG_GROUP` | `livecap` | Log group for structured backend logs |

Do not store `AWS_ACCESS_KEY_ID` or `AWS_SECRET_ACCESS_KEY` in `.env` on EC2. Use an EC2 IAM role instead.

## Frontend Environment Variables

Set these values before building the frontend:

| Variable | Example | Purpose |
| --- | --- | --- |
| `VITE_WS_URL` | `wss://your-ec2-domain/ws/transcribe` | Secure WebSocket endpoint |
| `VITE_API_BASE_URL` | `https://your-ec2-domain` | REST API base URL |

## Assumptions

- The backend runs on one EC2 instance for the MVP.
- The frontend is hosted as static files on S3 and served through CloudFront.
- TLS is required in production because browser microphone and WSS usage require a secure context.
- The user has permission to process any audio used during testing.

