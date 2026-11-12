# Git vá sáu lỗ hổng bảo mật: tác động trực tiếp đến coding-agent runtimes

- story_id: `git-six-security-vulnerabilities-nov2026`
- update_id: `initial`
- Ngày công bố: 2026-11-10
- Ngày digest (Asia/Singapore): 2026-11-12
- Tạo/cập nhật UTC: 2026-11-12T00:06:53.019Z

## Tổng quan
Git công bố các bản vá cho sáu CVE, trong đó có khả năng thực thi mã khi recursive clone một repository độc hại. Đây là sự kiện bảo mật upstream Git, không phải một phát hành agent model.

## Điều gì mới?
Theo [thông báo GitHub ngày 10/11](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/), các bản vá có trong Git 2.56.1 và các maintenance releases 2.55.1, 2.54.1, 2.53.1, 2.52.1, 2.51.3, 2.50.2.

- **CVE-2026-111760:** integer truncation ở đường dẫn index có thể dẫn đến ghi đè submodule `.git` bằng symlink và thực thi hook/config của attacker trong recursive clone.
- **CVE-2026-113408:** HEAD symref không được xác thực từ Git protocol v2 có thể dẫn đến path traversal và ghi ngoài thư mục ref.
- **CVE-2026-114467:** xử lý nhiều chữ ký GPG có thể ghi quá giới hạn stack.
- **CVE-2026-114469:** binary patch nén có thể bung quá giới hạn, gây out-of-bounds read.
- **CVE-2026-105437:** integer overflow khi merge kết quả lớn có thể gây heap corruption.
- **CVE-2026-114466:** fast-import streams có thể lợi dụng một số features để đọc/ghi file ngoài repository; các features nguy hiểm nay bị từ chối trừ khi explicitly allowed.

## Ý nghĩa cho AI/agent engineering
**Suy luận kỹ thuật:** coding agents thường clone repositories, merge PRs và áp dụng patches từ nguồn bên ngoài. Vì vậy, chính Git client trong sandbox là một phần attack surface, ngay cả khi agent có prompt-injection defenses. Ưu tiên vá Git trong runners, containers, local developer machines và bundled Git; hạn chế recursive clone từ nguồn không tin cậy. GitHub nói đã vá GitHub.com và đang phối hợp cập nhật các sản phẩm có bundled Git.

## Giới hạn bằng chứng
Các mô tả và mức độ ảnh hưởng dựa trên advisory của GitHub/Git upstream, không phải kiểm thử exploit độc lập trong bản tin. Không suy ra mọi môi trường đều có thể bị khai thác; điều kiện phụ thuộc lệnh, dữ liệu và bản Git.

**Nguồn gốc:** [GitHub security announcement](https://github.blog/open-source/git/git-security-vulnerabilities-announced-7/).