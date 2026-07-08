---
title: "Blog 3 - LLM Optimizer"
date: 2026-07-05
weight: 3
chapter: false
pre: " <b> 3.3 </b> "
---

# Tối ưu hóa LLM Inference trên Amazon SageMaker AI với BentoML LLM Optimizer

Triển khai các Large Language Models (LLMs) mã nguồn mở vào môi trường production là một quá trình phức tạp. Sự kết hợp giữa Amazon SageMaker AI và BentoML LLM Optimizer mang đến một giải pháp toàn diện để tự động hóa quá trình cấu hình, giải quyết triệt để bài toán cân bằng giữa hiệu năng và chi phí hạ tầng.

Dưới đây là chi tiết về cách tiếp cận này:

## 1. Những thách thức khi chạy LLM trên Production

Khi triển khai LLM, các kỹ sư thường gặp phải những rào cản kỹ thuật đáng kể sau:

- **Chi phí phần cứng đắt đỏ:** Các mô hình hàng tỷ tham số yêu cầu các instance GPU có dung lượng VRAM lớn, điều này có thể ngốn một khoản ngân sách khổng lồ nếu không được tối ưu đúng cách.
- **Sự đánh đổi giữa độ trễ (latency) và thông lượng (throughput):** Việc tăng thông lượng thường dẫn đến việc độ trễ tăng theo, ảnh hưởng trực tiếp đến trải nghiệm người dùng cuối.
- **Quá trình tinh chỉnh thủ công tốn thời gian:** Việc tìm ra sự kết hợp hoàn hảo giữa loại instance, tensor parallelism và quantization đòi hỏi rất nhiều vòng lặp thử và sai (trial-and-error).

## 2. BentoML LLM Optimizer giải quyết vấn đề này như thế nào?

Công cụ này đóng vai trò như một hệ thống benchmark và tìm kiếm tự động, thay thế hoàn toàn việc phỏng đoán:

- **Tự động hóa Profiling:** Hệ thống giả lập lưu lượng thực tế để đo lường hiệu năng của mô hình trên nhiều loại GPU instance khác nhau (chẳng hạn như G5 và P4 trên AWS).
- **Đóng gói chuẩn hóa:** BentoML tự động hóa việc container hóa mô hình và các thư viện phụ thuộc, đảm bảo tính nhất quán từ môi trường phát triển lên cloud.
- **Tích hợp sâu với SageMaker AI:** Tận dụng hạ tầng fully-managed của AWS, cho phép auto-scaling mượt mà và đảm bảo các tiêu chuẩn bảo mật cấp doanh nghiệp.

## 3. Những điểm đáng chú ý

- **Tối ưu VRAM hiệu quả:** Hệ thống cung cấp các tham số chính xác để áp dụng quantization (ví dụ: FP16, INT8), giúp các LLM lớn có thể chạy ổn định ngay cả trên các GPU có bộ nhớ hạn chế.
- **Đề xuất cấu hình tối ưu:** Công cụ chỉ ra cụ thể loại AWS Instance nào mang lại thông lượng cao nhất với chi phí trên mỗi token thấp nhất.
- **Giảm thiểu rủi ro:** Ngăn chặn tình trạng cấp phát thừa tài nguyên (over-provisioning) gây lãng phí, hoặc cấp phát thiếu (under-provisioning) dẫn đến thắt cổ chai hệ thống khi có lưu lượng tăng đột biến.

## 4. Giá trị kinh doanh

Việc áp dụng kiến trúc này giải phóng hoàn toàn các team MLOps và Data Engineering khỏi gánh nặng phải tự viết các kịch bản test thủ công. Nó giúp rút ngắn thời gian ra mắt (time-to-market) cho các tính năng Generative AI từ vài tuần xuống chỉ còn vài ngày, đồng thời mang lại sự minh bạch và khả năng kiểm soát chặt chẽ đối với chi phí cloud hàng tháng.

## 5. Các bước triển khai và sử dụng cơ bản

Để áp dụng giải pháp này vào dự án thực tế, quy trình chung thường bao gồm các bước sau:

1. **Bước 1 - Chuẩn bị môi trường:** Cài đặt thư viện `bentoml` và các công cụ hỗ trợ AWS (như `bentoML-sagemaker`), sau đó cấu hình một IAM Role với đầy đủ quyền tương tác với SageMaker và Amazon ECR.
2. **Bước 2 - Khai báo mô hình (Bento Build):** Tạo các file cấu hình (như `service.py` và `bentofile.yaml`) để khai báo LLM bạn muốn sử dụng. Tiếp theo, chạy lệnh build của BentoML để đóng gói mô hình thành một định dạng chuẩn.
3. **Bước 3 - Chạy LLM Optimizer:** Kích hoạt công cụ benchmark của BentoML. Hệ thống sẽ tự động cấp phát các môi trường test trên AWS và chạy load test với các tham số phần mềm và phần cứng khác nhau.
4. **Bước 4 - Đánh giá và Cấu hình:** Optimizer sẽ trả về một báo cáo trực quan so sánh thông lượng và độ trễ. Dựa trên phân tích này, bạn có thể chọn cấu hình có độ trễ p99 và chi phí tối ưu nhất cho use-case cụ thể của mình.
5. **Bước 5 - Triển khai lên SageMaker:** Sử dụng cấu hình đã chọn để push container lên Amazon ECR và tạo SageMaker Endpoint trực tiếp thông qua các lệnh CLI của BentoML, hoàn tất quá trình đưa mô hình lên production.

![Sơ đồ tổng quan về quy trình thực hiện trong bài viết.](/images/3-BlogsPosted/blog3-1.png)

[**Link bài viết trên AWS Study Group**](https://www.facebook.com/groups/awsstudygroupfcj/posts/2206721756759451/?notif_id=1783392652127913&notif_t=group_post_approved&ref=notif)
