---
title: "Clean-up & Learning Outcomes"
date: 2026-07-08
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# Clean-up & Learning Outcomes

## Clean-up

After completing the workshop, delete all resources to avoid ongoing charges.
Work through the list in order – some resources depend on others being removed
first (e.g., you cannot delete a VPC while resources inside it still exist).

> [!WARNING]
> Do **not** run `terraform destroy` on the full LiveCap environment without
> first reviewing the current Terraform state and having explicit approval.
> The commands below are a **manual, step-by-step clean-up** that lets you
> verify each deletion.

### 1. Stop and Delete the ECS Service

```powershell
# Scale down to 0 first to stop running tasks
aws ecs update-service `
  --cluster livecap-cluster-dev `
  --service livecap-service-dev `
  --desired-count 0 `
  --region ap-southeast-1 --profile livecap-codex

# Wait for tasks to stop
Start-Sleep 30

# Delete the service
aws ecs delete-service `
  --cluster livecap-cluster-dev `
  --service livecap-service-dev `
  --region ap-southeast-1 --profile livecap-codex
```

### 2. Delete the ECS Cluster

```powershell
aws ecs delete-cluster `
  --cluster livecap-cluster-dev `
  --region ap-southeast-1 --profile livecap-codex
```

### 3. Delete ECR Repository and Images

```powershell
# This deletes all images in the repository
aws ecr delete-repository `
  --repository-name livecap-backend `
  --force `
  --region ap-southeast-1 --profile livecap-codex
```

### 4. Empty and Delete the S3 Frontend Bucket

```powershell
# Empty the bucket first (delete objects and versions)
aws s3 rm s3://livecap-frontend-dev-720459752315 --recursive `
  --region ap-southeast-1 --profile livecap-codex

# Delete the bucket
aws s3api delete-bucket `
  --bucket livecap-frontend-dev-720459752315 `
  --region ap-southeast-1 --profile livecap-codex
```

### 5. Empty and Delete the S3 Transcript Bucket

```powershell
aws s3 rm s3://livecap-transcripts-dev-720459752315 --recursive `
  --region ap-southeast-1 --profile livecap-codex

aws s3api delete-bucket `
  --bucket livecap-transcripts-dev-720459752315 `
  --region ap-southeast-1 --profile livecap-codex
```

### 6. Delete the Application Load Balancer

```powershell
# Get ALB ARN
$albArn = aws elbv2 describe-load-balancers `
  --names livecap-alb-dev `
  --region ap-southeast-1 --profile livecap-codex `
  --query "LoadBalancers[0].LoadBalancerArn" --output text

# Delete listeners and target groups first, then the ALB
aws elbv2 delete-load-balancer --load-balancer-arn $albArn `
  --region ap-southeast-1 --profile livecap-codex
```

### 7. Delete CloudFront Distribution

Disabling a CloudFront distribution takes 5–15 minutes before it can be deleted:

```powershell
# Disable first, then delete (requires ETag)
# It is easier to do this from the AWS Console:
# CloudFront → Distributions → select distribution → Disable → wait → Delete
```

### 8. Delete NAT Gateway (if deployed)

```powershell
# Find NAT Gateway ID
$natId = aws ec2 describe-nat-gateways `
  --filter "Name=tag:Name,Values=livecap-nat-*" `
  --region ap-southeast-1 --profile livecap-codex `
  --query "NatGateways[0].NatGatewayId" --output text

aws ec2 delete-nat-gateway --nat-gateway-id $natId `
  --region ap-southeast-1 --profile livecap-codex

# NAT Gateway takes a few minutes to delete; also release the associated
# Elastic IP:
# EC2 Console → Elastic IPs → Actions → Release
```

### 9. Delete VPC and Network Resources

Delete in this order: Security Groups → Subnets → Internet Gateway (detach
first) → VPC.

```powershell
# It is easiest to do this from the VPC Console after deleting dependent resources
# VPC Console → Your VPCs → select livecap VPC → Actions → Delete VPC
```

### 10. Delete WAF Web ACLs

```powershell
# Delete from WAF Console or CLI (requires GetWebACL to get the LockToken first)
# WAF & Shield Console → Web ACLs → select → Delete
```

### 11. Delete CloudWatch Log Groups

```powershell
aws logs delete-log-group --log-group-name livecap `
  --region ap-southeast-1 --profile livecap-codex

# Delete ALB access log group if created
aws logs delete-log-group --log-group-name livecap-alb `
  --region ap-southeast-1 --profile livecap-codex
```

### 12. Delete CloudWatch Alarms (if created)

```powershell
aws cloudwatch delete-alarms `
  --alarm-names livecap-alb-5xx `
  --region ap-southeast-1 --profile livecap-codex
```

### 13. Delete IAM Roles and Policies

```powershell
# Detach policies before deleting roles
aws iam detach-role-policy `
  --role-name livecap-task-role `
  --policy-arn <policy-arn>

aws iam delete-role --role-name livecap-task-role
aws iam delete-role --role-name livecap-execution-role
aws iam delete-role --role-name livecap-wake-lambda-role

# Delete the IAM user if created only for this workshop
aws iam delete-user --user-name Codex
```

### 14. Delete Lambda Function (if deployed)

```powershell
aws lambda delete-function --function-name livecap-wake `
  --region ap-southeast-1 --profile livecap-codex
```

### 15. Delete AWS Budget

```powershell
# AWS Budgets Console → select budget → Actions → Delete
```

### Final Verification

After completing all steps, check that no billable resources remain:

```powershell
# Check for any remaining ECS resources
aws ecs list-clusters --region ap-southeast-1 --profile livecap-codex

# Check for running EC2/NAT/ALB resources
aws ec2 describe-nat-gateways --region ap-southeast-1 --profile livecap-codex `
  --filter "Name=state,Values=available"
```

---

## Learning Outcomes

After completing this workshop, you should be able to:

### Architecture

- ✅ Explain what problem LiveCap solves and who benefits from it
- ✅ Describe the AWS architecture: CloudFront, S3, ALB, ECS Fargate, ECR,
  Transcribe, Translate, CloudWatch, WAF, Lambda
- ✅ Explain the role of each service and how they are connected
- ✅ Trace the full request path from browser microphone to caption display

### Deployment

- ✅ Build a Docker image for `linux/amd64` from a Python FastAPI backend
- ✅ Push an immutable image to Amazon ECR using Git SHA tags
- ✅ Create an ECS task definition and update a Fargate service
- ✅ Build a React/Vite frontend and sync it to a private S3 bucket
- ✅ Create a CloudFront invalidation to refresh edge caches
- ✅ Configure CloudFront path behaviors for static assets, API, and WebSocket

### Testing

- ✅ Run the backend test suite (pytest) and frontend tests (Vitest)
- ✅ Verify the health endpoint through CloudFront
- ✅ Test a live WebSocket transcription session end-to-end
- ✅ Export a transcript and verify the S3 object and presigned URL

### Observability

- ✅ Read structured application logs in CloudWatch
- ✅ Understand ALB and ECS metrics and what they indicate
- ✅ Create a basic CloudWatch alarm for error conditions

### Security

- ✅ Understand the IAM least-privilege model (task execution vs. task role)
- ✅ Verify that S3 buckets are private and only accessible through CloudFront OAC
- ✅ Understand how WAF blocks managed threats without touching application code
- ✅ Explain why raw audio is never stored and how transcript expiry works

### Cost

- ✅ Identify the fixed-cost resources (ALB, NAT Gateway, WAF) vs. usage-based
  services (Transcribe, Translate)
- ✅ Explain how session limits and retention rules bound ongoing costs
- ✅ Understand the role of an AWS Budget alert and its limitations
- ✅ Clean up all resources to avoid ongoing charges after the workshop
