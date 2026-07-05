---
title: "Production Verification Evidence"
date: 2026-07-05
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Production Verification Evidence

## Automated Quality Gates

The main-branch GitHub Actions run completed successfully with four independent
jobs:

- Secret scan with Gitleaks;
- backend compile and 204 pytest tests;
- frontend tests and production build; and
- Terraform formatting, backend-disabled initialization, and validation.

![Successful LiveCap GitHub Actions run](/images/3-Project/github-actions-ci.png)

CI is validation-only. It does not deploy, run `terraform apply`, destroy
resources, or migrate state.

## Production Smoke Test

The production baseline was verified on 2026-07-04:

1. CloudFront `/` and `/app` returned successfully.
2. `/api/health` returned a healthy response.
3. WebSocket session start and ping/pong passed.
4. Real 16 kHz PCM produced finalized English text.
5. Amazon Translate returned Vietnamese text.
6. Session stop cleaned workers and registry state.
7. Export stored TXT in private S3 and returned a working presigned link.
8. Desktop and 390 px mobile layouts were checked.

## UI Evidence

The captured dashboard below contains finalized bilingual rows produced through
the deployed AWS path, not hard-coded sample text.

![Production caption dashboard evidence](/images/3-Project/livecap-dashboard.png)

## Known Boundaries

- WAF, private Fargate networking, wake Lambda, and scale-to-zero exist in the
  reviewed Terraform target but are not yet deployed.
- The live service has one task, so task replacement interrupts active sessions.
- CloudFront currently uses HTTP to the ALB origin; viewer traffic remains HTTPS/WSS.
