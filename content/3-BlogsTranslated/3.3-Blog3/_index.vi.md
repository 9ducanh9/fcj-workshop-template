---
title: "Bằng chứng xác minh production"
date: 2026-07-05
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Bằng chứng xác minh production

## Quality gate tự động

GitHub Actions trên main đã hoàn tất thành công với bốn job độc lập:

- Secret scan bằng Gitleaks;
- compile backend và 204 pytest test;
- frontend test và production build; và
- Terraform format, init không dùng backend thật và validate.

![GitHub Actions LiveCap đã chạy thành công](/images/3-Project/github-actions-ci.png)

CI chỉ làm nhiệm vụ validation. CI không deploy, chạy `terraform apply`, destroy
tài nguyên hoặc migrate state.

## Production smoke test

Baseline production đã được xác minh ngày 2026-07-04:

1. CloudFront `/` và `/app` trả response thành công.
2. `/api/health` trả trạng thái healthy.
3. WebSocket session start và ping/pong pass.
4. PCM 16 kHz thật tạo finalized English text.
5. Amazon Translate trả Vietnamese text.
6. Session stop cleanup worker và registry state.
7. Export lưu TXT trong S3 private và trả presigned link hoạt động.
8. Layout desktop và mobile 390 px đã được kiểm tra.

## Bằng chứng UI

Dashboard dưới đây chứa finalized bilingual row tạo qua luồng AWS đã deploy,
không phải sample text hard-code.

![Bằng chứng caption dashboard production](/images/3-Project/livecap-dashboard.png)

## Giới hạn đã biết

- WAF, Fargate private, wake Lambda và scale-to-zero nằm trong Terraform target
  đã review nhưng chưa deploy.
- Live service có một task nên quá trình thay task làm gián đoạn session active.
- CloudFront hiện dùng HTTP đến ALB origin; viewer traffic vẫn là HTTPS/WSS.
