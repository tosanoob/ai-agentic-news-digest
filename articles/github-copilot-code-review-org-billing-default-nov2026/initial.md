# Copilot Code Review đổi mặc định phân bổ chi phí

- story_id: github-copilot-code-review-org-billing-default-nov2026
- update_id: initial
- Ngày công bố: 2026-11-25. Digest: 2026-11-26. Bản phân tích chuẩn bị: 2026-11-26T00:51:50.317Z.

## Có gì mới?
GitHub thông báo từ 30/12/2026, nếu policy phân bổ chi phí Copilot Code Review cho thành viên có license của Copilot Business/Enterprise chưa được đặt, mặc định sẽ chuyển sang tổ chức sở hữu repository. Người quản trị đã chọn Member hoặc Organization không bị ghi đè. Chính sách riêng cho người không có license không thay đổi.

## Ngoại lệ
GitHub liệt kê ba trường hợp đặt về Member thay vì Organization: chưa bật chi tiêu AI Credits trả phí, có billing lock, hoặc không có billable customer. Mặc định mới vì vậy không đồng nghĩa mọi lượt review đều chuyển vào hóa đơn tổ chức.

## Việc kỹ sư nên kiểm
Với repo có nhiều review tự động, nên xác định chủ repo, policy có đang bỏ trống hay không và ai cần nhận cảnh báo ngân sách. Nếu dashboard nội bộ gán chi phí cố định theo người gọi, nên kiểm lại sau ngày áp dụng thay vì suy ra phân bổ từ số lượt review.

## Giới hạn
Đây là thông báo thay đổi bên chịu phí, không có bằng chứng bản tin này thay đổi đơn giá riêng của mỗi lượt review. Cần xem cài đặt và dữ liệu thanh toán của tổ chức để biết tác động thực tế.

[Nguồn gốc: GitHub Changelog](https://github.blog/changelog/2026-11-25-copilot-code-review-billing-will-default-to-the-organization/)
