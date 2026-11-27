# Parallel subagents khi dựng repo: thêm 1–5 điểm phần trăm, chi phí tới 3,8 lần

- story_id: parallel-subagents-coding-repository-construction-nov2026
- update_id: initial
- Ngày nguồn (UTC): 2026-11-25. Digest: 2026-11-27. Biên tập: 2026-11-27T06:31:54.509Z.

## Có gì mới?
Trên các task lấy ngẫu nhiên từ hai benchmark dựng repo, parallel subagents tăng tỷ lệ hidden test pass khoảng 1–5 điểm phần trăm và không thắng single-agent khi so cùng chi phí.

## Cơ chế
Nghiên cứu so một agent và lead có subagent trên NL2Repo và ProgramBench. Một phần chênh lệch đến từ khả năng kiểm tra lại: trong một số task khó của ProgramBench, yêu cầu single agent thăm dò chương trình tham chiếu thu hồi phần lớn lợi ích với chi phí thấp hơn. Các tác giả cũng tách hiệu ứng context mới và tính mô-đun.

## Việc đáng thử
Bắt đầu bằng một agent có tiêu chí kiểm thử rõ và đo theo ngân sách ngang nhau. Chỉ bật chạy song song nếu có phần việc độc lập hoặc cần thêm một lượt kiểm tra mà lead thường bỏ qua.

## Giới hạn
Đây là preprint về dựng repository từ đặc tả, không phải toàn bộ tác vụ lập trình. Kết luận theo điều kiện thử của hai benchmark, không loại trừ lợi ích ở repo thật. Bài này có trong raw log nhưng không có trong shortlist vì chạm trần arXiv.

[Nguồn gốc 1](https://arxiv.org/abs/2611.33893) · [Nguồn gốc 2](https://arxiv.org/html/2611.33893v1)
