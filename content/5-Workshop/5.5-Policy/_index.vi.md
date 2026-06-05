---
title: "Bảo mật, giám sát, kiểm thử và tối ưu chi phí"
date: 2026-05-12
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# Bảo mật, giám sát, kiểm thử và tối ưu chi phí

## Cân nhắc bảo mật

- Dùng HTTPS cho frontend thông qua CloudFront.
- Dùng WSS để stream microphone audio đến backend.
- Giữ Uvicorn private ở `127.0.0.1:8000`; chỉ expose Nginx ở port `443`.
- Giới hạn SSH chỉ từ IP cá nhân.
- Gắn IAM role vào EC2 thay vì lưu AWS key trong `.env`.
- Giữ S3 bucket private và dùng CloudFront Origin Access Control cho frontend hosting.
- Scope quyền S3 transcript vào `transcripts/*`.
- Set CORS `ALLOWED_ORIGIN` đúng bằng CloudFront frontend URL.
- Không xử lý hội thoại riêng tư nếu chưa có sự đồng ý.

## Monitoring và logging

LiveCap ghi structured backend logs vào CloudWatch thông qua logging service.

Các event quan trọng cần theo dõi:

- Session start và session end.
- Lỗi WebSocket connection.
- Lỗi Amazon Transcribe Streaming.
- Lỗi Amazon Translate.
- Lỗi upload S3 hoặc tạo pre-signed URL.
- Backend startup và shutdown.

Nếu CloudWatch chưa dùng được trong development, backend fallback về stdout logging để vẫn test local được.

## Checklist kiểm thử

| Khu vực | Cách kiểm tra |
| --- | --- |
| Backend health | `/api/health` trả về success |
| WebSocket | Browser kết nối được qua WSS |
| Audio format | Backend reject audio format sai |
| Transcription | Partial và finalized caption xuất hiện |
| Translation | Cả cột tiếng Việt và tiếng Anh đều có nội dung |
| Export | TXT transcript được upload lên S3 |
| Download | Pre-signed URL hoạt động trước khi hết hạn |
| Monitoring | CloudWatch nhận session và error logs |

## Tối ưu chi phí

- Dùng `t3.small` hoặc EC2 nhỏ cho MVP testing.
- Stop EC2 instance khi không test.
- Xóa transcript export không còn cần trong S3.
- Dùng lifecycle rule cho transcript bucket nếu test thường xuyên.
- Giữ CloudFront cache rule đơn giản.
- Tắt audio pipeline debug log sau khi troubleshooting xong.
- Giới hạn session duration bằng `SESSION_TIMEOUT`.

## Nhận thức về khả năng mở rộng

MVP dùng một EC2 instance để triển khai đơn giản. Cách này phù hợp cho đồ án bootcamp nhưng có giới hạn:

- Một instance giới hạn số WebSocket session đồng thời.
- Phiên bản production sau này nên cân nhắc Application Load Balancer hỗ trợ WSS và nhiều backend instances.
- ECS Fargate có thể được xem xét sau cho managed deployment và horizontal scaling.

