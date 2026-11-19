# GitHub Copilot team customizations GA: shared Agent Plugins

- **story_id:** `github-copilot-team-plugin-customizations-ga-nov2026`
- **update_id:** `initial`
- **Original event/publication date:** 2026-11-18
- **Digest date (Asia/Singapore):** 2026-11-19
- **Content created/updated (UTC):** 2026-11-19T00:04:12Z
- **Category:** enterprise

## Tổng quan
Team maintainers và org owners có thể đặt approved Agent Plugins làm team defaults trên VS Code, Copilot app và CLI; direct members nhận mặc định, child teams không kế thừa; enterprise/org policies luôn ưu tiên.

## Điều gì đã xảy ra và điểm mới
**Sự kiện được nguồn chính thức xác nhận:** Team maintainers hoặc org owners mở Customize Copilot tab của team, thêm marketplace từ repository hoặc marketplace được duyệt rồi chọn plugins. Plugins bật mặc định cho direct team members trong VS Code, Copilot app và Copilot CLI; members có thể tắt nếu policy cho phép. Child teams không kế thừa.

## Chi tiết kỹ thuật và ý nghĩa đối với AI/agent engineering
**Phân tích và suy luận kỹ thuật của người viết, không phải kết quả kiểm thử độc lập:** Đây là tầng phân phối agent skills/tools có quản trị theo team, giảm drift cấu hình giữa developers. Với enterprise, nên version-pin plugin packages, review nguồn marketplace, enforce allowlist, kiểm thử plugin updates và audit quyền tool.

## Evidence, availability và giới hạn
GA cho Copilot Business/Enterprise, không phải cơ chế ép buộc mọi thành viên; enterprise và org policies luôn thắng team defaults. Không có số liệu về năng suất hoặc an toàn được đánh giá độc lập.

Không có independent evaluation được tái lập trong bản tin này. Nếu nguồn nêu nhận định từ nhà cung cấp, chúng được xem là vendor claims, không phải bằng chứng benchmark độc lập. Không suy diễn thêm số liệu hay availability ngoài thông báo.

## Primary source
- [GitHub Changelog — GitHub Copilot team customizations GA: shared Agent Plugins](https://github.blog/changelog/2026-11-18-customize-github-copilot-for-your-team/) (ngày 2026-11-18).
