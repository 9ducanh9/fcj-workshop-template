---
title : "Create S3 Bucket and DynamoDB Table"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.3.1. </b> "
---

# Create S3 Bucket and DynamoDB Table

## Step 1: Create the S3 Bucket

Create one private bucket for the project.

Suggested bucket name:

```text
cognitive-coach-<your-name>-<account-id>
```

Recommended prefixes:

```text
uploads/
transcripts/
reports/
```

Configuration:

- Block all public access: enabled.
- Bucket versioning: optional for bootcamp demo.
- Server-side encryption: enable SSE-S3.
- Lifecycle rule: delete objects under `uploads/`, `transcripts/`, and `reports/` after 7 days for the demo environment.

## Step 2: Create the DynamoDB Table

Create a table named:

```text
CognitiveCoachJobs
```

Table design:

| Attribute | Type | Purpose |
| --- | --- | --- |
| `jobId` | String partition key | Unique job identifier |
| `status` | String | `UPLOADED`, `TRANSCRIBING`, `ANALYZING`, `COMPLETED`, or `FAILED` |
| `inputType` | String | `audio` or `text` |
| `inputS3Key` | String | Uploaded file path |
| `reportS3Key` | String | Final report path |
| `createdAt` | String | ISO timestamp |
| `updatedAt` | String | ISO timestamp |
| `errorMessage` | String | Failure reason if any |

Use on-demand capacity mode for a small bootcamp project.

## Step 3: Create IAM Roles

Create a Lambda execution role with permissions for:

- Writing logs to CloudWatch.
- Reading and writing objects in the project S3 bucket.
- Reading and writing items in the `CognitiveCoachJobs` table.
- Calling Bedrock model inference.

Create a Step Functions role with permissions for:

- Invoking required Lambda functions.
- Starting and checking Amazon Transcribe jobs if using audio input.
- Writing execution logs to CloudWatch.

Do not use `AdministratorAccess` for the final project roles. For the final report, keep the IAM design aligned with least-privilege principles.

## Validation

Confirm:

- The S3 bucket is not public.
- A test object can be uploaded to `uploads/`.
- The DynamoDB table exists and has `jobId` as the partition key.
- IAM roles exist with scoped permissions.
