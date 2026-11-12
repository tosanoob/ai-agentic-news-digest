# UPDATE: Claude Fable 5.2 GA trong GitHub Copilot — lưu ý data retention

- story_id: `anthropic-claude-fable-mythos-5-2-nov2026`
- update_id: `copilot-ga-2026-11-09`
- Ngày cập nhật gốc: 2026-11-09
- Ngày digest (Asia/Singapore): 2026-11-12
- Tạo/cập nhật UTC: 2026-11-12T00:06:53.019Z

## Tổng quan
Đây là **material availability/governance update** của sự kiện Anthropic ra mắt Fable/Mythos 5.2 ngày 09/11, đã được lưu trong ledger. GitHub thông báo Fable 5.2 GA trong Copilot, cùng những điều kiện xử lý dữ liệu có ý nghĩa đặc biệt với enterprise.

## Thay đổi mới được xác minh
Theo [GitHub Changelog](https://github.blog/changelog/2026-11-09-claude-fable-5-5-in-github-copilot/), Fable 5.2 được cung cấp cho Copilot Pro+, Max, Business, Enterprise trên VS Code, Visual Studio, Copilot CLI, cloud coding agent, Copilot app, github.com, mobile và các IDE khác; rollout theo đợt. Business/Enterprise phải bật model policy, mặc định tắt. Model được tính phí theo provider list pricing, usage-based.

**Quan trọng:** Fable 5.2 mặc định yêu cầu Anthropic lưu prompts/outputs để vận hành safety classifiers; GitHub cho biết dữ liệu đó không được dùng huấn luyện model. Một số enterprise đủ điều kiện có thể nhận ngoại lệ zero-data-retention đến hết năm 2026, sau đó yêu cầu Enterprise Frontier Safeguards. Chính sách này khác đáng kể với kỳ vọng ZDR phổ biến của doanh nghiệp.

## Đánh giá kỹ thuật
**Vendor claim:** GitHub nói thử nghiệm sớm cho thấy Fable 5.2 hoàn thành nhiều tasks hơn Fable 5.1 với ít steps/tool calls hơn, nhưng không công bố ở đây mẫu benchmark, confidence intervals hay chi phí chuẩn hóa. Không nên suy ra hiệu quả định lượng hoặc so sánh với Gemini 4 Carbon từ phát biểu này.

**Suy luận:** Khi đưa Fable 5.2 vào coding-agent pipeline có source code nội bộ, cần đánh giá data residency, retention, quyền admin, khả năng ZDR, pricing và tool access trước khi bật rộng. Chính sách model là một phần của agent governance, không chỉ model quality.

## Availability và bất định
Tính năng GA nhưng rollout không đồng thời cho mọi account. Quyền ZDR cần phê duyệt riêng, không tự kích hoạt. Bài đăng GitHub có URL slug `fable-5-5` nhưng tiêu đề và nội dung nói rõ Fable 5.2; ghi theo nội dung nguồn, không diễn giải slug thành phiên bản khác.

**Nguồn:** [GitHub Changelog](https://github.blog/changelog/2026-11-09-claude-fable-5-5-in-github-copilot/); [Anthropic model announcement](https://www.anthropic.com/claude-fable-and-mythos-5-2).