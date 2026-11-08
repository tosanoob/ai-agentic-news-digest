# VS Code 1.145: Copilot local automations bằng cron và quan sát remote agents

**story_id:** `vscode-copilot-1-145-local-automations-nov2026`  
**update_id:** `initial`  
**Ngày công bố nguồn:** 2026-11-06 (weekly release recap; không khẳng định mọi thay đổi ra mắt cùng ngày)  
**Ngày digest:** 2026-11-08 (Asia/Singapore)  
**Tạo/cập nhật nội dung (UTC):** 2026-11-08T00:41:00Z

## Tổng quan
Bản tổng hợp [GitHub Copilot weekly releases ngày 06/11](https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2/) nêu một số thay đổi riêng cho VS Code 1.145: local automations hỗ trợ cron expressions và custom agents từ workspace, cùng cải tiến quan sát phiên agent từ xa.

## Chi tiết kỹ thuật
Người dùng có thể đặt lịch các tác vụ local bằng cron, chọn workspace custom agents. Trong Agents window, khả năng preview remote apps và interactive canvases ở trạng thái preview, cần bật remote browser support và canvases trong settings. Experimental chat view modes cho phép thu gọn hoặc mở rộng reasoning/tool calls; lịch sử terminal được render khi người dùng mở ra thay vì tải đồng loạt. GitHub cũng mô tả thêm file context từ ngoài workspace, với cloud sessions hiện chỉ hỗ trợ hình ảnh.

## Ý nghĩa thực tế
**Suy luận:** Local cron automations có thể phục vụ các công việc định kỳ như kiểm tra repository, cập nhật tài liệu hoặc chạy các tác vụ được phép. Nhưng 'local automation' không đồng nghĩa với managed cloud scheduling: cần kiểm tra điều kiện máy chạy, quyền filesystem, credentials, hành vi retry và tính idempotent. Remote preview giúp người review kiểm tra output trực quan hơn, không thay thế automated tests.

## Giới hạn bằng chứng và khả dụng
Đây là **changelog của nhà cung cấp**, không phải benchmark. Một số tính năng được đánh dấu experimental/preview; không suy diễn GA hoặc khả năng hoạt động khi máy tắt. Những mục JetBrains Air và Xcode trong cùng weekly recap đã có ledger riêng nên không ghi trùng.

**Nguồn:** [GitHub Copilot weekly releases — November 2](https://github.blog/changelog/2026-11-06-github-copilot-weekly-releases-november-2/).
