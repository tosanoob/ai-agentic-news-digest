# GitHub Copilot bổ sung tám verified MCP connectors

- **story_id:** `github-copilot-verified-mcp-connectors-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-18
- **Digest date (Asia/Singapore):** 2026-11-19
- **Content created/updated (UTC):** 2026-11-19T00:04:12Z
- **Category:** protocol

## Tổng quan
Public preview thêm tám GitHub-verified MCP connectors: Box, Buildkite, Calendly, ClickUp, Mixpanel, Supabase, Webflow, Wix; có thể kết nối trên app/CLI/VS Code/web, chịu MCP allowlist và admin policies.

## Điều gì đã xảy ra và điểm mới
**Sự kiện được nguồn chính thức xác nhận:** Tám dịch vụ gồm Box (content/Box AI), Buildkite (CI pipelines), Calendly (meetings), ClickUp (tasks), Mixpanel (analytics), Supabase (database/projects), Webflow và Wix (website management). Kết nối trong Copilot app qua Customize, CLI qua /mcp > Connectors, VS Code qua Agents > Customizations hoặc github.com. Kết nối một lần để dùng trên các Copilot surfaces.

## Chi tiết kỹ thuật và ý nghĩa đối với AI/agent engineering
**Phân tích và suy luận kỹ thuật của người viết, không phải kết quả kiểm thử độc lập:** Cho phép coding agent kiểm tra schema Supabase trước migration hoặc điều tra Buildkite CI failure ngay trong coding session. Thiết kế production cần phân quyền từng connector, tránh cấp write scope cho read-only tasks, log tool calls và yêu cầu approval với thay đổi dữ liệu.

## Evidence, availability và giới hạn
Public preview trên mọi Copilot plans; Business/Enterprise cần bật Editor preview features và có thể phải cập nhật MCP allowlist. Một số nhà cung cấp yêu cầu bật MCP ở phía dịch vụ. Đây là mở rộng danh mục connector, KHÔNG phải MCP specification release. Không có benchmark độc lập.

Không có independent evaluation được tái lập trong bản tin này. Nếu nguồn nêu nhận định từ nhà cung cấp, chúng được xem là vendor claims, không phải bằng chứng benchmark độc lập. Không suy diễn thêm số liệu hay availability ngoài thông báo.

## Primary source
- [GitHub Changelog — GitHub Copilot bổ sung tám verified MCP connectors](https://github.blog/changelog/2026-11-18-connect-supabase-box-calendly-and-more-to-copilot/) (ngày 2026-11-18).
