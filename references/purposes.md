# Thư viện mục đích video

Mục đích là **video làm ra để làm gì**. File này dùng để **gợi ý style** cho từng mục đích, không phải luật: người dùng
chọn style nào cũng được, kể cả style không nằm trong gợi ý. Khung thời gian và "Thường cần" chỉ là tham khảo khi lên
kịch bản, bỏ qua được nếu người dùng muốn khác.

Mỗi mục có:
- **Mục tiêu:** người xem phải hiểu, nhớ hay làm gì sau khi xem.
- **Khung 60-90 s:** cấu trúc mặc định theo độ dài video của người dùng (xem "Yêu cầu trực tiếp" trong `motion-taste.md`).
- **Thường cần:** những thứ video loại này hay có (tham khảo, không bắt buộc).
- **Style gợi ý:** 2-3 style hợp mục đích này và hợp gu, xếp theo điểm của người dùng.
- **Hỏng khi:** lỗi thường gặp làm video nhàm hay rẻ tiền.
- **Gu của bạn:** rút từ mẫu đã chấm. Số mới nhất luôn lấy bằng `python3 $T/scripts/taste.py purpose <id>`.

Lưu ý khi đọc điểm theo mục đích: điểm của một mục đích phần lớn là điểm của **style** các mẫu thuộc mục đích đó. Ví dụ
explainer chỉ được 3,0 vì có cả mẫu chữ slide (1 điểm) lẫn mẫu Adobe kinetic type (5 điểm). Không kết luận "bạn ghét
explainer". Đọc phần "thích khi / ghét khi" bên dưới.

Cách dùng: khi người dùng chưa chọn style, đưa 2-3 "Style gợi ý" của mục đích đó để họ chọn. Khi người dùng đã chọn
style, không đổi theo file này. Thứ tự ưu tiên khi ghép brief vẫn là: luật cứng > yêu cầu trực tiếp > gu trong style >
rule chung > mặc định của style; mục đích chỉ góp ý ở bước chọn style và khung kịch bản.

---

## giai_thich - Video giải thích (explainer)
- **Mục tiêu:** người xem hiểu một khái niệm, quy trình hay cách một thứ hoạt động, và nhớ được 1 ý chính.
- **Khung 60-90 s:** hook bằng vấn đề hoặc câu hỏi (0-5 s) → 3-5 ý, mỗi ý 10-15 s, **mỗi ý một hình ẩn dụ** →
  tóm lại 1 câu (5 s) → logo/CTA (3-5 s).
- **Thường cần:** chữ đọc được trên điện thoại (chữ chính ≥ 5% chiều cao khung); một hình chủ thể mỗi cảnh; giọng đọc
  hoặc chữ dẫn mạch.
- **Hỏng khi:** thành slide chữ; liệt kê tính năng máy móc; icon nét mảnh trên nền trắng; bản đồ hiện sẵn rồi chỉ sáng
  dần từng khu.
- **Style gợi ý:** `kinetic_type` có chữ biến hình + nét vẽ tay (r1s1, r3s6) · `isometric` có camera di chuyển (r2s2) · `collage`
- **Gu của bạn** (7 mẫu, trung bình 3,0, tin cậy thấp):
  - Thích khi: chữ là nhân vật, biến hình liên tục, màu nhấn ấm (Adobe r1s1, 5); isometric có camera đi xuyên thành phố
    (Sitenna r2s2, 4); chuyển cảnh đẩy/trượt (push 4,7 trên 3 mẫu).
  - Ghét khi: chữ sans căn giữa trên nền trắng kiểu slide (r2s1, **luật cứng**); explainer SaaS icon mảnh (r2s7, 2);
    infographic lặp không có camera (r1s8, 2); nhân vật flat kiểu công ty (r3s4 style −).

## gioi_thieu_san_pham - Giới thiệu sản phẩm / app / tính năng
- **Mục tiêu:** người xem biết sản phẩm là gì, nó làm được điều gì khác, và muốn thử.
- **Khung 60-90 s:** hook bằng lợi ích hoặc nỗi đau (0-5 s) → sản phẩm xuất hiện trước giây 10 → 2-3 lợi ích, mỗi lợi
  ích một tình huống (15-20 s/lợi ích) → khoảnh khắc "wow" → tên + CTA (5 s).
- **Thường cần:** sản phẩm hoặc giao diện thật xuất hiện, nhưng **trong một câu chuyện hay thế giới**, không đứng một mình;
  tên sản phẩm đọc được ở cuối.
- **Hỏng khi:** đi lần lượt từng màn hình app; điện thoại 3D xoay trên gradient (luật cứng của bạn, r1s4); liệt kê tính năng.
- **Style gợi ý:** `kinetic_type` + `hand_drawn` kiểu hype film (r3s6) · `collage` với sản phẩm làm đạo cụ · `character_2d` có cá tính
- **Gu của bạn** (4 mẫu, 3,0, mâu thuẫn):
  - Thích khi: phim "hype" chữ serif khổng lồ + nét vẽ tay, UI chỉ chen vào vài khung (Affinity r3s6, 5).
  - Ghét khi: UI promo (1,0), flat vector (1,4), 3D sản phẩm, không khí công nghệ lạnh.
  - Cách làm hợp gu: để sản phẩm là **đạo cụ trong thế giới vẽ tay/collage**, không phải màn hình trên nền trống.

## quang_cao - Quảng cáo, chiến dịch
- **Mục tiêu:** người xem nhớ thương hiệu và có cảm xúc với nó; kết bằng slogan hoặc CTA.
- **Khung 60-90 s:** hook bằng hành động hoặc thế giới lạ (0-3 s) → nhân vật đi qua 3-5 thế giới/thử thách, mỗi chặng
  10-20 s → cao trào → sản phẩm/logo + slogan (5-8 s).
- **Thường cần:** một nhân vật hoặc vật có cá tính dẫn chuyện; sản phẩm là đích đến của hành trình.
- **Hỏng khi:** nhân vật an toàn kiểu công ty; mở đầu bằng thẻ tiêu đề đứng yên; nhịp chậm 5 s/cảnh (Vipps r4s5, 3).
- **Style gợi ý:** `collage` giấy cắt (r1s3, r2s3) · `character_2d` có cá tính (r3s1, r3s2) · `retro` game
- **Gu của bạn** (6 mẫu, **4,3, Nên, tin cậy cao**): mục đích bạn thích nhất.
  - Thích khi: collage giấy cắt (5,0 trên 2 mẫu: Mamos r1s3, Starbucks r2s3), 2D nhân vật cá tính (4,6 trên 5 mẫu:
    Bittrex r3s1, Mirinda r3s2), retro game (4,2), không khí vui tươi/năng động/hoài cổ ấm.
  - Ghét khi: kiểu cổ 1930 nhịp chậm, màu tối (r4s5, 3).

## phim_thuong_hieu - Phim thương hiệu / manifesto / rebrand
- **Mục tiêu:** người xem hiểu thương hiệu tin vào điều gì; cảm xúc hơn thông tin.
- **Khung 60-90 s:** câu mở mạnh (0-5 s) → vấn đề hay điều thương hiệu chống lại → lời tuyên bố (chữ to) → hình ảnh
  tương lai → logo.
- **Thường cần:** một câu tuyên bố rõ; chữ là điểm nhấn lớn.
- **Hỏng khi:** chữ tĩnh trên nền trống; ảnh stock; giọng sáo rỗng.
- **Style gợi ý:** `kinetic_type` + `hand_drawn` (r3s6) · `collage` in lụa giấy ấm (r4s4)
- **Gu của bạn** (1 mẫu, 5,0, tin cậy thấp): Affinity r3s6, chữ serif tràn khung đổi mỗi ~0,5 s + nét vẽ tay + màu nhấn
  lime trên đen.

## ident_intro - Ident, intro, mở màn sự kiện, logo reveal
- **Mục tiêu:** tạo không khí và để lại logo/tên trong 5-30 s (intro sự kiện có thể tới 60 s).
- **Khung:** 1 ý hình duy nhất biến đổi liên tục → logo khoá ở 2-3 s cuối.
- **Thường cần:** logo hoặc tên rõ ở cuối; có một "chữ ký" chuyển động lặp lại được.
- **Hỏng khi:** kết bằng màn tối; quá nhiều ý cho thời lượng ngắn.
- **Style gợi ý:** `hand_drawn` biến hình theo nhạc (r4s1) · `kinetic_type` chữ to · `isometric` (chưa có mẫu ident được thích, gợi ý từ gu chung)
- **Gu của bạn** (1 mẫu, 2,0): stop-motion đất sét cho lễ trao giải (r1s7) không hợp. Chưa đủ dữ liệu.

## video_nhac - Music video, lyric video, visual cho show
- **Mục tiêu:** hình phục vụ nhạc; người xem cảm nhịp.
- **Khung:** theo cấu trúc bài (intro / verse / drop); đổi hình trên phách mạnh.
- **Thường cần:** khớp beat; lời (nếu lyric video) đọc được.
- **Hỏng khi:** trừu tượng tối, chữ nhỏ (**luật cứng**, r1s2); chữ trắng đen không có hình.
- **Style gợi ý:** `hand_drawn` màu rực biến hình theo phách (r4s1) · `collage`
- **Gu của bạn** (3 mẫu, 2,0, Tránh, tin cậy vừa). Lưu ý: cả 3 mẫu đều thiếu nhân vật hoặc tối/đơn sắc (r1s2 1,
  r2s6 2, r2s4 3). Nhạc dẫn dắt hình thì bạn lại rất thích khi có nhân vật vẽ tay màu rực (Salsa r4s1, 5). Điểm thấp ở
  đây là vì style, chưa chắc vì mục đích.

## trailer - Trailer, teaser, montage
- **Mục tiêu:** người xem tò mò và muốn xem/đọc/chơi bản đầy đủ.
- **Khung 60-90 s:** tiêu đề hoặc hình gây tò mò → chuỗi khoảnh khắc đẹp nhất, nhịp tăng dần theo nhạc → tiêu đề cuối.
- **Thường cần:** nhạc dâng dần; tiêu đề chốt cuối.
- **Hỏng khi:** kể hết chuyện; nhịp đều từ đầu tới cuối.
- **Style gợi ý:** `collage` / minh hoạ in lụa giấy ấm (r4s4) · `character_2d` góc máy điện ảnh
- **Gu của bạn** (1 mẫu đã chấm, 5,0): montage minh hoạ giấy ấm in lụa, nhạc mở nhỏ rồi dâng (Biggest Story r4s4).
  The Bystanders (r4s2) chưa chấm.

## phim_ngan - Phim ngắn kể chuyện / nghệ thuật
- **Mục tiêu:** một câu chuyện hoặc thông điệp, không bán gì.
- **Khung 60-90 s:** thiết lập nhân vật (10 s) → biến cố → hậu quả → hình ảnh ẩn dụ kết.
- **Thường cần:** một nhân vật người xem theo được từ đầu tới cuối.
- **Hỏng khi:** mở bằng màn đen/tiêu đề dài; 3D hiện thực (không phải nhu cầu); rubber hose đen trắng (**luật cứng**).
- **Style gợi ý:** `hand_drawn` bút chì (r1s5) · `character_2d` (r2s5)
- **Gu của bạn** (4 mẫu, 3,25): vẽ tay bút chì (Balconada r1s5, 5) và 2D thông điệp môi trường (The Flat r2s5, 4 rồi 3).

## noi_dung_mxh - Nội dung mạng xã hội, doodle, loop
- **Mục tiêu:** dừng ngón tay lướt trong 1 s, xem hết, chia sẻ.
- **Khung:** hook chuyển động ngay khung 0; một ý; kết có thể lặp vòng.
- **Thường cần:** đọc được không cần tiếng; khổ theo nền tảng (9:16 / 1:1).
- **Style gợi ý:** `hand_drawn` màu rực (r4s1) · `character_2d` có cá tính · `kinetic_type` chữ to
- **Gu của bạn** (1 mẫu, 5,0): Google Doodle Salsa (r4s1), 2D vẽ tay màu rực biến hình theo nhạc.

## showreel - Showreel, demo kỹ thuật, demo font
- **Mục tiêu:** khoe năng lực hoặc một style.
- **Style gợi ý:** gắn các cảnh vào một mạch kể; style theo gu chung (`hand_drawn`, `collage`, `isometric`)
- **Gu của bạn** (2 mẫu, 2,0, Tránh): chuỗi cảnh rời không có mạch (Sparkol r3s3), demo font pixel (r2s8). Nếu phải
  làm, hãy gắn các cảnh vào một mạch kể.

---

## Thêm mục đích mới
Khi một mẫu không vừa mục đích nào: thêm một mục theo khung trên vào cuối file, thêm tag vào bảng `muc_dich` trong
`categories.md`, rồi gắn tag cho mẫu.
