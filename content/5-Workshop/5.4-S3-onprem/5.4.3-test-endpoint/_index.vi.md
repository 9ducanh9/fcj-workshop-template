---
title : "Gọi Bedrock từ Lambda"
date : 2026-05-12
weight : 3
chapter : false
pre : " <b> 5.4.3. </b> "
---

# Gọi Bedrock từ Lambda

## Trách nhiệm của Lambda

Analysis Lambda nên:

1. Đọc transcript text từ S3.
2. Tạo coaching prompt.
3. Invoke Amazon Bedrock.
4. Lưu response của model vào `reports/<jobId>/report.json`.
5. Cập nhật trạng thái DynamoDB thành `COMPLETED` hoặc `FAILED`.

## Schema output ví dụ

```json
{
  "summary": "The student explained the project idea but needs stronger evidence.",
  "mainTopic": "Defending an AWS AI communication coach project",
  "strongPoints": ["Clear target problem", "AWS service mapping is relevant"],
  "weakReasoning": ["Needs clearer business value", "Needs privacy explanation"],
  "improvedResponse": {
    "claim": "AWS is suitable because the workload needs managed AI and serverless orchestration.",
    "reason": "The system has upload, transcription, AI analysis, storage, and monitoring stages.",
    "evidence": "S3, Transcribe, Bedrock, Step Functions, DynamoDB, and CloudWatch each support one stage.",
    "example": "A student can upload a transcript and receive a structured coaching report."
  },
  "whyQuestions": [
    "Why is post-conversation analysis safer than live assistance?",
    "Why does this need cloud services?",
    "Why is Bedrock better than hard-coded rules for this use case?",
    "Why should users trust the feedback?",
    "Why is cleanup important?"
  ],
  "vietnameseSummary": "Sinh viên đã giải thích ý tưởng nhưng cần bổ sung giá trị thực tế và bảo mật."
}
```

## Xử lý lỗi

Cần xử lý các lỗi:

- Không tìm thấy transcript object.
- Chưa có quyền truy cập Bedrock model.
- Bedrock throttling hoặc timeout.
- Model output không đúng định dạng.
- Cập nhật DynamoDB thất bại.

## Kiểm tra

Dùng Lambda test console với event mẫu:

```json
{
  "jobId": "job-test",
  "bucket": "<bucket-name>",
  "transcriptKey": "uploads/job-test/sample_conversation.txt"
}
```

Xác nhận report được lưu vào S3 và DynamoDB item được cập nhật.
