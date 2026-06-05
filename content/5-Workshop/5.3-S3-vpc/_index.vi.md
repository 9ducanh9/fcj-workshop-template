---
title: "Nền tảng backend trên EC2"
date: 2026-05-12
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# Nền tảng backend trên EC2

Phần này chuẩn bị nền tảng backend cho LiveCap:

- EC2 instance cho FastAPI backend.
- IAM role để gọi AWS services.
- S3 bucket để lưu transcript.
- Backend dependencies và biến môi trường.
- systemd service và Nginx reverse proxy cho HTTPS/WSS.

Mục tiêu là giữ MVP đơn giản khi vận hành nhưng vẫn dùng dịch vụ AWS thật. Một EC2 instance là đủ cho đồ án bootcamp vì hỗ trợ WebSocket connection dài và dễ debug qua SSH, `systemctl` và logs.

