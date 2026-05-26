---
title : "Add Amazon Transcribe for Audio Input"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.4.2. </b> "
---

# Add Amazon Transcribe for Audio Input

## When to Use This Step

Use this step after transcript input works. Audio adds more variables, so it should not be the first path tested.

## Create a Transcription Job

For audio input, the workflow should:

1. Read the uploaded audio object from S3.
2. Start an Amazon Transcribe job.
3. Write the transcript output to `transcripts/<jobId>/`.
4. Continue to Bedrock analysis after the transcript is available.

Example AWS CLI command:

```powershell
aws transcribe start-transcription-job `
  --transcription-job-name cognitive-coach-job-test `
  --language-code en-US `
  --media MediaFileUri=s3://<bucket-name>/uploads/job-test/sample.mp3 `
  --output-bucket-name <bucket-name> `
  --output-key transcripts/job-test/
```

Check job status:

```powershell
aws transcribe get-transcription-job --transcription-job-name cognitive-coach-job-test
```

## Language Choices

Initial testing can use:

- `en-US` for English audio.
- `vi-VN` for Vietnamese audio if supported in your selected region.

## Validation

Confirm:

- The Transcribe job status becomes `COMPLETED`.
- A transcript JSON file appears in S3.
- The transcript text is readable enough for Bedrock analysis.

If audio quality is poor, use the transcript upload path for the final demo.
