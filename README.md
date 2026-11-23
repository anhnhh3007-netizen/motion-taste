# motion-taste

Skill cho Claude Code để **học gu motion graphics và animation** của một người qua từng vòng chấm mẫu, rồi dùng gu đó
khi thiết kế video.

- **Phỏng vấn gu:** Claude tự tìm 5-10 video mẫu có thật (≤ 90 s), xem bằng contact sheet, tách theo 14 category
  (style, không khí, mục đích, hook, nhịp, chuyển cảnh, chữ, chuyển động, màu, bố cục, kiểu hình, âm thanh, phụ đề, cấu trúc).
  Người dùng chấm từ "Rất thích" đến "Không bao giờ"; Claude chỉ ghi lại rule thích/ghét vào `motion-taste.md`, kèm
  audit và độ tin cậy.
- **Thiết kế theo style và mục đích:** ghép mục đích video (`references/purposes.md`: giải thích, giới thiệu sản phẩm,
  quảng cáo, phim thương hiệu, ident, video nhạc, trailer, phim ngắn, mạng xã hội, showreel) với ngữ pháp của một style
  trong `references/styles.md` (18 style) và gu đã học thành một style brief dựng được.

## Cấu trúc
| Đường dẫn | Nội dung |
|---|---|
| `SKILL.md` | Quy trình cho Claude: một vòng 5 bước, thiết kế theo style, định dạng dữ liệu |
| `motion-taste.md` | Bộ rule gu hiện tại (luật cứng, yêu cầu trực tiếp, Nên/Tránh, bảng bằng chứng) |
| `references/categories.md` | 14 category và bộ tag chuẩn |
| `references/build-recipes.md` | Công thức dựng từng style bằng Remotion; mặc định `code_polished` |
| `references/purposes.md` | 10 mục đích video: mục tiêu, khung 60-90 s, điều bắt buộc, gu |
| `references/styles.md` | Thư viện 18 style: nhận diện, ngữ pháp mặc định, cách dựng, lỗi làm rẻ tiền |
| `references/sourcing.md` | Tìm, lọc (≤ 90 s) và xem mẫu tiết kiệm token |
| `scripts/taste.py` | `status`, `new-round`, `coverage`, `export`, `import-ratings`, `audit`, `style [id]`, `purpose [id]` |
| `scripts/probe.js` | Chạy trong trình duyệt: đo nhịp cắt và vẽ contact sheet 12 khung của một video |
| `data/rounds/` | Mẫu, phần phân tích và điểm chấm của từng vòng |

## Cài đặt
```bash
git clone https://github.com/anhnhh3007-netizen/motion-taste ~/.claude/skills/motion-taste
```
Cần Python 3 (không cần thư viện ngoài cho `taste.py`). Trang chấm điểm là một Claude artifact riêng của tác giả;
người khác có thể chấm trong tin nhắn (`1: 5`, `2: 3 chữ+ màu-`).

Mẫu tham khảo chỉ được ghi bằng link và mô tả; skill không lưu lại video hay khung hình của người khác.
