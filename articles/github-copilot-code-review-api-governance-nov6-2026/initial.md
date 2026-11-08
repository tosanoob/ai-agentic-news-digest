# GitHub Copilot Code Review: API quản trị và provenance của nhận xét

**story_id:** `github-copilot-code-review-api-governance-nov6-2026`  
**update_id:** `initial`  
**Ngày công bố gốc:** 2026-11-06  
**Ngày digest:** 2026-11-08 (Asia/Singapore)  
**Tạo/cập nhật nội dung (UTC):** 2026-11-08T00:41:00Z

## Tổng quan
GitHub công bố khả năng quản lý chính sách Copilot code review bằng REST/GraphQL API ở cấp enterprise, organization và repository, đồng thời cải thiện thông tin attribution, giao diện tổng hợp nhận xét và độ tin cậy của phiên review. Đây là thông báo sản phẩm, không phải benchmark độc lập.

## Điều gì mới?
Theo [GitHub Changelog ngày 06/11](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/), API có thể xác định review/comment do Copilot tạo, trả về review effort nếu có, và chỉ ra skills, MCP servers hoặc custom instructions mà Copilot **báo cáo** đã dùng để tạo comment. Enterprise có thể quản lý quyền bật/tắt; organization quản lý effort và runner; repository quản lý effort và việc dùng MCP/custom instructions. Chính sách cấp cao hơn không bị cấp thấp hơn ghi đè.

Các enterprise/organization settings endpoints (gồm runner endpoint) không hỗ trợ GitHub Apps hoặc fine-grained PAT; repository settings endpoints có thể dùng các credential này với quyền Administration tương ứng. Đây là hạn chế quan trọng khi xây dựng automation.

GitHub cũng cho biết balanced reviews sử dụng ba reviewer models và một model khác tổng hợp findings. Phiên review hiển thị AI credits tiêu thụ; các phiên lỗi hoặc timeout được retry một lần, có thể chuyển model hợp lệ khác.

## Ý nghĩa kỹ thuật
**Suy luận kỹ thuật:** Doanh nghiệp có thể triển khai policy-as-code cho code review và audit cấu hình MCP/skills trong pipeline. Tuy nhiên, trường nguồn là thông tin agent *báo cáo*, không phải cryptographic proof rằng mọi tool call đã xảy ra đúng như mô tả. Nên đối chiếu với execution logs và repository checks. Cấu trúc multi-model review cũng không mặc nhiên chứng minh giảm false positives.

## Bằng chứng, giới hạn và khả dụng
**Sự thật được công bố bởi vendor:** API settings, provenance fields, credit display, retry và multi-model review. **Chưa có:** controlled benchmark về precision, recall, task completion hoặc ROI. GitHub nêu khả dụng cho các gói Copilot Pro, Pro+, Max, Business và Enterprise; endpoint permission khác nhau theo cấp quản trị.

**Nguồn gốc:** [GitHub Changelog 06/11/2026](https://github.blog/changelog/2026-11-06-copilot-code-review-api-management-and-review-overview-updates/).
