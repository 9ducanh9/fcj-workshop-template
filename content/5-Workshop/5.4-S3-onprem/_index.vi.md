---
title: "Triển khai frontend và tích hợp AWS"
date: 2026-05-12
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

# Triển khai frontend và tích hợp AWS

Phần này kết nối toàn bộ ứng dụng LiveCap:

1. Build React + TypeScript frontend.
2. Host static frontend trong S3.
3. Phân phối frontend qua CloudFront.
4. Stream audio đến Amazon Transcribe Streaming.
5. Dịch finalized segment bằng Amazon Translate.
6. Export transcript lên S3 và trả về pre-signed link.

Yêu cầu kỹ thuật quan trọng nhất là secure WebSocket streaming. Trong production, browser phải kết nối backend qua `wss://`, không dùng `ws://`.

