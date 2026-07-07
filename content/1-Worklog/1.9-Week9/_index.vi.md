---
title: "Nhật ký tuần 9"
date: 2026-06-12
weight: 9
chapter: false
pre: " <b> 1.9. </b> "
---

# Nhật ký tuần 9

## 12/06/2026

### Công việc đã thực hiện

- Bắt đầu triển khai prototype cho project LiveCap dựa trên requirements và kiến trúc đã thống nhất ở tuần trước.
- Chuẩn bị cấu trúc source code cho frontend và backend.
- Xác định các module chính cần xây dựng: giao diện người dùng, WebSocket backend, xử lý audio stream, transcript, translation và export.

### Kết quả đạt được

- Hoàn thành bước chuẩn bị ban đầu cho quá trình implementation.
- Xác định rõ các thành phần kỹ thuật cần triển khai trong prototype.
- Nhóm bắt đầu chuyển từ giai đoạn thiết kế hệ thống sang giai đoạn xây dựng sản phẩm thực tế.

---

## 13/06/2026

### Công việc đã thực hiện

- Thành viên Công nghệ phần mềm bắt đầu xây dựng frontend bằng React/Vite.
- Thiết kế giao diện cơ bản gồm nút bắt đầu/kết thúc phiên, khu vực hiển thị caption và khu vực hiển thị bản dịch.
- Thảo luận cách hiển thị nội dung song ngữ để người dùng dễ theo dõi trong thời gian thực.
- Thành viên Hệ thống thông tin kiểm tra lại giao diện theo user flow đã thiết kế.

### Kết quả đạt được

- Có giao diện frontend ban đầu cho LiveCap.
- Xác định được bố cục hiển thị transcript và translation.
- User flow trên giao diện bám sát yêu cầu ban đầu: bắt đầu phiên → nhận caption → xem bản dịch → kết thúc và xuất transcript.

---

## 14/06/2026

### Công việc đã thực hiện

- Thành viên Công nghệ phần mềm bắt đầu xây dựng backend bằng FastAPI.
- Tạo các endpoint cơ bản và chuẩn bị WebSocket endpoint cho realtime session.
- Thiết kế session lifecycle ở mức ban đầu: tạo phiên, duy trì kết nối, nhận dữ liệu và kết thúc phiên.
- Thành viên Hệ thống thông tin hỗ trợ kiểm tra logic xử lý phiên so với yêu cầu hệ thống.

### Kết quả đạt được

- Backend prototype bước đầu được hình thành.
- WebSocket được xác định là cơ chế chính để truyền dữ liệu realtime giữa frontend và backend.
- Nhóm hiểu rõ hơn cách một phiên caption cần được quản lý từ lúc bắt đầu đến lúc kết thúc.

---

## 15/06/2026

### Công việc đã thực hiện

- Tìm hiểu và triển khai bước đầu phần thu âm từ microphone trên trình duyệt.
- Nghiên cứu cách lấy audio input từ người dùng và gửi dữ liệu âm thanh về backend theo từng đoạn nhỏ.
- Thành viên Học máy kiểm tra yêu cầu audio format cho Amazon Transcribe Streaming: PCM, mono và sample rate.
- Ghi nhận các lỗi có thể xảy ra: người dùng từ chối quyền microphone, mất kết nối hoặc trình duyệt không hỗ trợ.

### Kết quả đạt được

- Có hướng xử lý microphone input trên frontend.
- Hiểu rõ hơn yêu cầu kỹ thuật của audio streaming.
- Bổ sung được các error state cần xử lý trong giao diện và tài liệu UAT.

---

## 16/06/2026

### Công việc đã thực hiện

- Bắt đầu tích hợp backend với Amazon Transcribe Streaming.
- Kiểm tra cấu hình AWS credential, region và quyền truy cập cần thiết.
- Thành viên Học máy nghiên cứu cách xử lý partial transcript và final transcript.
- Thành viên Hệ thống thông tin ghi nhận các tiêu chí đánh giá chất lượng transcript: độ trễ, độ chính xác và khả năng nhận diện tiếng Việt/tiếng Anh.

### Kết quả đạt được

- Backend có bước tích hợp ban đầu với Amazon Transcribe Streaming.
- Nhóm hiểu rõ hơn cách AWS trả về transcript theo thời gian thực.
- Xác định được cần phân biệt partial result và final result để tránh hiển thị nội dung bị trùng hoặc chưa ổn định.

---

## 17/06/2026

### Công việc đã thực hiện

- Bắt đầu tích hợp Amazon Translate vào luồng xử lý transcript.
- Thiết kế cách xử lý nội dung sau khi có transcript final: nhận text → gửi sang Amazon Translate → trả kết quả dịch về frontend.
- Kiểm tra cách hiển thị song ngữ giữa tiếng Việt và tiếng Anh.
- Cập nhật tài liệu mô tả luồng dữ liệu realtime của hệ thống.

### Kết quả đạt được

- Có luồng xử lý ban đầu cho transcript và translation.
- Xác định được cách kết hợp Amazon Transcribe Streaming và Amazon Translate trong backend.
- Làm rõ hơn flow kỹ thuật: audio stream → speech-to-text → translation → frontend display.

---

## 18/06/2026

### Công việc đã thực hiện

- Review lại prototype sau tuần đầu implementation.
- Kiểm tra các chức năng đã triển khai: frontend cơ bản, backend FastAPI, WebSocket session, microphone input, Transcribe integration và Translate integration ở mức ban đầu.
- Ghi nhận các lỗi còn tồn tại: độ ổn định kết nối, độ trễ transcript, xử lý partial/final transcript và trải nghiệm giao diện.
- Cập nhật kế hoạch cho tuần tiếp theo: hoàn thiện export transcript, kiểm thử end-to-end và chuẩn bị triển khai thử trên AWS.

### Kết quả đạt được

- Hoàn thành prototype kỹ thuật ban đầu của LiveCap.
- Xác định được các vấn đề cần tiếp tục cải thiện trước khi demo.
- Nhóm có định hướng rõ hơn cho giai đoạn tích hợp, kiểm thử và deployment ở tuần tiếp theo.

---

## Tổng kết tuần

Trong tuần này, nhóm bắt đầu triển khai prototype thực tế cho LiveCap, bao gồm xây dựng frontend bằng React/Vite, phát triển backend bằng FastAPI, thiết kế WebSocket session, xử lý microphone input và tích hợp bước đầu với Amazon Transcribe Streaming và Amazon Translate. Em học được rằng realtime application phức tạp hơn so với ứng dụng web thông thường vì hệ thống phải xử lý dữ liệu liên tục, duy trì kết nối WebSocket, quản lý trạng thái phiên và phản hồi nhanh cho người dùng. Việc phân biệt partial transcript và final transcript cũng là điểm kỹ thuật quan trọng để đảm bảo nội dung hiển thị không bị trùng hoặc gây khó hiểu. Sau tuần này, LiveCap đã có prototype ban đầu và nhóm sẵn sàng tiếp tục hoàn thiện export transcript, xử lý lỗi, kiểm thử end-to-end và triển khai thử trên AWS trong tuần tiếp theo.
