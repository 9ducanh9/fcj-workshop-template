---
title: "Week 6 Worklog"
date: 2026-05-12
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

# Week 6 Worklog

## Work Completed

- Studied Amazon Transcribe job flow for audio-to-text processing.
- Reviewed audio input requirements, supported formats, language codes, and output locations.
- Added transcript upload fallback for cases where audio transcription is not reliable.

## Results Achieved

- Added Transcribe to the architecture as an optional path for audio input.
- Defined `en-US` and `vi-VN` as initial language choices for testing.
- Documented that demo audio should be short, clear, and consent-based.

## Learning Outcomes

- Speech-to-text quality depends on audio quality, noise, language, and speaking style.
- A good workshop should include fallback steps so another learner can still complete it.
