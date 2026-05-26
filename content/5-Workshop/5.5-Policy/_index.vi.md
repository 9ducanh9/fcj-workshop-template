---
title : "Bảo mật, monitoring, kiểm thử và tối ưu chi phí"
date : 2026-05-12
weight : 5
chapter : false
pre : " <b> 5.5. </b> "
---

# Bảo mật, monitoring, kiểm thử và tối ưu chi phí

## Cân nhắc bảo mật

### Quyền riêng tư dữ liệu

- Chỉ upload hội thoại được phép xử lý.
- Không dùng hội thoại bí mật của công ty, khách hàng hoặc cá nhân để demo.
- Giữ toàn bộ S3 bucket ở trạng thái private.
- Dùng pre-signed URL để upload thay vì public write access.
- Áp dụng lifecycle deletion cho dữ liệu demo.

### IAM least privilege

Dùng quyền được giới hạn:

- Lambda chỉ đọc/ghi S3 bucket của dự án.
- Lambda chỉ update table `CognitiveCoachJobs`.
- Lambda chỉ invoke Bedrock model cần dùng.
- Step Functions chỉ invoke các Lambda trong workflow.
- Transcribe chỉ ghi vào S3 output prefix đã chọn.

### Ranh giới an toàn AI

Hệ thống cần nói rõ rằng output AI là feedback coaching, không phải sự thật tuyệt đối. Người dùng phải tự đánh giá lại gợi ý.

## Monitoring và logging

Dùng CloudWatch để theo dõi:

- Lambda invocation error.
- Lambda duration và timeout.
- Step Functions failed execution.
- Bedrock invocation error.
- Transcribe job failure.

Screenshot nên có:

- CloudWatch log group của analysis Lambda.
- Step Functions execution history.
- DynamoDB item trước và sau khi hoàn thành.

## Kiểm thử và validation

| Test | Kết quả kỳ vọng |
| --- | --- |
| Upload transcript | Object xuất hiện trong S3 `uploads/` |
| Start job | DynamoDB item chuyển sang `UPLOADED` hoặc `ANALYZING` |
| Analyze transcript | Bedrock trả về report có cấu trúc |
| Save report | S3 có `reports/<jobId>/report.json` |
| Retrieve result | API trả về status và report |
| Thiếu file | Job status thành `FAILED` với error message |
| Lỗi quyền Bedrock | Lỗi xuất hiện trong CloudWatch và job fail an toàn |

## Tối ưu chi phí

- Dùng audio ngắn khi test.
- Ưu tiên transcript input trong quá trình phát triển lặp lại.
- Giữ prompt ngắn gọn để giảm token Bedrock.
- Dùng DynamoDB on-demand cho traffic thấp.
- Xóa S3 object sau demo.
- Xóa Lambda version, API, state machine, log group và table không còn dùng.

## Nhận thức về khả năng mở rộng

Kiến trúc này mở rộng tốt hơn một server đơn vì:

- S3 xử lý object storage độc lập.
- Lambda scale theo request.
- Step Functions theo dõi từng job execution.
- DynamoDB hỗ trợ request volume cao nếu thiết kế key phù hợp.

Tuy nhiên, phiên bản bootcamp này chưa có đầy đủ tính năng production như quota đa người dùng, authentication nâng cao, phát hiện PII hoặc model evaluation pipeline.
