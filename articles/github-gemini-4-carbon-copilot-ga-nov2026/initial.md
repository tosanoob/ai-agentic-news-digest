# Gemini 4 Carbon chính thức khả dụng trong GitHub Copilot

- **story_id:** `github-gemini-4-carbon-copilot-ga-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-10
- **Ngày digest (Asia/Singapore):** 2026-11-11
- **content_created_at (UTC):** 2026-11-11T00:26:12.217Z
- **content_updated_at (UTC):** 2026-11-11T00:26:12.217Z
- **Phân loại:** model_release

## Tổng quan
GitHub mở Gemini 4 Carbon cho Copilot Pro+, Max, Business, Enterprise trên IDE, CLI và coding agent; usage-based provider list pricing, rollout theo đợt và enterprise model policy.

## Điều gì xảy ra và điểm mới
**Thông tin do nhà cung cấp công bố:** GitHub xác nhận Gemini 4 Carbon đã GA trong GitHub Copilot, có thể chọn ở VS Code, Visual Studio, Copilot CLI, coding agent, Copilot app, github.com, mobile, JetBrains, Xcode và Eclipse. Các gói được hỗ trợ: Pro+, Max, Business và Enterprise. Thanh toán theo bảng giá nhà cung cấp qua usage-based billing; rollout theo đợt. Quản trị viên Business/Enterprise có thể điều khiển model policy. ([nguồn chính thức](https://github.blog/changelog/2026-11-10-gemini-4-carbon-in-github-copilot/)).

## Chi tiết kỹ thuật và tác động thực tế
**Phân tích của người viết:** Agent platform cần phân biệt model availability theo tenant, policy và pricing; benchmark model đơn lẻ không phản ánh kết quả end-to-end trong Copilot harness. Đây là suy luận về thiết kế hệ thống, không phải kết quả kiểm thử độc lập.

## Bằng chứng, giới hạn và availability
Đây là thông báo tích hợp và GA trên Copilot, không chứng minh Gemini 4 Carbon vừa được Google ra mắt ngày 10/11. GitHub không công bố benchmark so sánh độc lập trong changelog. **Đánh giá độc lập:** chưa được xác minh trong bản tin này. **Peer review:** không áp dụng cho thông báo sản phẩm/chính sách. Không suy diễn benchmark khi nguồn không cung cấp điều kiện đánh giá.

## Nguồn gốc
- [Thông báo chính thức ngày 2026-11-10](https://github.blog/changelog/2026-11-10-gemini-4-carbon-in-github-copilot/)
