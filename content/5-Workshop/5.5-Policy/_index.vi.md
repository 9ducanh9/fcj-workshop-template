---
title: "Bảo mật, quan sát, kiểm thử và chi phí"
date: 2026-07-05
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# Bảo mật, quan sát, kiểm thử và chi phí

## Control bảo mật đã triển khai

- IAM role thay credential AWS tĩnh trong container và source code.
- Frontend và transcript S3 bucket đều private; frontend truy cập qua OAC.
- Transcript download dùng presigned URL có thời hạn.
- Không lưu raw audio; transcript object hết hạn sau 14 ngày.
- CORS giới hạn frontend origin được chấp nhận.
- Giới hạn session global/per-IP và timeout 30 phút giảm abuse.
- Gitleaks chạy trong CI; tfstate, tfvars, plan và `.env` thật không được track.
- ECR image dùng tag immutable từ Git SHA và kết quả scan được review.

## Trạng thái WAF và network

Hai Web ACL đã deploy: CloudFront (`CLOUDFRONT`) và ALB (`REGIONAL`). Managed
rules và rate rule đang ở BLOCK; probe XSS và Log4J qua domain production trả
HTTP 403. ALB chỉ nhận traffic từ CloudFront origin-facing prefix list.

Custom VPC `10.20.0.0/16` có hai public và hai private subnet trên hai AZ. ALB
nằm ở public subnets; Fargate task nằm ở private subnets, không có public IP.
Một NAT Gateway tại `1a` là tradeoff cost-sensitive và vẫn là outbound
dependency single-AZ.

## Quan sát hệ thống

- FastAPI phát structured session/integration log đến CloudWatch khi handler
  khởi tạo được, nếu không sẽ fallback stdout.
- Backend log retention là 14 ngày.
- ALB, ECS và Lambda cung cấp metric CloudWatch chuẩn.
- Terraform target định nghĩa dashboard cho ECS CPU/memory, ALB traffic/health,
  wake Lambda và WAF mà không bật Container Insights tốn thêm phí.

CloudWatch dashboard, WAF logging, Budget và retention 14 ngày đã được apply.
Container Insights không bật để tránh chi phí bổ sung.

## CI và verification

GitHub Actions kiểm tra mọi pull request và push vào main:

1. Gitleaks scan secret với toàn bộ Git history.
2. Python 3.11 compile backend và pytest.
3. Node 20 cài frontend, chạy test và production build.
4. Terraform 1.10.5 format/validate với `-backend=false`.

CI chủ ý không deploy production, Terraform apply, destroy hoặc migrate state.

## Kiểm soát chi phí

- Transcribe và Translate tính theo usage, chủ yếu chạy khi có session active.
- Giới hạn duration/concurrency kiểm soát AI usage ngoài ý muốn.
- Transcript và log cùng retention 14 ngày.
- Terraform target có AWS Budget `$50/month` cấu hình được; alert billing có độ
  trễ, không phải enforcement realtime.
- Wake Lambda đã pass controlled `0 -> 1`. Automatic idle scale-down vẫn tắt
  cho tới khi hoàn tất rollback window và test grace period riêng.

ALB, NAT Gateway và WAF vẫn có fixed/baseline cost khi tồn tại. Scale ECS về 0
không xóa các khoản phí này.

## Rủi ro còn lại

- Một NAT Gateway tạo single-AZ outbound dependency.
- Registry in-memory chưa cho phép scale an toàn nhiều task.
- Một active task khiến thay task làm gián đoạn WebSocket đang chạy.
- Legacy stack vẫn tồn tại trong rollback window và làm tăng chi phí tạm thời.
- Finding package nền trong ECR vẫn được theo dõi đến khi có bản vá tương thích.
