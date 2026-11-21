# GitHub GA quyền security advisory theo custom repository roles

- **story_id:** `github-security-advisory-custom-role-ga-nov2026`
- **update_id:** `initial`
- **Ngày công bố gốc:** 2026-11-20
- **Ngày digest (Asia/Singapore):** 2026-11-21
- **Tạo/cập nhật nội dung (UTC):** 2026-11-21T00:34:17Z
- **Loại:** security

## Tổng quan

GitHub cho phép phân quyền quản lý private vulnerability reports và security advisories theo từng repository, thay vì cấp quyền quản trị rộng.

## Điều gì xảy ra và điểm mới

Bốn quyền: View; Create/Edit/Manage; Accept private reports and close/reopen advisories; Publish advisories and request CVEs. Hai quyền sau yêu cầu View hoặc Create/Edit/Manage. Merge từ temporary private fork vẫn cần repository admin hoặc security manager; người có các quyền mới không thể xóa private fork. Confidential comments đòi hỏi quyền Create/Edit/Manage và write access.

Nguồn chính thức: [GitHub — GitHub GA quyền security advisory theo custom repository roles](https://github.blog/changelog/2026-11-20-security-advisory-permissions-are-now-generally-available/).

## Chi tiết kỹ thuật và tác động đến AI/agent engineering

Một vulnerability-triage agent hoặc security response team có thể được phân quyền hẹp theo repository, tách quyền đọc báo cáo, phân loại và công bố CVE. Nên giữ publish/CVE request dưới approval của người có trách nhiệm; kiểm tra custom-role support theo plan.

## Bằng chứng, khả dụng và giới hạn

GA chỉ trên các organization plans hỗ trợ custom repository roles, gồm Enterprise Cloud. Đây là thay đổi authorization, không chứng minh hiệu quả phát hiện lỗ hổng hoặc chất lượng báo cáo AI.

**Phân loại bằng chứng:** Các khả năng, phạm vi triển khai và số liệu được ghi nhận từ công bố GitHub (vendor-reported facts/claims). Những khuyến nghị kiến trúc ở phần tác động là suy luận kỹ thuật của bài viết, không phải kết quả thử nghiệm độc lập. Không có peer-reviewed benchmark cho sự kiện này.

## Nguồn gốc

- [Thông báo và dữ liệu chính thức của GitHub](https://github.blog/changelog/2026-11-20-security-advisory-permissions-are-now-generally-available/)
