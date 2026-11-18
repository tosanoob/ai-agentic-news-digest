# GitHub Copilot Evals public preview cho skills, agents và MCP

- **story_id:** `github-copilot-evals-preview-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-17
- **Ngày digest (Asia/Singapore):** 2026-11-18
- **Tạo/cập nhật nội dung (UTC):** 2026-11-18T00:36:53Z
- **Loại:** agent_framework

## Tổng quan
Evals dùng Vally làm local evaluation engine; hỗ trợ tạo test, duyệt từng run, xem checks pass/fail, so sánh trước/sau chỉnh skills, agents, MCP.

## Sự kiện và điểm mới
Theo [thông báo chính thức của GitHub](https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview/), Có thể tạo eval bằng ngôn ngữ tự nhiên hoặc /eval; đặt realistic task và expected evidence, xem trajectory và failed checks. Tích hợp VS Code extension, Copilot CLI plugin và Copilot app marketplace.

## Chi tiết kỹ thuật và giới hạn triển khai
Có thể tạo eval bằng ngôn ngữ tự nhiên hoặc /eval; đặt realistic task và expected evidence, xem trajectory và failed checks. Tích hợp VS Code extension, Copilot CLI plugin và Copilot app marketplace. Đây là mô tả tính năng hoặc kết quả do nhà cung cấp công bố, không mặc định chứng minh năng lực vận hành trong mọi môi trường. Việc sử dụng thực tế cần kiểm tra quyền truy cập, trạng thái preview/GA, cấu hình agent harness và khả năng đo lường.

## Ý nghĩa thực tiễn cho AI/agent engineering
**Phân tích và khuyến nghị của tác giả:** Đưa regression testing vào agent engineering: version hóa test cases, cố định môi trường, chạy nhiều seeds, đo pass@k, chi phí và tool-call side effects trước khi promote skill.

## Bằng chứng, độ tin cậy và tính khả dụng
**Sự kiện được xác minh:** GitHub công bố ngày 17/11/2026 tại URL gốc bên dưới. **Tuyên bố của nhà cung cấp / giới hạn:** Public preview; kết quả một run không đủ kết luận thống kê. Không có benchmark độc lập về hiệu quả Evals so với harness khác. **Đánh giá độc lập:** chưa được xác minh trong lần nghiên cứu này; không coi vendor claims là independent evaluation.

## Nguồn chính
- [GitHub Changelog — GitHub Copilot Evals public preview cho skills, agents và MCP](https://github.blog/changelog/2026-11-17-github-copilot-evals-is-now-in-public-preview/)
