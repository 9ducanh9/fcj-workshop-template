---
title : "Tổng quan workshop"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

# Tổng quan workshop

## Use case

Cognitive Communication Coach giúp người dùng xem lại hội thoại sau khi cuộc trò chuyện kết thúc. Người dùng upload transcript hoặc file audio ngắn. Hệ thống phân tích nội dung và trả về báo cáo coaching có cấu trúc:

- Tóm tắt hội thoại.
- Chủ đề và mục tiêu chính.
- Điểm lập luận yếu hoặc câu trả lời chưa rõ.
- Gợi ý phản hồi mạnh hơn theo cấu trúc claim, reason, evidence và example.
- Năm câu hỏi "tại sao" để luyện tập.
- Ghi chú học tập bằng tiếng Anh và tiếng Việt.

## Sơ đồ kiến trúc

{{< mermaid align="left" >}}
flowchart LR
  User["Người dùng / học viên"] --> Client["Browser hoặc API client"]
  Client --> APIGW["Amazon API Gateway"]
  APIGW --> UploadFn["Lambda: tạo upload URL"]
  APIGW --> ResultFn["Lambda: lấy kết quả"]
  UploadFn --> S3["S3 private bucket"]
  S3 --> Workflow["Step Functions"]
  Workflow --> Transcribe["Amazon Transcribe"]
  Workflow --> AnalyzeFn["Lambda: gọi Bedrock"]
  AnalyzeFn --> Bedrock["Amazon Bedrock"]
  Workflow --> DDB["DynamoDB job table"]
  ResultFn --> DDB
  Workflow --> Logs["CloudWatch Logs"]
{{< /mermaid >}}

## Dịch vụ AWS sử dụng

| Dịch vụ | Trách nhiệm |
| --- | --- |
| Amazon S3 | Lưu audio/transcript upload và report tạo ra |
| Amazon API Gateway | Cung cấp REST API endpoint |
| AWS Lambda | Chạy logic backend và tích hợp Bedrock |
| AWS Step Functions | Điều phối xử lý bất đồng bộ |
| Amazon Transcribe | Chuyển audio thành văn bản |
| Amazon Bedrock | Tạo phản hồi coaching có cấu trúc |
| Amazon DynamoDB | Lưu metadata và trạng thái job |
| Amazon CloudWatch | Lưu log và hỗ trợ troubleshooting |
| AWS IAM | Áp dụng least-privilege access |

## Vì sao chọn kiến trúc này

Workflow xử lý bất đồng bộ vì transcription và AI analysis có thể mất thời gian. Cách này tránh tuyên bố hệ thống là trợ lý thời gian thực. Step Functions giúp từng bước xử lý dễ quan sát, DynamoDB giúp truy vấn trạng thái job, và S3 cung cấp lưu trữ bền vững với chi phí thấp.

## Screenshot cần chụp

Sau khi triển khai, cần chụp:

- S3 bucket có các prefix `uploads/`, `transcripts/`, `reports/`.
- DynamoDB job item có trạng thái cập nhật.
- Step Functions execution graph.
- CloudWatch log stream của Lambda.
- Output báo cáo coaching cuối cùng.
