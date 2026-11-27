# Google ADK Python 2.15: đo agent đúng ít nhất một lần và đúng ở mọi lần chạy

- story_id: google-adk-python-v2-15-eval-nov2026
- update_id: initial
- Ngày nguồn (UTC): 2026-11-25. Digest: 2026-11-27. Biên tập: 2026-11-27T06:31:54.509Z.

## Có gì mới?
Bản 2.15.0 thêm pass@k, pass^k và chấm từng tham số tool; bản vá 2.15.1 phát hành ngày 25/11 xử lý lưu kết quả stream A2A và tương thích sampling với Anthropic SDK.

## Cơ chế
ADK CLI đo riêng một test case thành công ít nhất một lần hoặc thành công ở mọi lần trong k lượt, rồi tổng hợp qua tập eval. Chấm tham số tool có thể cho điểm từng trường, thay vì chỉ tính đúng hoặc sai cả lần gọi. Bản 2.15.1 sửa phần lưu output của RemoteA2aAgent bằng cách hoàn tác hành vi lưu stream khi thiếu last_chunk, và sửa tương thích sampling qua các phiên bản Anthropic SDK.

## Việc đáng thử
Với một fixture yêu cầu giữ lại hai nguồn mâu thuẫn và chuyển cho người duyệt, chạy lại năm lần với input cố định. Đo cả thành công ít nhất một lần lẫn thành công cả năm lần. Các trường tool nhạy cảm có thể giữ tiêu chí bắt buộc riêng, không để điểm trung bình che lỗi.

## Giới hạn
Hai metric được công bố trong 2.15.0 ngày 19/11; mục này gộp bản vá phát hành 25/11 UTC, không coi chúng là tính năng mới của 2.15.1. Release notes không chứng minh cải thiện chất lượng trên ứng dụng của bạn.

[Nguồn gốc 1](https://github.com/google/adk-python/releases/tag/v2.15.1) · [Nguồn gốc 2](https://github.com/google/adk-python/releases/tag/v2.15.0)
