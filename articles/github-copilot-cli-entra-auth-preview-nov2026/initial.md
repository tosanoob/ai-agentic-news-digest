# BACKFILL: Copilot CLI hỗ trợ Microsoft Entra sign-in và M365 inference

- **story_id:** `github-copilot-cli-entra-auth-preview-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-17
- **Digest date (Asia/Singapore):** 2026-11-19
- **Content created/updated (UTC):** 2026-11-19T00:04:12Z
- **Category:** enterprise

## Tổng quan
Public preview: Copilot CLI 1.0.113+ hỗ trợ Entra SSO cho GitHub EMU qua OIDC hoặc dùng Microsoft 365 Copilot inference/license tùy entitlement; Windows/macOS trước, Linux sau; có thể dùng Work IQ MCP.

## Điều gì đã xảy ra và điểm mới
**Sự kiện được nguồn chính thức xác nhận:** Hai đường xác thực khác nhau: (1) Entra sign-in vào GitHub Enterprise Managed User qua OIDC, dùng GitHub inference và cần Copilot Business/Enterprise + CLI policy; (2) Frontier organizations với M365 Copilot license và usage billing có thể dùng Microsoft 365 inference không cần GitHub account. Hỗ trợ Windows/macOS, yêu cầu CLI 1.0.113+. Work IQ MCP có thể cấp work context.

## Chi tiết kỹ thuật và ý nghĩa đối với AI/agent engineering
**Phân tích và suy luận kỹ thuật của người viết, không phải kết quả kiểm thử độc lập:** Quan trọng với enterprise agents vì tách identity provider, inference provider và license governance. Trước khi triển khai, xác nhận entitlement, data boundaries, policy, billing, scope của Work IQ MCP và tránh nhầm SSO thành quyền truy cập dữ liệu.

## Evidence, availability và giới hạn
Public preview, giới hạn OIDC EMU và Windows/macOS; Linux chưa có. Microsoft 365 inference khác GitHub inference và chịu policies/limits khác nhau. Không có benchmark hiệu năng mới.

Không có independent evaluation được tái lập trong bản tin này. Nếu nguồn nêu nhận định từ nhà cung cấp, chúng được xem là vendor claims, không phải bằng chứng benchmark độc lập. Không suy diễn thêm số liệu hay availability ngoài thông báo.

## Primary source
- [GitHub Changelog — BACKFILL: Copilot CLI hỗ trợ Microsoft Entra sign-in và M365 inference](https://github.blog/changelog/2026-11-17-github-copilot-cli-adds-microsoft-entra-sign-in-as-a-preview/) (ngày 2026-11-17).
