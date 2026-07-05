---
title: "Sự kiện 4: Enterprise Cloud Architectures and Industry Applications"
date: 2026-07-04
weight: 4
chapter: false
pre: " <b> 4.4. </b> "
---

# Enterprise Cloud Architectures and Industry Applications

| Trường | Nội dung |
| --- | --- |
| Tên sự kiện | Enterprise Cloud Architectures and Industry Applications |
| Ngày/giờ | 04 tháng 7 năm 2026 |
| Địa điểm | AWS Event Hall, Tầng 26, Bitexco Financial Tower, TP. Hồ Chí Minh |
| Vai trò | Người tham gia |

## Mở đầu

Là sinh viên năm cuối ngành Hệ thống Thông tin và đang tham gia AWS Bootcamp, sự kiện giúp em nhìn rõ khoảng cách giữa việc biết công nghệ và khả năng dùng công nghệ để giải quyết vấn đề doanh nghiệp.

Bốn phần chia sẻ đề cập đến thị trường cloud và career visibility; Data Architecture thực tế; giao tiếp và chiến lược “Blue Ocean”; tư duy AI cho fresher. Giá trị lớn nhất với em là cách chuyển các bài học thành hành động cho nghề nghiệp và project của em.

## Chủ đề 1 – Nguyễn Gia Hưng: Thị trường cloud, khoảng cách kỹ năng và career visibility

![Nguyễn Gia Hưng chia sẻ về thị trường việc làm và xu hướng nghề nghiệp](/images/4-EventParticipated/Event4/nguyen-gia-hung.png)

*Nguyễn Gia Hưng chia sẻ về thị trường việc làm, xu hướng nghề nghiệp và định hướng phát triển năng lực trong lĩnh vực cloud.*

Anh Nguyễn Gia Hưng chia sẻ rằng **cloud-first đang dần trở thành định hướng mặc định của doanh nghiệp hiện đại**. Cloud Computing không còn chỉ là một xu hướng kỹ thuật, mà là chiến lược dài hạn liên quan đến hạ tầng và hoạt động kinh doanh. Theo phần trình bày, AWS không vào Việt Nam chỉ để bán giấy phép rồi rời đi. Chiến lược đầu tư có thể nhìn qua ba trụ cột: nhân lực địa phương, hạ tầng và thế hệ nhân tài tương lai.

Phần lớn nhân sự Amazon/AWS tại Việt Nam là người Việt, cho thấy sự đầu tư vào năng lực bản địa. Các hạng mục như CDN, caching, Local Zone và nền tảng độ trễ thấp thể hiện cam kết hạ tầng dài hạn. Trụ cột còn lại là phát triển thế hệ builder tiếp theo: thị trường cần người có thể xây dựng hệ thống chứ không chỉ nắm lý thuyết.

AI có thể hỗ trợ hoặc thay thế một số tác vụ junior, trong khi kỳ vọng về tư duy hệ thống tăng lên. Ngay cả intern có thể bị loại nếu chưa hiểu production system, Kubernetes hoặc hạ tầng. Bằng cấp, chứng chỉ và tiếng Anh vẫn hữu ích nhưng chỉ là một phần của “vé vào cửa”; độ sâu dự án và bằng chứng học tập công khai mới làm năng lực đáng tin cậy.

Anh tóm tắt quá trình phát triển nghề nghiệp bằng công thức:

> **Result = Capability × Visibility × Consistency**

Capability là năng lực thật; Visibility thể hiện qua networking, GitHub, blog, side project và giao tiếp; Consistency là học liên tục. Nhiều cơ hội đến từ referral hoặc mạng lưới nội bộ. Một dự án có source code rõ, README, hướng dẫn triển khai và giải thích kiến trúc vì vậy thuyết phục hơn sản phẩm chỉ chạy trên máy cá nhân. Việc định vị cũng nên kết hợp role với domain, chẳng hạn cloud/data trong tài chính hoặc bán lẻ.

Từ phần này, em nhận ra học dịch vụ AWS là chưa đủ. Em phải chứng minh mình có thể xây dựng, giải thích, tài liệu hóa và cải tiến một hệ thống. Chứng chỉ là tín hiệu đầu vào, không phải đích đến. Với project của em, Amazon Transcribe và Amazon Translate chỉ là điểm bắt đầu; dự án còn phải thể hiện tư duy triển khai, bảo mật, giám sát, chi phí, khả năng mở rộng và tài liệu vận hành.

## Chủ đề 2 – Bình Cẩm Vĩnh: Khoảng cách thực tế trong Data Architecture

![Bình Cẩm Vĩnh chia sẻ về nền tảng cần thiết cho Data Architecture](/images/4-EventParticipated/Event4/binh-cam-vinh.png)

*Bình Cẩm Vĩnh trình bày các nền tảng kỹ thuật và tư duy hệ thống cần thiết khi phát triển trong lĩnh vực dữ liệu.*

Anh Bình Cẩm Vĩnh phân tích sự khác biệt giữa bài tập ở trường và hệ thống dữ liệu doanh nghiệp. Ở trường, dữ liệu thường sạch, nhỏ và yêu cầu rõ; làm sai thường chỉ mất điểm. Trong doanh nghiệp, dữ liệu đến từ nhiều nguồn, thay đổi liên tục và có định nghĩa khác nhau giữa các bộ phận. Yêu cầu có thể đổi nhanh, còn sai sót có thể làm gián đoạn production, ảnh hưởng doanh thu và niềm tin.

Thông điệp “**One framework for every platform**” cho thấy sinh viên không nên chỉ học thuộc công cụ. Điều quan trọng là hiểu “DNA” kiến trúc. Với Data Engineering, khung cốt lõi có thể gồm thu thập, xử lý, lưu trữ, quản trị và phân phối dữ liệu. Khi hiểu luồng này, mỗi công cụ hoặc dịch vụ cloud mới được đặt đúng vai trò.

Qua startup, doanh nghiệp lớn như Heineken và fintech như ZaloPay, diễn giả cho thấy kỹ thuật chỉ là một phần. Mỗi môi trường có yêu cầu khác nhau về xây dựng từ đầu, thống nhất khái niệm kinh doanh, tải cao và độ ổn định. Kỹ sư phải chuyển yêu cầu kinh doanh thành ngôn ngữ kỹ thuật. AI hỗ trợ code hoặc báo cáo nhưng chưa thay được hiểu biết nghiệp vụ, quyết định kiến trúc và giao tiếp.

Bài học của em là Data Architecture không đơn giản là chọn database, ETL hay dashboard. Phần khó hơn nằm ở luồng dữ liệu, định nghĩa nghiệp vụ, quyền sở hữu, độ tin cậy và khả năng thích ứng khi yêu cầu đổi. Đây là nền tảng chung cho Cloud/Data Platform Engineering, BSA và Solution Architect.

Trong project của em, em cần mô tả rõ transcript bắt đầu từ đâu, dữ liệu phiên âm và bản dịch được xử lý hoặc lưu trữ thế nào, định dạng export phục vụ người dùng ra sao và thời gian lưu giữ phù hợp là bao lâu. Hệ thống cũng cần tính đến phiên bị gián đoạn, dữ liệu chưa hoàn chỉnh, lỗi dịch vụ và nhu cầu phân tích tương lai. Như vậy, project này mới trở thành một hệ thống nhỏ nhưng thực tế, không phải bản demo chỉ chạy thành công một lần.

## Chủ đề 3 – Trần Như: Vượt qua nỗi sợ, giao tiếp và chiến lược Blue Ocean

![Trần Như tại sự kiện Enterprise Cloud Architectures and Industry Applications](/images/4-EventParticipated/Event4/nhu-tran.png)

*Trần Như giao lưu cùng người tham dự tại sự kiện Enterprise Cloud Architectures and Industry Applications.*

Chị Trần Như phân tích rằng chúng ta thường sợ hậu quả của lỗi sai như điểm thấp, bị đánh giá hoặc làm gia đình thất vọng. Nỗi sợ nói trước đám đông cũng đến từ việc sợ bị phán xét. Một cách cải thiện là giao tiếp cởi mở và xem việc trình bày như một dạng thực tập, giảm sợ hãi qua trải nghiệm lặp lại.

Hiểu lầm thường đến từ góc nhìn khác nhau: kỹ thuật tập trung tạo giá trị, còn sales tập trung truyền đạt giá trị. Giao tiếp tốt đòi hỏi hiểu ý định phía sau yêu cầu. Small talk cũng giúp giảm khoảng cách với quản lý và tạo visibility về thái độ, giao tiếp, độ tin cậy mà không phải khoe bản thân.

Ứng tuyển qua job board là bước vào “Red Ocean” có nhiều ứng viên; “Blue Ocean” được tạo qua quan hệ, niềm tin, cộng đồng và sự hiện diện nhất quán. Chị từng bị Amazon từ chối mười lần, nhưng lần thứ mười một được một senior công nhận sự tận tâm và giới thiệu với Hiring Manager. Câu chuyện cho thấy uy tín và quan hệ có thể mở ra cơ hội ngoài một lần gửi CV.

Em nhận ra giao tiếp không phải “kỹ năng mềm” tách rời chuyên môn. Nó tác động trực tiếp đến làm rõ yêu cầu, phối hợp nhóm, phỏng vấn và cơ hội nghề nghiệp. Nếu hướng đến BSA hoặc Solution Architect, em phải biết đặt câu hỏi, nhận ra ý định ẩn, giải thích trade-off và xây dựng niềm tin với stakeholder. Em cũng không nên chờ đến khi “hoàn toàn sẵn sàng” mới xuất hiện; visibility phải được xây dựng đều qua cộng đồng, sự kiện, LinkedIn, GitHub và chia sẻ dự án.

Project của em liên hệ trực tiếp với bài học này vì nó giải quyết một vấn đề giao tiếp: giúp người dùng theo dõi workshop, cuộc họp và thảo luận song ngữ rõ ràng hơn. Em cần trình bày project từ nỗi đau và giá trị người dùng nhận được, không chỉ từ danh sách dịch vụ kỹ thuật.

## Chủ đề 4 – Nguyễn Khang: Tư duy AI và hướng đi dài hạn cho fresher

![Nguyễn Khang chia sẻ về kỹ năng và tư duy cho fresher trong kỷ nguyên AI](/images/4-EventParticipated/Event4/khang-nguyen.png)

*Nguyễn Khang trình bày chủ đề AI-Ready Freshers và cách xây dựng nền tảng trong bối cảnh AI phát triển nhanh.*

Anh Nguyễn Khang đưa ra nguyên tắc: **“You can outsource thinking, but you cannot outsource understanding.”** AI có thể tăng tốc công việc nhưng không thể thay thế sự hiểu biết của người dùng. AI là một bộ khuếch đại: nền tảng tốt giúp làm nhanh hơn; nền tảng yếu có thể khiến người dùng chấp nhận kết quả sai mà không nhận ra. Sinh viên vẫn cần kiến thức vững về lập trình, system design, cloud, data và nghiệp vụ.

Khi chọn việc, fresher cần cân nhắc Passion, Responsibility và Benefit. Benefit không chỉ là lương mà còn gồm trải nghiệm, mạng lưới và kiến thức. Một công việc có mentor tốt, bài toán đủ khó và exposure thực tế có thể tạo nền tảng dài hạn tốt hơn mức lương ban đầu cao.

Doanh nghiệp đánh giá fresher qua Attitude, Skill level, Experience, Exposure và Talent. Thái độ phản ánh tiềm năng học hỏi và độ tin cậy; Exposure thể hiện độ đa dạng của trải nghiệm, không chỉ số năm làm việc. Diễn giả khuyên nên hỏi “tại sao”, xây dựng tầm nhìn dài hạn, làm việc đa chức năng và duy trì nhất quán. Tính chính trực còn thể hiện ở việc làm dự án vượt mức tối thiểu để lấy điểm.

Em có thể dùng AI để tăng tốc coding, tài liệu hóa, debugging và so sánh kiến trúc, nhưng không giao việc hiểu AWS hoặc yêu cầu cho AI. Với project của em, AI nên là reviewer và accelerator. Em phải tự giải thích CloudFront, S3, CloudWatch, Transcribe, Translate và vì sao kiến trúc mục tiêu có thể cân nhắc ALB, ECS/Fargate, WAF; đồng thời trình bày trade-off về chi phí, độ trễ, bảo mật và vận hành.

## Bài học tổng hợp sau sự kiện

Bốn chủ đề tạo thành một mạch thống nhất. Từ anh Nguyễn Gia Hưng, em học rằng phát triển nghề nghiệp cần Capability, Visibility và Consistency. Từ anh Bình Cẩm Vĩnh, em hiểu hệ thống thực tế đòi hỏi tư duy kiến trúc cùng khả năng hiểu business. Từ chị Trần Như, em nhận ra giao tiếp, sự hiện diện và quan hệ tin cậy có thể tạo ra cơ hội ngoài quy trình ứng tuyển công khai. Từ anh Nguyễn Khang, em xác định AI nên khuếch đại năng lực chứ không thay thế sự hiểu biết.

Kỹ thuật cần thiết nhưng chưa đủ. Để theo đuổi Cloud/Data Platform Engineering, Business System Analyst và Solution Architect, em phải hiểu kinh doanh, giao tiếp rõ, xây dựng visibility và học nhất quán. Ba hướng này gặp nhau ở khả năng hiểu nhu cầu, thiết kế hệ thống và giải thích giải pháp bằng ngôn ngữ kỹ thuật lẫn kinh doanh.

## Đóng góp cá nhân và kế hoạch áp dụng vào project của em

Sau sự kiện, em xác định năm nhóm hành động cụ thể:

1. **Phát triển project của em từ “working demo” thành sản phẩm có tư duy production.** Em sẽ làm rõ kiến trúc, runtime flow, vai trò dịch vụ AWS và phân biệt phần đã triển khai với kiến trúc mục tiêu. Tài liệu cần nêu chi phí, bảo mật, logging, monitoring và hướng mở rộng.

2. **Tăng visibility của dự án.** Em sẽ giữ repository rõ ràng, cải thiện README, setup guide và viết bài kỹ thuật. Mỗi thay đổi cần trả lời: em học gì, đổi gì và vì sao. GitHub, LinkedIn sẽ là bằng chứng của quá trình học, không chỉ là nơi đăng kết quả.

3. **Hiểu người dùng và nghiệp vụ.** Em cần xác định ai sử dụng project này, họ gặp khó khăn ở đâu và đầu ra nào hữu ích. Transcript export phải dễ đọc, có cấu trúc, hỗ trợ xem lại workshop, cuộc họp và trao đổi song ngữ thay vì chỉ là dữ liệu tải xuống.

4. **Sử dụng AI có trách nhiệm.** Em sẽ dùng AI để review code, tài liệu, kiến trúc và phát hiện vấn đề production. Mọi đề xuất quan trọng phải được kiểm tra và em phải tự giải thích quyết định cuối cùng. Khả năng kiểm chứng vẫn là trách nhiệm của người xây dựng.

5. **Chuẩn bị có định hướng.** Em sẽ đào sâu AWS, data flow, system design, deployment và luyện cách giải thích hệ thống bằng ngôn ngữ kỹ thuật lẫn nghiệp vụ. Em cũng cần tham gia sự kiện, xây dựng quan hệ và cập nhật GitHub, blog, LinkedIn đều đặn thay vì chỉ làm gần deadline.

## Kết luận

Sẵn sàng cho nghề nghiệp không chỉ là biết công cụ. Em cần hiểu hệ thống, kinh doanh, giao tiếp, AI và cách làm năng lực được nhìn thấy. Bước tiếp theo là cải thiện project của em như một sản phẩm kỹ thuật và portfolio artifact thể hiện quá trình học, tư duy production cùng định hướng nghề nghiệp.
