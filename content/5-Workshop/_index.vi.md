---
title: "Workshop kỹ thuật"
date: 2026-05-12
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# Workshop kỹ thuật

## LiveCap: Phụ đề và dịch song ngữ thời gian thực trên AWS

LiveCap là một ứng dụng web tạo phụ đề và dịch song ngữ theo thời gian thực. Ứng dụng thu âm từ microphone trong trình duyệt, stream audio đến backend FastAPI qua WebSocket, dùng Amazon Transcribe Streaming để tạo phụ đề, dùng Amazon Translate để dịch Việt-Anh, và hiển thị phụ đề song ngữ theo hai cột.

Dự án phù hợp cho workshop, lớp học, sự kiện cộng đồng và buổi họp có người tham gia nói tiếng Việt hoặc tiếng Anh. Hệ thống cũng hỗ trợ export transcript dạng TXT, lưu vào Amazon S3 và trả về download link có thời hạn.

## Các phần trong workshop

1. Tổng quan workshop và kiến trúc.
2. Điều kiện tiên quyết.
3. Nền tảng backend trên Amazon EC2.
4. Triển khai frontend và tích hợp dịch vụ AWS.
5. Bảo mật, giám sát, kiểm thử và tối ưu chi phí.
6. Cleanup.

