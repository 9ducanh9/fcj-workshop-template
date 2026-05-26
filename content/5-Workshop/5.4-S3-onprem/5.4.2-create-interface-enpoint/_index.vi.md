---
title : "Thêm Amazon Transcribe cho audio input"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.4.2. </b> "
---

# Thêm Amazon Transcribe cho audio input

## Khi nào dùng bước này

Dùng bước này sau khi transcript input đã chạy ổn. Audio có nhiều biến số hơn nên không nên là luồng test đầu tiên.

## Tạo transcription job

Với audio input, workflow nên:

1. Đọc audio object đã upload từ S3.
2. Start Amazon Transcribe job.
3. Ghi transcript output vào `transcripts/<jobId>/`.
4. Tiếp tục phân tích bằng Bedrock sau khi transcript sẵn sàng.

Ví dụ AWS CLI:

```powershell
aws transcribe start-transcription-job `
  --transcription-job-name cognitive-coach-job-test `
  --language-code en-US `
  --media MediaFileUri=s3://<bucket-name>/uploads/job-test/sample.mp3 `
  --output-bucket-name <bucket-name> `
  --output-key transcripts/job-test/
```

Kiểm tra trạng thái job:

```powershell
aws transcribe get-transcription-job --transcription-job-name cognitive-coach-job-test
```

## Lựa chọn ngôn ngữ

Test ban đầu có thể dùng:

- `en-US` cho audio tiếng Anh.
- `vi-VN` cho audio tiếng Việt nếu region đã chọn hỗ trợ.

## Kiểm tra

Xác nhận:

- Transcribe job chuyển sang trạng thái `COMPLETED`.
- File transcript JSON xuất hiện trong S3.
- Transcript đủ rõ để Bedrock phân tích.

Nếu audio kém chất lượng, hãy dùng luồng upload transcript cho demo cuối.
