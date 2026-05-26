---
title: "Project Proposal"
date: 2026-05-12
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Project Proposal

## Project Title

**Cognitive Communication Coach: AI-Powered Conversation Reflection System on AWS**

## 1. Project Overview

The project is a bilingual AI coaching system that analyzes a short conversation recording or transcript after the conversation ends. It produces a structured report with a summary, topic intent, weak reasoning points, improved response suggestions, and practice questions.

The system is not designed to secretly answer for users during a live conversation. Instead, it helps users review their own communication, understand where their reasoning was unclear, and practice better responses for future situations.

## 2. Problem Being Solved

Students, interns, and junior professionals often struggle in conversations even when they understand part of the topic. Common issues include:

- Not organizing thoughts quickly under pressure.
- Freezing when challenged with repeated "why" questions.
- Giving answers without evidence or examples.
- Realizing better responses only after the conversation ends.
- Having no structured way to review and improve communication.

The problem is not only language fluency. It is also reasoning structure, confidence, and reflection.

## 3. Goals

- Build a practical AWS-based system using at least three AWS services.
- Allow users to upload a short audio file or transcript for analysis.
- Convert speech to text using Amazon Transcribe when audio is provided.
- Use Amazon Bedrock to generate a coaching report.
- Store job status and results in a structured way.
- Provide reproducible implementation steps, testing, monitoring, security, cost, and cleanup documentation.
- Keep the project realistic for one student and suitable for a bootcamp final project.

## 4. Solution Architecture

{{< mermaid align="left" >}}
flowchart LR
  User["User browser"] --> APIGW["Amazon API Gateway"]
  APIGW --> UploadLambda["Lambda: create upload URL"]
  UploadLambda --> S3["Amazon S3 private bucket"]
  S3 --> SFN["AWS Step Functions workflow"]
  SFN --> Transcribe["Amazon Transcribe"]
  SFN --> Bedrock["Amazon Bedrock"]
  SFN --> DDB["Amazon DynamoDB"]
  APIGW --> ResultLambda["Lambda: get job result"]
  ResultLambda --> DDB
  SFN --> CW["Amazon CloudWatch"]
{{< /mermaid >}}

## 5. AWS Services Used

| Service | Role | Reason for Selection |
| --- | --- | --- |
| Amazon S3 | Stores uploaded audio, transcripts, and generated reports | Durable, low-cost object storage with private access controls |
| AWS Lambda | Handles upload URL creation, job creation, and result retrieval | Serverless compute suitable for short backend tasks |
| Amazon API Gateway | Exposes REST API endpoints for the frontend or test client | Managed API layer with authentication and throttling options |
| AWS Step Functions | Orchestrates transcription and AI analysis workflow | Makes async processing visible, retryable, and easier to debug |
| Amazon Transcribe | Converts audio conversation files into text | Managed speech-to-text service, avoids building custom ASR |
| Amazon Bedrock | Generates structured coaching feedback | Managed foundation model access without managing model infrastructure |
| Amazon DynamoDB | Stores job metadata, status, and report references | Serverless NoSQL database with simple key-value access pattern |
| Amazon CloudWatch | Stores logs and operational metrics | Required for debugging, monitoring, and validation |
| AWS IAM | Controls service permissions | Supports least-privilege security design |

## 6. Timeline

| Phase | Duration | Deliverables |
| --- | --- | --- |
| Requirement analysis | Week 1 | Problem statement, user journey, project scope |
| AWS foundation | Weeks 2-3 | IAM review, S3 bucket, DynamoDB table, basic Lambda |
| AI workflow | Weeks 4-6 | Transcribe flow, Bedrock prompt, Step Functions workflow |
| API and validation | Weeks 7-8 | API Gateway endpoints, sample input testing |
| Documentation | Weeks 9-10 | Workshop steps, diagrams, screenshots, bilingual content |
| Optimization and defense | Weeks 11-12 | Security review, cost cleanup, final rehearsal |

## 7. Budget Awareness

This project is designed for low bootcamp-scale usage:

- Audio files should be limited to 3-5 minutes during testing.
- S3 storage should remain small because only sample files are used.
- Lambda and Step Functions usage should stay within low-volume testing.
- Bedrock cost depends on model choice and token usage, so prompts should be concise.
- All resources must be cleaned up after the demo to avoid unnecessary charges.

The final report should include a screenshot or exported estimate from AWS Pricing Calculator after the student's actual region and model choice are confirmed.

## 8. Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| Audio transcription is inaccurate | AI report quality decreases | Use clear sample audio, allow transcript upload fallback |
| Bedrock output is too vague | Weak demo value | Use a structured prompt and fixed evaluation rubric |
| Cost grows from repeated AI calls | Unexpected charges | Limit file duration, delete test files, monitor usage |
| Privacy concerns | Sensitive conversation data exposure | Private S3, least-privilege IAM, retention cleanup, consent notice |
| Workflow errors are hard to debug | Implementation delays | Use Step Functions execution history and CloudWatch logs |
| Scope creep into real-time assistant | Project becomes unrealistic | Keep MVP async and post-conversation only |

## 9. Success Criteria

- A sample audio or transcript can be uploaded.
- The system creates a job record and stores processing status.
- Audio input is converted into text, or a text transcript is accepted directly.
- Bedrock produces a structured coaching report.
- Results can be retrieved and reviewed.
- Logs, errors, permissions, cost controls, and cleanup steps are documented.
