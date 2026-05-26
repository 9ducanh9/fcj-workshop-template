---
title : "Invoke Bedrock from Lambda"
date : 2026-05-12
weight : 3
chapter : false
pre : " <b> 5.4.3. </b> "
---

# Invoke Bedrock from Lambda

## Lambda Responsibility

The analysis Lambda should:

1. Read transcript text from S3.
2. Build the coaching prompt.
3. Invoke Amazon Bedrock.
4. Save the model response to `reports/<jobId>/report.json`.
5. Update DynamoDB status to `COMPLETED` or `FAILED`.

## Example Output Schema

```json
{
  "summary": "The student explained the project idea but needs stronger evidence.",
  "mainTopic": "Defending an AWS AI communication coach project",
  "strongPoints": ["Clear target problem", "AWS service mapping is relevant"],
  "weakReasoning": ["Needs clearer business value", "Needs privacy explanation"],
  "improvedResponse": {
    "claim": "AWS is suitable because the workload needs managed AI and serverless orchestration.",
    "reason": "The system has upload, transcription, AI analysis, storage, and monitoring stages.",
    "evidence": "S3, Transcribe, Bedrock, Step Functions, DynamoDB, and CloudWatch each support one stage.",
    "example": "A student can upload a transcript and receive a structured coaching report."
  },
  "whyQuestions": [
    "Why is post-conversation analysis safer than live assistance?",
    "Why does this need cloud services?",
    "Why is Bedrock better than hard-coded rules for this use case?",
    "Why should users trust the feedback?",
    "Why is cleanup important?"
  ],
  "vietnameseSummary": "Sinh viên đã giải thích ý tưởng nhưng cần bổ sung giá trị thực tế và bảo mật."
}
```

## Error Handling

Handle these errors:

- Missing transcript object.
- Bedrock model access denied.
- Bedrock throttling or timeout.
- Invalid model output.
- DynamoDB update failure.

## Validation

Use the Lambda test console with a sample event:

```json
{
  "jobId": "job-test",
  "bucket": "<bucket-name>",
  "transcriptKey": "uploads/job-test/sample_conversation.txt"
}
```

Confirm the report is saved to S3 and the DynamoDB item is updated.
