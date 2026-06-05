---
title : "Build và deploy frontend"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.4.1. </b> "
---

# Build và deploy frontend

## Bước 1: Build React app

Từ thư mục frontend:

```bash
cd livecap/frontend
npm install

VITE_WS_URL=wss://your-ec2-domain/ws/transcribe \
VITE_API_BASE_URL=https://your-ec2-domain \
npm run build
```

Output được tạo trong `frontend/dist/`.

## Bước 2: Tạo S3 bucket cho frontend

```bash
aws s3 mb s3://livecap-frontend --region us-east-1
```

Giữ public access ở trạng thái blocked. CloudFront nên truy cập bucket qua Origin Access Control.

## Bước 3: Upload static build

Upload asset dài hạn với immutable cache headers:

```bash
aws s3 sync frontend/dist/ s3://livecap-frontend/ \
  --delete \
  --cache-control "max-age=31536000,immutable" \
  --exclude "index.html"
```

Upload `index.html` riêng với no-cache:

```bash
aws s3 cp frontend/dist/index.html s3://livecap-frontend/index.html \
  --cache-control "no-cache,no-store,must-revalidate"
```

## Bước 4: Tạo CloudFront distribution

Cấu hình khuyến nghị:

- Origin: frontend S3 bucket.
- Origin access: Origin Access Control.
- Viewer protocol policy: Redirect HTTP to HTTPS.
- Default root object: `index.html`.
- Custom error response: `403` đến `/index.html` với response code `200` cho client-side routing.

Sau khi distribution chuyển sang `Deployed`, ghi lại CloudFront domain và set backend `ALLOWED_ORIGIN` bằng URL đó.

