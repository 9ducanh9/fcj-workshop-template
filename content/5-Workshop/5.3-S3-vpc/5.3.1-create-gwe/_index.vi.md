---
title: "Build và publish backend container"
date: 2026-07-05
weight: 1
chapter: false
pre: " <b> 5.3.1. </b> "
---

# Build và publish backend container

## Bước 1: Kiểm tra backend

FastAPI cung cấp `/api/health`, REST route export và `/ws/transcribe`. Trước khi
build image, chạy:

```powershell
cd backend
python -m pip install -r requirements-dev.txt
python -m compileall app
python -m pytest
```

Baseline đồ án đã xác minh có 204 backend test pass.

## Bước 2: Build cho Fargate

Dockerfile cài dependency Python đã pin version, copy application, expose port
8000 và có container health check. Image được build theo kiến trúc runtime của
ECS và smoke test `/api/health` trước khi publish.

Không đưa `.env` hoặc AWS credential vào image. Local dùng AWS profile; ECS
inject setting và dùng IAM role khi chạy.

## Bước 3: Push image immutable

ECR lưu backend image. Deployment tag được tạo từ Git commit thay vì `latest`,
nhờ đó task definition luôn trỏ đến artifact có thể truy vết. Demo công khai đã
xác minh dùng tag `1ef4250-amd64`.

```text
source commit -> Docker image -> ECR tag immutable -> ECS task definition
```

## Tách IAM role

- **Task execution role:** pull image từ ECR và ghi container log.
- **Task role:** gọi Transcribe, Translate, transcript S3, CloudWatch và action
  ECS scale-down tối thiểu nếu bật.
- **Wake Lambda role:** chỉ describe/update ECS service được chọn trong target.

Cách tách này ngăn application kế thừa quyền deployment quá rộng.
