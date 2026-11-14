# GitHub Copilot app hỗ trợ GitHub Enterprise Server ở trạng thái GA

- **story_id:** `github-copilot-app-ghes-ga-nov2026`
- **update_id:** `initial`
- **Ngày sự kiện/công bố:** 2026-11-13
- **Ngày digest (Asia/Singapore):** 2026-11-14
- **Created/updated UTC:** 2026-11-14T00:44:16Z
- **Loại:** enterprise

## Tổng quan

Copilot app 1.2.0+ đưa kết nối GHES từ opt-in preview lên GA cho remote repositories, issues, PRs; phải đăng nhập GitHub.com/GHE.com trước và cloud sessions chưa hỗ trợ GHES.

## Điều gì xảy ra và điểm mới

GitHub công bố GHES integration trong GitHub Copilot app đạt GA ngày 13/11, sau giai đoạn opt-in preview. Người dùng có thể thêm GHES account để làm việc với remote repositories, issues và pull requests. Điều kiện: đăng nhập GitHub.com hoặc GHE.com trước, sau đó Settings > Accounts > Add account > GitHub Enterprise Server. Cần Copilot app phiên bản 1.2.0 trở lên.

## Ý nghĩa thực tiễn với AI/agent engineering (phân tích, không phải vendor claim)

Enterprise teams dùng self-hosted GitHub có thêm lựa chọn agent workspace thống nhất cho repository context. Nhưng kiến trúc deployment cần tách khả năng truy cập GHES metadata/repository khỏi cloud execution: cloud sessions chưa hỗ trợ GHES. Kiểm tra network, identity boundaries và data handling trước khi áp dụng.

## Bằng chứng, giới hạn và availability

GA chỉ cho kết nối GHES trong Copilot app, không phải tuyên bố hỗ trợ mọi agent feature trên GHES. Không có benchmark về task success hoặc security posture.

## Nguồn chính thức

- [Nguồn công bố](https://github.blog/changelog/2026-11-13-github-enterprise-server-support-in-the-github-copilot-app/)

**Phân loại bằng chứng:** Ngày công bố, API/availability và tính năng là thông tin từ nhà cung cấp; các đánh giá kỹ thuật và đề xuất triển khai là suy luận của người viết. Không có benchmark độc lập mới được xác minh cho sự kiện này.
