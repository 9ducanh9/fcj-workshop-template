---
title : "Build and Deploy the Frontend"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.4.1. </b> "
---

# Build and Deploy the Frontend

## Step 1: Build the React App

From the frontend directory:

```bash
cd livecap/frontend
npm install

VITE_WS_URL=wss://your-ec2-domain/ws/transcribe \
VITE_API_BASE_URL=https://your-ec2-domain \
npm run build
```

The output is generated in `frontend/dist/`.

## Step 2: Create a Frontend S3 Bucket

```bash
aws s3 mb s3://livecap-frontend --region us-east-1
```

Keep public access blocked. CloudFront should access the bucket through Origin Access Control.

## Step 3: Upload the Static Build

Upload long-lived assets with immutable cache headers:

```bash
aws s3 sync frontend/dist/ s3://livecap-frontend/ \
  --delete \
  --cache-control "max-age=31536000,immutable" \
  --exclude "index.html"
```

Upload `index.html` separately with no-cache:

```bash
aws s3 cp frontend/dist/index.html s3://livecap-frontend/index.html \
  --cache-control "no-cache,no-store,must-revalidate"
```

## Step 4: Create a CloudFront Distribution

Recommended settings:

- Origin: the frontend S3 bucket.
- Origin access: Origin Access Control.
- Viewer protocol policy: Redirect HTTP to HTTPS.
- Default root object: `index.html`.
- Custom error response: `403` to `/index.html` with response code `200` for client-side routing.

After the distribution status becomes `Deployed`, record the CloudFront domain and set backend `ALLOWED_ORIGIN` to that URL.

