---
title: "Sản phẩm và trải nghiệm người dùng"
date: 2026-07-05
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Sản phẩm và trải nghiệm người dùng

## Landing page

Route `/` giới thiệu LiveCap theo phong cách dark SaaS. GSAP ScrollTrigger tạo
animation cho product story, caption sequence và kiến trúc đơn giản. Các hiệu
ứng nặng được tách khỏi dashboard live.

![Landing page LiveCap được phục vụ qua CloudFront](/images/3-Project/livecap-landing.png)

## Caption dashboard

Route `/app` ưu tiên vận hành realtime ổn định, gồm:

- control Start, Stop, Export TXT và Clear;
- connection state và countdown session 30 phút;
- chọn microphone;
- hai cột original/translated finalized text;
- speaker label và timestamp;
- trạng thái reconnect/error; và
- layout responsive desktop/mobile.

![Dashboard LiveCap có caption song ngữ finalized](/images/3-Project/livecap-dashboard.png)

Chỉ finalized transcript segment được append. Partial text không làm bẩn
transcript export. Ảnh dashboard được chụp khi microphone WAV kiểm soát được đi
qua luồng production WebSocket, Transcribe và Translate.

## Luồng người dùng

1. Mở CloudFront URL và vào `/app`.
2. Chọn **Start** và cấp quyền microphone.
3. Chờ WebSocket session chuyển sang Recording.
4. Nói tiếng Việt hoặc tiếng Anh.
5. Đọc finalized bilingual row.
6. Chọn **Stop**, sau đó **Export TXT** nếu cần transcript.
