---
title: "Tự đánh giá"
date: 2026-05-12
weight: 6
chapter: false
pre: " <b> 6. </b> "
---

# Tự đánh giá

## Kiến thức kỹ thuật

Tôi hiểu rõ hơn về kiến trúc serverless, object storage, thiết kế API, điều phối workflow, tích hợp dịch vụ AI, thiết kế quyền IAM và quan sát hệ thống trên AWS. Dự án giúp tôi kết nối nhiều dịch vụ AWS thành một hệ thống thực tế thay vì học rời rạc từng dịch vụ.

## Khả năng học tập

Tôi học được cách thu hẹp một ý tưởng sản phẩm tham vọng thành MVP thực tế. Ý tưởng ban đầu là trợ lý giao tiếp AI thời gian thực, nhưng bản triển khai cuối tập trung vào phản tư sau hội thoại vì an toàn hơn, rẻ hơn, dễ triển khai lại hơn và phù hợp hơn với đồ án bootcamp.

## Tinh thần chủ động

Tôi đề xuất một use case gốc dựa trên vấn đề giao tiếp thực tế: nhiều người hiểu một phần chủ đề nhưng khó sắp xếp và bảo vệ ý tưởng khi trao đổi. Tôi tự điều chỉnh phạm vi, chọn dịch vụ AWS và xây dựng cấu trúc workshop để người khác có thể làm theo.

## Kỷ luật

Tôi duy trì worklog theo tuần, viết tài liệu triển khai, và bổ sung các phần kiểm thử, giám sát, bảo mật, chi phí và cleanup. Tôi cũng giữ phạm vi dự án vừa đủ để tránh phức tạp hóa như hệ thống production.

## Giao tiếp

Dự án giúp tôi luyện cách giải thích lựa chọn kiến trúc rõ ràng hơn: vì sao cần từng dịch vụ AWS, trade-off nào đã được chọn, và hệ thống xử lý quyền riêng tư, chi phí, lỗi như thế nào.

## Làm việc nhóm

Trong bootcamp, tôi học từ mentor, trao đổi với bạn học, tài liệu AWS Study Group và các buổi sự kiện. Tôi dùng phản hồi để tinh chỉnh ý tưởng từ một trợ lý AI quá rộng thành một dự án cloud có thể hoàn thành.

## Giải quyết vấn đề

Thử thách chính là cân bằng giữa tham vọng và tính khả thi. Tôi giải quyết bằng cách chuyển từ real-time sang xử lý bất đồng bộ, cho phép upload transcript làm phương án dự phòng, và dùng Step Functions cùng CloudWatch để quan sát lỗi.

## Đóng góp cá nhân

Đóng góp cá nhân của tôi bao gồm:

- Xác định vấn đề và user journey.
- Thiết kế kiến trúc serverless trên AWS.
- Xây dựng prompt Bedrock và rubric đánh giá.
- Viết tài liệu workshop song ngữ.
- Chuẩn bị kịch bản test, bước validation, review bảo mật và kế hoạch cleanup.

## Điểm cần cải thiện

- Bổ sung frontend UI hoàn chỉnh thay vì chủ yếu kiểm thử qua API.
- Chụp thêm screenshot AWS thực tế sau triển khai.
- So sánh nhiều model Bedrock về chất lượng và chi phí.
- Thêm xác thực bằng Amazon Cognito nếu mở rộng ngoài phạm vi MVP bootcamp.
