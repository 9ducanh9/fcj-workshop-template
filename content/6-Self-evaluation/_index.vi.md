---
title: "Tự đánh giá"
date: 2026-05-12
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

# Tự đánh giá

## Kiến thức kỹ thuật

Tôi hiểu rõ hơn về thiết kế ứng dụng cloud thời gian thực, WebSocket communication, triển khai EC2, static hosting bằng S3, phân phối qua CloudFront, thiết kế IAM role, Amazon Transcribe Streaming, Amazon Translate và CloudWatch logging. LiveCap giúp tôi kết nối frontend audio capture, backend streaming và các dịch vụ AI managed của AWS thành một hệ thống thực tế.

## Khả năng học tập

Tôi học cách biến một ý tưởng lấy cảm hứng từ sự kiện thành MVP cụ thể. Thay vì chỉ viết về một trợ lý AI lý thuyết, tôi tập trung vào use case có thể triển khai lại: phụ đề song ngữ thời gian thực cho workshop và cuộc họp. Tôi cũng học cách đọc kỹ giới hạn dịch vụ, đặc biệt là secure WebSocket, quyền microphone trên browser và độ trễ transcription.

## Tinh thần chủ động

Tôi chọn LiveCap vì dự án giải quyết một vấn đề giao tiếp thật mà tôi gặp trong các sự kiện kỹ thuật song ngữ. Tôi xác định user journey, tìm hiểu các dịch vụ AWS cần dùng, xây dựng cấu trúc backend/frontend và viết tài liệu triển khai để người khác có thể làm theo.

## Kỷ luật

Tôi giữ kiến trúc trong phạm vi bootcamp: một EC2 backend, frontend host bằng S3 + CloudFront, và các dịch vụ AWS managed cho transcription, translation, storage và logging. Tôi tránh thêm độ phức tạp production không cần thiết như ECS, Kubernetes, user authentication, multi-room support hoặc AI summarization.

## Giao tiếp

Dự án giúp tôi luyện cách giải thích vì sao dùng từng dịch vụ AWS. Tôi thực hành bảo vệ lựa chọn EC2 cho WebSocket session dài, CloudFront cho HTTPS static delivery, S3 cho transcript storage, IAM role cho an toàn credential và CloudWatch cho khả năng quan sát hệ thống.

## Làm việc nhóm

Tôi học từ mentor FCAJ, AWS Study Group và các sự kiện cộng đồng. Feedback giúp tôi cải thiện tài liệu và tập trung vào bằng chứng triển khai thực tế thay vì chỉ mô tả ý tưởng sản phẩm.

## Giải quyết vấn đề

Thử thách chính là hỗ trợ real-time audio streaming bằng kiến trúc đơn giản nhưng vẫn có thể bảo vệ về mặt kỹ thuật. Tôi giải quyết bằng cách dùng EC2 cho FastAPI WebSocket backend persistent, Nginx cho TLS/WSS forwarding và các dịch vụ AWS managed cho speech-to-text, translation, storage và logging.

## Đóng góp cá nhân

Đóng góp cá nhân của tôi bao gồm:

- Xác định use case LiveCap và phạm vi MVP.
- Thiết kế kiến trúc AWS.
- Triển khai và tài liệu hóa flow backend FastAPI.
- Chuẩn bị hướng triển khai React frontend.
- Tích hợp Amazon Transcribe Streaming, Amazon Translate, S3, CloudFront, EC2, IAM và CloudWatch trong thiết kế workshop.
- Viết tài liệu song ngữ với các bước setup, testing, monitoring, security, cost và cleanup.

## Điểm cần cải thiện

- Bổ sung thêm screenshot AWS từ môi trường deploy cuối.
- Kiểm thử speaker diarization kỹ hơn với audio nhiều người nói và có nhiễu.
- Thêm load testing cho nhiều WebSocket session đồng thời.
- Bổ sung kế hoạch production tương lai với ALB và nhiều backend instances.
- Chỉ cân nhắc authentication nếu dự án mở rộng vượt phạm vi MVP bootcamp.

