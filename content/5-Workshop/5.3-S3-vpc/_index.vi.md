---
title : "Tạo nền tảng lưu trữ và job"
date : 2026-05-12
weight : 3
chapter : false
pre : " <b> 5.3. </b> "
---

# Tạo nền tảng lưu trữ và job

Phần này tạo nền tảng cho workflow AI:

- S3 bucket private để lưu file upload và report.
- DynamoDB table để lưu trạng thái job.
- IAM role và policy cho Lambda và Step Functions.

Mục tiêu là giữ data model đơn giản và dễ kiểm tra trong demo cuối.
