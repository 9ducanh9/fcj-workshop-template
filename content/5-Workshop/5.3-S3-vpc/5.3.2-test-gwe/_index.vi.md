---
title : "Tạo API upload và lấy kết quả"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.3.2. </b> "
---

# Tạo API upload và lấy kết quả

## Thiết kế API

Tạo REST API đơn giản với các endpoint:

| Method | Path | Mục đích |
| --- | --- | --- |
| `POST` | `/upload-url` | Tạo pre-signed S3 upload URL |
| `POST` | `/jobs` | Tạo processing job sau khi upload |
| `GET` | `/jobs/{jobId}` | Lấy trạng thái và kết quả job |

## Lambda tạo upload URL

Lambda tạo upload URL nên:

1. Nhận file name và input type.
2. Tạo `jobId` duy nhất.
3. Tạo S3 key trong `uploads/`.
4. Trả về pre-signed URL.
5. Có thể insert job item ban đầu vào DynamoDB.

Ví dụ response:

```json
{
  "jobId": "job-20260512-001",
  "uploadUrl": "https://s3-presigned-url-example",
  "s3Key": "uploads/job-20260512-001/sample.txt"
}
```

## Lambda tạo job

Lambda tạo job nên:

1. Kiểm tra object đã upload có tồn tại trong S3.
2. Insert hoặc update DynamoDB item với status `UPLOADED`.
3. Start Step Functions execution.
4. Trả về `jobId` và trạng thái hiện tại.

Ví dụ response:

```json
{
  "jobId": "job-20260512-001",
  "status": "UPLOADED",
  "message": "Processing workflow started"
}
```

## Lambda lấy kết quả

Lambda lấy kết quả nên:

1. Đọc job item từ DynamoDB.
2. Nếu status là `COMPLETED`, trả về vị trí report hoặc nội dung report.
3. Nếu status là `FAILED`, trả về lý do lỗi.
4. Nếu vẫn đang xử lý, trả về trạng thái hiện tại.

## Kiểm tra

Hãy test bằng transcript trước vì tránh biến số từ audio transcription:

```powershell
aws s3 cp sample_conversation.txt s3://<bucket-name>/uploads/job-test/sample_conversation.txt
```

Sau đó tạo DynamoDB test item thủ công hoặc gọi API `/jobs` và xác nhận job xuất hiện trong table.
