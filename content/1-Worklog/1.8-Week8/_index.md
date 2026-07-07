---
title: "Week 8 Worklog"
date: 2026-06-05
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

# Week 8 Worklog

## 05/06/2026

### Work Completed

- Organized role assignments and responsibilities for each team member based on their major and strengths.
- Defined each member's role in the LiveCap project: Information Systems handles BA/SA and data management; Networking handles cloud infrastructure and security; Machine Learning handles speech and language processing; Software Engineering handles frontend, backend, WebSocket, and testing.
- Clarified responsibility boundaries between roles to avoid overlapping work during implementation.
- Identified key deliverables for each role, including SRS, use cases, BPMN/activity diagrams, ERD, KPIs, infrastructure design, speech-to-text pipeline, and test suite.

### Results Achieved

- The team had a clear work assignment structure before starting project implementation.
- Each member understood their main responsibilities, scope, and required deliverables.
- The Information Systems role was defined to focus on requirements analysis, process design, data modeling, KPIs, UAT, and system documentation.
- Established a foundation for effective collaboration between frontend, backend, AI processing, and cloud infrastructure.

---

## 06/06/2026

### Work Completed

- Analyzed the LiveCap problem in detail from both the user and system perspectives.
- Identified the main user groups: students, workshop attendees, technical content learners, and those who need to follow bilingual content.
- Drafted functional requirements: start session, record audio, receive captions, translate content, save transcript, and export file.
- Drafted non-functional requirements: low latency, stable connection, data security, scalability, and browser usability.

### Results Achieved

- Completed the initial system requirements draft for LiveCap.
- Clarified what the system needs to do, how users interact with it, and what outputs are expected.
- Established a foundation for developing the SRS document and refining the MVP scope.
- Prevented scope creep beyond the core goal of real-time captioning, translation, and transcript export.

---

## 07/06/2026

### Work Completed

- Designed the main business process flow for LiveCap: user starts session → system records audio → sends audio stream → receives captions → translates content → displays in real time → exports transcript.
- Drafted use cases for the system's core features.
- Designed an initial data model for the key entities: session, transcript segment, speaker, translation, and export file.
- Identified the data fields required per session: start time, end time, language, transcript content, translation, and export status.

### Results Achieved

- Produced a description of the system's main operational process.
- Identified the key use cases within the MVP.
- Produced an initial data model to support transcript storage and export.
- Further clarified the Information Systems member's role in system logic design and data management.

---

## 08/06/2026

### Work Completed

- Discussed the initial technical architecture of LiveCap as a team.
- Identified the main system components: frontend, WebSocket backend, Amazon Transcribe Streaming, Amazon Translate, Amazon S3, and Amazon CloudWatch.
- Analyzed the real-time data flow: microphone → frontend → WebSocket backend → Amazon Transcribe → Amazon Translate → frontend displays captions and translations.
- Discussed the approach to browser-side audio processing and the bilingual display interface for users.

### Results Achieved

- Finalized the high-level architecture for LiveCap's MVP.
- The team agreed that the backend needs to handle real-time communication via WebSocket.
- Clarified the role of each AWS service: Transcribe Streaming for speech-to-text, Translate for bilingual translation, S3 for transcript export storage, and CloudWatch for logging and monitoring.
- Established a technical foundation to begin prototype development.

---

## 09/06/2026

### Work Completed

- Started preparing the development environment for the project.
- The Software Engineering member began setting up the frontend structure with React/Vite and the backend with FastAPI.
- Discussed how the backend should manage the session lifecycle: create session, maintain connection, receive audio stream, and end session.
- Identified the key UI states to handle: loading, microphone permission denied, connecting, connected, reconnecting, and error.
- The Information Systems member continued updating the requirements document based on the team's technical design.

### Results Achieved

- Established a clearer implementation direction for both frontend and backend.
- Identified the key states that matter for user experience.
- Clarified how the system handles a full caption session from start to finish.
- Updated the requirements document to better reflect real-world implementation constraints.

---

## 10/06/2026

### Work Completed

- Defined the plan for integrating AWS services into the prototype.
- The Machine Learning member researched Amazon Transcribe Streaming configuration, audio format requirements, partial transcripts, and final transcripts.
- The Networking member researched required infrastructure components: EC2, S3, CloudFront, security groups, HTTPS/TLS, and WebSocket Secure.
- The Information Systems member defined the KPIs to track: caption latency, transcript accuracy, session duration, error rate, and export status.
- Discussed initial testing criteria for UAT and system testing.

### Results Achieved

- The team had a clearer integration plan across frontend, backend, AI services, and AWS infrastructure.
- Identified the key KPIs for evaluating system quality.
- Established initial testing directions for core features: starting a session, receiving captions, translating content, and exporting transcripts.
- Confirmed that the team would use AWS managed services for speech-to-text and translation rather than training custom AI models.

---

## 11/06/2026

### Work Completed

- Reviewed the overall progress from the first week of team-based project implementation.
- Verified alignment between system requirements, technical architecture, each member's role, and end-of-term deliverables.
- Added technical risks to monitor: real-time latency, Vietnamese/English recognition quality, microphone errors, WebSocket disconnection, and AWS costs.
- Updated system documentation: functional requirements, non-functional requirements, use cases, data model, KPIs, and UAT plan.
- Prepared the plan for the following week: begin prototype implementation, test the real-time caption flow, and finalize key integration components.

### Results Achieved

- Completed the team organization and initial system design phase for LiveCap.
- Produced a foundational set of documentation to support implementation and project reporting.
- The team reached consensus on the MVP implementation direction, functional scope, and risks to manage.
- Ready to move into a more intensive implementation phase in the following week.

---

## Weekly Summary

This week, the team transitioned from the ideation phase into team organization and system design for LiveCap. Assigning clear roles to the four members — Information Systems, Networking, Machine Learning, and Software Engineering — made it clear who is responsible for requirements analysis, cloud infrastructure, speech and language processing, and software development. Through the Information Systems role, I learned how to analyze a project not just technically, but also from a business process and operational perspective — covering problem statement, functional and non-functional requirements, use cases, data modeling, KPIs, and UAT planning. By the end of the week, the team had a solid documentation and architecture foundation to begin prototype development in the coming weeks.
