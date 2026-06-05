---
title: "Frontend Deployment and AWS Integrations"
date: 2026-05-12
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

# Frontend Deployment and AWS Integrations

This section connects the full LiveCap application:

1. Build the React + TypeScript frontend.
2. Host the static frontend in S3.
3. Serve it through CloudFront.
4. Stream audio to Amazon Transcribe Streaming.
5. Translate finalized segments with Amazon Translate.
6. Export transcripts to S3 and return pre-signed links.

The most important technical requirement is secure WebSocket streaming. In production, the browser must connect to the backend through `wss://`, not plain `ws://`.

