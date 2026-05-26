---
title: "Nhật ký tuần 8"
date: 2026-05-12
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

# Nhật ký tuần 8

## Công việc đã thực hiện

- Tìm hiểu AWS Step Functions để điều phối workflow.
- Thiết kế luồng bất đồng bộ: tạo job, transcribe nếu cần, phân tích transcript, lưu kết quả, cập nhật trạng thái.
- Xem các mẫu retry và error handling.

## Kết quả đạt được

- Thêm Step Functions để quan sát vòng đời xử lý.
- Định nghĩa lỗi có thể retry và lỗi không nên retry.
- Lên kế hoạch log CloudWatch cho Lambda và Step Functions execution.

## Bài học

- Orchestration giúp hệ thống serverless phức tạp dễ debug và dễ giải thích hơn.
- Execution history hữu ích cho cả phát triển và demo đồ án cuối.
