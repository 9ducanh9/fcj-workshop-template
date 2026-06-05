---
title : "Stream audio đến Amazon Transcribe"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.4.2. </b> "
---

# Stream audio đến Amazon Transcribe

## Audio pipeline

Browser thu microphone audio và gửi PCM audio chunk đến backend qua WSS. Backend chuyển các chunk này đến Amazon Transcribe Streaming.

Audio format mong đợi:

| Thuộc tính | Giá trị |
| --- | --- |
| Encoding | PCM |
| Sample rate | 16 kHz |
| Channels | Mono |
| Bit depth | 16-bit |

## Trách nhiệm backend

FastAPI WebSocket handler nên:

1. Nhận WebSocket connection mới.
2. Gán session ID duy nhất.
3. Start một hoặc nhiều Transcribe Streaming session.
4. Forward binary audio frame đến Transcribe.
5. Chuyển partial và finalized Transcribe event thành LiveCap segment message.
6. Map raw speaker label như `spk_0` thành nhãn dễ đọc như `Speaker 1`.
7. Gửi partial và finalized caption về browser.
8. Ghi lỗi Transcribe thông qua logging service.

## Kiểm tra

Test bằng câu ngắn tiếng Việt và tiếng Anh:

- Browser hiển thị trạng thái microphone đang capture.
- Backend ghi session start event.
- Partial caption xuất hiện khi người dùng đang nói.
- Finalized caption thay thế partial text.
- Speaker label hiển thị nhất quán trong một session.
- Lỗi tích hợp Transcribe được gửi về frontend và ghi log.

