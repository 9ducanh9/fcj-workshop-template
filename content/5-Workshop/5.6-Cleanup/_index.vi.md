---
title : "Cleanup"
date : 2026-05-12
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

# Cleanup

Cleanup là bước bắt buộc để tránh phát sinh chi phí AWS không cần thiết sau demo.

## Thứ tự cleanup

1. Dừng hoặc xóa Step Functions execution nếu còn đang chạy.
2. Xóa API Gateway deployment và API.
3. Xóa các Lambda function của dự án.
4. Xóa Amazon Transcribe test job nếu không còn cần.
5. Xóa object trong S3 bucket:
   - `uploads/`
   - `transcripts/`
   - `reports/`
6. Xóa S3 bucket.
7. Xóa DynamoDB table `CognitiveCoachJobs`.
8. Xóa CloudWatch log group được tạo cho Lambda và Step Functions.
9. Xóa IAM role và policy chỉ dùng cho dự án này.
10. Kiểm tra AWS Billing and Cost Management để chắc chắn không còn resource phát sinh phí.

## Kiểm tra sau cleanup

Xác nhận:

- S3 bucket không còn tồn tại.
- DynamoDB table không còn tồn tại.
- API Gateway endpoint không còn phản hồi.
- Lambda function đã bị xóa.
- Step Functions state machine đã bị xóa.
- CloudWatch logs đã xóa nếu không cần làm bằng chứng.
- Không còn resource liên quan đến dự án trong region đã chọn.

Nếu cần screenshot cho báo cáo cuối, hãy chụp trước khi xóa resource.
