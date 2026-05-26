---
title : "Create Upload and Result API"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.3.2. </b> "
---

# Create Upload and Result API

## API Design

Create a simple REST API with these endpoints:

| Method | Path | Purpose |
| --- | --- | --- |
| `POST` | `/upload-url` | Generate a pre-signed S3 upload URL |
| `POST` | `/jobs` | Create a processing job after upload |
| `GET` | `/jobs/{jobId}` | Retrieve job status and result |

## Upload URL Lambda

The upload URL Lambda should:

1. Receive a file name and input type.
2. Create a unique `jobId`.
3. Generate an S3 key under `uploads/`.
4. Return a pre-signed URL.
5. Optionally insert an initial job item in DynamoDB.

Example response:

```json
{
  "jobId": "job-20260512-001",
  "uploadUrl": "https://s3-presigned-url-example",
  "s3Key": "uploads/job-20260512-001/sample.txt"
}
```

## Create Job Lambda

The create job Lambda should:

1. Validate that the uploaded object exists in S3.
2. Insert or update the DynamoDB item with status `UPLOADED`.
3. Start the Step Functions execution.
4. Return the `jobId` and current status.

Example response:

```json
{
  "jobId": "job-20260512-001",
  "status": "UPLOADED",
  "message": "Processing workflow started"
}
```

## Result Lambda

The result Lambda should:

1. Read the job item from DynamoDB.
2. If status is `COMPLETED`, return the report location or report content.
3. If status is `FAILED`, return the failure reason.
4. If still processing, return the current status.

## Validation

Use a transcript file first because it avoids audio transcription variables:

```powershell
aws s3 cp sample_conversation.txt s3://<bucket-name>/uploads/job-test/sample_conversation.txt
```

Then create a manual DynamoDB test item or trigger the `/jobs` API and confirm that the job appears in the table.
