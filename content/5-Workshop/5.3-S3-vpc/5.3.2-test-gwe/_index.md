---
title : "Deploy and Test the FastAPI Backend"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.3.2. </b> "
---

# Deploy and Test the FastAPI Backend

## Step 1: Install Backend Dependencies

SSH into the EC2 instance and install runtime dependencies.

```bash
sudo dnf install -y python3.11 python3.11-pip git nginx
git clone https://github.com/your-org/livecap.git
cd livecap/backend
pip3.11 install -r requirements.txt
```

## Step 2: Configure Environment

```bash
cp .env.example .env
nano .env
```

Minimum production values:

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

## Step 3: Manual Backend Test

Run the API manually first:

```bash
uvicorn app.main:app --host 127.0.0.1 --port 8000
```

Open the health endpoint from the instance:

```bash
curl http://127.0.0.1:8000/api/health
```

Expected result:

- The API returns a healthy response.
- No AWS credential is stored in `.env`.
- If CloudWatch is unavailable during local testing, logging falls back to stdout.

## Step 4: Run with systemd

Copy the provided systemd unit and enable the service:

```bash
sudo cp deploy/livecap.service /etc/systemd/system/livecap.service
sudo systemctl daemon-reload
sudo systemctl enable livecap
sudo systemctl start livecap
sudo systemctl status livecap
```

View service logs:

```bash
sudo journalctl -u livecap -f
```

## Step 5: Configure Nginx for HTTPS/WSS

Nginx terminates TLS and forwards traffic to Uvicorn.

```bash
sudo cp deploy/nginx.conf /etc/nginx/conf.d/livecap.conf
sudo nginx -t
sudo systemctl reload nginx
```

After TLS is configured, the WebSocket endpoint should be available at:

```text
wss://your-ec2-domain/ws/transcribe
```

