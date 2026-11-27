# OpenAI Agents SDK 0.26.0 đổi thứ tự metadata MCP và kiểm Realtime cuối lượt

- story_id: openai-agents-python-v0-26-0-nov2026
- update_id: initial
- Ngày nguồn (UTC): 2026-11-24. Digest: 2026-11-27. Biên tập: 2026-11-27T06:31:54.509Z.

## Có gì mới?
Metadata truyền trực tiếp từng lần gọi MCP được ưu tiên hơn resolver và mặc định discovery; Realtime kiểm phần output còn lại khi kết thúc lượt.

## Cơ chế
Nếu cùng khóa metadata xuất hiện ở nhiều lớp, giá trị tường minh theo lần gọi đứng trước resolver của ứng dụng và mặc định discovery. Guardrail Realtime kiểm phần văn bản hoặc transcript âm thanh còn lại ở cuối lượt. Release cũng siết Storage mount trong Docker và yêu cầu ứng dụng cấp phép ảnh local cho Codex tool.

## Việc đáng thử
Trước khi nâng cấp, kiểm thử một tool có metadata trùng giữa ba nguồn và một lượt Realtime ngắn kết thúc ngay sau chunk cuối. Nếu ứng dụng dùng mount Docker hoặc ảnh local trong Codex tool, kiểm lại quyền và hành vi lỗi phù hợp.

## Giới hạn
Các thay đổi thuộc bản Python SDK 0.26.0, không phải sự thay đổi của chuẩn MCP hay mặc định ở mọi runtime. Ghi chú release không phải phép đo độ trễ hay bảo đảm guardrail phát hiện mọi lỗi.

[Nguồn gốc 1](https://github.com/openai/openai-agents-python/releases/tag/v0.26.0)
