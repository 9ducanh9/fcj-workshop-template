---
title : "Điều phối và kiểm tra workflow đầy đủ"
date : 2026-05-12
weight : 4
chapter : false
pre : " <b> 5.4.4. </b> "
---

# Điều phối và kiểm tra workflow đầy đủ

## Step Functions state machine

Tạo state machine điều phối các bước xử lý. Phiên bản bootcamp đơn giản có thể gồm các state:

1. `MarkAnalyzing`
2. `AnalyzeTranscript`
3. `SaveResult`
4. `MarkCompleted`
5. `HandleFailure`

Nếu triển khai audio input, thêm:

1. `StartTranscription`
2. `WaitForTranscription`
3. `CheckTranscriptionStatus`

## Luồng transcript tối thiểu

Để demo cuối ổn định, luồng transcript là đủ:

```text
Uploaded transcript -> Step Functions -> Lambda -> Bedrock -> S3 report -> DynamoDB status
```

## Test case 1: Phân tích transcript thành công

Input:

```json
{
  "jobId": "job-test-001",
  "bucket": "<bucket-name>",
  "transcriptKey": "uploads/job-test-001/sample_conversation.txt"
}
```

Kết quả kỳ vọng:

- Step Functions execution thành công.
- DynamoDB status chuyển thành `COMPLETED`.
- Report nằm tại `reports/job-test-001/report.json`.
- CloudWatch logs không có unhandled exception.

## Test case 2: Thiếu transcript

Input trỏ tới transcript key không tồn tại.

Kết quả kỳ vọng:

- Workflow chuyển sang xử lý lỗi.
- DynamoDB status thành `FAILED`.
- `errorMessage` giải thích S3 object bị thiếu.
- CloudWatch logs có chi tiết lỗi.

## Test case 3: Lỗi quyền Bedrock

Tạm dùng model ID chưa được bật, hoặc bỏ quyền Bedrock khỏi role test.

Kết quả kỳ vọng:

- Lambda bắt được lỗi access.
- Workflow fail có kiểm soát.
- Lỗi hiển thị trong CloudWatch và DynamoDB.

## Checklist validation cuối

- Upload path hoạt động.
- Truy xuất được trạng thái job.
- Output Bedrock đúng cấu trúc report.
- Có log.
- Failure case quan sát được.
- Cleanup được tài liệu hóa.
