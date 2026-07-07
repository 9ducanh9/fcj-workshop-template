---
title: "Week 10 Worklog"
date: 2026-06-19
weight: 10
chapter: false
pre: " <b> 1.10. </b> "
---

# Week 10 Worklog

## 19/06/2026

### Work Completed

- Continued refining the LiveCap prototype following the previous week's work.
- Improved the caption and translation processing flow on the frontend.
- Reviewed how transcript content is displayed to make it easier to read during real-time use.
- The Information Systems member reviewed the interface against the key use cases that were designed.

### Results Achieved

- Caption and translation display became clearer and more readable.
- The system's user flow was more stable compared to the initial prototype version.
- Core features continued to align with the defined MVP scope.

---

## 20/06/2026

### Work Completed

- Built the transcript export feature for after a session ends.
- Designed the transcript format to include timestamps, speaker, original content, and translation.
- Tested how to store transcripts for download or upload to Amazon S3.
- The Information Systems member updated the data model for session, transcript segment, speaker, and translation entities.

### Results Achieved

- Produced an initial transcript export feature.
- The transcript format was clearer and better suited to the goal of helping users review workshop or meeting content.
- The data model was updated to more closely reflect the system's actual functionality.

---

## 21/06/2026

### Work Completed

- Integrated transcript storage with Amazon S3.
- Verified the access permissions required for the backend to write transcript files to S3.
- Discussed file naming conventions, organizing data by session, and access control.
- The Networking member reviewed IAM configurations for S3, Transcribe, Translate, and CloudWatch.

### Results Achieved

- Determined how to save exported transcripts to Amazon S3.
- Gained a clearer understanding of IAM's role in granting the backend access to AWS services.
- Added transcript data security requirements to the system documentation.

---

## 22/06/2026

### Work Completed

- Prepared a trial deployment of the FastAPI backend to a cloud environment.
- The Networking member configured EC2, security groups, ports, and domain/reverse proxy settings for testing.
- Tested the connection between the frontend and backend over HTTPS/WSS.
- Noted technical issues related to WebSocket Secure, CORS, and firewall configuration.

### Results Achieved

- Established a trial deployment environment for the backend.
- The team gained a clearer understanding of the challenges in moving a real-time application from local to cloud.
- Confirmed that HTTPS/WSS is a critical requirement for the frontend to communicate securely with the backend.

---

## 23/06/2026

### Work Completed

- Configured basic logging and monitoring using Amazon CloudWatch.
- Monitored backend logs, connection errors, AWS service errors, and session processing states.
- Identified the log types to observe during the demo: start session, stop session, transcript received, translation completed, and export completed.
- The Information Systems member mapped these log events to the KPIs defined earlier.

### Results Achieved

- The system had basic logging in place to support debugging and monitoring.
- The team could observe errors more effectively during trial runs.
- KPIs such as latency, error rate, and session status had a clearer basis for tracking.

---

## 24/06/2026

### Work Completed

- Performed end-to-end testing of LiveCap's main user flows.
- Tested the full user journey: open application → grant microphone permission → start session → receive captions → receive translation → end session → export transcript.
- Noted errors related to microphone permission, WebSocket disconnection, caption latency, and loading/error states.
- Updated test cases and UAT documentation based on the testing results.

### Results Achieved

- Identified the key issues that need to be resolved before the demo is finalized.
- The test case and UAT documentation became more comprehensive for the core features.
- The team gained a better understanding of evaluating the system from a real user experience perspective, not just whether the code runs.

---

## 25/06/2026

### Work Completed

- Reviewed the overall implementation progress for the week.
- Summarized the completed components: frontend, backend, WebSocket, Transcribe, Translate, S3 export, CloudWatch logging, and trial deployment.
- Noted areas for improvement in the following week: latency optimization, reconnect handling, UI improvements, cost management, and documentation completion.
- Updated the system report covering architecture, data flow, test results, issue list, and completion plan.

### Results Achieved

- LiveCap had a prototype version that could be tested through a full end-to-end flow.
- The core MVP components were integrated at a functional level.
- The team identified the items to optimize before preparing for the final demo and submission.

---

## Weekly Summary

This week, the team focused on completing the core features of LiveCap and moving the system from a local prototype into a cloud integration and trial deployment phase. Key work included building the transcript export feature, storing transcripts on Amazon S3, configuring IAM, trial-deploying the backend, setting up HTTPS/WSS, configuring CloudWatch logging, and conducting end-to-end testing. I learned that deploying a cloud system involves much more than writing code — it also requires IAM access control, connection security, network configuration, logging, monitoring, error handling, and real-world testing. After this week, LiveCap has an MVP version with all core components integrated — frontend, backend, Amazon Transcribe Streaming, Amazon Translate, Amazon S3, and Amazon CloudWatch — providing a solid base to optimize, test, and finalize documentation in the remaining weeks.
