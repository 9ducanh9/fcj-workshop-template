---
title : "Chuẩn bị input mẫu và prompt"
date : 2026-05-12
weight : 1
chapter : false
pre : " <b> 5.4.1. </b> "
---

# Chuẩn bị input mẫu và prompt

## Hội thoại mẫu

Dùng transcript ngắn trước. Cách này giảm rủi ro và giúp kiểm tra phân tích Bedrock trước khi thêm audio transcription.

Ví dụ:

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

## Cấu trúc prompt Bedrock

Prompt nên yêu cầu model trả về báo cáo coaching có cấu trúc:

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

## Chất lượng output kỳ vọng

Báo cáo nên:

- Bám sát transcript.
- Thực tế, không chung chung.
- Được trình bày như feedback coaching.
- Có phần song ngữ khi cần.
- Đủ rõ để người học luyện tập.

## Kiểm tra

Trước khi tự động hóa toàn bộ workflow, hãy test prompt thủ công trong Amazon Bedrock console với transcript mẫu và lưu screenshot report tạo ra.
