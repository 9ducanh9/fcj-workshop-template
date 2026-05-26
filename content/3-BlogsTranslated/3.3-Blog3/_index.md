---
title: "Blog 3: Security, Privacy, and Cost Boundaries for AI Conversation Data"
date: 2026-05-12
weight: 3
chapter: false
pre: " <b> 3.3. </b> "
---

# Blog 3: Security, Privacy, and Cost Boundaries for AI Conversation Data

## Why This Matters

Conversation data can contain personal opinions, names, plans, business information, or sensitive feedback. An AI communication coach must be designed carefully even if it is only a bootcamp project.

## Privacy Boundaries

The system should follow these rules:

- Only upload conversations that the user is allowed to process.
- Keep the S3 bucket private.
- Use pre-signed URLs instead of public upload access.
- Delete test audio and reports after the demo.
- Avoid using real confidential conversations during testing.

## Security Boundaries

IAM policies should follow least privilege:

- Lambda can write only to the required S3 prefixes.
- Step Functions can invoke only the required Lambda functions.
- Bedrock access should be limited to the selected model if possible.
- DynamoDB access should be limited to the project table.
- CloudWatch access should be used for logs, not broad administration.

## Cost Boundaries

AI and transcription services can create cost if used carelessly. The project controls cost by:

- Limiting audio duration to 3-5 minutes.
- Testing with small sample files.
- Keeping prompts concise.
- Deleting S3 objects after testing.
- Removing unused API, Lambda, Step Functions, DynamoDB, and log resources during cleanup.

## Key Lesson

Responsible AI architecture is not only about model output. It also includes consent, data protection, permission boundaries, monitoring, and cleanup.
