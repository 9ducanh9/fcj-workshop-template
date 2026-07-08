---
title: "Deploy & Verify ECS Fargate Service"
date: 2026-07-08
weight: 2
chapter: false
pre: " <b> 5.3.2. </b> "
---

# Deploy & Verify ECS Fargate Service

## Step 1 – Create or Update the ECS Task Definition

A task definition tells ECS how to run your container: which image, how much
CPU/memory, which ports, which IAM roles, and what environment variables.

Update the image URI in your task definition to the SHA tag you just pushed,
then register a new revision:

```powershell
# Register new task definition revision
aws ecs register-task-definition `
  --cli-input-json file://infrastructure/task-definition.json `
  --region ap-southeast-1 --profile livecap-codex
```

Key fields in the task definition:

| Field | Value |
|---|---|
| Family | `livecap-backend-dev` |
| Container name | `livecap-backend` |
| Image | `<account>.dkr.ecr.ap-southeast-1.amazonaws.com/livecap-backend:<sha>-amd64` |
| Port mapping | Container 8000 → Host 8000 |
| CPU | 256 (0.25 vCPU) |
| Memory | 512 MB |
| Execution role | `livecap-execution-role` (pulls image, writes logs) |
| Task role | `livecap-task-role` (calls Transcribe, Translate, S3) |
| Network mode | `awsvpc` |

## Step 2 – Update the ECS Service

Tell the ECS service to deploy the new task definition revision:

```powershell
$cluster = "livecap-cluster-dev"
$service = "livecap-service-dev"
$taskDef = "livecap-backend-dev:<revision>"  # replace with actual revision number

aws ecs update-service `
  --cluster $cluster `
  --service $service `
  --task-definition $taskDef `
  --region ap-southeast-1 `
  --profile livecap-codex

# Wait until the service is stable (new task healthy, old task stopped)
aws ecs wait services-stable `
  --cluster $cluster `
  --services $service `
  --region ap-southeast-1 `
  --profile livecap-codex
```

## Step 3 – Verify the Service is Running

Check the service status from the console or CLI:

```powershell
aws ecs describe-services `
  --cluster livecap-cluster-dev `
  --services livecap-service-dev `
  --region ap-southeast-1 --profile livecap-codex `
  --query "services[0].{Status:status,Running:runningCount,Desired:desiredCount}"
```

Expected output:

```json
{
  "Status": "ACTIVE",
  "Running": 1,
  "Desired": 1
}
```

The AWS Console shows the service with one running task:

![ECS service detail showing 1 running task and service status ACTIVE](/images/5-Workshop/5.3-S3-vpc/ecs_service_detail.png)

![ECS tasks tab showing one running task with its task ID and status](/images/5-Workshop/5.3-S3-vpc/ecs_tasks_running.png)

## Step 4 – Verify the ALB Health Check

The ALB checks `/api/health` on port 8000 every 30 seconds. Only targets that
pass the health check receive traffic.

View the ALB and its target group in the console:

![Application Load Balancer list showing livecap ALB](/images/5-Workshop/5.3-S3-vpc/alb_list.png)

![ALB detail showing target groups and listener rules](/images/5-Workshop/5.3-S3-vpc/alb_detail.png)

Test the health endpoint directly through CloudFront:

```powershell
Invoke-RestMethod https://dpeohr327wt9l.cloudfront.net/api/health
```

Expected response:

```json
{"status": "healthy", "version": "1.0.0"}
```

## Step 5 – Verify the ECS Cluster

The cluster detail page shows all services, running tasks, and capacity
providers. A healthy cluster has desired = running for all services.

![ECS cluster detail page showing livecap-cluster-dev with services](/images/5-Workshop/5.3-S3-vpc/ecs_cluster_detail.png)

## Session Safety

Before the backend opens any Transcribe or Translate stream, it checks an
in-memory session registry:

- Maximum **4 concurrent sessions** globally (process-wide)
- Maximum **1 active session per client IP**

Rejected clients receive a `TOO_MANY_SESSIONS` WebSocket close message without
incurring any AI service cost. Every session exit path (stop, timeout, error,
disconnect) cleans up audio queues, worker tasks, and the registry entry.
