---
title : "Orchestrate and Validate the Full Workflow"
date : 2026-05-12
weight : 4
chapter : false
pre : " <b> 5.4.4. </b> "
---

# Orchestrate and Validate the Full Workflow

## Step Functions State Machine

Create a state machine that coordinates the processing stages. A simple bootcamp version can use these states:

1. `MarkAnalyzing`
2. `AnalyzeTranscript`
3. `SaveResult`
4. `MarkCompleted`
5. `HandleFailure`

If you implement audio input, add:

1. `StartTranscription`
2. `WaitForTranscription`
3. `CheckTranscriptionStatus`

## Minimal Transcript Path

For a reliable final demo, the transcript path is enough:

```text
Uploaded transcript -> Step Functions -> Lambda -> Bedrock -> S3 report -> DynamoDB status
```

## Test Case 1: Successful Transcript Analysis

Input:

```json
{
  "jobId": "job-test-001",
  "bucket": "<bucket-name>",
  "transcriptKey": "uploads/job-test-001/sample_conversation.txt"
}
```

Expected result:

- Step Functions execution succeeds.
- DynamoDB status becomes `COMPLETED`.
- Report exists under `reports/job-test-001/report.json`.
- CloudWatch logs show no unhandled exception.

## Test Case 2: Missing Transcript

Input references a transcript key that does not exist.

Expected result:

- Workflow moves to failure handling.
- DynamoDB status becomes `FAILED`.
- `errorMessage` explains that the S3 object is missing.
- CloudWatch logs contain the failure details.

## Test Case 3: Bedrock Access Error

Temporarily use a model ID that is not enabled, or remove Bedrock permission from the test role.

Expected result:

- Lambda catches the access error.
- Workflow fails in a controlled way.
- Error is visible in CloudWatch and DynamoDB.

## Final Validation Checklist

- Upload path works.
- Job status can be retrieved.
- Bedrock output follows the report structure.
- Logs are available.
- Failure cases are visible.
- Cleanup steps are documented.
