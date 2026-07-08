---
title: "Sự kiện 2: FCAJ Community Day 2026"
date: 2026-05-23
weight: 2
chapter: false
pre: " <b> 4.2. </b> "
---

# Sự kiện 2: FCAJ Community Day 2026

| Trường | Nội dung |
| --- | --- |
| Tên sự kiện | FCAJ Community Day 2026 |
| Ngày/giờ | 23 tháng 5 năm 2026 |
| Địa điểm | AWS Event Hall, Tầng 26, Bitexco Financial Tower, TP. Hồ Chí Minh |
| Vai trò | Người tham gia |

![Ảnh chụp chung tại FCAJ Community Day 2026](/images/4-EventParticipated/Event2/group-photo.png)

*Các diễn giả, ban tổ chức và người tham dự tại FCAJ Community Day 2026.*

FCAJ Community Day 2026 giúp em nhìn AI ở góc độ thực tế hơn: AI không còn chỉ là một chatbot độc lập mà đang trở thành một thành phần của hệ thống phần mềm, có kiến trúc, workflow, dữ liệu, bảo mật, chi phí vận hành và trách nhiệm khi áp dụng trong doanh nghiệp. Các phần chia sẻ đi từ định hướng nghề nghiệp, cách thiết kế context, tự động hóa công việc bằng AI Agent, tối ưu hạ tầng với CloudFront cho đến việc kiểm soát LLM và xây dựng hệ thống multi-agent.

## Phần mở đầu – Nguyễn Gia Hưng: AI và sự thay đổi của thị trường việc làm

![Nguyễn Gia Hưng chia sẻ phần mở đầu về AI và thị trường việc làm](/images/4-EventParticipated/Event2/nguyen-gia-hung-opening.png)

*Nguyễn Gia Hưng chia sẻ ngắn về tác động của AI đối với thị trường việc làm và sự chuẩn bị cần thiết của sinh viên.*

Anh Nguyễn Gia Hưng mở đầu sự kiện bằng bối cảnh AI đang làm giảm chi phí và thời gian phát triển phần mềm. Khi việc tạo prototype, viết code, sửa lỗi và xây dựng MVP trở nên nhanh hơn, số lượng sản phẩm phần mềm có thể tăng mạnh. Điều này không đồng nghĩa với việc nhu cầu nhân sự IT biến mất. Ngược lại, những người có khả năng xác định đúng vấn đề, xây dựng, vận hành, sửa lỗi, tối ưu và mở rộng hệ thống sẽ càng quan trọng.

Tuy nhiên, bằng đại học hoặc khả năng sử dụng một số công cụ kỹ thuật không còn đủ để tạo lợi thế. Sinh viên cần hiểu nghiệp vụ doanh nghiệp, có sản phẩm thực tế thay vì chỉ có demo, biết kết nối giải pháp kỹ thuật với business use case, đồng thời phát triển kỹ năng mềm và ngoại ngữ. Việc học cũng không thể dừng lại sau khi hoàn thành một khóa học vì công nghệ và nhu cầu thị trường liên tục thay đổi.

Điều em rút ra là AI có thể giúp em viết code nhanh hơn nhưng không thể thay em quyết định bài toán nào đáng giải quyết. Giá trị của một kỹ sư nằm ở khả năng hiểu người dùng, làm rõ yêu cầu và thiết kế giải pháp tạo ra kết quả thực tế.

## Chủ đề 1 – Tinh Truong: Context Is Everything

Chủ đề **Context Is Everything** làm rõ rằng sức mạnh của mô hình AI chưa đủ để bảo đảm một kết quả hữu ích. Khi context thiếu rõ ràng hoặc chứa quá nhiều thông tin không liên quan, AI dễ hiểu sai mục tiêu, trả lời lan man hoặc tạo ra kết quả khó sử dụng.

![Các thành phần tạo nên context hiệu quả cho AI](/images/4-EventParticipated/Event2/context-is-everything-details.png)

*Goal, situation, constraints và relevant evidence biến một yêu cầu mơ hồ thành bài toán có thể xử lý.*

Một context hiệu quả cần xác định ít nhất bốn yếu tố:

* **Goal:** Kết quả cuối cùng cần đạt được.
* **Persona:** Đối tượng sử dụng kết quả, chẳng hạn người mới học, developer, architect hoặc business user.
* **Format:** Cấu trúc đầu ra mong muốn như bảng, checklist, tài liệu kỹ thuật hoặc JSON.
* **Related data:** Dữ liệu, bằng chứng và thông tin thực sự liên quan đến bài toán.

Diễn giả cũng cảnh báo về tư duy “Internet Builder”: thấy framework, template, prompt hoặc thư viện nào thú vị cũng đưa vào hệ thống mà không đọc kỹ hoặc hiểu bản chất. Cách làm này khiến dự án bị nhồi nhét thành phần dư thừa, context của AI trở nên hỗn loạn và cuối cùng sinh ra code khó kiểm soát.

Một hướng tiếp cận tốt hơn là xây dựng AI Mindset và một “Second Brain” có tổ chức. Công cụ ghi chú như Obsidian có thể giúp lưu trữ kiến thức, liên kết các khái niệm và ghi lại quá trình ra quyết định. Khi kiến thức được tổ chức tốt, người dùng không chỉ đặt prompt chính xác hơn mà còn có thể giải thích cách họ học, kiểm chứng thông tin và sử dụng AI trong công việc.

Bài học em rút ra là **Prompt Engineering thực chất là Context Engineering**. AI càng mạnh thì người dùng càng phải biết định hướng, giới hạn và cung cấp đúng dữ liệu thay vì chỉ đưa thật nhiều dữ liệu.

## Chủ đề 2 – Phạm Nguyễn Hải Anh: Friendly AI Assistant with Amazon Quick

![Phạm Nguyễn Hải Anh trình bày Friendly AI Assistant with Amazon Quick](/images/4-EventParticipated/Event2/friendly-ai-amazon-quick.png)

*[Phạm Nguyễn Hải Anh](https://www.linkedin.com/in/anhpnh/) giới thiệu cách xây dựng trợ lý AI thân thiện với Amazon Quick.*

Phần trình bày **Friendly AI Assistant with Amazon Quick** sử dụng một bài toán rất gần với doanh nghiệp: tự động hóa quá trình tổng hợp và tạo báo cáo cho cấp quản lý. Trong thực tế, dữ liệu có thể nằm rải rác trong Excel, email, biên bản họp, Jira, Google Workspace hoặc Microsoft Teams. Người lập báo cáo phải thu thập dữ liệu, hiểu ý nghĩa, xác định xu hướng, tạo biểu đồ, tóm tắt điểm chính và gửi kết quả cho đúng người.

Giải pháp được trình bày sử dụng AI Agent như “bộ não” xử lý yêu cầu và kết nối các công cụ bên ngoài thông qua MCP như những “cánh tay nối dài”. Nhờ đó, AI không chỉ sinh văn bản mà còn có thể đọc file, phân tích dữ liệu, tạo dashboard, tóm tắt cuộc họp hoặc hỗ trợ gửi báo cáo qua workflow có sẵn.

Điểm đáng chú ý là người quản lý không nhất thiết phải có kiến thức BI chuyên sâu. Họ có thể cung cấp một file Excel thô và đặt yêu cầu bằng ngôn ngữ tự nhiên để nhận phân tích xu hướng, biểu đồ hoặc danh sách bất thường. Tuy vậy, hệ thống vẫn cần kiểm soát quyền truy cập, nguồn dữ liệu và bước xác nhận trước khi thực hiện hành động có ảnh hưởng đến người khác.

Em nhận ra một chatbot chỉ thực sự tạo giá trị khi được đặt vào quy trình cụ thể. **AI Agent có giá trị lớn nhất khi được kết nối với workflow và công cụ thật của doanh nghiệp**, có đầu vào, đầu ra và người chịu trách nhiệm rõ ràng.

## Chủ đề 3 – Nguyễn Thịnh: From Edge To Origin – CloudFront as Your Foundation

![Nguyễn Thịnh trình bày kiến trúc Amazon CloudFront từ edge đến origin](/images/4-EventParticipated/Event2/cloudfront-thinh-nguyen.png)

*[Nguyễn Thịnh](https://www.linkedin.com/in/thinhnguyen1211/) trình bày cách CloudFront kết nối edge với origin.*

Chủ đề **From Edge To Origin: CloudFront as Your Foundation** phân tích CloudFront ở ba khía cạnh: kiểm soát chi phí, tăng cường bảo mật và cải thiện hiệu năng.

Về chi phí, một rủi ro phổ biến khi vận hành cloud là “bill shock”, tức hóa đơn tăng đột biến do traffic bất thường, tấn công hoặc cấu hình chưa phù hợp. Cơ chế flat-rate pricing giúp doanh nghiệp dự đoán chi phí tốt hơn; khi lưu lượng vượt ngưỡng, hệ thống có thể giới hạn băng thông thay vì tiếp tục phát sinh chi phí ngoài kiểm soát.

Về bảo mật, CloudFront đứng tại edge trước origin server. Mạng lưới điểm hiện diện giúp hấp thụ hoặc chặn traffic xấu sớm hơn, hỗ trợ DDoS protection, geo-blocking và giảm khả năng request độc hại đi trực tiếp vào backend. VPC Origin còn cho phép origin nằm trong mạng riêng và không cần public trực tiếp ra Internet, từ đó giảm bề mặt tấn công.

Về hiệu năng, CloudFront hỗ trợ caching, HTTP/3 và xử lý TLS/TCP handshake gần người dùng. Static assets có thể được phục vụ từ edge thay vì quay lại origin cho mọi request, giúp giảm độ trễ và tải CPU tại backend. Tuy nhiên, cache policy phải được thiết kế đúng vì nội dung động, dữ liệu cá nhân và luồng realtime không thể xử lý giống tài nguyên tĩnh.

Bài học em rút ra là **CloudFront không chỉ là CDN tăng tốc website mà còn là một lớp kiểm soát bảo mật, chi phí và hiệu năng của kiến trúc**. Khi mô tả hệ thống, em cần giải thích rõ request đi từ người dùng qua edge đến origin như thế nào, thành phần nào được cache và thành phần nào phải đi thẳng đến backend.

## Chủ đề 4 – Lê Phạm Ngọc Uyển, Nguyễn Ngọc Quỳnh Mai và Nguyễn Phương Thảo: 36 hrs with LotusHacks

![Nhóm UTMorpho chia sẻ hành trình từ ý tưởng đến sản phẩm tại LotusHacks](/images/4-EventParticipated/Event2/utmorpho-team.png)

*[Lê Phạm Ngọc Uyển](https://www.linkedin.com/in/lephamngocuyen/), [Nguyễn Ngọc Quỳnh Mai](https://www.linkedin.com/in/nnquynhmai/) và [Nguyễn Phương Thảo](https://www.linkedin.com/in/thao-ngph/) chia sẻ hành trình xây dựng UTMorpho trong 36 giờ.*

**36 hrs with LotusHacks – Building UTMorpho from Idea to Reality** là một case study thực chiến về việc xây dựng sản phẩm AI trong thời gian rất ngắn. UTMorpho sử dụng AI để tạo giao diện từ ảnh vẽ tay hoặc mô tả của người dùng, đồng thời cho phép chỉnh sửa trực tiếp kết quả. Khả năng chỉnh sửa là phần quan trọng vì đầu ra ban đầu của AI hiếm khi hoàn toàn phù hợp với nhu cầu cuối cùng.

Nhóm áp dụng kiến trúc serverless và chia nhiệm vụ cho nhiều agent, chẳng hạn agent đọc hình ảnh, agent tạo layout/CSS và agent sinh code. Việc chuyên môn hóa giúp mỗi agent tập trung vào một nhiệm vụ cụ thể thay vì yêu cầu một model xử lý toàn bộ quy trình trong một context lớn.

Trong quá trình phát triển, nhóm gặp các vấn đề phổ biến như giới hạn token và over-generation. AI có xu hướng thêm chi tiết hoặc chức năng không được yêu cầu, khiến sản phẩm phức tạp hơn và tiêu tốn thời gian kiểm tra. Trong hackathon, điều này đặc biệt nguy hiểm vì thời gian có hạn.

Bài học lớn nhất với em là phải bảo vệ core value của sản phẩm. Một sản phẩm AI tốt không phải là sản phẩm chứa nhiều AI nhất mà là sản phẩm **dùng AI đúng chỗ để giải quyết một vấn đề rõ ràng**. Phạm vi nhỏ, vòng phản hồi nhanh và khả năng chỉnh sửa kết quả thường có giá trị hơn một danh sách tính năng dài nhưng chưa hoàn thiện.

## Chủ đề 5 – Đào Minh Đức: Non-Determinism of “Deterministic” LLM Settings

![Đào Minh Đức giải thích vai trò của Temperature, Top-P và Top-K](/images/4-EventParticipated/Event2/duc-dao-minh.png)

*[Đào Minh Đức](https://www.linkedin.com/in/itsdmd/) trình bày ảnh hưởng của Temperature, Top-P và Top-K đến tính ổn định của đầu ra LLM.*

Trong **Non-Determinism of “Deterministic” LLM Settings**, [Đào Minh Đức](https://www.linkedin.com/in/itsdmd/) giải thích rằng LLM vẫn có thể tạo ra kết quả khác nhau ngay cả khi Temperature được đặt bằng 0. LLM về bản chất là mô hình xác suất; ngoài tham số sampling, sai số số học, phép làm tròn và cách GPU thực hiện tính toán song song cũng có thể tạo ra khác biệt nhỏ. Trên môi trường cloud, cách nhà cung cấp gom và xử lý nhiều request để tối ưu tài nguyên cũng có thể ảnh hưởng đến đầu ra.

Điều này có ý nghĩa lớn đối với production. Một kết quả đúng trong lần demo đầu tiên không chứng minh rằng hệ thống sẽ ổn định ở mọi lần chạy. Nếu tác vụ yêu cầu độ tin cậy cao, đội phát triển cần thiết kế thêm các lớp kiểm soát:

* Chạy nhiều lần hoặc dùng nhiều agent để đối chiếu và vote kết quả.
* Sử dụng JSON mode hoặc schema để ràng buộc định dạng.
* Có validation, error handling và fallback.
* Kiểm thử nhiều bộ dữ liệu và tình huống khác nhau.
* Cân nhắc self-host model khi cần mức kiểm soát cao hơn.
* Chấp nhận và đo lường trade-off giữa độ chính xác, chi phí và độ trễ.

Bài học em rút ra là **hệ thống sử dụng LLM phải được thiết kế để chịu được sai lệch**, thay vì giả định model luôn trả về một đáp án giống nhau.

## Chủ đề 6 – Lâm Hoàng Cát Vy: Enterprise-Grade Multi-Agent System

![Lâm Hoàng Cát Vy trình bày kiến trúc multi-agent cho startup credit scoring](/images/4-EventParticipated/Event2/lam-hoang-cat-vy.png)

*[Lâm Hoàng Cát Vy](https://www.linkedin.com/in/lam-hoang-cat-vy/) trình bày case study Enterprise-Grade Multi-Agent System cho startup credit scoring.*

Chủ đề **Enterprise-Grade Multi-Agent System: The Case of Startup Credit Scoring** trình bày một use case phức tạp: đánh giá tín dụng cho startup. Startup thường chưa có tài sản thế chấp hoặc lịch sử báo cáo tài chính dài như doanh nghiệp truyền thống, nên bài toán cần kết hợp nhiều loại dữ liệu và góc nhìn chuyên môn.

Kiến trúc multi-agent chia trách nhiệm thành các vai trò như agent phân tích tài chính, agent nghiên cứu thị trường, agent đánh giá rủi ro và manager agent tổng hợp kết quả. Cách tiếp cận này giống một nhóm chuyên gia, giúp giảm tải context cho từng agent và tăng mức độ chuyên môn hóa.

Tuy nhiên, khó khăn lớn nhất trong doanh nghiệp không chỉ nằm ở model. Hệ thống cần quản lý quyền truy cập, guardrails chống prompt injection, audit trail để lưu vết quyết định và cơ chế xác định trách nhiệm khi đầu ra sai. Dữ liệu tài chính cũng đòi hỏi bảo mật và phân quyền nghiêm ngặt.

Diễn giả còn nhấn mạnh Knowledge Transfer và Context Engineering. Không thể chỉ đưa hàng trăm trang PDF vào hệ thống rồi kỳ vọng AI tự trở thành chuyên gia. Người có kiến thức nghiệp vụ phải lựa chọn dữ liệu quan trọng, giải thích cách đánh giá và thiết kế context phù hợp cho từng agent.

Bài học em rút ra là **AI doanh nghiệp là một bài toán phần mềm hoàn chỉnh**, bao gồm architecture, security, permission, audit, guardrails, infrastructure và domain knowledge. Việc thêm nhiều agent chỉ có ý nghĩa khi mỗi agent có trách nhiệm rõ ràng và cơ chế phối hợp có thể kiểm soát.

## Bài học tổng hợp

Sau Event 2, em thấy rõ AI đang thay đổi cách xây dựng phần mềm nhưng không làm mất vai trò của kỹ sư. AI tăng tốc triển khai, còn con người vẫn phải hiểu bài toán, thiết kế context, kiểm soát dữ liệu và chịu trách nhiệm với kết quả.

Những điểm em rút ra gồm:

* AI giúp phát triển nhanh hơn nhưng con người phải xác định đúng vấn đề.
* Prompt Engineering thực chất là kỹ năng thiết kế context.
* AI Agent tạo giá trị khi được kết nối với workflow và công cụ thật.
* CloudFront hỗ trợ đồng thời hiệu năng, bảo mật và kiểm soát chi phí.
* Sản phẩm AI cần tập trung vào core value thay vì nhồi nhét tính năng.
* LLM có tính xác suất nên cần validation, error handling và kiểm thử nghiêm túc.
* AI doanh nghiệp cần permission, audit trail, guardrails và domain knowledge.

Buổi event đặc biệt phù hợp với định hướng Business System Analyst và Solution Architect của em. Một BSA cần hiểu business use case, đặt câu hỏi đúng và chuyển nhu cầu thành yêu cầu hệ thống. Một Solution Architect cần đánh giá architecture, security, cost, scalability và trade-off. Tóm lại, lợi thế không nằm ở việc dùng nhiều công cụ AI nhất mà ở khả năng thiết kế và kiểm soát một hệ thống giải quyết đúng vấn đề.
