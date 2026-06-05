---
title: "Self Evaluation"
date: 2026-05-12
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

# Self Evaluation

## Technical Knowledge

I improved my understanding of real-time cloud application design, WebSocket communication, EC2 deployment, S3 static hosting, CloudFront distribution, IAM role design, Amazon Transcribe Streaming, Amazon Translate, and CloudWatch logging. LiveCap helped me connect frontend audio capture, backend streaming, and managed AWS AI services into one practical system.

## Learning Ability

I learned how to turn an event-inspired idea into a concrete MVP. Instead of only documenting a theoretical AI assistant, I focused on a reproducible use case: real-time bilingual captions for workshops and meetings. I also learned to read service limitations carefully, especially around secure WebSocket connections, browser microphone permissions, and real-time transcription latency.

## Initiative

I selected LiveCap because it solves a real communication problem I experienced in bilingual technical events. I defined the user journey, studied the AWS services needed, built the backend/frontend structure, and documented a deployment path that another learner can reproduce.

## Discipline

I kept the architecture within bootcamp scope: one EC2 backend, S3 + CloudFront frontend hosting, and managed AWS services for transcription, translation, storage, and logging. I avoided adding unnecessary production complexity such as ECS, Kubernetes, user authentication, multi-room support, or AI summarization.

## Communication

The project improved my ability to explain why each AWS service is used. I practiced justifying EC2 for long-lived WebSocket sessions, CloudFront for HTTPS static delivery, S3 for transcript storage, IAM roles for credential safety, and CloudWatch for operational visibility.

## Teamwork

I learned from FCAJ mentors, AWS Study Group sessions, and community events. Feedback helped me improve the documentation and focus on practical implementation evidence instead of only describing the product idea.

## Problem Solving

The main design challenge was supporting real-time audio streaming in a simple but defensible architecture. I solved this by using EC2 for the persistent FastAPI WebSocket backend, Nginx for TLS/WSS forwarding, and managed AWS services for speech-to-text, translation, storage, and logging.

## Project Contribution

My personal contribution includes:

- Defining the LiveCap use case and MVP boundaries.
- Designing the AWS architecture.
- Implementing and documenting the FastAPI backend flow.
- Preparing the React frontend deployment path.
- Integrating Amazon Transcribe Streaming, Amazon Translate, S3, CloudFront, EC2, IAM, and CloudWatch in the workshop design.
- Writing bilingual documentation with setup, testing, monitoring, security, cost, and cleanup steps.

## Areas to Improve

- Add more AWS screenshots from the final deployed environment.
- Improve speaker diarization validation with noisy multi-speaker test audio.
- Add load testing for concurrent WebSocket sessions.
- Add a future production plan using ALB and multiple backend instances.
- Consider authentication only if the project grows beyond the bootcamp MVP.

