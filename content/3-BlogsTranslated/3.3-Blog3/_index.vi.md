---
title: "Blog 3: Bảo mật, quyền riêng tư và chi phí cho dữ liệu hội thoại AI"
date: 2026-05-12
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Blog 3: Bảo mật, quyền riêng tư và chi phí cho dữ liệu hội thoại AI

## Vì sao quan trọng

Dữ liệu hội thoại có thể chứa quan điểm cá nhân, tên người, kế hoạch, thông tin kinh doanh hoặc phản hồi nhạy cảm. Một hệ thống AI coach giao tiếp cần được thiết kế cẩn thận ngay cả khi chỉ là dự án bootcamp.

## Ranh giới quyền riêng tư

Hệ thống nên tuân theo các nguyên tắc:

- Chỉ upload hội thoại mà người dùng có quyền xử lý.
- Giữ S3 bucket ở trạng thái private.
- Dùng pre-signed URL thay vì public upload.
- Xóa audio và report test sau demo.
- Không dùng hội thoại bí mật thật trong quá trình test.

## Ranh giới bảo mật

IAM policy nên theo nguyên tắc least privilege:

- Lambda chỉ được ghi vào các S3 prefix cần thiết.
- Step Functions chỉ được invoke các Lambda cần thiết.
- Quyền Bedrock nên giới hạn theo model đã chọn nếu có thể.
- DynamoDB access chỉ giới hạn ở table của dự án.
- CloudWatch access dùng cho log, không cấp quyền quản trị rộng.

## Ranh giới chi phí

Dịch vụ AI và transcription có thể phát sinh chi phí nếu dùng không kiểm soát. Dự án kiểm soát chi phí bằng cách:

- Giới hạn audio 3-5 phút.
- Test bằng file mẫu nhỏ.
- Viết prompt ngắn gọn.
- Xóa object S3 sau khi test.
- Xóa API, Lambda, Step Functions, DynamoDB và log không còn dùng trong bước cleanup.

## Bài học chính

Kiến trúc AI có trách nhiệm không chỉ nằm ở output của model. Nó còn bao gồm consent, bảo vệ dữ liệu, giới hạn quyền, monitoring và cleanup.
