---
title: "Backend Foundation on EC2"
date: 2026-05-12
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# Backend Foundation on EC2

This section prepares the backend foundation for LiveCap:

- EC2 instance for the FastAPI backend.
- IAM role for AWS service access.
- S3 bucket for transcript storage.
- Backend dependencies and environment variables.
- systemd service and Nginx reverse proxy for HTTPS/WSS.

The goal is to keep the MVP operationally simple while still using real AWS services. A single EC2 instance is enough for a bootcamp project because it supports persistent WebSocket connections and is easy to debug through SSH, `systemctl`, and logs.

