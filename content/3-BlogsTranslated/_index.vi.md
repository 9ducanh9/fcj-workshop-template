---
title: "Dự án đã triển khai"
date: 2026-07-05
weight: 3
chapter: false
pre: " <b> 3. </b> "
---

# Dự án đã triển khai

## LiveCap chạy công khai trên AWS

LiveCap đã được triển khai thành công thành một ứng dụng web công khai trên AWS.

- **Ứng dụng:** [https://dpeohr327wt9l.cloudfront.net](https://dpeohr327wt9l.cloudfront.net)
- **Caption dashboard:** [https://dpeohr327wt9l.cloudfront.net/app](https://dpeohr327wt9l.cloudfront.net/app)
- **Health endpoint:** [https://dpeohr327wt9l.cloudfront.net/api/health](https://dpeohr327wt9l.cloudfront.net/api/health)
- **Source repository:** [https://github.com/9ducanh9/livecap](https://github.com/9ducanh9/livecap)

Luồng production đã được xác minh từ browser qua CloudFront, ALB, ECS Fargate,
Amazon Transcribe, Amazon Translate và export transcript vào S3 private. Các
trang sau mô tả sản phẩm, kiến trúc AWS đang deploy và bằng chứng verification.

![Landing page LiveCap](/images/3-Project/livecap-landing.png)
