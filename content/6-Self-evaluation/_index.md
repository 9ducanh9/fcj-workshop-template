---
title: "Self Evaluation"
date: 2026-05-12
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

# Self Evaluation

## Technical Knowledge

I improved my understanding of serverless architecture, object storage, API design, workflow orchestration, AI service integration, IAM permission design, and observability on AWS. The project helped me connect individual AWS services into one practical system instead of learning them separately.

## Learning Ability

I learned to reduce an ambitious product idea into a realistic MVP. The original idea was a real-time AI communication assistant, but the final implementation focuses on post-conversation reflection because it is safer, cheaper, more reproducible, and technically defensible for a bootcamp project.

## Initiative

I proposed an original use case based on a real communication problem I observed: people often understand a topic partially but struggle to organize and defend ideas during conversations. I independently redesigned the scope, selected AWS services, and created a workshop structure that another learner can follow.

## Discipline

I followed a weekly worklog, documented implementation steps, and included testing, monitoring, security, cost, and cleanup sections. I also kept the project bounded to avoid unrealistic production-level complexity.

## Communication

The project improved my ability to explain architecture choices clearly. I practiced describing why each AWS service is needed, what trade-offs were made, and how the system handles privacy, cost, and failure scenarios.

## Teamwork

During the bootcamp, I learned from mentors, peer discussions, AWS Study Group materials, and event sessions. I used feedback to refine the idea from an overly broad AI assistant into a focused, deliverable cloud project.

## Problem Solving

The main design challenge was balancing ambition and feasibility. I solved this by moving from real-time processing to asynchronous processing, adding transcript upload as a fallback, and using Step Functions plus CloudWatch to make errors observable.

## Project Contribution

My personal contribution includes:

- Defining the problem and target user journey.
- Designing the AWS serverless architecture.
- Creating the Bedrock coaching prompt and evaluation rubric.
- Writing bilingual workshop documentation.
- Preparing test scenarios, validation steps, security review, and cleanup plan.

## Areas to Improve

- Add a complete frontend UI instead of relying mainly on API testing.
- Capture more real AWS screenshots after deployment.
- Compare multiple Bedrock models for quality and cost.
- Add authentication with Amazon Cognito if extending beyond the bootcamp MVP.
