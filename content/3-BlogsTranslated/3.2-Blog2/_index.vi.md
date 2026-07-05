---
title: "Kiến trúc AWS đã triển khai"
date: 2026-07-05
weight: 2
chapter: false
pre: " <b> 3.2. </b> "
---

# Kiến trúc AWS đã triển khai

## Topology runtime đã xác minh

{{< mermaid align="left" >}}
flowchart LR
  Browser["Trình duyệt"] -->|HTTPS/WSS| CF["CloudFront"]
  CF -->|OAC| FE["S3 frontend private"]
  CF -->|HTTP origin| ALB["ALB public multi-AZ"]
  ALB -->|port 8000| Task["Một ECS Fargate task"]
  ECR["ECR image immutable"] -.-> Task
  Task --> Transcribe["Transcribe Streaming"]
  Task --> Translate["Translate"]
  Task --> S3["S3 transcript private"]
  Task -.-> CW["CloudWatch"]
{{< /mermaid >}}

| Khu vực | Deployment đã xác minh |
| --- | --- |
| Region | `ap-southeast-1` |
| Frontend | S3 origin private phục vụ qua CloudFront OAC |
| Backend entry | CloudFront `/api/*`, `/ws/*` đến ALB public |
| Availability | ALB trải trên `ap-southeast-1a` và `1b` |
| Compute | ECS service có một Fargate task |
| Image | ECR tag immutable `1ef4250-amd64` |
| Transcript | S3 private, chỉ TXT, retention 14 ngày |
| Log | CloudWatch retention 14 ngày |

## Luồng request và response

1. Browser kết nối HTTPS/WSS đến CloudFront.
2. CloudFront lấy frontend asset từ S3 private qua OAC.
3. API/WebSocket request được route đến ALB.
4. ALB chỉ gửi traffic đến Fargate target healthy.
5. FastAPI stream PCM đến Transcribe và finalized text đến Translate.
6. Caption trả về qua Fargate -> ALB -> CloudFront -> browser.
7. TXT export được lưu trong transcript bucket private.

## Kiến trúc target đã review

Hình sau là target đã review, không phải claim tài nguyên đã deploy. Target bổ
sung VPC riêng hai AZ, task private, một NAT Gateway, WAF COUNT, wake Lambda,
scale-to-zero, dashboard và budget.

![Kiến trúc target LiveCap đã review](/images/3-Project/livecap-target-architecture.png)
