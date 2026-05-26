---
title: "Nhật ký tuần 4"
date: 2026-05-12
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

# Nhật ký tuần 4

## Công việc đã thực hiện

- Thiết kế kiến trúc AWS mức cao đầu tiên.
- Mapping hành động người dùng với thành phần AWS: upload, xử lý, phân tích, lưu trữ, truy xuất.
- Tìm hiểu S3 private bucket, pre-signed URL, object prefix và lifecycle cleanup.

## Kết quả đạt được

- Chọn Amazon S3 làm lớp lưu trữ audio, transcript và report.
- Định nghĩa cấu trúc prefix đơn giản: `uploads/`, `transcripts/`, `reports/`.
- Bổ sung yêu cầu bảo mật S3 vào proposal.

## Bài học

- Thiết kế storage phải bao gồm access control và cleanup policy, không chỉ tạo bucket.
- Pre-signed URL hữu ích để upload có kiểm soát mà không cần public bucket.
