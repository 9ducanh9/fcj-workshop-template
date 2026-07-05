---
title: "Deployed AWS Architecture"
date: 2026-07-05
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# Deployed AWS Architecture

## Verified Runtime Topology

{{< mermaid align="left" >}}
flowchart LR
  Browser["Browser"] -->|HTTPS/WSS| CF["CloudFront"]
  CF -->|OAC| FE["Private S3 frontend"]
  CF -->|HTTP origin| ALB["Public multi-AZ ALB"]
  ALB -->|port 8000| Task["One ECS Fargate task"]
  ECR["ECR immutable image"] -.-> Task
  Task --> Transcribe["Transcribe Streaming"]
  Task --> Translate["Translate"]
  Task --> S3["Private transcript S3"]
  Task -.-> CW["CloudWatch"]
{{< /mermaid >}}

| Area | Verified deployment |
| --- | --- |
| Region | `ap-southeast-1` |
| Frontend | Private S3 origin delivered through CloudFront OAC |
| Backend entry | CloudFront `/api/*`, `/ws/*` to public ALB |
| Availability | ALB spans `ap-southeast-1a` and `1b` |
| Compute | ECS service with one Fargate task |
| Image | Immutable ECR tag `1ef4250-amd64` |
| Transcript | Private S3, TXT only, 14-day retention |
| Logs | CloudWatch, 14-day retention |

## Request and Response Path

1. The browser uses HTTPS/WSS with CloudFront.
2. CloudFront fetches frontend assets from private S3 through OAC.
3. API/WebSocket requests are routed to the ALB.
4. The ALB sends traffic only to the healthy Fargate target.
5. FastAPI streams PCM to Transcribe and finalized text to Translate.
6. Captions return through Fargate -> ALB -> CloudFront -> browser.
7. Exported TXT is stored in the private transcript bucket.

## Reviewed Target Architecture

The following diagram is the reviewed target, not a claim about resources
already deployed. It introduces a dedicated two-AZ VPC, private tasks, one NAT
Gateway, WAF COUNT rules, wake Lambda, scale-to-zero, dashboard, and budget.

![Reviewed LiveCap target architecture](/images/3-Project/livecap-target-architecture.png)
