---
title : "Tạo S3 bucket và DynamoDB table"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.3.1. </b> "
---

# Tạo S3 bucket và DynamoDB table

## Bước 1: Tạo S3 bucket

Tạo một bucket private cho dự án.

Tên bucket gợi ý:

```text
cognitive-coach-<your-name>-<account-id>
```

Prefix gợi ý:

```text
uploads/
transcripts/
reports/
```

Cấu hình:

- Block all public access: bật.
- Bucket versioning: tùy chọn cho demo bootcamp.
- Server-side encryption: bật SSE-S3.
- Lifecycle rule: xóa object trong `uploads/`, `transcripts/`, `reports/` sau 7 ngày với môi trường demo.

## Bước 2: Tạo DynamoDB table

Tạo table tên:

```text
CognitiveCoachJobs
```

Thiết kế table:

| Thuộc tính | Kiểu | Mục đích |
| --- | --- | --- |
| `jobId` | String partition key | Mã job duy nhất |
| `status` | String | `UPLOADED`, `TRANSCRIBING`, `ANALYZING`, `COMPLETED`, hoặc `FAILED` |
| `inputType` | String | `audio` hoặc `text` |
| `inputS3Key` | String | Đường dẫn file upload |
| `reportS3Key` | String | Đường dẫn report cuối |
| `createdAt` | String | ISO timestamp |
| `updatedAt` | String | ISO timestamp |
| `errorMessage` | String | Lý do lỗi nếu có |

Dùng on-demand capacity mode cho dự án bootcamp nhỏ.

## Bước 3: Tạo IAM role

Tạo Lambda execution role có quyền:

- Ghi log vào CloudWatch.
- Đọc và ghi object trong S3 bucket của dự án.
- Đọc và ghi item trong table `CognitiveCoachJobs`.
- Gọi Bedrock model inference.

Tạo Step Functions role có quyền:

- Invoke các Lambda cần thiết.
- Start và kiểm tra Amazon Transcribe job nếu dùng audio input.
- Ghi execution log vào CloudWatch.

Không dùng `AdministratorAccess` cho role của đồ án cuối. Báo cáo cuối nên thể hiện rõ tư duy phân quyền theo nguyên tắc least privilege.

## Kiểm tra

Xác nhận:

- S3 bucket không public.
- Upload được object test vào `uploads/`.
- DynamoDB table tồn tại và có `jobId` là partition key.
- IAM role tồn tại với quyền được giới hạn.
