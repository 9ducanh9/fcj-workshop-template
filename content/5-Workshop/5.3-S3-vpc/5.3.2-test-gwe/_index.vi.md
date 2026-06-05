---
title : "Deploy và kiểm tra FastAPI backend"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.3.2. </b> "
---

# Deploy và kiểm tra FastAPI backend

## Bước 1: Cài backend dependencies

SSH vào EC2 instance và cài runtime dependencies.

```bash
sudo dnf install -y python3.11 python3.11-pip git nginx
git clone https://github.com/your-org/livecap.git
cd livecap/backend
pip3.11 install -r requirements.txt
```

## Bước 2: Cấu hình environment

```bash
cp .env.example .env
nano .env
```

Giá trị production tối thiểu:

```env
AWS_REGION=us-east-1
S3_BUCKET=livecap-transcripts
DOWNLOAD_LINK_EXPIRATION=86400
SESSION_TIMEOUT=1800
MAX_SPEAKERS=5
TRANSCRIBE_LANGUAGE_CODE=vi-VN
BILINGUAL_DUAL_STREAM=true
ALLOWED_ORIGIN=https://your-cloudfront-domain
CLOUDWATCH_LOG_GROUP=livecap
```

## Bước 3: Test backend thủ công

Chạy API thủ công trước:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Gọi health endpoint từ instance:

```bash
curl http://127.0.0.1:8000/api/health
```

Kết quả mong đợi:

- API trả về healthy response.
- Không lưu AWS credential trong `.env`.
- Nếu CloudWatch chưa dùng được khi test local, logging fallback về stdout.

## Bước 4: Chạy bằng systemd

Copy systemd unit có sẵn và enable service:

```bash
sudo cp deploy/livecap.service /etc/systemd/system/livecap.service
sudo systemctl daemon-reload
sudo systemctl enable livecap
sudo systemctl start livecap
sudo systemctl status livecap
```

Xem service logs:

```bash
sudo journalctl -u livecap -f
```

## Bước 5: Cấu hình Nginx cho HTTPS/WSS

Nginx terminate TLS và forward traffic đến Uvicorn.

```bash
sudo cp deploy/nginx.conf /etc/nginx/conf.d/livecap.conf
sudo nginx -t
sudo systemctl reload nginx
```

Sau khi TLS được cấu hình, WebSocket endpoint sẽ có dạng:

```text
wss://your-ec2-domain/ws/transcribe
```

