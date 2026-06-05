---
title: "Điều kiện tiên quyết"
date: 2026-05-12
weight: 2
chapter: false
pre: " <b> 5.2. </b> "
---

# Điều kiện tiên quyết

## Công cụ cần có

| Công cụ | Phiên bản khuyến nghị | Mục đích |
| --- | --- | --- |
| Python | 3.11 trở lên | Chạy FastAPI backend |
| Node.js | 18 LTS trở lên | Build React + Vite frontend |
| npm | 9 trở lên | Cài frontend dependencies |
| AWS CLI | v2 | Tạo và kiểm tra AWS resources |
| Git | Bản ổn định mới | Clone và cập nhật source code |
| Nginx | Theo package của OS | Reverse proxy và forward WSS trên EC2 |

## Yêu cầu tài khoản AWS

Tài khoản AWS cần quyền sử dụng:

- Amazon EC2
- Amazon S3
- Amazon CloudFront
- AWS IAM
- Amazon Transcribe Streaming
- Amazon Translate
- Amazon CloudWatch Logs

Dùng nhất quán một AWS Region cho các tích hợp backend. Cấu hình tham chiếu của LiveCap dùng `us-east-1` cho Transcribe, Translate, S3 và CloudWatch.

## Biến môi trường backend

Copy `backend/.env.example` thành `backend/.env` và cấu hình các giá trị:

| Biến | Ví dụ | Mục đích |
| --- | --- | --- |
| `AWS_REGION` | `us-east-1` | Region cho AWS service call |
| `S3_BUCKET` | `livecap-transcripts` | Bucket lưu TXT transcript export |
| `DOWNLOAD_LINK_EXPIRATION` | `86400` | Thời hạn pre-signed URL theo giây |
| `SESSION_TIMEOUT` | `1800` | Thời lượng tối đa của streaming session |
| `MAX_SPEAKERS` | `5` | Giới hạn speaker diarization |
| `TRANSCRIBE_LANGUAGE_CODE` | `vi-VN` | Ngôn ngữ fallback cho Transcribe |
| `BILINGUAL_DUAL_STREAM` | `true` | Bật chế độ song ngữ Việt-Anh |
| `ALLOWED_ORIGIN` | CloudFront URL | Frontend origin được CORS cho phép |
| `CLOUDWATCH_LOG_GROUP` | `livecap` | Log group cho structured backend logs |

Không lưu `AWS_ACCESS_KEY_ID` hoặc `AWS_SECRET_ACCESS_KEY` trong `.env` trên EC2. Hãy dùng IAM role gắn với EC2.

## Biến môi trường frontend

Set các giá trị này trước khi build frontend:

| Biến | Ví dụ | Mục đích |
| --- | --- | --- |
| `VITE_WS_URL` | `wss://your-ec2-domain/ws/transcribe` | Secure WebSocket endpoint |
| `VITE_API_BASE_URL` | `https://your-ec2-domain` | REST API base URL |

## Giả định triển khai

- Backend chạy trên một EC2 instance trong MVP.
- Frontend được host dạng static files trên S3 và phân phối qua CloudFront.
- Production cần TLS vì microphone trên browser và WSS yêu cầu secure context.
- Người dùng có quyền xử lý audio được dùng khi kiểm thử.

