---
title: "Verify the End-to-End Workflow"
date: 2026-07-05
weight: 4
chapter: false
pre: " <b> 5.4.4. </b> "
---

# Verify the End-to-End Workflow

## Reviewer Walkthrough

1. Open the CloudFront landing page and `/api/health`.
2. Enter `/app`, select **Start**, and allow microphone access.
3. Confirm the UI reaches Recording and the WebSocket session starts.
4. Speak a short English or Vietnamese sentence.
5. Confirm one finalized bilingual row appears in both columns.
6. Verify heartbeat keeps the socket healthy and **Stop** ends cleanly.
7. Select **Export TXT** and open the temporary download link.

## Automated Gates

| Area | Gate |
| --- | --- |
| Backend | `python -m compileall app` and 204 tests |
| Frontend | 11 tests and production build |
| Terraform | format, `init -backend=false`, and validate |
| Secrets | Gitleaks full-history scan |
| Container | health check and local smoke test |
| Dependencies | production npm audit and ECR scan review |

GitHub Actions runs Backend, Frontend, Terraform, and Secret scan jobs on pull
requests and main pushes. It does not deploy, apply Terraform, or migrate state.

![Successful verification jobs on GitHub Actions](/images/3-Project/github-actions-ci.png)

## Verified Production Evidence

On 2026-07-07, the target custom VPC path passed CloudFront health, WebSocket
`session_start`/`pong`, 16 kHz PCM transcription, English-to-Vietnamese
translation, clean stop, S3 export, and presigned TXT download. WAF blocked XSS
and Log4J probes with HTTP 403.

![Production health, WebSocket, and WAF verification](/images/5-Workshop/livecap-runtime-security-verification.png)

A controlled scale test moved target ECS from `1 -> 0`, called `/api/wake`,
received `202 waking`, then observed the task at `1/1` with health 200. Automatic
idle scale-down remains disabled, so this proves the controlled `0 -> 1` wake
flow only.

![Verified scale-to-zero and wake flow](/images/5-Workshop/livecap-scale-zero-wake-verification.png)

## Expected Failure Cases

- Denied microphone permission produces a user-visible error.
- Session-limit rejection returns `TOO_MANY_SESSIONS` before AWS streaming work.
- Unexpected disconnect retries only three times, then stops capture.
- Timeout automatically ends the session at 30 minutes.
- Unhealthy ECS targets receive no ALB traffic until health checks pass.
