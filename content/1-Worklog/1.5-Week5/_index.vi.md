---
title: "Nhật ký tuần 5"
date: 2026-05-12
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

# Nhật ký tuần 5

## Công việc đã thực hiện

- Tìm hiểu Lambda event handling và cách dùng Python SDK `boto3`.
- Thiết kế các backend function để tạo upload URL, bắt đầu job phân tích và lấy kết quả.
- Tìm hiểu DynamoDB partition key và thiết kế item để theo dõi trạng thái job.

## Kết quả đạt được

- Chọn `jobId` làm partition key cho DynamoDB.
- Định nghĩa trạng thái job: `UPLOADED`, `TRANSCRIBING`, `ANALYZING`, `COMPLETED`, `FAILED`.
- Thiết kế API đơn giản gồm `/upload-url`, `/jobs`, và `/jobs/{jobId}`.

## Bài học

- DynamoDB hiệu quả khi access pattern đơn giản và được biết trước.
- API cần trả về trạng thái rõ ràng để người dùng hiểu quá trình xử lý bất đồng bộ.
