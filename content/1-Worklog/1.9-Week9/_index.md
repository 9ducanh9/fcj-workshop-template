---
title: "Week 9 Worklog"
date: 2026-06-12
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

# Week 9 Worklog

## 12/06/2026

### Work Completed

- Started prototype development for LiveCap based on the requirements and architecture agreed upon in the previous week.
- Prepared the source code structure for both frontend and backend.
- Identified the main modules to build: user interface, WebSocket backend, audio stream processing, transcript, translation, and export.

### Results Achieved

- Completed the initial preparation for the implementation phase.
- Clearly identified the technical components required in the prototype.
- The team began transitioning from system design into actual product development.

---

## 13/06/2026

### Work Completed

- The Software Engineering member started building the frontend using React/Vite.
- Designed the basic interface including start/stop session buttons, a caption display area, and a translation display area.
- Discussed how to display bilingual content so users can follow both languages in real time.
- The Information Systems member reviewed the interface against the designed user flow.

### Results Achieved

- Produced an initial frontend interface for LiveCap.
- Determined the layout for displaying transcript and translation content.
- The interface user flow aligned with the original requirements: start session → receive captions → view translation → end session and export transcript.

---

## 14/06/2026

### Work Completed

- The Software Engineering member started building the backend using FastAPI.
- Created basic endpoints and prepared a WebSocket endpoint for real-time sessions.
- Designed the initial session lifecycle: create session, maintain connection, receive data, and end session.
- The Information Systems member helped verify session-handling logic against system requirements.

### Results Achieved

- An initial backend prototype took shape.
- WebSocket was confirmed as the primary mechanism for real-time data transfer between frontend and backend.
- The team gained a clearer understanding of how a caption session needs to be managed from start to finish.

---

## 15/06/2026

### Work Completed

- Researched and began implementing browser-side microphone capture.
- Studied how to capture audio input from the user and send audio data to the backend in small chunks.
- The Machine Learning member verified the audio format requirements for Amazon Transcribe Streaming: PCM, mono channel, and appropriate sample rate.
- Identified potential error cases: microphone permission denied, connection loss, and unsupported browser.

### Results Achieved

- Established an approach for handling microphone input on the frontend.
- Gained a clearer understanding of the technical requirements for audio streaming.
- Added error states to be handled in both the interface and the UAT documentation.

---

## 16/06/2026

### Work Completed

- Started integrating the backend with Amazon Transcribe Streaming.
- Verified AWS credential configuration, region settings, and required access permissions.
- The Machine Learning member studied how to handle partial transcripts and final transcripts.
- The Information Systems member documented the transcript quality evaluation criteria: latency, accuracy, and Vietnamese/English recognition capability.

### Results Achieved

- The backend had an initial integration step with Amazon Transcribe Streaming.
- The team gained a clearer understanding of how AWS returns transcripts in real time.
- Identified the need to distinguish between partial and final results to avoid displaying duplicate or unstable content.

---

## 17/06/2026

### Work Completed

- Started integrating Amazon Translate into the transcript processing flow.
- Designed how to handle content after a final transcript is received: receive text → send to Amazon Translate → return translation to frontend.
- Tested how bilingual content between Vietnamese and English would be displayed.
- Updated the documentation describing the system's real-time data flow.

### Results Achieved

- Established an initial processing flow for transcript and translation.
- Determined how to combine Amazon Transcribe Streaming and Amazon Translate within the backend.
- Further clarified the technical flow: audio stream → speech-to-text → translation → frontend display.

---

## 18/06/2026

### Work Completed

- Reviewed the prototype after the first week of implementation.
- Tested the implemented features: basic frontend, FastAPI backend, WebSocket sessions, microphone input, Transcribe integration, and Translate integration at an initial level.
- Noted remaining issues: connection stability, transcript latency, partial/final transcript handling, and interface experience.
- Updated the plan for the following week: finalize transcript export, conduct end-to-end testing, and prepare for a trial deployment on AWS.

### Results Achieved

- Completed the initial technical prototype for LiveCap.
- Identified areas that still need improvement before the demo.
- The team had a clearer direction for the integration, testing, and deployment phase in the following week.

---

## Weekly Summary

This week, the team began real-world prototype development for LiveCap, including building the frontend with React/Vite, developing the backend with FastAPI, designing WebSocket sessions, handling microphone input, and completing initial integrations with Amazon Transcribe Streaming and Amazon Translate. I learned that real-time applications are more complex than standard web apps because the system must process data continuously, maintain WebSocket connections, manage session state, and respond to users quickly. Distinguishing between partial and final transcripts was also an important technical detail to ensure displayed content is not duplicated or confusing. After this week, LiveCap has an initial prototype, and the team is ready to finalize transcript export, handle errors, conduct end-to-end testing, and trial-deploy on AWS in the following week.
