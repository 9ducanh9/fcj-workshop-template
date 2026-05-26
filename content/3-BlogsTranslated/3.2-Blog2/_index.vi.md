---
title: "Blog 2: Thiết kế workflow AI serverless với Step Functions"
date: 2026-05-12
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# Blog 2: Thiết kế workflow AI serverless với Step Functions

## Vì sao cần điều phối workflow

Cognitive Communication Coach có nhiều bước xử lý. Người dùng upload file, hệ thống có thể transcribe audio, sau đó Bedrock phân tích transcript, cuối cùng kết quả được lưu để truy xuất.

Nếu toàn bộ logic nằm trong một Lambda lớn, việc debug sẽ khó. AWS Step Functions giúp workflow hiển thị rõ và dễ giải thích hơn.

## Các bước workflow

1. Kiểm tra file hoặc transcript đầu vào.
2. Bắt đầu transcription nếu đầu vào là audio.
3. Chờ kết quả transcription.
4. Gửi transcript đến Bedrock.
5. Lưu báo cáo coaching có cấu trúc.
6. Cập nhật trạng thái job trong DynamoDB.

## Vì sao không dùng một Lambda duy nhất?

Một Lambda duy nhất ban đầu có vẻ đơn giản, nhưng có nhiều vấn đề:

- Khó biết bước nào bị lỗi.
- Khó retry riêng một bước.
- Khó giải thích trạng thái xử lý cho người dùng.
- Có nguy cơ timeout nếu transcription và AI analysis mất nhiều thời gian.

Step Functions tách workflow thành các state rõ ràng và có execution history.

## Thiết kế AWS thực tế

Dự án dùng Lambda cho tác vụ nhỏ và Step Functions để điều phối. Đây là cách thiết kế serverless hợp lý: function ngắn xử lý từng đơn vị công việc, còn dịch vụ workflow managed điều phối toàn bộ tiến trình.

## Bài học chính

Kiến trúc cloud tốt không chỉ làm cho dịch vụ chạy được. Nó còn giúp hệ thống dễ hiểu, dễ quan sát và có khả năng phục hồi khi lỗi xảy ra.
