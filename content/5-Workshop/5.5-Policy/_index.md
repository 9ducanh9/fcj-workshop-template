---
title: "Security, Monitoring, Testing, and Cost Optimization"
date: 2026-05-12
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# Security, Monitoring, Testing, and Cost Optimization

## Security Considerations

- Use HTTPS for the frontend through CloudFront.
- Use WSS for microphone audio streaming to the backend.
- Keep Uvicorn private on `127.0.0.1:8000`; expose only Nginx on port `443`.
- Restrict SSH access to your own IP.
- Attach an IAM role to EC2 instead of storing AWS keys in `.env`.
- Keep S3 buckets private and use CloudFront Origin Access Control for frontend hosting.
- Scope transcript S3 permissions to `transcripts/*`.
- Set CORS `ALLOWED_ORIGIN` to the exact CloudFront frontend URL.
- Do not process private conversations without consent.

## Monitoring and Logging

LiveCap writes structured backend logs to CloudWatch through the logging service.

Important events to monitor:

- Session start and session end.
- WebSocket connection errors.
- Amazon Transcribe Streaming errors.
- Amazon Translate errors.
- Amazon S3 upload or pre-signed URL errors.
- Backend startup and shutdown.

If CloudWatch is unavailable in development, the backend falls back to stdout logging so local testing can continue.

## Testing Checklist

| Area | Validation |
| --- | --- |
| Backend health | `/api/health` returns success |
| WebSocket | Browser can connect over WSS |
| Audio format | Backend rejects invalid audio format |
| Transcription | Partial and finalized captions appear |
| Translation | Both Vietnamese and English columns are filled |
| Export | TXT transcript is uploaded to S3 |
| Download | Pre-signed URL works before expiration |
| Monitoring | CloudWatch receives session and error logs |

## Cost Optimization

- Use `t3.small` or another small EC2 instance for MVP testing.
- Stop the EC2 instance when not testing.
- Delete unused exported transcripts from S3.
- Use lifecycle rules on the transcript bucket if testing often.
- Keep CloudFront cache rules simple.
- Disable verbose audio pipeline debug logs after troubleshooting.
- Limit session duration with `SESSION_TIMEOUT`.

## Scalability Awareness

The MVP uses one EC2 instance to keep deployment simple. This is acceptable for a bootcamp project but has limits:

- One instance limits concurrent WebSocket sessions.
- A future production version should consider an Application Load Balancer with WSS support and multiple backend instances.
- ECS Fargate could be considered later for managed deployment and horizontal scaling.

