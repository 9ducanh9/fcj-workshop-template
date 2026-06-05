---
title : "Translate Captions and Export Transcripts"
date : 2026-05-12
weight : 3
chapter : false
pre : " <b> 5.4.3. </b> "
---

# Translate Captions and Export Transcripts

## Translation Flow

LiveCap always renders two columns:

- Vietnamese on the left.
- English on the right.

When a finalized segment is spoken in Vietnamese, Amazon Translate produces English text. When a finalized segment is spoken in English, Amazon Translate produces Vietnamese text. The frontend receives both `text_vi` and `text_en` for display.

Example segment message:

```json
{
  "type": "finalized_segment",
  "segment_id": "segment-001",
  "speaker_label": "Speaker 1",
  "text_vi": "Xin chào mọi người",
  "text_en": "Hello everyone",
  "spoken_language": "vi",
  "is_final": true
}
```

## Transcript Export

When the user exports a session:

1. Frontend sends the accumulated transcript to the backend.
2. Backend serializes it into TXT.
3. Backend uploads the TXT file to S3 under `transcripts/`.
4. Backend generates a time-limited pre-signed URL.
5. Frontend displays the download link.

## Validation

| Test | Expected result |
| --- | --- |
| Vietnamese speech | Vietnamese text appears on the left, English translation appears on the right |
| English speech | Vietnamese translation appears on the left, English text appears on the right |
| Empty export | Backend returns a valid empty transcript file |
| Export with captions | S3 receives a TXT object under `transcripts/` |
| Download link | Pre-signed URL downloads the TXT file before expiration |

