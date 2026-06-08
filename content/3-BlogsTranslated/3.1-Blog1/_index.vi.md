---
title: "Blog 1: Sắp xếp ưu tiên kiến trúc với Tech Roadmap Prioritization (TRP)"
date: 2026-06-08
weight: 1
chapter: false
pre: " <b> 3.1. </b> "
---

# Blog 1: Sắp xếp ưu tiên kiến trúc với Tech Roadmap Prioritization (TRP)

> **Bài gốc:** [Align your architecture backlog with Tech Roadmap Prioritization (TRP)](https://aws.amazon.com/blogs/architecture/align-your-architecture-backlog-with-tech-roadmap-prioritization-trp/) – AWS Architecture Blog

Xin chào mọi người, hôm nay mình muốn chia sẻ một góc nhìn thiên về "tư duy kiến trúc" mà mình rút ra sau khi đọc bài "Align your architecture backlog with Tech Roadmap Prioritization (TRP)" trên AWS Architecture Blog. Đây không phải bài hướng dẫn dùng dịch vụ AWS cụ thể, mà là cách AWS gợi ý tổ chức sắp xếp thứ tự ưu tiên cho các initiative kiến trúc khi nguồn lực luôn có hạn.

Mình thấy chủ đề này khá sát với thực tế: đi làm thì việc gì cũng "nghe quan trọng", backlog lúc nào cũng đầy ắp, nhưng không thể làm hết cùng lúc. Câu hỏi khó không còn là "xài dịch vụ nào của AWS" mà là "trong tất cả những việc hợp lý đó, mình nên làm cái gì trước, cái gì sau, và vì sao". Framework TRP chính là câu trả lời AWS đưa ra cho bài toán đó, thông qua một phiên họp khoảng một giờ với stakeholder để cùng nhau đặt mọi initiative lên một ma trận chung và thảo luận.

Trong bài viết gốc, AWS mô tả TRP như một cách để biến "danh sách ý tưởng" thành backlog kiến trúc có thứ tự ưu tiên rõ ràng, gắn với roadmap công nghệ dài hạn. Kết quả quan trọng nhất của phiên TRP không phải là một slide đẹp, mà là việc business owner, technical owner và kiến trúc sư đều hiểu tại sao một số việc được làm ngay, một số việc phải de‑risk trước, và một số việc tạm thời gác lại.

## Vì sao backlog kiến trúc không thể chỉ là danh sách việc cần làm?

Trong thực tế, một tổ chức thường có song song rất nhiều việc "nghe đều đúng": hiện đại hóa hệ thống legacy, xây data platform, mở rộng sang thị trường mới, nâng cấp bảo mật, tối ưu chi phí hạ tầng… nhưng ngân sách, nhân lực và thời gian luôn bị giới hạn. Nếu thiếu cấu trúc, thứ tự ưu tiên dễ bị quyết định bởi "ai nói to hơn" trong cuộc họp, hoặc bị ảnh hưởng bởi sự cố gần nhất thay vì chiến lược dài hạn.

Ở góc nhìn kiến trúc, backlog vì thế không nên chỉ là list ticket trên Jira, mà phải là danh mục các initiative đã được thảo luận và xếp thứ tự dựa trên tác động business và mức độ sẵn sàng của tổ chức. Bài TRP của AWS nhấn mạnh rằng rủi ro lớn nhất không chỉ là chọn nhầm công nghệ, mà là cả team không "ở cùng một trang" về ưu tiên – người thì nghĩ tối ưu chi phí là quan trọng nhất, người lại muốn đẩy nhanh tính năng mới.

## TRP – ma trận nhỏ, góc nhìn lớn

Điểm mình thấy hay ở TRP là sự đơn giản nhưng có cấu trúc. AWS đề xuất trong phiên ưu tiên, mọi initiative đều được vẽ lên một ma trận hai trục:

- **Trục X** thể hiện chi phí hoặc độ phức tạp triển khai: càng về bên phải thì càng tốn kém và phức tạp.
- **Trục Y** thể hiện tác động business: càng lên cao thì càng tạo ra giá trị (doanh thu, giảm rủi ro, cải thiện trải nghiệm khách hàng, giảm chi phí vận hành…).

Ngoài ra, từng "bong bóng" trên ma trận còn có **kích thước** (độ quan trọng chiến lược) và **màu sắc** để phân nhóm theo các chủ đề như *Modernize*, *Optimize*, *Monetize* – giúp tổ chức không bị lệch hẳn sang một kiểu initiative duy nhất.

![Ma trận TRP – Ví dụ roadmap ưu tiên kiến trúc](/images/3-BlogsTranslated/trp-matrix.png)

Chỉ với ma trận đó, cả phòng có thể nhìn nhanh và hiểu:

- **Góc trên bên trái (Strategic Quick Wins):** những việc tác động cao nhưng chi phí thấp – các strategic quick wins nên làm sớm để tạo đà và chứng minh giá trị.
- **Góc trên bên phải (Strategic Transformations):** những thay đổi tác động cao nhưng chi phí/độ phức tạp cũng cao – các big bet cần được de‑risk bằng PoC, workshop, nâng cấp kỹ năng trước khi commit full.
- **Góc dưới bên trái (Tactical Quick Wins):** các việc tác động thấp nhưng chi phí thấp – có thể gom lại thành đợt "dọn backlog", xử lý nợ kỹ thuật nhỏ nhưng gây khó chịu.
- **Góc dưới bên phải (Questionable Initiatives):** những việc tác động thấp, chi phí cao – đáng để chất vấn và thường chỉ giữ lại để minh bạch, chứ không nên ưu tiên trừ khi bối cảnh thay đổi.

Nhìn theo cách này, backlog kiến trúc không còn là danh sách "vô thứ tự" nữa, mà là bản đồ ưu tiên giúp mọi người đọc được câu chuyện: chúng ta đang chọn đặt nguồn lực ở đâu, và đang chủ động hoãn những gì.

## Vai trò của kiến trúc sư trong một phiên TRP

Một điểm mình khá thích là cách bài viết định vị vai trò kiến trúc sư. Trong phiên TRP, kiến trúc sư không phải người "phán" initiative nào đúng sai, mà là người **thiết kế cuộc đối thoại** và **điều phối**.

AWS gợi ý tối thiểu phải có cả business owner và technical owner trong phòng, để mỗi initiative đều được nhìn dưới hai lăng kính: nó tạo giá trị gì và nó có khả thi không. Nhiệm vụ của kiến trúc sư là:

- **Giữ cuộc trao đổi tập trung** vào việc so sánh tương đối giữa các initiative, tránh sa đà vào thiết kế chi tiết cho từng cái.
- **Dịch các đề xuất kỹ thuật sang ngôn ngữ outcome** (ví dụ "giảm downtime" hay "rút ngắn time-to-market"), để business có thể tham gia quyết định.
- **Phá vỡ tâm lý "cái gì cũng priority 1"** bằng các câu hỏi so sánh: "Nếu chỉ có thể chọn một việc trong quý này, mọi người sẽ chọn cái nào?".

Nói cách khác, kiến trúc sư không chỉ thiết kế hệ thống, mà còn thiết kế cả cách tổ chức ra quyết định về hệ thống đó. Đây là một lớp kỹ năng mình nghĩ rất đáng để những người đang học cloud để ý từ sớm.

## Bài học cho người mới học AWS / Cloud

Nghe thì có vẻ rất "enterprise", nhưng với mình, TRP mang lại vài bài học thực tế cho cả những bạn đang ở mức học chứng chỉ nền tảng hoặc mới lab các dịch vụ cơ bản trên AWS:

### Bắt đầu từ outcome, không bắt đầu từ dịch vụ

Trước khi hỏi "Dùng EC2 hay Lambda?", hãy hỏi "Bài toán muốn cải thiện cái gì: hiệu năng, chi phí, độ tin cậy, hay tốc độ ra feature?". Đây cũng là tinh thần chung của AWS Well‑Architected Framework.

### Tập suy nghĩ theo portfolio thay vì từng project lẻ

Một tổ chức khỏe sẽ có tỷ lệ hợp lý giữa các initiative về hiện đại hóa, tối ưu, và tạo dòng giá trị mới, chứ không dồn hết vào một phía.

### Artifact tốt là một phần của công việc kiến trúc

Ma trận TRP là một artifact sống, có thể mang ra xem lại khi chiến lược, ngân sách hoặc rủi ro thay đổi. Ở mức cá nhân, việc biết tạo diagram, document, matrix rõ ràng sẽ giúp cloud engineer/architect dễ được tin tưởng hơn.

### Alignment là "non‑functional requirement" của kiến trúc

Dù hệ thống có đẹp thế nào trên giấy, nếu team không đồng thuận về ưu tiên và thứ tự thực hiện, thì khả năng cao vẫn dẫn đến rework, trễ deadline, hoặc đốt nguồn lực vào những việc không tạo đủ giá trị.

---

Đối với mình, việc đọc bài TRP không giúp mình "xài AWS giỏi hơn" ngay lập tức, nhưng giúp mình đổi góc nhìn về vai trò của kiến trúc sư cloud: không chỉ là người rành dịch vụ, mà còn là người giúp tổ chức ra quyết định công nghệ một cách có cấu trúc và minh bạch. Ngay cả khi tụi mình đang ở giai đoạn học Cloud Practitioner hay mới lab mấy dịch vụ cơ bản, việc tiếp xúc sớm với những framework như TRP có thể là lợi thế lớn – sau này khi bước vào các cuộc thảo luận lớn hơn, mình không chỉ nói được "how" mà còn đặt được câu hỏi "why" đúng chỗ.
