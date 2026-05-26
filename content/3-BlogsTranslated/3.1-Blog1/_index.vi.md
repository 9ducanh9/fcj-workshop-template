---
title: "Blog 1: Từ trợ lý AI thời gian thực đến MVP AWS thực tế"
date: 2026-05-12
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Blog 1: Từ trợ lý AI thời gian thực đến MVP AWS thực tế

## Ý tưởng ban đầu

Ý tưởng ban đầu của tôi là một trợ lý giao tiếp AI có khả năng nghe hội thoại trực tiếp, hiểu ngữ cảnh, phát hiện khi người dùng bối rối và gợi ý phản hồi tốt hơn theo thời gian thực.

Động lực của ý tưởng là thật: nhiều người gặp khó khăn trong hội thoại vì không sắp xếp được suy nghĩ nhanh, khó bảo vệ ý tưởng khi bị áp lực, hoặc không trả lời rõ khi bị hỏi "tại sao" nhiều lần.

## Vì sao phạm vi ban đầu quá rủi ro

Phiên bản thời gian thực có nhiều rủi ro:

- Speech-to-text và AI generation có thể không đủ nhanh cho hội thoại tự nhiên.
- Speaker diarization dễ lỗi khi có tiếng ồn, accent hoặc nhiều người nói chồng lên nhau.
- Việc nghe trực tiếp tạo rủi ro về quyền riêng tư và consent.
- Trợ lý live có thể làm người dùng phụ thuộc hoặc bị hiểu là thao túng hội thoại.
- Demo dễ lỗi do micro, trình duyệt, mạng hoặc độ trễ model.

## Quyết định MVP cuối

Tôi thiết kế lại dự án thành **Cognitive Communication Coach xử lý sau hội thoại**. Thay vì hỗ trợ bí mật trong cuộc trò chuyện live, hệ thống phân tích recording hoặc transcript sau khi hội thoại kết thúc.

MVP này vẫn giữ mục tiêu cốt lõi: giúp người dùng cải thiện tư duy và giao tiếp. Tuy nhiên, nó thực tế hơn cho một học viên và dễ viết thành workshop AWS.

## Liên hệ với AWS

Phạm vi này cho phép tôi thể hiện kiến trúc AWS thật:

- S3 để lưu trữ private object.
- Transcribe để chuyển audio thành văn bản.
- Bedrock để tạo output coaching.
- Lambda và API Gateway cho backend serverless.
- Step Functions để điều phối workflow.
- DynamoDB để lưu trạng thái job.
- CloudWatch để log và monitoring.

## Bài học chính

Đồ án mạnh không phải là ý tưởng lớn nhất. Đồ án mạnh là ý tưởng có thể triển khai, kiểm thử, giải thích, bảo mật, giám sát và cleanup đúng cách.
