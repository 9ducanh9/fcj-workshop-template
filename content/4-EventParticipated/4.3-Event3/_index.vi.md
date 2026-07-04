---
title: "Sự kiện 3: Week 3 Reflection – Data Analytics, DevOps, AWS Community và tư duy xây dựng hệ thống thực tế"
date: 2026-06-13
weight: 3
chapter: false
pre: " <b> 4.3. </b> "
---

# Week 3 Reflection: Data Analytics, DevOps, AWS Community và tư duy xây dựng hệ thống thực tế

| Trường | Nội dung |
| --- | --- |
| Tên sự kiện | Week 3 Reflection: Data Analytics, DevOps, AWS Community và tư duy xây dựng hệ thống thực tế |
| Ngày/giờ | 13 tháng 6 năm 2026 |
| Địa điểm | AWS Event Hall, Tầng 26, Bitexco Financial Tower, TP. Hồ Chí Minh |
| Vai trò | Người tham gia |

## Mở đầu

Week 3 giúp tôi quan sát công việc công nghệ qua bốn góc độ liên quan: Data Analytics Engineering trong doanh nghiệp; DevOps và vòng đời ứng dụng; cộng đồng AWS; và thiết kế giải pháp qua bài toán URL Shortening Service.

Điểm chung là kỹ thuật chỉ tạo giá trị khi đi cùng tư duy hệ thống, nghiệp vụ, giao tiếp và vận hành. LiveCap vì vậy không nên dừng ở việc kết nối dịch vụ AWS, mà phải thể hiện vấn đề người dùng, luồng dữ liệu và quyết định kiến trúc.

## Chủ đề 1 – Cường Nguyễn và Đạt Phạm: Data Analytics Engineer và văn hóa MNC

Hai diễn giả cho thấy Data Analytics Engineering khác bài phân tích ở trường. Tại Kamereo, công việc gồm báo cáo ngày, tuần, tháng; dashboard xu hướng; phát hiện bất thường và root cause analysis cho quyết định vận hành. Tại Colgate-Palmolive, dữ liệu gắn với máy móc, IoT, tối ưu chi phí sản xuất, hiệu quả vận hành và chuyển đổi số.

Data Analytics Engineer không chỉ báo cáo số liệu. Khi GMV biến động, dashboard mới trả lời “điều gì đã xảy ra”; critical thinking phải tìm “vì sao” và đề xuất cải thiện. Data Storytelling chuyển số liệu thành câu chuyện để stakeholder hiểu và hành động.

Mô hình phát triển gồm **Follower**, người học theo hướng dẫn; **Learner**, bắt đầu chủ động nhưng vẫn cần mentor; **Problem Solver**, có thể phân tích và đề xuất; **System Thinker**, nhìn thấy quan hệ và rủi ro dài hạn; cuối cùng là **Super Star**, người xây dựng tầm nhìn và phát triển thế hệ sau. Văn hóa MNC còn dùng mô hình STAR để đánh giá hành vi, kinh nghiệm và No-Blame Post-Mortem để tìm nguyên nhân gốc thay vì quy lỗi cá nhân.

Tôi nhận ra giá trị của Data Analytics Engineering nằm ở việc giúp doanh nghiệp hiểu chuyện gì xảy ra, nguyên nhân và quyết định tiếp theo. Điều này liên quan trực tiếp đến Cloud/Data Platform Engineering, BSA và Solution Architect, nơi kỹ thuật phải gắn với bối cảnh nghiệp vụ.

Với LiveCap, transcript nên trở thành đầu ra dễ đọc, có timestamp, người nói, bản dịch, tóm tắt và định dạng export tái sử dụng. Khi có lỗi, tôi cần ghi triệu chứng, nguyên nhân gốc và cách phòng ngừa thay vì chỉ vá để hệ thống chạy lại.

## Chủ đề 2 – Trong H. Truong: Giải mã vai trò DevOps Engineer

Anh Trong H. Truong làm rõ rằng DevOps không chỉ là CI/CD, Docker, Kubernetes hay xử lý sự cố lúc nửa đêm. Bản chất là hiểu ứng dụng được build, test, deploy, cấu hình, giám sát và bảo trì thế nào.

Lộ trình bắt đầu từ Linux, networking và Python hoặc Golang, sau đó đi vào cách ứng dụng chạy, build, test, deploy và quản lý environment variable. Thực hành nên bắt đầu bằng ứng dụng đơn giản, tự động hóa, thêm monitoring, rồi học qua việc làm hỏng và sửa hệ thống.

Triết lý chính là hỏi **“Why” trước “How”**: hiểu lý do quan trọng hơn sao chép command. DevOps không phải vai trò “người hùng cô độc”; giao tiếp và automation phải làm quy trình rõ, lặp lại được cho cả nhóm. System thinking kết nối application, infrastructure, security và operations. AI tạo đòn bẩy nhưng không thay sự hiểu biết.

Bài học của tôi là DevOps chính là production thinking. LiveCap cần build, deploy, cấu hình an toàn, logging, monitoring, error handling, kiểm soát chi phí và phục hồi. Tôi phải giải thích không chỉ “triển khai thế nào” mà cả “vì sao chọn mô hình này”.

Tôi cần giải thích được CloudFront, S3, CloudWatch, Transcribe, Translate và khi nào kiến trúc mục tiêu nên cân nhắc ALB, ECS/Fargate hay WAF. Mỗi lựa chọn có trade-off về đơn giản, chi phí, mở rộng, bảo mật và vận hành. AI có thể review, nhưng quyết định cuối cùng phải do tôi hiểu và trình bày được.

## Chủ đề 3 – Danh Hoàng Hiếu Nghị: Hệ sinh thái AWS và cộng đồng

Anh Danh Hoàng Hiếu Nghị nhấn mạnh rằng có được công việc Solutions Architect, DevOps Engineer hay Software Engineer chỉ là điểm bắt đầu. Phát triển nghề nghiệp còn đến từ cộng đồng, sự kiện, chia sẻ, networking và đóng góp, không chỉ lớp học hay chứng chỉ.

**First Cloud AI Journey**, phát triển từ First Cloud Journey, cung cấp lộ trình cloud và AI có cấu trúc. **AWS Student Builder Group** kết nối sinh viên với các learner, builder khác. **AWS Community Builder** và **AWS Partners** mở rộng cơ hội kết nối, đóng góp và phát triển chuyên môn.

Tôi hiểu cộng đồng là môi trường xây dựng visibility, consistency và bản sắc nghề nghiệp. Sinh viên có thể trưởng thành bằng cách đặt câu hỏi, viết reflection, tài liệu hóa dự án và chia sẻ điều đã học. Những hoạt động này cũng rèn giao tiếp và khả năng tạo niềm tin cần cho Cloud/Data Platform Engineering, BSA và Solution Architect.

Phản hồi cộng đồng giúp kiểm tra LiveCap có giải quyết đúng vấn đề workshop, cuộc họp và học tập song ngữ hay không. Tiến độ trên GitHub hoặc LinkedIn là bằng chứng về năng lực và tính nhất quán. AWS Bootcamp có thể trở thành điểm khởi đầu cho việc học AWS và tham gia cộng đồng lâu dài.

## Chủ đề 4 – Kiên và Thọ: Thiết kế giải pháp AWS qua URL Shortening Service

Hai diễn giả trình bày URL Shortening Service: hệ thống nhận URL dài, tạo URL ngắn và redirect về địa chỉ ban đầu. Tính năng đơn giản nhưng đòi hỏi thiết kế có thể mở rộng và vận hành ổn định.

Các câu hỏi gồm cách tạo mã duy nhất, lưu mapping, xử lý traffic lớn, redirect nhanh, theo dõi sử dụng và duy trì availability. Người thiết kế phải xem scalability, routing, storage, latency, monitoring và vận hành như một hệ thống thống nhất.

Ví dụ thể hiện tư duy Solution Architect: bắt đầu từ yêu cầu, xác định non-functional requirements, chọn thành phần và giải thích trade-off. Không nên thêm dịch vụ để sơ đồ trông phức tạp; mỗi thành phần phải giải quyết một yêu cầu cụ thể.

LiveCap cũng có độ phức tạp ẩn: truyền audio, phiên âm, dịch, lưu transcript, export, giám sát lỗi, chi phí và mở rộng. Chất lượng dự án vì vậy nằm cả ở kiến trúc và khả năng giải thích vì sao kiến trúc phù hợp, không chỉ ở danh sách tính năng.

## Bài học tổng hợp sau Week 3

Bốn chủ đề bổ sung cho nhau: dữ liệu phải dẫn đến quyết định; DevOps phải hiểu vận hành thật; cộng đồng AWS xây dựng visibility và consistency; một dịch vụ đơn giản vẫn cần system design nghiêm túc khi mở rộng.

Kỹ thuật cần thiết nhưng chưa đủ. Nghiệp vụ, giao tiếp, cộng đồng, production mindset và tư duy hệ thống là nền tảng chung cho Cloud/Data Platform Engineering, Business System Analyst và Solution Architect.

## Đóng góp cá nhân và kế hoạch áp dụng vào LiveCap

Sau Week 3, tôi xác định năm nhóm hành động:

1. **Cải thiện production readiness.** Tôi sẽ rà soát deployment flow, làm rõ environment configuration, bổ sung tài liệu logging, monitoring, error handling và retry. Kiến trúc cần mô tả cách mở rộng, cân nhắc chi phí, bảo mật và phương án phục hồi khi thành phần gặp lỗi.

2. **Tăng giá trị dữ liệu và giá trị người dùng.** Transcript và bản dịch cần được xem là dữ liệu có thể tái sử dụng. Tôi sẽ cải thiện export format, xem xét timestamp, speaker separation, chất lượng dịch và session history dựa trên điều người dùng thực sự cần sau workshop hoặc cuộc họp.

3. **Cải thiện tài liệu và visibility.** README, giải thích kiến trúc và hướng dẫn setup/deployment phải đủ rõ để người khác hiểu dự án. Tôi sẽ tiếp tục viết reflection, cập nhật tiến độ trên GitHub và chia sẻ phù hợp trên LinkedIn như bằng chứng về capability, visibility và consistency.

4. **Thực hành DevOps và system thinking.** Tôi không xem một lần deploy thành công là điểm kết thúc. Tôi cần hiểu LiveCap chạy, lỗi, phục hồi, ghi log và mở rộng thế nào; luôn hỏi “why” trước khi chọn công cụ. AI được dùng để review và tăng tốc, nhưng tôi phải tự giải thích từng quyết định.

5. **Chuẩn bị cho định hướng nghề nghiệp.** Tôi sẽ đào sâu AWS, data architecture, system design và deployment; đồng thời luyện cách giải thích hệ thống bằng ngôn ngữ kỹ thuật lẫn kinh doanh. Việc tham gia cộng đồng, đặt câu hỏi và tài liệu hóa quá trình học sẽ giúp tôi từng bước chuyển từ Learner sang Problem Solver và System Thinker.

## Kết luận

Week 3 giúp tôi hiểu kỹ thuật thực tế không chỉ là viết code hoặc sử dụng dịch vụ cloud. Data Analytics cần tạo tác động kinh doanh; DevOps cần hiểu vận hành; cộng đồng AWS cần sự tham gia và đóng góp; còn thiết kế giải pháp cần tư duy hệ thống. Bước tiếp theo của tôi là tiếp tục phát triển LiveCap thành một dự án kỹ thuật và portfolio artifact thể hiện rõ quá trình học, production mindset và định hướng nghề nghiệp.
