---
title : "Cleanup"
date : 2026-05-12
weight : 6
chapter : false
pre : " <b> 5.6. </b> "
---

# Cleanup

Cleanup is required to avoid unnecessary AWS charges after the demo.

## Cleanup Order

1. Stop or delete Step Functions executions if any are still running.
2. Delete API Gateway deployment and API.
3. Delete Lambda functions used by the project.
4. Delete Amazon Transcribe test jobs if they are no longer needed.
5. Delete objects in the S3 bucket:
   - `uploads/`
   - `transcripts/`
   - `reports/`
6. Delete the S3 bucket.
7. Delete the DynamoDB table `CognitiveCoachJobs`.
8. Delete CloudWatch log groups created for Lambda and Step Functions.
9. Delete IAM roles and policies created only for this project.
10. Review AWS Billing and Cost Management to confirm no unexpected active resources remain.

## Validation After Cleanup

Confirm:

- S3 bucket no longer exists.
- DynamoDB table no longer exists.
- API Gateway endpoint no longer responds.
- Lambda functions are deleted.
- Step Functions state machine is deleted.
- CloudWatch logs are deleted if not needed for evidence.
- No active resources related to the project remain in the selected region.

If screenshots are needed for final submission, capture them before deleting the resources.
