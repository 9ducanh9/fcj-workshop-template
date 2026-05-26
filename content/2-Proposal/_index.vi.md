---
title: "Đề xuất dự án"
date: 2026-05-12
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Đề xuất dự án

## Tên dự án

**Cognitive Communication Coach: Hệ thống AI phản tư hội thoại trên AWS**

## 1. Tổng quan dự án

Dự án là một hệ thống huấn luyện giao tiếp song ngữ, dùng AI để phân tích một đoạn ghi âm hoặc bản ghi hội thoại sau khi cuộc trò chuyện kết thúc. Hệ thống tạo báo cáo gồm tóm tắt nội dung, mục tiêu trao đổi, điểm yếu trong lập luận, gợi ý phản hồi tốt hơn và câu hỏi luyện tập.

Hệ thống không nhằm mục đích trả lời thay người dùng trong hội thoại trực tiếp. Thay vào đó, hệ thống giúp người dùng nhìn lại cách giao tiếp của mình, hiểu chỗ lập luận chưa rõ, và luyện tập phản hồi tốt hơn cho lần sau.

## 2. Vấn đề cần giải quyết

Sinh viên, thực tập sinh và nhân sự mới thường gặp khó khăn khi trao đổi dù đã có hiểu biết nhất định về chủ đề. Một số vấn đề thường gặp:

- Khó sắp xếp ý nhanh khi bị áp lực.
- Bị khựng lại khi liên tục bị hỏi "tại sao".
- Trả lời thiếu bằng chứng hoặc ví dụ.
- Chỉ nghĩ ra câu trả lời tốt hơn sau khi buổi trao đổi đã kết thúc.
- Thiếu một quy trình có cấu trúc để tự đánh giá và cải thiện giao tiếp.

Vấn đề không chỉ nằm ở ngoại ngữ, mà còn ở cấu trúc tư duy, sự tự tin và khả năng phản tư.

## 3. Mục tiêu

- Xây dựng một hệ thống thực tế trên AWS, dùng tối thiểu ba dịch vụ AWS.
- Cho phép người dùng tải lên audio ngắn hoặc transcript để phân tích.
- Dùng Amazon Transcribe để chuyển giọng nói thành văn bản khi đầu vào là audio.
- Dùng Amazon Bedrock để tạo báo cáo huấn luyện giao tiếp.
- Lưu trạng thái xử lý và kết quả theo cấu trúc rõ ràng.
- Viết tài liệu triển khai lại được từ đầu đến cuối, bao gồm kiểm thử, giám sát, bảo mật, chi phí và dọn dẹp.
- Giữ phạm vi phù hợp với một học viên bootcamp.

## 4. Kiến trúc giải pháp

{{< mermaid align="left" >}}
flowchart LR
  User["Trình duyệt người dùng"] --> APIGW["Amazon API Gateway"]
  APIGW --> UploadLambda["Lambda: tạo upload URL"]
  UploadLambda --> S3["Amazon S3 private bucket"]
  S3 --> SFN["AWS Step Functions workflow"]
  SFN --> Transcribe["Amazon Transcribe"]
  SFN --> Bedrock["Amazon Bedrock"]
  SFN --> DDB["Amazon DynamoDB"]
  APIGW --> ResultLambda["Lambda: lấy kết quả"]
  ResultLambda --> DDB
  SFN --> CW["Amazon CloudWatch"]
{{< /mermaid >}}

## 5. Dịch vụ AWS sử dụng

| Dịch vụ | Vai trò | Lý do lựa chọn |
| --- | --- | --- |
| Amazon S3 | Lưu audio, transcript và báo cáo sinh ra | Lưu trữ object bền vững, chi phí thấp, hỗ trợ private access |
| AWS Lambda | Tạo upload URL, tạo job, lấy kết quả | Serverless compute phù hợp với tác vụ backend ngắn |
| Amazon API Gateway | Cung cấp REST API cho frontend hoặc test client | Lớp API managed, hỗ trợ xác thực và giới hạn request |
| AWS Step Functions | Điều phối workflow transcription và phân tích AI | Dễ quan sát, retry và debug xử lý bất đồng bộ |
| Amazon Transcribe | Chuyển file hội thoại audio thành văn bản | Dịch vụ speech-to-text managed, không cần tự xây ASR |
| Amazon Bedrock | Sinh phản hồi huấn luyện có cấu trúc | Truy cập foundation model managed, không cần vận hành model |
| Amazon DynamoDB | Lưu metadata job, trạng thái và tham chiếu kết quả | NoSQL serverless phù hợp truy vấn key-value đơn giản |
| Amazon CloudWatch | Lưu log và metric vận hành | Hỗ trợ debug, giám sát và xác thực |
| AWS IAM | Kiểm soát quyền giữa các dịch vụ | Thiết kế least privilege |

## 6. Tiến độ

| Giai đoạn | Thời lượng | Kết quả |
| --- | --- | --- |
| Phân tích yêu cầu | Tuần 1 | Problem statement, user journey, phạm vi dự án |
| Nền tảng AWS | Tuần 2-3 | IAM, S3 bucket, DynamoDB table, Lambda cơ bản |
| Workflow AI | Tuần 4-6 | Luồng Transcribe, prompt Bedrock, Step Functions |
| API và kiểm thử | Tuần 7-8 | API Gateway endpoint, kiểm thử input mẫu |
| Tài liệu | Tuần 9-10 | Workshop step, sơ đồ, screenshot, nội dung song ngữ |
| Tối ưu và bảo vệ | Tuần 11-12 | Review bảo mật, chi phí, cleanup, luyện bảo vệ |

## 7. Nhận thức về chi phí

Dự án được thiết kế cho quy mô bootcamp chi phí thấp:

- Audio test nên giới hạn 3-5 phút.
- Dung lượng S3 thấp vì chỉ dùng file mẫu.
- Lambda và Step Functions chỉ chạy ở mức test.
- Chi phí Bedrock phụ thuộc model và số token, nên prompt cần ngắn gọn.
- Phải cleanup toàn bộ tài nguyên sau demo để tránh phát sinh chi phí.

Báo cáo cuối nên bổ sung ảnh chụp hoặc file estimate từ AWS Pricing Calculator theo region và model thực tế.

## 8. Rủi ro

| Rủi ro | Ảnh hưởng | Cách giảm thiểu |
| --- | --- | --- |
| Transcript không chính xác | Chất lượng báo cáo AI giảm | Dùng audio rõ, hỗ trợ phương án upload transcript |
| Kết quả Bedrock chung chung | Demo kém thuyết phục | Dùng prompt có cấu trúc và rubric cố định |
| Chi phí tăng do gọi AI nhiều | Phát sinh phí ngoài dự kiến | Giới hạn thời lượng file, xóa file test, theo dõi usage |
| Dữ liệu hội thoại nhạy cảm | Rủi ro lộ thông tin | S3 private, IAM least privilege, cleanup, thông báo consent |
| Workflow khó debug | Chậm tiến độ | Dùng execution history của Step Functions và CloudWatch Logs |
| Mở rộng thành trợ lý real-time | Phạm vi vượt quá sức | Giữ MVP ở dạng xử lý sau hội thoại |

## 9. Tiêu chí thành công

- Upload được audio hoặc transcript mẫu.
- Hệ thống tạo job record và lưu trạng thái xử lý.
- Audio được chuyển thành văn bản, hoặc transcript text được nhận trực tiếp.
- Bedrock tạo báo cáo huấn luyện có cấu trúc.
- Người dùng truy xuất và xem được kết quả.
- Có tài liệu về log, lỗi, phân quyền, kiểm soát chi phí và cleanup.
