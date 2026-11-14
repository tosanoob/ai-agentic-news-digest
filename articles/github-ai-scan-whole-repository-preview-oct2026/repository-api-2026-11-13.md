# UPDATE: GitHub AI Scan cho toàn repository hỗ trợ bật/tắt bằng REST API

- **story_id:** `github-ai-scan-whole-repository-preview-oct2026`
- **update_id:** `repository-api-2026-11-13`
- **Ngày sự kiện/công bố:** 2026-11-13
- **Ngày digest (Asia/Singapore):** 2026-11-14
- **Created/updated UTC:** 2026-11-14T00:44:16Z
- **Loại:** security

## Tổng quan

Material update từ AI Scan repository preview 28/10: REST GET/PATCH ở org/repo nay hỗ trợ repository_scan enabled/disabled; policy kế thừa, lỗi 422 khi bị chặn; bật setting không tự chạy scan và mỗi scan tốn AI credits.

## Điều gì xảy ra và điểm mới

Ngày 28/10 GitHub công bố AI Scan cho toàn repository ở public preview. Ngày 13/11 hãng bổ sung quản lý enablement qua REST API, mở rộng từ khả năng API cho PR scan đã có trước đó. Các endpoints GET/PATCH /orgs/{org}/code-scanning/ai-scan và /repos/{owner}/{repo}/code-scanning/ai-scan nhận repository_scan=enabled|disabled, có thể cập nhật cùng pr_scan. Nếu organization tắt thì repository không tự bật được; nếu organization bật thì repo kế thừa và có thể opt out. Enterprise policy cấm sẽ trả HTTP 422; khi một request cập nhật cả hai settings mà có phần bị chặn thì không thay đổi setting nào.

## Ý nghĩa thực tiễn với AI/agent engineering (phân tích, không phải vendor claim)

Security platform teams có thể đưa AI Scan enablement vào infrastructure-as-code, drift detection và rollout theo nhóm repositories. Cần tách configuration automation khỏi execution scheduler: bật setting không tự khởi chạy scan; người có write access phải chạy on demand. Dự toán credits và phân quyền trước khi tự động hóa trên nhiều repos.

## Bằng chứng, giới hạn và availability

Public preview; hỗ trợ public organization repos và private/internal repos có GitHub Code Security hoặc GitHub Advanced Security, phụ thuộc enterprise policy; GHES chưa hỗ trợ. Chưa có independent precision/recall benchmark. Đây là material update của cùng story, không phải sản phẩm AI Scan mới.

## Nguồn chính thức

- [Nguồn công bố](https://github.blog/changelog/2026-11-13-manage-ai-scan-for-repositories-using-the-rest-api/)
- [Nguồn công bố](https://github.blog/changelog/2026-10-28-ai-scan-for-repositories-in-public-preview/)

**Phân loại bằng chứng:** Ngày công bố, API/availability và tính năng là thông tin từ nhà cung cấp; các đánh giá kỹ thuật và đề xuất triển khai là suy luận của người viết. Không có benchmark độc lập mới được xác minh cho sự kiện này.
