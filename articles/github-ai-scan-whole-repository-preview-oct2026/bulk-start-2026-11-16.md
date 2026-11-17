# UPDATE: GitHub AI Scan cho phép chạy quét đồng loạt tối đa 20 repositories

- **story_id:** `github-ai-scan-whole-repository-preview-oct2026`
- **update_id:** `bulk-start-2026-11-16`
- **Original event/publication date:** 2026-11-16
- **Digest date (Asia/Singapore):** 2026-11-17
- **Content created (UTC):** 2026-11-17T00:40:52Z
- **Content updated (UTC):** 2026-11-17T00:40:52Z
- **Type:** Verified material update

## Tổng quan
GitHub mở rộng AI Scan cho repositories từ khả năng bật/tắt cấu hình qua REST API (13/11) sang khả năng **khởi chạy đồng loạt** tối đa 20 repositories (16/11). Đây là cập nhật thực thi, không phải phát hành scanner hoàn toàn mới.

## Điều gì mới
**Sự kiện được GitHub xác nhận:** quản trị viên có thể chọn tối đa 20 repositories để khởi chạy scan khi bật setting cấp organization, hoặc từ trang code scanning alerts cấp organization. Có thể chạy riêng một repository từ trang alerts của nó. AI Scan vẫn ở **public preview**; hỗ trợ github.com và GitHub Enterprise Cloud with data residency; không yêu cầu Copilot license.

## Chi tiết kỹ thuật
Scanner phân tích default branch, tạo findings trong code scanning backlog cùng CodeQL. Theo công bố ban đầu ngày 28/10, AI Scan có thể kiểm tra ngôn ngữ CodeQL không hỗ trợ và phát hiện thêm các vấn đề mà rule-based analysis bỏ sót. Điều này là **tuyên bố của GitHub**, chưa có benchmark độc lập precision/recall. Các scans tiêu thụ Code Security AI credits; bật setting không tương đương tự động chạy scan, như GitHub đã giải thích ngày 13/11.

## Ý nghĩa với agent engineering
Đối với enterprise security agents, có thể tách pipeline thành policy configuration → selection → bulk execution → findings triage → remediation → re-scan. Cần rate/cost budget, quyền truy cập và idempotency, nhất là khi retry sau timeout. Giới hạn 20 repositories mỗi batch không chứng minh có thể quét vô hạn song song.

## Evidence, availability và giới hạn
Đây là thông báo vendor, chưa có controlled benchmark so sánh với CodeQL. Không có bằng chứng tính năng hỗ trợ GitHub Enterprise Server hoặc tự chạy định kỳ. Khả năng truy cập repository phụ thuộc enterprise policy, license và quyền người dùng. Không suy diễn rằng tất cả findings đều là vulnerabilities thực.

## Nguồn
- [GitHub Changelog, 16/11/2026 — Bulk start AI Scan](https://github.blog/changelog/2026-11-16-bulk-start-ai-scan-for-repositories/)
- [GitHub Changelog, 13/11/2026 — Manage AI Scan with REST](https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api/)
- [GitHub Changelog, 28/10/2026 — AI Scan public preview](https://github.blog/changelog/2026-10-28-ai-scan-for-repositories-in-public-preview/)
