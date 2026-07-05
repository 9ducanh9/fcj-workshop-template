---
title: "Product and User Experience"
date: 2026-07-05
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Product and User Experience

## Landing Page

The `/` route introduces LiveCap with an Apple-style dark SaaS presentation.
GSAP ScrollTrigger animates the product story, caption sequence, and simplified
architecture. These heavier effects are isolated from the live dashboard.

![LiveCap landing page deployed through CloudFront](/images/3-Project/livecap-landing.png)

## Caption Dashboard

The `/app` route is designed for stable real-time operation. It provides:

- Start, Stop, Export TXT, and Clear controls;
- connection state and a 30-minute session countdown;
- microphone selection;
- two caption columns for original and translated finalized text;
- speaker labels and timestamps;
- reconnect and error state; and
- responsive desktop/mobile layout.

![LiveCap dashboard with finalized bilingual captions](/images/3-Project/livecap-dashboard.png)

Only finalized transcript segments are appended. Partial text does not pollute
the exported session transcript. The displayed dashboard evidence was captured
while a controlled microphone WAV passed through the production WebSocket,
Transcribe, and Translate path.

## User Flow

1. Open the CloudFront URL and enter `/app`.
2. Select **Start** and grant microphone permission.
3. Wait for the WebSocket session to reach Recording.
4. Speak Vietnamese or English.
5. Read the finalized bilingual row.
6. Select **Stop**, then **Export TXT** if a transcript is required.
