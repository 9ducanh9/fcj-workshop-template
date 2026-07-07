---
title: "Nhật ký tuần 8"
date: 2026-06-05
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

# Nhật ký tuần 8

## 05/06/2026

### Công việc đã thực hiện

- Tổ chức phân chia vai trò và trách nhiệm cho các thành viên trong nhóm dựa trên chuyên ngành và thế mạnh của từng người.
- Xác định vai trò cụ thể của từng thành viên trong project LiveCap: Hệ thống thông tin phụ trách BA/SA và quản lý dữ liệu; Mạng phụ trách cloud infrastructure và security; Học máy phụ trách speech/language processing; Công nghệ phần mềm phụ trách frontend, backend, WebSocket và testing.
- Làm rõ ranh giới trách nhiệm giữa các vai trò để tránh trùng lặp công việc.
- Xác định các đầu ra chính của từng vai trò như SRS, use case, BPMN/activity diagram, ERD, KPI, infrastructure, speech-to-text pipeline và test suite.

### Kết quả đạt được

- Nhóm có cơ cấu phân công công việc rõ ràng trước khi bắt đầu triển khai project.
- Mỗi thành viên hiểu rõ phần việc chính, phạm vi trách nhiệm và deliverables cần hoàn thành.
- Vai trò thành viên Hệ thống thông tin được xác định tập trung vào phân tích yêu cầu, thiết kế quy trình, mô hình dữ liệu, KPI, UAT và tài liệu hệ thống.
- Tạo nền tảng để nhóm phối hợp hiệu quả hơn giữa frontend, backend, AI processing và cloud infrastructure.

---

## 06/06/2026

### Công việc đã thực hiện

- Phân tích chi tiết bài toán của LiveCap dưới góc nhìn người dùng và hệ thống.
- Xác định các nhóm người dùng chính: sinh viên, người tham gia workshop, người học technical content và người cần theo dõi nội dung song ngữ.
- Viết nháp các yêu cầu chức năng: bắt đầu phiên, thu âm, nhận caption, dịch nội dung, lưu transcript và xuất file.
- Viết nháp các yêu cầu phi chức năng: độ trễ thấp, độ ổn định kết nối, bảo mật dữ liệu, khả năng mở rộng và khả năng sử dụng trên trình duyệt.

### Kết quả đạt được

- Hoàn thiện bản nháp yêu cầu hệ thống ban đầu cho LiveCap.
- Xác định rõ hơn hệ thống cần làm gì, người dùng sử dụng như thế nào và kết quả đầu ra cần có là gì.
- Có nền tảng để phát triển tài liệu SRS và làm rõ phạm vi MVP.
- Tránh được việc project bị mở rộng quá nhiều ngoài mục tiêu chính là realtime caption, translation và transcript export.

---

## 07/06/2026

### Công việc đã thực hiện

- Thiết kế quy trình nghiệp vụ chính của LiveCap: người dùng bắt đầu phiên → hệ thống thu âm → gửi audio stream → nhận caption → dịch nội dung → hiển thị realtime → xuất transcript.
- Phác thảo use case cho các chức năng chính của hệ thống.
- Thiết kế mô hình dữ liệu ban đầu cho các đối tượng: session, transcript segment, speaker, translation và export file.
- Xác định các thông tin cần lưu cho mỗi phiên như thời gian bắt đầu/kết thúc, ngôn ngữ, nội dung transcript, bản dịch và trạng thái export.

### Kết quả đạt được

- Có bản mô tả quy trình hoạt động chính của hệ thống.
- Xác định được các use case quan trọng trong MVP.
- Có mô hình dữ liệu ban đầu phục vụ cho việc lưu trữ và xuất transcript.
- Làm rõ hơn vai trò của thành viên Hệ thống thông tin trong việc thiết kế logic hệ thống và quản lý dữ liệu.

---

## 08/06/2026

### Công việc đã thực hiện

- Cùng nhóm thảo luận kiến trúc kỹ thuật ban đầu của LiveCap.
- Xác định các thành phần chính: frontend, backend WebSocket, Amazon Transcribe Streaming, Amazon Translate, Amazon S3 và Amazon CloudWatch.
- Phân tích luồng dữ liệu realtime: microphone → frontend → backend WebSocket → Amazon Transcribe → Amazon Translate → frontend hiển thị caption/translation.
- Thảo luận hướng xử lý audio trên trình duyệt và giao diện hiển thị song ngữ cho người dùng.

### Kết quả đạt được

- Hoàn thiện kiến trúc high-level cho MVP của LiveCap.
- Nhóm thống nhất backend cần xử lý realtime communication thông qua WebSocket.
- Xác định rõ vai trò của từng AWS service: Transcribe Streaming cho speech-to-text, Translate cho dịch song ngữ, S3 lưu transcript export và CloudWatch cho logging/monitoring.
- Có cơ sở kỹ thuật để bắt đầu triển khai prototype.

---

## 09/06/2026

### Công việc đã thực hiện

- Bắt đầu chuẩn bị môi trường phát triển cho project.
- Thành viên Công nghệ phần mềm bắt đầu chuẩn bị cấu trúc frontend React/Vite và backend FastAPI.
- Thảo luận cách backend quản lý session lifecycle: tạo phiên, duy trì kết nối, nhận audio stream và kết thúc phiên.
- Xác định các trạng thái cần xử lý trên giao diện: loading, microphone permission denied, connecting, connected, reconnecting và error.
- Thành viên Hệ thống thông tin tiếp tục cập nhật tài liệu yêu cầu dựa trên thiết kế kỹ thuật của nhóm.

### Kết quả đạt được

- Có định hướng triển khai rõ ràng hơn cho frontend và backend.
- Xác định được các trạng thái quan trọng trong trải nghiệm người dùng.
- Làm rõ hơn cách hệ thống xử lý một caption session từ lúc bắt đầu đến lúc kết thúc.
- Tài liệu yêu cầu được cập nhật sát hơn với khả năng triển khai thực tế.

---

## 10/06/2026

### Công việc đã thực hiện

- Xác định kế hoạch tích hợp AWS services vào prototype.
- Thành viên Học máy nghiên cứu cấu hình Amazon Transcribe Streaming, audio format, partial và final transcript.
- Thành viên Mạng nghiên cứu các thành phần hạ tầng cần có: EC2, S3, CloudFront, security group, HTTPS/TLS và WebSocket Secure.
- Thành viên Hệ thống thông tin xác định các KPI cần theo dõi: độ trễ caption, độ chính xác transcript, thời gian phiên, tỷ lệ lỗi và trạng thái export.
- Thảo luận các tiêu chí kiểm thử ban đầu cho UAT và system testing.

### Kết quả đạt được

- Nhóm có kế hoạch tích hợp rõ hơn giữa frontend, backend, AI service và hạ tầng AWS.
- Xác định được các KPI quan trọng để đánh giá chất lượng hệ thống.
- Có hướng kiểm thử ban đầu cho các chức năng chính: bắt đầu phiên, nhận caption, dịch nội dung và xuất transcript.
- Làm rõ rằng nhóm sử dụng AWS managed services cho speech-to-text và translation, không tự huấn luyện mô hình AI.

---

## 11/06/2026

### Công việc đã thực hiện

- Review lại toàn bộ tiến độ của tuần đầu tiên triển khai project theo nhóm.
- Kiểm tra sự liên kết giữa yêu cầu hệ thống, kiến trúc kỹ thuật, vai trò từng thành viên và deliverables cuối kỳ.
- Bổ sung các rủi ro kỹ thuật cần theo dõi: độ trễ realtime, chất lượng nhận dạng tiếng Việt/tiếng Anh, lỗi microphone, mất kết nối WebSocket và chi phí AWS.
- Cập nhật tài liệu hệ thống: yêu cầu chức năng, yêu cầu phi chức năng, use case, mô hình dữ liệu, KPI và kế hoạch UAT.
- Chuẩn bị kế hoạch cho tuần tiếp theo: triển khai prototype, kiểm thử realtime caption và hoàn thiện các phần tích hợp chính.

### Kết quả đạt được

- Hoàn thành bước tổ chức nhóm và thiết kế hệ thống ban đầu cho LiveCap.
- Có bộ tài liệu nền tảng phục vụ cho quá trình triển khai và báo cáo đồ án.
- Nhóm thống nhất hướng triển khai MVP, phạm vi chức năng và các rủi ro cần kiểm soát.
- Sẵn sàng chuyển sang giai đoạn implementation mạnh hơn trong tuần tiếp theo.

---

## Tổng kết tuần

Trong tuần này, nhóm bắt đầu chuyển từ giai đoạn định hình ý tưởng sang giai đoạn tổ chức và thiết kế hệ thống cho LiveCap. Việc phân chia vai trò rõ ràng cho bốn thành viên giúp xác định ai phụ trách phân tích yêu cầu, ai phụ trách hạ tầng cloud, ai phụ trách speech/language processing và ai phụ trách phát triển phần mềm. Thông qua vai trò Hệ thống thông tin, em học được cách phân tích project không chỉ ở góc độ kỹ thuật mà còn ở góc độ nghiệp vụ và vận hành — từ problem statement, functional/non-functional requirements, use case, mô hình dữ liệu đến KPI và UAT. Sau tuần này, nhóm đã có nền tảng vững chắc về tài liệu và kiến trúc để bắt đầu triển khai prototype trong các tuần tiếp theo.
