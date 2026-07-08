---
title: "Xác minh workflow end-to-end"
date: 2026-07-05
weight: 4
chapter: false
pre: " <b> 5.4.4. </b> "
---

# Xác minh workflow end-to-end

## Luồng trình bày cho reviewer

1. Mở landing page CloudFront và `/api/health`.
2. Vào `/app`, chọn **Start** và cấp quyền microphone.
3. Xác nhận UI chuyển sang Recording và WebSocket session bắt đầu.
4. Nói một câu ngắn bằng tiếng Anh hoặc tiếng Việt.
5. Xác nhận một finalized bilingual row xuất hiện ở hai cột.
6. Kiểm tra heartbeat giữ socket và **Stop** kết thúc sạch.
7. Chọn **Export TXT** và mở temporary download link.

## Gate tự động

| Khu vực | Gate |
| --- | --- |
| Backend | `python -m compileall app` và 204 test |
| Frontend | 11 test và production build |
| Terraform | format, `init -backend=false` và validate |
| Secret | Gitleaks scan toàn history |
| Container | health check và smoke test local |
| Dependency | production npm audit và review ECR scan |

GitHub Actions chạy Backend, Frontend, Terraform và Secret scan trên pull
request và push vào main. CI không deploy, apply Terraform hoặc migrate state.

![Các verification job đã pass trên GitHub Actions](/images/3-Project/github-actions-ci.png)

## Bằng chứng production đã xác minh

Ngày 2026-07-07, target custom VPC đã pass CloudFront health, WebSocket
`session_start`/`pong`, transcription PCM 16 kHz, dịch Anh-Việt, stop sạch,
S3 export và presigned TXT download. WAF chặn probe XSS và Log4J với HTTP 403.

![Health, WebSocket và WAF production](/images/5-Workshop/livecap-runtime-security-verification.png)

Controlled scale test đưa ECS target từ `1 -> 0`, gọi `/api/wake`, nhận
`202 waking`, sau đó task trở lại `1/1` và health 200. Automatic idle scale-down
vẫn tắt; vì vậy bằng chứng này chỉ xác nhận controlled `0 -> 1` wake flow.

![Scale-to-zero và wake flow đã xác minh](/images/5-Workshop/livecap-scale-zero-wake-verification.png)

## Trường hợp lỗi mong đợi

- Từ chối microphone tạo lỗi rõ ràng trên UI.
- Vượt session limit trả `TOO_MANY_SESSIONS` trước khi mở AWS stream.
- Disconnect bất ngờ chỉ retry ba lần rồi dừng capture.
- Timeout tự kết thúc session ở 30 phút.
- ALB không gửi traffic đến ECS target unhealthy.
