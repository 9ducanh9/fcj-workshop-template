---
title: "Clean-up & Kết quả cần đạt"
date: 2026-07-08
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# Clean-up & Kết quả cần đạt

## Clean-up

Sau khi hoàn thành workshop, hãy xóa tất cả tài nguyên để tránh phát sinh chi
phí liên tục. Thực hiện theo thứ tự – một số tài nguyên phụ thuộc vào việc
xóa tài nguyên khác trước (ví dụ: không thể xóa VPC khi các tài nguyên bên
trong vẫn còn).

> [!WARNING]
> **Không** chạy `terraform destroy` trên môi trường LiveCap đầy đủ mà không
> review Terraform state hiện tại và có sự chấp thuận rõ ràng. Các lệnh dưới
> đây là quy trình **clean-up thủ công từng bước** để bạn xác minh từng thao
> tác xóa.

### 1. Dừng và xóa ECS Service

```powershell
# Scale về 0 để dừng task đang chạy
aws ecs update-service `
  --cluster livecap-cluster-dev `
  --service livecap-service-dev `
  --desired-count 0 `
  --region ap-southeast-1 --profile livecap-codex

# Chờ task dừng
Start-Sleep 30

# Xóa service
aws ecs delete-service `
  --cluster livecap-cluster-dev `
  --service livecap-service-dev `
  --region ap-southeast-1 --profile livecap-codex
```

### 2. Xóa ECS Cluster

```powershell
aws ecs delete-cluster `
  --cluster livecap-cluster-dev `
  --region ap-southeast-1 --profile livecap-codex
```

### 3. Xóa ECR Repository và tất cả image

```powershell
# Lệnh này xóa tất cả image trong repository
aws ecr delete-repository `
  --repository-name livecap-backend `
  --force `
  --region ap-southeast-1 --profile livecap-codex
```

### 4. Làm trống và xóa S3 Frontend Bucket

```powershell
# Làm trống bucket trước (xóa object và version)
aws s3 rm s3://livecap-frontend-dev-720459752315 --recursive `
  --region ap-southeast-1 --profile livecap-codex

# Xóa bucket
aws s3api delete-bucket `
  --bucket livecap-frontend-dev-720459752315 `
  --region ap-southeast-1 --profile livecap-codex
```

### 5. Làm trống và xóa S3 Transcript Bucket

```powershell
aws s3 rm s3://livecap-transcripts-dev-720459752315 --recursive `
  --region ap-southeast-1 --profile livecap-codex

aws s3api delete-bucket `
  --bucket livecap-transcripts-dev-720459752315 `
  --region ap-southeast-1 --profile livecap-codex
```

### 6. Xóa Application Load Balancer

```powershell
# Lấy ALB ARN
$albArn = aws elbv2 describe-load-balancers `
  --names livecap-alb-dev `
  --region ap-southeast-1 --profile livecap-codex `
  --query "LoadBalancers[0].LoadBalancerArn" --output text

# Xóa listener và target group trước, rồi xóa ALB
aws elbv2 delete-load-balancer --load-balancer-arn $albArn `
  --region ap-southeast-1 --profile livecap-codex
```

### 7. Xóa CloudFront Distribution

Vô hiệu hóa CloudFront distribution cần 5–15 phút trước khi có thể xóa:

```powershell
# Dễ thực hiện hơn qua AWS Console:
# CloudFront → Distributions → chọn distribution → Disable → chờ → Delete
```

### 8. Xóa NAT Gateway (nếu đã deploy)

```powershell
# Tìm NAT Gateway ID
$natId = aws ec2 describe-nat-gateways `
  --filter "Name=tag:Name,Values=livecap-nat-*" `
  --region ap-southeast-1 --profile livecap-codex `
  --query "NatGateways[0].NatGatewayId" --output text

aws ec2 delete-nat-gateway --nat-gateway-id $natId `
  --region ap-southeast-1 --profile livecap-codex

# NAT Gateway cần vài phút để xóa; sau đó release Elastic IP liên kết:
# EC2 Console → Elastic IPs → Actions → Release
```

### 9. Xóa VPC và tài nguyên mạng

Xóa theo thứ tự: Security Group → Subnet → Internet Gateway (detach trước) → VPC.

```powershell
# Dễ thực hiện hơn qua VPC Console sau khi đã xóa tài nguyên phụ thuộc:
# VPC Console → Your VPCs → chọn livecap VPC → Actions → Delete VPC
```

### 10. Xóa WAF Web ACL

```powershell
# Xóa từ WAF Console (cần GetWebACL để lấy LockToken trước)
# WAF & Shield Console → Web ACLs → chọn → Delete
```

### 11. Xóa CloudWatch Log Group

```powershell
aws logs delete-log-group --log-group-name livecap `
  --region ap-southeast-1 --profile livecap-codex

# Xóa log group ALB nếu đã tạo
aws logs delete-log-group --log-group-name livecap-alb `
  --region ap-southeast-1 --profile livecap-codex
```

### 12. Xóa CloudWatch Alarm (nếu đã tạo)

```powershell
aws cloudwatch delete-alarms `
  --alarm-names livecap-alb-5xx `
  --region ap-southeast-1 --profile livecap-codex
```

### 13. Xóa IAM Role và Policy

```powershell
# Detach policy trước khi xóa role
aws iam detach-role-policy `
  --role-name livecap-task-role `
  --policy-arn <policy-arn>

aws iam delete-role --role-name livecap-task-role
aws iam delete-role --role-name livecap-execution-role
aws iam delete-role --role-name livecap-wake-lambda-role

# Xóa IAM user nếu chỉ tạo cho workshop này
aws iam delete-user --user-name Codex
```

### 14. Xóa Lambda Function (nếu đã deploy)

```powershell
aws lambda delete-function --function-name livecap-wake `
  --region ap-southeast-1 --profile livecap-codex
```

### 15. Xóa AWS Budget

```powershell
# AWS Budgets Console → chọn budget → Actions → Delete
```

### Kiểm tra cuối

Sau khi hoàn thành tất cả bước, xác minh không còn tài nguyên tính phí nào:

```powershell
# Kiểm tra tài nguyên ECS còn lại
aws ecs list-clusters --region ap-southeast-1 --profile livecap-codex

# Kiểm tra tài nguyên EC2/NAT/ALB đang chạy
aws ec2 describe-nat-gateways --region ap-southeast-1 --profile livecap-codex `
  --filter "Name=state,Values=available"
```

---

## Kết quả cần đạt

Sau khi hoàn thành workshop này, bạn cần đạt được:

### Kiến trúc

- ✅ Giải thích được LiveCap giải quyết vấn đề gì và ai hưởng lợi
- ✅ Mô tả được kiến trúc AWS: CloudFront, S3, ALB, ECS Fargate, ECR,
  Transcribe, Translate, CloudWatch, WAF, Lambda
- ✅ Giải thích vai trò của từng dịch vụ và cách chúng kết nối với nhau
- ✅ Theo dõi được toàn bộ đường đi request từ microphone trình duyệt đến hiển thị phụ đề

### Triển khai

- ✅ Build Docker image `linux/amd64` từ backend Python FastAPI
- ✅ Push image bất biến lên Amazon ECR bằng Git SHA tag
- ✅ Tạo ECS task definition và cập nhật Fargate service
- ✅ Build React/Vite frontend và sync lên S3 private
- ✅ Tạo CloudFront invalidation để refresh edge cache
- ✅ Cấu hình CloudFront path behavior cho static asset, API và WebSocket

### Kiểm thử

- ✅ Chạy bộ test backend (pytest) và frontend (Vitest)
- ✅ Xác minh health endpoint qua CloudFront
- ✅ Test một phiên phiên âm WebSocket trực tiếp end-to-end
- ✅ Export transcript và xác minh S3 object và presigned URL

### Quan sát hệ thống

- ✅ Đọc được structured application log trong CloudWatch
- ✅ Hiểu metric ALB và ECS và ý nghĩa của chúng
- ✅ Tạo được CloudWatch alarm cơ bản cho điều kiện lỗi

### Bảo mật

- ✅ Hiểu mô hình IAM least-privilege (task execution role vs. task role)
- ✅ Xác minh S3 bucket private chỉ truy cập được qua CloudFront OAC
- ✅ Hiểu cách WAF chặn managed threat mà không cần chạm vào code ứng dụng
- ✅ Giải thích tại sao raw audio không bao giờ được lưu và cách transcript expiry hoạt động

### Chi phí

- ✅ Xác định được tài nguyên chi phí cố định (ALB, NAT Gateway, WAF) so với
  dịch vụ theo mức sử dụng (Transcribe, Translate)
- ✅ Giải thích cách giới hạn session và lifecycle rule kiểm soát chi phí liên tục
- ✅ Hiểu vai trò của AWS Budget alert và giới hạn của nó
- ✅ Xóa sạch tất cả tài nguyên để tránh phát sinh chi phí sau workshop
