---
title : "Prepare Sample Input and Prompt"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.4.1. </b> "
---

# Prepare Sample Input and Prompt

## Sample Conversation

Use a short transcript first. This reduces risk and helps validate the Bedrock analysis before adding audio transcription.

Example:

```text
Mentor: Why did you choose this project?
Student: I want to build an AI assistant for communication.
Mentor: Why is that useful?
Student: Because many people cannot explain ideas clearly under pressure.
Mentor: Why should this use AWS?
Student: AWS provides storage, transcription, AI analysis, workflow orchestration, and monitoring.
Mentor: What happens if AI is wrong?
Student: The system should be used as coaching feedback, not final truth.
```

## Bedrock Prompt Structure

The prompt should ask the model to return a structured coaching report:

```text
You are a communication coach. Analyze the transcript.
Return:
1. Short summary
2. Main topic
3. Strong points
4. Weak reasoning points
5. Improved answer using claim, reason, evidence, example
6. Five why-chain practice questions
7. Safety note that feedback is a suggestion
8. Vietnamese summary
```

## Expected Output Quality

The report should be:

- Specific to the transcript.
- Practical and not generic.
- Framed as coaching feedback.
- Bilingual where required.
- Clear enough for a learner to practice from.

## Validation

Before automating the full workflow, manually test the prompt in the Amazon Bedrock console with the sample transcript and save a screenshot of the generated report.
