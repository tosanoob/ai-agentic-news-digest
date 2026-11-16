# Agweb: trình duyệt WebKit dành cho coding agents trên macOS

- **story_id:** `agweb-webkit-browser-for-coding-agents-nov2026`
- **update_id:** `initial`
- **Ngày sự kiện:** 2026-11-14
- **Ngày digest:** 2026-11-16 (Asia/Singapore)
- **Created/updated UTC:** 2026-11-16T00:21:16Z
- **Loại bằng chứng:** source chính thức của dự án; các đánh giá kỹ thuật được ghi rõ là suy luận

## Tổng quan
Agweb là trình duyệt Swift/WebKit cho macOS để coding agents điều khiển web qua CLI mà không chiếm focus của người dùng. Dự án công khai được giới thiệu ngày 14/11.

## Điều gì mới và chi tiết kỹ thuật
Theo [README tác giả](https://github.com/paul-nameless/agweb), agent có thể mở trang, lấy snapshot với element references, click và nhận diff của thay đổi sau thao tác, giảm nhu cầu chụp snapshot liên tục. Mỗi agent có workspace tabs, dashboard theo dõi, profile đăng nhập dùng chung và chế độ chuyển giao login/MFA cho người dùng. Hỗ trợ skill cho Claude Code và Codex; MIT license.

## Ý nghĩa kỹ thuật
Suy luận: Persistent browser workspace và action diffs có thể giảm tool round trips cho browser agents, nhất là khi nhiều agents chạy song song. Phải thử riêng login flows, isolation giữa profiles, khả năng agent truy cập dữ liệu phiên đăng nhập và chính sách website.

## Evidence, availability và giới hạn
Yêu cầu macOS 26 trở lên. WebKit không cung cấp Chrome DevTools Protocol cho công cụ này; không hỗ trợ Chrome extensions và một số hành vi Chrome-specific. Route mocks giới hạn fetch/XHR. Những tuyên bố tiết kiệm RAM/token chưa được benchmark độc lập với workload tương đương. Không thay thế Playwright cho mọi trường hợp.

**Nguồn:** [Repository & README](https://github.com/paul-nameless/agweb).
