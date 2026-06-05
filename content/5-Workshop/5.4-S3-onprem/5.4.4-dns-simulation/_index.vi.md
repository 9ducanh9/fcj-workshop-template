---
title : "Kiểm tra workflow end-to-end"
date : 2026-05-12
weight : 4
chapter : false
pre : " <b> 5.4.4. </b> "
---

# Kiểm tra workflow end-to-end

## Luồng test end-to-end

Dùng workflow này sau khi đã cấu hình EC2, Nginx, CloudFront, S3 và environment variables:

```text
Mở frontend -> cấp quyền microphone -> start capture -> nói tiếng Việt/Anh
-> nhận live captions -> stop capture -> export transcript
-> upload TXT lên S3 -> tải bằng pre-signed URL
```

## Test cases

| Test case | Kết quả mong đợi |
| --- | --- |
| Health check | `GET /api/health` trả về success |
| Từ chối microphone | Frontend hiển thị lỗi quyền microphone |
| WebSocket connection | Browser kết nối đến `wss://.../ws/transcribe` |
| Nói tiếng Việt | Cột tiếng Việt và tiếng Anh đều có nội dung |
| Nói tiếng Anh | Source tiếng Anh và bản dịch tiếng Việt được hiển thị |
| Speaker label | Caption có `Speaker 1`, `Speaker 2`, ... |
| Export transcript | S3 lưu TXT output và trả về pre-signed URL |
| Lỗi Transcribe | Frontend nhận lỗi và CloudWatch ghi failure |
| Lỗi upload S3 | Backend trả export error và log service bị ảnh hưởng |

## Bằng chứng cần chụp

Cho báo cáo cuối, cần chụp screenshot:

- Trạng thái CloudFront distribution.
- S3 frontend bucket và transcript bucket.
- EC2 instance đang chạy.
- `systemctl status livecap`.
- Browser hiển thị bilingual captions.
- S3 object được tạo sau khi export.
- CloudWatch log stream có session events.

