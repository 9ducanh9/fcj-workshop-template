---
title : "Điều kiện tiên quyết"
date : 2026-05-12
weight : 2
chapter : false
pre : " <b> 5.2. </b> "
---

# Điều kiện tiên quyết

## Kiến thức cần có

- Biết thao tác cơ bản trên AWS Management Console.
- Hiểu khái niệm IAM: user, role, policy, least privilege.
- Hiểu cơ bản về dịch vụ serverless.
- Biết Python hoặc JavaScript cơ bản để đọc Lambda code.
- Biết test REST API bằng `curl`, Postman hoặc API Gateway test console.

## Chuẩn bị tài khoản AWS

1. Dùng tài khoản AWS học tập cá nhân hoặc tài khoản training được cho phép.
2. Chọn một AWS Region hỗ trợ Amazon Bedrock và Amazon Transcribe.
3. Bật quyền truy cập model Bedrock dự định sử dụng.
4. Cấu hình AWS CLI nếu muốn test bằng CLI.
5. Tạo billing alarm hoặc budget trước khi test.

## Region gợi ý

Hãy dùng region có đủ dịch vụ trong tài khoản của bạn. Nếu Bedrock model chưa khả dụng ở region mong muốn, chọn region khác được hỗ trợ và giữ toàn bộ resource trong cùng một region.

## Công cụ local

- AWS CLI v2.
- Python 3.11 hoặc mới hơn để đọc code.
- Text editor.
- Tùy chọn: Postman để test API.

## Input mẫu

Dùng transcript ngắn và không nhạy cảm khi test:

```text
Mentor: Why did you choose this project?
Student: I want to build an AI assistant for communication.
Mentor: Why is that useful?
Student: Because many people cannot explain ideas clearly under pressure.
Mentor: Why should this use AWS?
Student: AWS provides storage, transcription, AI analysis, workflow orchestration, and monitoring.
```

## Nguyên tắc an toàn

- Không upload hội thoại bí mật.
- Không upload hội thoại nếu chưa có consent cần thiết.
- Giữ audio test ngắn, tốt nhất dưới năm phút.
- Xóa file test trong bước cleanup.

## File hỗ trợ trong workshop

Các ví dụ hỗ trợ nằm trong `/files/cognitive-coach/`:

- [sample_conversation.txt](/files/cognitive-coach/sample_conversation.txt)
- [bedrock_prompt.md](/files/cognitive-coach/bedrock_prompt.md)
- [lambda_analyze_transcript.py](/files/cognitive-coach/lambda_analyze_transcript.py)
- [state_machine.asl.json](/files/cognitive-coach/state_machine.asl.json)
- [iam_policy_example.json](/files/cognitive-coach/iam_policy_example.json)
