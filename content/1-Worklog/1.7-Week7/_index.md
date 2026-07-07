---
title: "Week 7 Worklog"
date: 2026-05-29
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

# Week 7 Worklog

## 29/05/2026

### Work Completed

- Consolidated knowledge gained across the first six weeks of self-study on AWS services, cloud computing, and real-world use cases.
- Started thinking about final project directions that could apply the AWS services already studied.
- Listed several real-world problems that could potentially be solved with cloud services.

### Results Achieved

- Determined the need for a project that is practical, demonstrable, and makes use of multiple AWS services.
- Established a direction to transition from the self-study phase into real-world project development.
- Began forming an initial idea around an application that supports users in workshops and meetings.

---

## 30/05/2026

### Work Completed

- Brainstormed project ideas related to voice processing, transcription, translation, and supporting learners in workshops.
- Analyzed common pain points when attending technical workshops: difficulty following long sessions, incomplete note-taking, and language barriers.
- Compared several project directions based on feasibility, practical value, and suitability for AWS services.

### Results Achieved

- Identified an initial problem statement: workshop and meeting participants may struggle to follow, retain, and fully understand the content.
- Chose an initial project direction: building an application that supports real-time captioning, translation, and transcription.
- Established a foundation to develop the idea into the LiveCap project.

---

## 31/05/2026

### Work Completed

- Named and shaped the initial concept for the **LiveCap** project.
- Defined the core project goal: helping users better understand workshop and meeting content through real-time captions and transcripts.
- Drafted the project introduction, problem statement, and expected outcomes.

### Results Achieved

- Formed the core concept of LiveCap.
- Identified target users: students, workshop attendees, technical content learners, and anyone who needs to follow bilingual content.
- Produced a first draft of the project description.

---

## 01/06/2026

### Work Completed

- Researched AWS services suitable for LiveCap.
- Explored the role of **Amazon Transcribe Streaming** in converting speech to text in real time.
- Studied **Amazon Translate**, **Amazon S3**, and **Amazon CloudWatch** in the context of the project.

### Results Achieved

- Identified the core AWS services for the MVP: Amazon Transcribe Streaming for real-time speech-to-text, Amazon Translate for bilingual translation between Vietnamese and English, Amazon S3 for transcript storage, and Amazon CloudWatch for basic logging.
- Gained a clearer understanding of how AWS services can be combined to form a complete solution.

---

## 02/06/2026

### Work Completed

- Drafted the initial user flow for LiveCap.
- Identified the main user steps: open the application, start a session, view real-time captions, view translations, and export the transcript after the session ends.
- Defined the MVP scope to avoid the project expanding beyond what is achievable.

### Results Achieved

- Completed the initial user flow for LiveCap.
- Identified the core MVP features: Start/Stop caption session, real-time transcript display, bilingual translation, and post-session transcript export.
- Established a clearer direction for the architecture design and implementation phase.

---

## 03/06/2026

### Work Completed

- Drafted the first high-level architecture for LiveCap.
- Identified the main system components: frontend, real-time backend, Amazon Transcribe Streaming, Amazon Translate, Amazon S3, and CloudWatch.
- Described the data flow from microphone input to caption and translation display on the interface.

### Results Achieved

- Produced an initial high-level architecture overview for the project.
- Gained a clearer understanding of the role of a WebSocket backend in handling real-time audio.
- Identified the basic runtime flow: microphone input → frontend → backend → AWS Transcribe → Translate → frontend display → transcript storage.

---

## 04/06/2026

### Work Completed

- Reviewed the overall concept, user flow, and initial architecture for LiveCap.
- Adjusted the project scope to focus on the most important features.
- Prepared a plan for prototype implementation in the coming weeks.

### Results Achieved

- Finalized the main direction for the LiveCap project.
- Completed the initial MVP scope definition.
- Identified the next steps: begin backend and frontend prototype development and test the real-time caption flow.

---

## Weekly Summary

This week, I transitioned from the self-study phase into real-world final project development. Starting from a real user problem — difficulty following long workshop sessions, incomplete note-taking, and language barriers — I formed the idea for **LiveCap**, an application that supports real-time captioning, translation, and transcript export. I learned that a good project should start from a real user problem, and then select appropriate AWS services to address it. By the end of the week, the project had a clear problem statement, user flow, MVP scope, and high-level architecture — a solid foundation to begin prototype development in the coming weeks.
