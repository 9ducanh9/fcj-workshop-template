---
title: "Sự kiện 1: AWS Study Group Technical Sharing"
date: 2026-05-09
weight: 1
chapter: false
pre: " <b> 4.1. </b> "
---

# Sự kiện 1: AWS Study Group Technical Sharing

| Trường | Nội dung |
| --- | --- |
| Tên sự kiện | AWS Study Group Technical Sharing |
| Ngày/giờ | 09 tháng 5 năm 2026 |
| Địa điểm | AWS Event Hall, Tầng 26, Bitexco Financial Tower, TP. Hồ Chí Minh |
| Vai trò | Người tham gia |

![Ảnh chụp chung tại AWS Study Group Technical Sharing](/images/4-EventParticipated/Event1/group-photo.png)

*Diễn giả, ban tổ chức và người tham dự AWS Study Group Technical Sharing.*

Buổi event đầu tiên tập trung vào một chủ đề rất thực tế đối với sinh viên công nghệ hiện nay: **làm sao để học hiệu quả hơn, dùng AI đúng cách hơn và chuẩn bị tốt hơn cho môi trường làm việc thực tế**.

Bốn phần chia sẻ tuy khác nhau về nội dung nhưng cùng hướng đến một điểm chung: trong thời đại AI, người học không chỉ cần biết sử dụng công cụ mà còn phải có **nền tảng tư duy**, **khả năng đặt câu hỏi**, **kỷ luật học tập** và **quy trình làm việc rõ ràng**.

## Chủ đề 1 – Huỳnh Hoàng Long: Addicted to Learning Like You're Addicted to Social Media

![Huỳnh Hoàng Long chia sẻ tại AWS Study Group Technical Sharing](/images/4-EventParticipated/Event1/long-hoang.png)

*[Huỳnh Hoàng Long](https://www.linkedin.com/in/huynhhoanglong1812003/) chia sẻ về cách xây dựng động lực và duy trì thói quen học tập.*

Phần chia sẻ đầu tiên nói về cách “hack” não bộ để biến việc học trở nên hấp dẫn hơn, tương tự cách mạng xã hội và game online giữ chân người dùng.

Điểm đáng chú ý là mạng xã hội và game không khiến người dùng quay lại chỉ vì phần thưởng mà còn vì cảm giác **mong đợi phần thưởng**. Dopamine không đơn giản xuất hiện khi chúng ta nhận được kết quả mà còn xuất hiện mạnh khi não dự đoán một phần thưởng sắp đến. Nếu áp dụng cơ chế này vào học tập, việc học có thể bớt nhàm chán và dễ duy trì hơn.

Một số cách em có thể áp dụng gồm:

* Tạo streak học mỗi ngày để hình thành cảm giác tiếc nếu bỏ lỡ.
* Chia nhỏ mục tiêu học tập thay vì đặt một mục tiêu quá lớn.
* Tự thưởng sau khi hoàn thành một cột mốc.
* Biến quá trình học thành một hệ thống có level, checkpoint và achievement.

Ví dụ, thay vì đặt mục tiêu “học hết cloud trong một tháng”, em có thể chia nhỏ theo từng dịch vụ: hôm nay học S3, hôm sau học IAM, tiếp theo là Lambda hoặc CloudWatch. Cách này làm mục tiêu rõ ràng hơn, giảm cảm giác quá tải và tạo cảm giác tiến bộ liên tục.

Điều em rút ra là **kỷ luật học tập không nhất thiết phải bắt đầu bằng việc ép bản thân học thật nhiều**. Em có thể bắt đầu bằng cách thiết kế lại môi trường học để mỗi nhiệm vụ đều có phản hồi, tiến độ và phần thưởng rõ ràng.

## Chủ đề 2 – Nguyễn Thịnh: Automated Prompt Engineering – Enhancing LLM Output Quality

![Nguyễn Thịnh trình bày lý do Prompt Engineering quan trọng](/images/4-EventParticipated/Event1/thinh-nguyen.png)

*[Nguyễn Thịnh](https://www.linkedin.com/in/thinhnguyen1211/) trình bày cách xây dựng prompt rõ ràng và tối ưu chất lượng đầu ra của AI.*

Phần thứ hai đi sâu vào Prompt Engineering, tức là cách giao tiếp với AI để nhận được đầu ra tốt hơn. Một prompt tốt không chỉ là một câu hỏi đơn giản mà nên có cấu trúc rõ ràng với bảy thành phần:

* **Role:** AI cần đóng vai trò gì.
* **Instruction:** AI cần thực hiện nhiệm vụ gì.
* **Context:** Bối cảnh của bài toán.
* **Input:** Dữ liệu đầu vào.
* **Output format:** Định dạng đầu ra mong muốn.
* **Example:** Ví dụ minh họa.
* **Constraint:** Các ràng buộc cần tuân thủ.

AI không thể tự hiểu hoàn toàn ý định của người dùng nếu prompt còn mơ hồ. Prompt càng làm rõ vai trò, ngữ cảnh, dữ liệu và định dạng thì kết quả càng dễ kiểm soát và kiểm chứng.

Diễn giả cũng đề cập đến token và cách tối ưu prompt. Với tiếng Việt, lượng token có thể lớn hơn nên khi làm việc với LLM cần chú ý độ dài đầu vào, cách chia nhỏ yêu cầu và mức độ chi tiết thực sự cần thiết. Các kỹ thuật như Chain of Thought, Self-consistency và Tree of Thoughts cũng được giới thiệu để hỗ trợ các bài toán suy luận phức tạp.

Điểm em thấy thực tế nhất là phần demo Prompt Optimizer trên AWS. Ứng dụng kết hợp CloudFront, S3, Cognito, API Gateway, Lambda, Bedrock và DynamoDB. Đây là ví dụ cho thấy việc đưa AI vào một hệ thống thực tế không chỉ dừng ở gọi chatbot mà còn liên quan đến xác thực, backend, cơ sở dữ liệu, logging, bảo mật và chi phí vận hành.

Bài học em rút ra là **Prompt Engineering không chỉ là viết câu hỏi hay mà là thiết kế cách giao tiếp giữa con người, AI và hệ thống phần mềm**.

## Chủ đề 3 – Nguyễn Khang: AI-ready Freshers – Skill and Mindset in the AI Era

![Nguyễn Khang trình bày Growth Mindset và thói quen hỏi Why](/images/4-EventParticipated/Event1/khang-nguyen.png)

*[Nguyễn Khang](https://www.linkedin.com/in/khangck/) chia sẻ về nền tảng, tư duy giải quyết vấn đề và thái độ cần thiết của fresher trong thời đại AI.*

Phần chia sẻ thứ ba tập trung vào sinh viên năm ba, năm tư đang chuẩn bị đi làm trong bối cảnh AI phát triển nhanh. Thông điệp chính là: **AI không thay thế em, AI khuếch đại em**.

Nếu một người chưa có nền tảng, AI có thể khiến họ phụ thuộc và dễ bộc lộ điểm yếu khi bài toán thay đổi. Ngược lại, nếu có tư duy tốt, AI sẽ giúp họ làm nhanh hơn, mở rộng năng lực và tạo ra kết quả tốt hơn.

Doanh nghiệp không nhất thiết cần fresher biết thật nhiều công cụ. Những yếu tố quan trọng hơn gồm:

* Có kiến thức nền tảng.
* Có tư duy giải quyết vấn đề.
* Biết giải thích vì sao chọn một giải pháp.
* Có thái độ làm việc nghiêm túc.
* Có integrity, tức là làm đúng ngay cả khi không có ai kiểm tra.

Một ý rất đáng nhớ là nhiều quyết định kỹ thuật trong doanh nghiệp không đơn giản là đúng hoặc sai tuyệt đối. Một giải pháp có thể đúng trong ngữ cảnh này nhưng không phù hợp trong ngữ cảnh khác. Vì vậy, câu hỏi “Why?” thường quan trọng hơn câu hỏi “What?”. Em không chỉ cần biết em đang làm gì mà còn phải hiểu tại sao em lựa chọn cách làm đó.

Phần này đặc biệt liên quan đến định hướng Solution Architect hoặc Business System Analyst của em. Hai vai trò đều yêu cầu khả năng phân tích vấn đề, đặt câu hỏi, hiểu trade-off và giải thích quyết định cho người khác chứ không chỉ biết sử dụng công cụ.

Bài học em rút ra là **fresher không nên chỉ chạy theo công cụ mới mà cần xây dựng nền tảng, luyện tư duy và học cách chịu trách nhiệm với quyết định của bản thân**.

## Chủ đề 4 – Nguyễn Phương Thảo: BMAD Method – Đưa đội ngũ Agile và AI vào trong IDE

![Nguyễn Phương Thảo chia sẻ về khả năng thích ứng và Party Mode](/images/4-EventParticipated/Event1/thao-nguyen-phuong.png)

*[Nguyễn Phương Thảo](https://www.linkedin.com/in/thao-ngph/) giới thiệu BMAD Method và cách tổ chức quy trình phát triển phần mềm với nhiều vai trò AI.*

Phần cuối giới thiệu BMAD Method, một cách tiếp cận có quy trình hơn khi sử dụng AI trong phát triển phần mềm.

Vấn đề thường gặp khi dùng AI để code là người dùng đưa quá nhiều yêu cầu vào một cuộc trò chuyện dài. Sau một thời gian, AI có thể mất ngữ cảnh, hiểu sai yêu cầu, sinh ra code khó bảo trì hoặc tạo ra những phần không phù hợp với hệ thống hiện tại.

BMAD Method giải quyết vấn đề này bằng cách mô phỏng một quy trình phát triển phần mềm với nhiều vai trò:

* Product Manager phân tích nhu cầu.
* Architect thiết kế kiến trúc.
* Scrum Master chia nhỏ Epic và Story.
* Developer triển khai từng phần.
* QA/QC hoặc Reviewer kiểm thử và phản biện.

Thay vì yêu cầu AI “code toàn bộ project”, phương pháp này chia dự án thành các bước nhỏ: brainstorm tính năng, tạo BRD, thiết kế kiến trúc, chia story, phê duyệt story, triển khai, review và kiểm thử. Cách làm này giảm tình trạng quá tải context và giúp con người kiểm soát chất lượng tốt hơn.

Điểm em thấy quan trọng là BMAD không biến AI thành người thay thế hoàn toàn developer. AI có thể đảm nhận nhiều vai trò hỗ trợ nhưng con người vẫn là người duyệt, định hướng và chịu trách nhiệm cuối cùng.

Bài học em rút ra là **muốn dùng AI để code hiệu quả thì không nên chỉ prompt theo cảm hứng mà cần có tài liệu, quy trình, story rõ ràng và các bước review liên tục**.

## Bài học tổng kết

Sau buổi event, em nhận thấy bốn chủ đề có thể kết nối thành một bức tranh chung:

* Muốn học tốt, em cần biết cách thiết kế động lực học tập.
* Muốn dùng AI tốt, em cần giao tiếp rõ ràng với AI.
* Muốn làm việc tốt trong thời đại AI, em cần nền tảng và tư duy “Why”.
* Muốn dùng AI để phát triển phần mềm, em cần một quy trình chứ không chỉ cần prompt.

Điều em rút ra nhiều nhất là AI không làm giảm giá trị của kiến thức nền tảng. Ngược lại, AI khiến nền tảng trở nên quan trọng hơn vì người có nền tảng sẽ biết cách kiểm tra, điều hướng và khai thác AI hiệu quả.

Tóm lại, event giúp em nhận ra rằng lợi thế trong thời đại AI không nằm ở việc sử dụng nhiều công cụ nhất mà nằm ở khả năng học nhanh, tư duy rõ ràng, đặt câu hỏi đúng và làm việc một cách có trách nhiệm.
