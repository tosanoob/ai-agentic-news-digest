# GitHub Actions chấm dứt ARM32 Linux/Windows trên hosted runners từ 08/12/2026

- **story_id:** `github-actions-arm32-hosted-runner-retirement-nov2026`
- **update_id:** `initial`
- **Ngày công bố:** 2026-11-12
- **Ngày digest (Asia/Singapore):** 2026-11-15
- **Created/updated UTC:** 2026-11-15T00:08:26.617Z
- **Loại:** github_release / runtime infrastructure

## Tổng quan

GitHub thông báo GitHub Actions hosted runners sẽ ngừng hỗ trợ thực thi jobs ARM32 trên Linux và Windows trước hoặc vào ngày 08/12/2026, bao gồm native AArch32 user-space execution. Đây là một thay đổi tương thích hạ tầng CI, không phải bản phát hành model hay giao thức agent.

## Điều gì xảy ra và điểm mới

Theo [GitHub Changelog ngày 12/11/2026](https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement/), nguyên nhân được GitHub liên hệ với việc ngừng hỗ trợ Node 20 và Node 24 không hỗ trợ ARM32. Thông báo áp dụng cho **GitHub-hosted** Linux và Windows runners; không tự suy ra mọi self-hosted runners hoặc ARM64 đều bị loại bỏ.

## Chi tiết kỹ thuật và tác động

ARM32/AArch32 khác ARM64/AArch64. Workflows thực thi native 32-bit ARM binaries, cross-architecture tests, legacy embedded toolchains hoặc phụ thuộc vào môi trường AArch32 trên hosted runners cần kiểm tra trước 08/12. Trong coding-agent pipelines, agent có thể tạo PR thành công nhưng test/build thất bại nếu runner không còn hỗ trợ kiến trúc mục tiêu. Nên kiểm kê workflow matrices, runner images, dependencies và build/test architecture, sau đó chuyển workload phù hợp sang ARM64 hoặc self-hosted environment được quản trị; không coi ARM64 là thay thế tương đương nếu binaries bắt buộc 32-bit.

## Đề xuất triển khai (phân tích)

1. Tìm `arm32`, `aarch32`, `armv7` trong workflows và scripts.
2. Phân biệt native execution với cross-compilation; xác định có thực sự phụ thuộc AArch32 user-space hay không.
3. Chạy canary trên runner thay thế, lưu artifacts và regression results.
4. Với autonomous agents, thêm environment capability checks trước khi lập kế hoạch test để tránh retry loops không thể thành công.

## Evidence, availability và giới hạn

**Fact được xác minh:** thông báo ngày 12/11 và mốc ngừng hỗ trợ 08/12/2026. **Suy luận kỹ thuật:** ảnh hưởng đến coding-agent CI và hướng migration. GitHub không đưa ra benchmark về performance, tỷ lệ workflow bị ảnh hưởng hay chi phí chuyển đổi. Chưa xác minh kết quả sau deadline; không khẳng định retirement đã xảy ra.

**Nguồn chính thức:** [GitHub Changelog — Actions for ARM32 Linux & Windows retirement (12/11/2026)](https://github.blog/changelog/2026-11-12-actions-for-arm32-linux-windows-retirement/).
