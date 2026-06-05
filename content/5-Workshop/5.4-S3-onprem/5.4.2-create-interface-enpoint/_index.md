---
title : "Stream Audio to Amazon Transcribe"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.4.2. </b> "
---

# Stream Audio to Amazon Transcribe

## Audio Pipeline

The browser captures microphone audio and sends PCM audio chunks to the backend over WSS. The backend forwards those chunks to Amazon Transcribe Streaming.

Expected audio format:

| Property | Value |
| --- | --- |
| Encoding | PCM |
| Sample rate | 16 kHz |
| Channels | Mono |
| Bit depth | 16-bit |

## Backend Responsibilities

The FastAPI WebSocket handler should:

1. Accept a new WebSocket connection.
2. Assign a unique session ID.
3. Start one or more Transcribe Streaming sessions.
4. Forward binary audio frames to Transcribe.
5. Convert partial and finalized Transcribe events into LiveCap segment messages.
6. Map raw speaker labels such as `spk_0` to user-friendly labels such as `Speaker 1`.
7. Send partial and finalized captions back to the browser.
8. Log Transcribe errors through the logging service.

## Validation

Test with short Vietnamese and English phrases:

- Browser shows active microphone capture.
- Backend logs a session start event.
- Partial captions appear while the user is speaking.
- Finalized captions replace partial text.
- Speaker labels are displayed consistently within one session.
- Transcribe integration errors are surfaced to the frontend and logged.

