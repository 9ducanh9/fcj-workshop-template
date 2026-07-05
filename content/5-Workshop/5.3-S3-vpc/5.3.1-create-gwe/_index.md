---
title: "Build and Publish the Backend Container"
date: 2026-07-05
weight: 1
chapter: false
pre: " <b> 5.3.1. </b> "
---

# Build and Publish the Backend Container

## Step 1: Verify the Backend

The FastAPI application exposes `/api/health`, REST export routes, and
`/ws/transcribe`. Before building an image, run:

```powershell
cd backend
python -m pip install -r requirements-dev.txt
python -m compileall app
python -m pytest
```

The verified submission baseline contains 204 passing backend tests.

## Step 2: Build for Fargate

The repository Dockerfile installs pinned Python dependencies, copies the
application, exposes port 8000, and includes a container health check. Build
for the ECS runtime architecture and smoke-test `/api/health` locally.

Do not bake `.env` or AWS credentials into the image. Local execution uses an
AWS profile; ECS injects settings and uses IAM roles at runtime.

## Step 3: Push an Immutable Image

ECR stores the backend image. The deployment tag is derived from the Git commit
instead of `latest`, so a task definition points to a reproducible artifact.
The verified public demo uses image tag `1ef4250-amd64`.

```text
source commit -> Docker image -> immutable ECR tag -> ECS task definition
```

## IAM Separation

- **Task execution role:** pull from ECR and write container logs.
- **Task role:** call Transcribe, Translate, transcript S3, CloudWatch, and the
  optional least-privilege ECS scale-down action.
- **Wake Lambda role:** only describe/update the selected ECS service in the
  reviewed target.

This separation prevents the application from inheriting broad deployment
permissions.
