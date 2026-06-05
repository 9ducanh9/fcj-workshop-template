---
title : "Validate the End-to-End Workflow"
date : 2026-05-12
weight : 4
chapter : false
pre : " <b> 5.4.4. </b> "
---

# Validate the End-to-End Workflow

## End-to-End Test Path

Use this workflow after EC2, Nginx, CloudFront, S3, and environment variables are configured:

```text
Open frontend -> allow microphone -> start capture -> speak Vietnamese/English
-> receive live captions -> stop capture -> export transcript
-> upload TXT to S3 -> download with pre-signed URL
```

## Test Cases

| Test case | Expected result |
| --- | --- |
| Health check | `GET /api/health` returns success |
| Microphone denied | Frontend shows microphone permission error |
| WebSocket connection | Browser connects to `wss://.../ws/transcribe` |
| Vietnamese speech | Vietnamese and English columns are populated |
| English speech | English source and Vietnamese translation are populated |
| Speaker label | Captions include `Speaker 1`, `Speaker 2`, etc. |
| Export transcript | S3 stores TXT output and returns a pre-signed URL |
| Transcribe failure | Frontend receives an error and CloudWatch records the failure |
| S3 upload failure | Backend returns an export error and logs the affected service |

## Evidence to Capture

For the final report, capture screenshots of:

- CloudFront distribution status.
- S3 frontend bucket and transcript bucket.
- EC2 instance running.
- `systemctl status livecap`.
- Browser showing bilingual captions.
- S3 object created after export.
- CloudWatch log stream with session events.

