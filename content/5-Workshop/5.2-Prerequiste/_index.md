---
title : "Prerequisites"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

# Prerequisites

## Required Knowledge

- Basic AWS Management Console navigation.
- Basic IAM concepts: user, role, policy, least privilege.
- Basic understanding of serverless services.
- Basic Python or JavaScript familiarity for Lambda code.
- Basic REST API testing with `curl`, Postman, or API Gateway test console.

## AWS Account Preparation

1. Use a personal AWS learning account or approved training account.
2. Select one AWS Region that supports Amazon Bedrock and Amazon Transcribe.
3. Enable access to the Bedrock model you plan to use.
4. Configure AWS CLI if you will test with CLI commands.
5. Set a billing alarm or budget before testing.

## Suggested Region

Use a region where the required services are available in your account. If Bedrock model access is limited in your preferred region, choose another supported region and keep all resources in the same region.

## Local Tools

- AWS CLI v2.
- Python 3.11 or later for local code review.
- A text editor.
- Optional: Postman for API testing.

## Sample Input

Use a short non-sensitive transcript during testing:

```text
Mentor: Why did you choose this project?
Student: I want to build an AI assistant for communication.
Mentor: Why is that useful?
Student: Because many people cannot explain ideas clearly under pressure.
Mentor: Why should this use AWS?
Student: AWS provides storage, transcription, AI analysis, workflow orchestration, and monitoring.
```

## Safety Rules

- Do not upload confidential conversations.
- Do not upload a conversation unless all required consent has been obtained.
- Keep test audio short, ideally under five minutes.
- Delete test files during cleanup.

## Files Provided in This Workshop

Supporting examples are stored under `/files/cognitive-coach/`:

- [sample_conversation.txt](/files/cognitive-coach/sample_conversation.txt)
- [bedrock_prompt.md](/files/cognitive-coach/bedrock_prompt.md)
- [lambda_analyze_transcript.py](/files/cognitive-coach/lambda_analyze_transcript.py)
- [state_machine.asl.json](/files/cognitive-coach/state_machine.asl.json)
- [iam_policy_example.json](/files/cognitive-coach/iam_policy_example.json)
