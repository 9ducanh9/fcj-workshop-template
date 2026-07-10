---
title: "Ki?m th?, B?o m?t & Ki?m soát chi phí"
date: 2026-07-08
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# Ki?m th?, B?o m?t & Ki?m soát chi phí

## Quality gate trên GitHub Actions

Workflow trên nhánh `main` ch?y b?n job d?c l?p tru?c khi thay d?i du?c xem là
d?t quality gate:

- Quét secret b?ng Gitleaks trên toàn b? l?ch s? Git.
- Compile backend và ch?y 204 test b?ng pytest.
- Ch?y frontend test và t?o production build.
- Ki?m tra Terraform format, `init -backend=false` và `validate`.

![GitHub Actions LiveCap dã ch?y thành công](/images/5-Workshop/github-actions-ci.png)

CI ch? th?c hi?n validation. Workflow không deploy, không ch?y
`terraform apply`, không destroy tài nguyên và không migrate Terraform state.

## Ki?m th? ch?c nang

### Backend – 204 Unit Test

```powershell
cd backend
python -m pytest -v
```

B? test bao g?m:

- Vòng d?i WebSocket session (m?, audio, dóng, timeout)
- Session registry (gi?i h?n global và theo IP)
- Qu?n lý Transcribe stream (b?t d?u, partial result, finalize)
- Tích h?p Translate (ch? finalized, ch?n ngôn ng?)
- S3 export (serialize TXT, t?o presigned URL)
- X? lý l?i (l?i Transcribe, m?t k?t n?i, d?n d?p)

T?t c? 204 test pass trên Python 3.11. Th?i gian ch?y: kho?ng 8 giây.

### Frontend – 11 Vitest Test

```powershell
cd frontend
npm test
```

Bao g?m: render component, chuy?n tr?ng thái WebSocket hook, session timer và
tr?ng thái l?i quy?n microphone. Không có l? h?ng production t?i th?i di?m
phát hành.

### Terraform – Ch? ki?m tra cú pháp

CI không bao gi? apply h? t?ng. Ch? validate format và cú pháp:

```powershell
terraform -chdir=infrastructure/terraform fmt -check
terraform -chdir=infrastructure/terraform init -backend=false
terraform -chdir=infrastructure/terraform validate
```

### Quét secret b?ng Gitleaks

```powershell
gitleaks detect --source . --verbose
```

Gitleaks ch?y trên toàn b? l?ch s? Git. Scan s?ch là di?u ki?n b?t bu?c tru?c
m?i l?n `git push`.

## Log và Metric

### Application Log trên CloudWatch

Backend FastAPI emit structured JSON log vào log group `/ecs/livecap-backend-dev`
c?a CloudWatch. Retention log là 14 ngày.

```powershell
# Stream log tr?c ti?p
aws logs tail /ecs/livecap-backend-dev --follow --region ap-southeast-1 --profile livecap-camgiacntn
```

Các s? ki?n log chính b?n s? th?y trong m?t phiên:
- `session_start` – m? phiên m?i, kèm session ID và client IP hash
- `websocket_connect` – k?t n?i WebSocket du?c thi?t l?p
- `websocket_disconnect` – client ng?t k?t n?i ho?c timeout
- `session_end` – phiên dóng, kèm th?i lu?ng và lý do
- `integration_error` – l?i t? Transcribe, Translate ho?c S3

![CloudWatch log group – log group livecap](/images/5-Workshop/5.5-Policy/cloudwatch_log_groups.png)

![Chi ti?t log group livecap v?i các log stream](/images/5-Workshop/5.5-Policy/cloudwatch_livecap_log_groups.png)

![Chi ti?t log stream CloudWatch – s? ki?n phiên backend](/images/5-Workshop/5.5-Policy/cloudwatch_log_group_detail.png)

![Log event m?u t? m?t phiên phiên âm tr?c ti?p](/images/5-Workshop/5.5-Policy/cloudwatch_log_events.png)

### Metric quan tr?ng c?n theo dõi

| Metric | Ngu?n | Ý nghia |
|---|---|---|
| `HTTPCode_Target_5XX_Count` | ALB | L?i backend tr? v? CloudFront |
| `HealthyHostCount` | ALB Target Group | S? Fargate task healthy |
| `CPUUtilization` | ECS | CPU c?a task (c?nh báo n?u > 80%) |
| `MemoryUtilization` | ECS | B? nh? c?a task |
| `BlockedRequests` | WAF | WAF dang ch? d?ng ch?n threat |
| `T? l? l?i 4xx/5xx` | CloudFront | T? l? l?i end-to-end |

### T?o CloudWatch Alarm (ví d?)

T?o alarm kích ho?t khi ALB tr? v? l?i 5XX:

```powershell
aws cloudwatch put-metric-alarm `
  --alarm-name "livecap-alb-5xx" `
  --metric-name "HTTPCode_Target_5XX_Count" `
  --namespace "AWS/ApplicationELB" `
  --statistic Sum `
  --period 300 `
  --threshold 5 `
  --comparison-operator GreaterThanOrEqualToThreshold `
  --evaluation-periods 1 `
  --alarm-actions "arn:aws:sns:ap-southeast-1:720459752315:livecap-alerts" `
  --region ap-southeast-1 --profile livecap-camgiacntn
```

## B?o m?t

### Ðã tri?n khai

| Bi?n pháp | Cách tri?n khai |
|---|---|
| Không dùng root account | Deploy b?ng IAM user `camgiacntn` |
| IAM least privilege | Tách bi?t task execution role và task role |
| Không hardcode credential | Ch? dùng IAM role; không có key trong `.env`, image hay Git |
| S3 frontend private | Block public access + OAC origin |
| S3 transcript private | Block public access; presigned URL h?t h?n sau 24 gi? |
| HTTPS m?i noi | CloudFront terminate viewer TLS |
| WAF ? CloudFront và ALB | Managed rule ? ch? d? BLOCK; rate-based rule |
| Gi?i h?n CORS | `ALLOWED_ORIGIN` gi?i h?n frontend origin du?c ch?p nh?n |
| Gi?i h?n session | 4 global + 1/IP ngan chi phí Transcribe ngoài ki?m soát |
| H?t h?n transcript | S3 lifecycle rule 14 ngày; không luu raw audio |
| Quét secret | Gitleaks ch?y trong CI trên toàn b? l?ch s? Git |
| Image tag b?t bi?n | Git SHA tag ngan drift do tag `latest` không c? d?nh |

### Xác minh WAF

C? hai Web ACL d?u ? ch? d? BLOCK. Probe production dã xác nh?n:

- T?n công XSS (Cross-site scripting) ? HTTP 403
- Chu?i khai thác Log4J ? HTTP 403

![Xác minh b?o m?t runtime WAF – XSS và Log4J b? ch?n](/images/5-Workshop/livecap-runtime-security-verification.png)

## T?i uu chi phí

### Chi phí chính hi?n t?i (ap-southeast-1)

| Tài nguyên | Co s? tính phí | T?i uu |
|---|---|---|
| ECS Fargate | Theo vCPU-giây + GB-giây | Scale v? 0 khi không dùng (tính nang target) |
| ALB | C? d?nh theo gi? + LCU | Phát sinh phí k? c? khi ECS = 0; ch? xóa khi destroy toàn b? stack |
| NAT Gateway | Theo gi? + theo GB data | M?t NAT ? m?t AZ (trade-off chi phí) |
| Amazon Transcribe | Theo phút audio | Gi?i h?n session gi?i h?n m?c s? d?ng |
| Amazon Translate | Theo tri?u ký t? | Ch? d?ch finalized segment |
| CloudWatch | Log ingestion + luu tr? | Retention 14 ngày gi?i h?n chi phí |
| WAF | Theo ACL + theo rule | Chi phí c? d?nh; x?ng dáng v?i kh? nang blocking |

### Bi?n pháp ti?t ki?m chi phí dã áp d?ng

- **Retention log và transcript 14 ngày** – tránh luu tr? vô h?n.
- **Gi?i h?n th?i lu?ng session (30 phút)** – gi?i h?n t?i da phút Transcribe m?i phiên.
- **Gi?i h?n d?ng th?i session** – ngan chi phí Transcribe/Translate do l?m d?ng.
- **Ch? d?ch text finalized** – k?t qu? partial/interim b? lo?i tru?c khi d?ch, ti?t ki?m ký t?.
- **ECS scale-to-zero (target)** – Wake Lambda dua desired count t? 0 ? 1 khi có request d?u tiên; scale-down t? d?ng tr? v? 0 sau th?i gian không ho?t d?ng.

### AWS Budget (Terraform target)

M?t AWS Budget alert du?c d?nh nghia trong Terraform target ? m?c **$50/tháng**.
Nó g?i thông báo tr?c ti?p d?n **email subscriber** khi chi tiêu th?c t? ho?c
d? báo g?n d?n ngu?ng (không qua SNS).

> **Luu ý:** Budget alert là tín hi?u billing b? tr?, không ph?i enforcement
> th?i gian th?c. Nó giúp b?n phát hi?n chi phí ngoài ki?m soát trong vài gi?,
> không ph?i vài giây.
