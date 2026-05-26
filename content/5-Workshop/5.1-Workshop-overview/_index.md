---
title : "Workshop Overview"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.1. </b> "
---

# Workshop Overview

## Use Case

The Cognitive Communication Coach helps users review a conversation after it ends. The user uploads a transcript or short audio file. The system analyzes the content and returns a structured coaching report:

- Conversation summary.
- Main topic and intent.
- Weak reasoning or unclear answers.
- Suggested stronger response using claim, reason, evidence, and example.
- Five "why" challenge questions for practice.
- Learning notes in English and Vietnamese.

## Architecture Diagram

{{< mermaid align="left" >}}
flowchart LR
  User["User / learner"] --> Client["Browser or API client"]
  Client --> APIGW["Amazon API Gateway"]
  APIGW --> UploadFn["Lambda: create upload URL"]
  APIGW --> ResultFn["Lambda: get result"]
  UploadFn --> S3["S3 private bucket"]
  S3 --> Workflow["Step Functions"]
  Workflow --> Transcribe["Amazon Transcribe"]
  Workflow --> AnalyzeFn["Lambda: call Bedrock"]
  AnalyzeFn --> Bedrock["Amazon Bedrock"]
  Workflow --> DDB["DynamoDB job table"]
  ResultFn --> DDB
  Workflow --> Logs["CloudWatch Logs"]
{{< /mermaid >}}

## AWS Services Used

| Service | Responsibility |
| --- | --- |
| Amazon S3 | Store uploaded audio/transcripts and generated reports |
| Amazon API Gateway | Expose REST API endpoints |
| AWS Lambda | Run backend logic and Bedrock integration |
| AWS Step Functions | Orchestrate async processing |
| Amazon Transcribe | Convert audio files to text |
| Amazon Bedrock | Generate structured coaching feedback |
| Amazon DynamoDB | Store job metadata and status |
| Amazon CloudWatch | Store logs and support troubleshooting |
| AWS IAM | Enforce least-privilege access |

## Why This Architecture

The workflow is asynchronous because audio transcription and AI analysis can take time. This avoids pretending the system is a real-time assistant. Step Functions makes each stage visible, DynamoDB keeps job status queryable, and S3 provides low-cost durable storage.

## Screenshot Evidence to Capture

After implementation, capture screenshots of:

- S3 bucket with `uploads/`, `transcripts/`, and `reports/` prefixes.
- DynamoDB job item with status updates.
- Step Functions execution graph.
- CloudWatch log stream for Lambda.
- Final coaching report output.
