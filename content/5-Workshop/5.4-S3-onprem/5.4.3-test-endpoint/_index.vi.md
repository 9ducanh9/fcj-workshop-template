---
title : "Dịch caption và export transcript"
date : 2026-05-12
weight : 3
chapter : false
pre : " <b> 5.4.3. </b> "
---

# Dịch caption và export transcript

## Luồng dịch

LiveCap luôn hiển thị hai cột:

- Tiếng Việt ở bên trái.
- Tiếng Anh ở bên phải.

Khi finalized segment được nói bằng tiếng Việt, Amazon Translate tạo text tiếng Anh. Khi finalized segment được nói bằng tiếng Anh, Amazon Translate tạo text tiếng Việt. Frontend nhận cả `text_vi` và `text_en` để hiển thị.

Ví dụ segment message:

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

## Export transcript

Khi người dùng export session:

1. Frontend gửi transcript đã tích lũy đến backend.
2. Backend serialize transcript thành TXT.
3. Backend upload TXT file lên S3 dưới prefix `transcripts/`.
4. Backend tạo pre-signed URL có thời hạn.
5. Frontend hiển thị download link.

## Kiểm tra

| Test | Kết quả mong đợi |
| --- | --- |
| Nói tiếng Việt | Text tiếng Việt ở cột trái, bản dịch tiếng Anh ở cột phải |
| Nói tiếng Anh | Bản dịch tiếng Việt ở cột trái, text tiếng Anh ở cột phải |
| Export rỗng | Backend trả về file transcript rỗng hợp lệ |
| Export có caption | S3 nhận TXT object dưới `transcripts/` |
| Download link | Pre-signed URL tải được TXT file trước khi hết hạn |

