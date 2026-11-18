# GitHub Copilot browser use public preview qua Chrome extension

- **story_id:** `github-copilot-browser-use-preview-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-17
- **Ngày digest (Asia/Singapore):** 2026-11-18
- **Tạo/cập nhật nội dung (UTC):** 2026-11-18T00:36:53Z
- **Loại:** agent_framework

## Tổng quan
Copilot CLI, Copilot app, VS Code và JetBrains có browser use public preview qua GitHub Copilot Chrome extension, hỗ trợ debug, UI tests và web workflows.

## Sự kiện và điểm mới
Theo [thông báo chính thức của GitHub](https://github.blog/changelog/2026-11-17-let-github-copilot-interact-with-your-browser/), Cần cài extension, bật browser use trong từng client và kiểm tra trạng thái Connected; extension có permission controls. Browser use có thể phối hợp computer use.

## Chi tiết kỹ thuật và giới hạn triển khai
Cần cài extension, bật browser use trong từng client và kiểm tra trạng thái Connected; extension có permission controls. Browser use có thể phối hợp computer use. Đây là mô tả tính năng hoặc kết quả do nhà cung cấp công bố, không mặc định chứng minh năng lực vận hành trong mọi môi trường. Việc sử dụng thực tế cần kiểm tra quyền truy cập, trạng thái preview/GA, cấu hình agent harness và khả năng đo lường.

## Ý nghĩa thực tiễn cho AI/agent engineering
**Phân tích và khuyến nghị của tác giả:** Coding agents có thể kiểm chứng UI trực tiếp sau khi sửa code, tạo feedback loop build-test-inspect. Cần giới hạn origin, session, credentials và xác nhận hành động gây side effects.

## Bằng chứng, độ tin cậy và tính khả dụng
**Sự kiện được xác minh:** GitHub công bố ngày 17/11/2026 tại URL gốc bên dưới. **Tuyên bố của nhà cung cấp / giới hạn:** Chỉ preview; không có benchmark browser-task success, browser compatibility hoặc safety. Agent quan sát UI không chứng minh đã hiểu backend logic. **Đánh giá độc lập:** chưa được xác minh trong lần nghiên cứu này; không coi vendor claims là independent evaluation.

## Nguồn chính
- [GitHub Changelog — GitHub Copilot browser use public preview qua Chrome extension](https://github.blog/changelog/2026-11-17-let-github-copilot-interact-with-your-browser/)
