---
title: "Week 11 Worklog"
date: 2026-06-26
weight: 11
chapter: false
pre: " <b> 1.11. </b> "
---

# Week 11 Worklog

## 26/06/2026

### Work Completed

- Reviewed the LiveCap MVP version after all core components had been integrated.
- Tested the main system flows: start session, receive captions, translate content, end session, and export transcript.
- Noted areas for improvement: WebSocket stability, error handling, real-time latency, microphone permission, and user experience when the connection drops.

### Results Achieved

- Identified the items to optimize before finalizing the demo.
- Produced a list of bugs and improvements to address during the production-readiness phase.
- The team agreed to focus on stability, security, monitoring, and user experience rather than adding new features.

---

## 27/06/2026

### Work Completed

- Improved the session management mechanism in the backend.
- Added logic to limit the number of active sessions to prevent excessive system usage.
- Considered session timeout to cap session duration and reduce the risk of uncontrolled costs.
- Tested how to clean up resources after a user ends or loses a session connection.

### Results Achieved

- The backend managed caption sessions more clearly and safely.
- Reduced the risk of sessions hanging or continuing to run after a user leaves the system.
- The system had a better foundation for controlling resources and costs when running on AWS.

---

## 28/06/2026

### Work Completed

- Improved the frontend experience during real-time connection.
- Added UI states: connecting, connected, reconnecting, error, and microphone permission denied.
- Reviewed how captions and translations are displayed to make content clearer during use.
- Re-validated the user flow against the use cases designed during the system analysis phase.

### Results Achieved

- The interface responded more accurately to the system's real-time states.
- Users could more easily understand when the system was connecting, had lost connection, or encountered a microphone error.
- The main interface flows aligned more closely with the requirements documentation and UAT criteria.

---

## 29/06/2026

### Work Completed

- Reviewed the system's basic security configurations.
- Re-checked IAM permissions for the services: Transcribe, Translate, S3, and CloudWatch.
- Reviewed CORS configuration, security groups, HTTPS/WSS settings, and S3 bucket access control.
- Discussed how to protect the system during a public demo, including access restrictions, firewall rules, and WAF at a directional level.

### Results Achieved

- The system had a clearer security posture.
- AWS access was reviewed to follow the principle of granting only the necessary permissions.
- The team gained a deeper understanding of the importance of security when deploying a real-time application to cloud.

---

## 30/06/2026

### Work Completed

- Focused on monitoring and cost optimization for the system.
- Reviewed CloudWatch logs to track backend errors, session states, and errors when calling AWS services.
- Considered log and transcript retention policies to avoid storing data longer than necessary.
- Discussed ways to reduce costs when the system has no active users, particularly for the backend and services running continuously.

### Results Achieved

- The system had a clearer observability mechanism through logs.
- The team identified the key log types to monitor during demos and debugging.
- Established a cost optimization direction: managing sessions, limiting usage time, and avoiding running resources unnecessarily.

---

## 01/07/2026

### Work Completed

- Set up and tested automated testing steps for the project.
- Tested backend tests, frontend builds, and infrastructure configuration validation steps.
- Reviewed secrets and configuration to avoid exposing sensitive information in source code.
- Updated technical documentation related to testing, deployment, and security notes.

### Results Achieved

- The project had a clearer quality assurance process before the demo.
- Reduced the risk of errors caused by untested code changes.
- Technical documentation was more complete regarding how to test, build, and deploy the system.

---

## 02/07/2026

### Work Completed

- Reviewed the full system after the optimization phase of the week.
- Re-checked all core components: frontend, backend, WebSocket, Transcribe, Translate, S3, CloudWatch, IAM, and deployment.
- Updated the issue list, test results, UAT checklist, and the remaining items to complete before final submission.
- Prepared content for the final week: report, system documentation, demo flow, and project summary.

### Results Achieved

- LiveCap was more stable compared to the initial prototype version.
- Key concerns around session management, error handling, monitoring, security, and cost had been reviewed.
- The team was ready to move into the final phase: completing documentation, running UAT, preparing the demo, and writing the end-of-term report.

---

## Weekly Summary

This week, the team focused on improving the stability and operational readiness of LiveCap. With the core MVP features already in place, the priority shifted away from adding new functionality and toward addressing critical concerns: session lifecycle management, WebSocket reconnection, error handling, IAM permissions, monitoring, logging, and cost optimization. I learned that a system that runs is not yet a complete system — when deployed to cloud, it also needs to be evaluated for security, resilience, observability, and cost control. After this week, LiveCap has a more stable foundation to move into the final phase: completing documentation, running UAT, preparing the demo, and wrapping up the project.
