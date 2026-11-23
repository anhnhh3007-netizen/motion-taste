# Motion taste: gu video của tôi

Bộ rule rút từ các vòng chấm mẫu (skill `motion-taste`). Mỗi rule ghi phạm vi áp dụng: `motion` (motion graphics dựng
bằng code), `animation` (phim hoạt hình) hoặc `cả hai`, kèm độ tin cậy và mẫu dẫn chứng.

Trạng thái: **4 vòng · 28 mẫu đã chấm (2026-11-22).** Độ nhất quán: mẫu chiếu lại lệch 1 điểm (đạt).

## Tóm tắt gu
Sau 4 vòng (28 mẫu), điều bạn thích rõ nhất là **2D có cá tính và năng lượng**: cartoon cel màu rực kể chuyện nhanh
(Bittrex r3s1, Mirinda r3s2, Starbucks r2s3), thế giới vẽ tay hoặc giấy cắt có vân (r1s5, r2s3), và chữ to biến đổi
nhanh đi cùng nét vẽ tay (Affinity r3s6). Hook mạnh bằng chuyển động ngay khung đầu, nhịp 1-2 s/cảnh hoặc hình biến liên tục theo nhạc (Salsa r4s1). Minh hoạ giấy ấm có texture in cũng được "Rất thích" (r4s4). Bạn **không**
thích 2D nhân vật kiểu công ty an toàn (Sparkol, Pipedrive), rubber hose đen trắng, video chỉ có chữ tĩnh kiểu slide,
explainer liệt kê, UI sản phẩm, trừu tượng tối. 3D chưa phải nhu cầu.

## Yêu cầu trực tiếp
Điều bạn nói thẳng (không phải suy từ điểm chấm). Ưu tiên ngay sau luật cứng, đè lên rule rút từ điểm.
- **Độ dài video: 60-90 s** (khoảng 1 phút đến 1 phút 30). Cấu trúc, số cảnh và hook phải tính cho độ dài này.
  (vòng 1, trả lời câu hỏi audit)
- **Nhịp nhanh hơn 3-4 s/cảnh:** mục tiêu khoảng **1-2 s/cảnh**, với 60-90 s là khoảng 35-60 cú cắt hoặc đổi trạng
  thái lớn. (vòng 1, trả lời câu hỏi audit)

## Bài học từ video Claude làm (trọng số cao)
Rút từ video **do Claude dựng** rồi bạn chấm mù, nên phản ánh đúng cái Claude làm được. Xếp ngay sau "Yêu cầu trực
tiếp", trên mọi rule rút từ mẫu tham khảo. Chi tiết: `data/own/`.
- **Hoàn thiện và chuyên nghiệp trước, style sau.** Thử nghiệm AB1: bản theo gu (giấy kem phẳng, nét rung giả vẽ tay
  bằng code, mặt cười trên mọi vật, em bé hình que, Marker Felt) bị chấm **Không thích (2)**, vì "trông nghiệp dư, trẻ
  con". Bản mặc định (không gian xanh than `#0E1430`, Mặt Trời phát sáng, gradient, chiều sâu, Avenir Next Heavy) được
  **Thích (4)**, vì "trông chuyên nghiệp, đẹp". · cả hai
  - Khi chỉ dựng bằng code: **không giả vẽ tay bằng nét nguệch ngoạc**. Dùng hình vector sạch có ánh sáng, gradient,
    phát sáng, nhiều lớp sâu. Không gắn mắt/mặt cười lên mọi vật; tối đa một nhân vật có mặt.
  - Rule "vẽ tay", "collage" trong phần Nên là gu về **mẫu do studio vẽ thật**. Chỉ áp dụng khi có tài sản hình chất
    lượng (ảnh sinh, hình vẽ sẵn, ảnh cắt), không áp bằng hiệu ứng code.
  - Font tay kiểu Marker Felt / Chalkboard: không dùng.
- **Giải thích phải rõ:** mỗi lúc một ý, một hình chủ thể. Tránh nhiều vệt, nhiều đường chồng chéo trên màn hình
  (đoạn tia xanh nảy 8 lần của AB1-A "rối, khó hiểu"). Thêm thông tin thật làm điểm tựa (con số, nhãn ngắn), như
  "8 phút 20 giây", "sóng ngắn → tán xạ mạnh" của AB1-B. · cả hai
- **Camera bám theo vật và chuyển cảnh thông minh:** match cut (chấm → Mặt Trời), whip theo hướng chuyển động, camera
  đẩy vào chi tiết ở điểm va chạm. Bạn nêu đích danh đây là điểm thích ở AB1-B. · cả hai
- Nền tối không gian xanh than với vật phát sáng cam/xanh được thích (AB1-B), khớp rule cũ: nền tối ổn khi có màu nhấn
  rực và năng lượng; chỉ tránh tối bí ẩn, trừu tượng không có chủ thể.

## Luật cứng
- **Không** làm video trừu tượng tối: nền gần như đen, hình mờ trôi chậm, chữ rất nhỏ, gần như không có nội dung để
  đọc. (vòng 1, r1s2 "Không bao giờ")
- **Không** làm UI/app promo kiểu điện thoại 3D xoay trên nền gradient xanh lạnh, đi lần lượt từng màn rồi kết bằng nút
  store. (vòng 1, r1s4 "Không bao giờ")
- **Không** làm explainer chỉ có chữ kiểu slide: câu sans căn giữa trên nền trắng, chen ảnh stock, gần như không chuyển
  động. (vòng 2, r2s1 "Không bao giờ")
- **Không** làm hoạt hình rubber hose đen trắng kiểu 1920s: nét mực, nền xám, nhân vật kiểu Mickey 1928. (vòng 3, r3s5
  "Không bao giờ")

## Theo mục đích video
Dùng để **gợi ý style** khi bạn chưa chọn, không bắt buộc: bạn chọn style nào cũng được. Khung 60-90 s và style gợi ý
của từng mục đích: `references/purposes.md`. Điểm theo mục đích chủ yếu phản ánh style của các mẫu, nên đọc "thích khi /
ghét khi", đừng đọc riêng con số.
| Mục đích | Điểm (mẫu) | Thích khi | Ghét khi |
|---|---|---|---|
| **Quảng cáo, chiến dịch** | **4,3 (6) · Nên, tin cậy cao** | Collage giấy cắt, 2D nhân vật cá tính đi qua nhiều thế giới, retro game, vui tươi (r1s3, r2s3, r3s1, r3s2) | Kiểu cổ nhịp chậm màu tối (r4s5) |
| Video giải thích | 3,0 (7) | Chữ là nhân vật biến hình liên tục (r1s1); isometric có camera đi xuyên (r2s2); chuyển cảnh đẩy | Chữ kiểu slide (luật cứng), icon nét mảnh, liệt kê, nhân vật flat kiểu công ty |
| Giới thiệu sản phẩm | 3,0 (4) · mâu thuẫn | Hype film chữ serif khổng lồ + nét vẽ tay, UI chỉ chen vài khung (r3s6) | UI promo, điện thoại 3D (luật cứng), flat vector |
| Phim thương hiệu | 5,0 (1) | Chữ tràn khung đổi nhanh + nét vẽ tay (r3s6) | - |
| Trailer, montage | 5,0 (1) | Minh hoạ giấy ấm in lụa, nhạc dâng dần (r4s4) | - |
| Nội dung mạng xã hội | 5,0 (1) | 2D vẽ tay màu rực biến hình theo nhạc (r4s1) | - |
| Phim ngắn | 3,25 (4) | Vẽ tay bút chì (r1s5), 2D thông điệp (r2s5) | 3D hiện thực, rubber hose đen trắng |
| Ident, intro | 2,0 (1) | - | Stop-motion đất sét kết màn tối (r1s7) |
| Video nhạc | 2,0 (3) · Tránh | (Salsa r4s1 cho thấy nhạc dẫn hình vẫn được khi có nhân vật màu rực) | Trừu tượng tối, chữ trắng đen không hình |
| Showreel | 2,0 (2) · Tránh | - | Chuỗi cảnh rời không mạch kể |

Mục đích có ít bằng chứng (1 mẫu): gợi ý style theo gu chung (vẽ tay, collage, 2D nhân vật có cá tính, isometric).

## Nên
### Style
- **2D nhân vật có cá tính mạnh**, không phải nhân vật "an toàn": cel shading màu rực, tạo dáng phóng đại, thế giới riêng
  (game đua xe retro r3s1, cartoon ảo giác r3s2, giấy cắt r2s3). Ba mẫu này 4-5 điểm và bạn bấm + cho style. Nhân vật
  flat dáng dài kiểu SaaS (r3s4 style −) và minh hoạ công ty (r3s3) thì không. · animation, dùng được cho motion
- `hand_drawn` (4,6 trên 7 mẫu, tin cậy vừa): nét bút chì/bút sáp/nét vẽ tay tự vẽ ra; mảng phẳng không viền co giãn theo nhạc (r4s1 "Rất thích", style +). (r1s5, r2s4, r3s2, r3s6, r4s1)
- `collage` giấy cắt 2D và minh hoạ có texture in lụa, hoa văn dân gian (4,4 trên 4 mẫu, tin cậy vừa), không phải stop-motion đất sét. (r1s3, r2s3, r4s4 "Rất thích", style + hình +)
- `isometric` có camera luôn di chuyển (4,6). (r2s2)
- Kinetic type **chỉ khi** chữ to, đổi nhanh và có nét vẽ tay hoặc minh hoạ đi kèm (r3s6 "Rất thích", r1s1).
### Không khí
- **Năng động** (4,1 trên 4 mẫu, tin cậy vừa) và **vui tươi**: hào hứng, nghịch, có chút điên. (r3s1, r3s2, r3s6, r2s3)
### Hook
- **Chuyển động mạnh ngay khung 0** (4,0 trên 6 mẫu, tin cậy vừa): vật thể đã đang chuyển động hoặc đổi liên tục trong
  giây đầu - màn chọn tay đua đổi nhân vật mỗi ~0,5 s (r3s1), chữ serif khổng lồ đổi từ mỗi ~0,5 s (r3s6), lon bị xúc
  tu ôm (r3s2). Không mở bằng logo đứng yên hay màn đen. · cả hai
### Nhịp và cắt cảnh
- Theo yêu cầu trực tiếp: **1-2 s/cảnh**. Một cảnh được dài hơn (tới ~4 s) **nếu hình biến hình liên tục theo phách**, gần như không khung nào đứng yên: Salsa cắt ~3,7 s/cảnh, 7% khung đứng yên, bạn vẫn bấm + cho nhịp (r4s1). Thứ cần đếm là số lần đổi trạng thái lớn, không chỉ số cú cắt. Mẫu bạn thích nhất vòng 3 đo được ~2 s/cảnh, chỉ 9% khung đứng yên (r3s1).
  Giữa các cú cắt luôn có chuyển động dày. · cả hai
### Chuyển cảnh
- Bạn bấm + cho chuyển cảnh của r3s2 (biến hình, zoom xuyên vào vật), r3s4 (hình khối biến thành cảnh sau, UI trượt
  vào), r3s6 (cắt cứng, nét vẽ biến thành chữ). Ưu tiên **biến hình có chủ đích** (bấm + cho morph theo phách của r4s1) và **đẩy/trượt lớp** (`push` 4,0 trên
  7 mẫu); tránh hoà tan. · cả hai
### Chữ
- Chữ **to, có cá tính**: serif đậm tràn khung (`serif` 4,3 trên 3 mẫu, r3s6), chữ vẽ tay/cắt giấy đậm ở cảnh chốt
  (r2s3, r3s2). Chữ luôn đi cùng hình hoặc nét vẽ, không đứng một mình trên nền trống. · cả hai
### Chuyển động
- **Parallax nhiều lớp** (5,0), **lò xo nảy / squash & stretch** (4,2 trên 7 mẫu), **camera động** bám theo hành động
  (4,2 trên 7 mẫu). Bạn bấm + cho chuyển động của r3s1, r3s4, r3s6. (r1s3, r2s3, r3s1, r3s2)
### Màu
- Hai bảng bạn đều thích: (a) **rực, bão hoà cao**: tím than `#2B1B4E`, hồng `#E8508A`, cam `#F59A3C`, vàng `#FFE23A`,
  tím `#8A4FD6` (r3s1, r3s2); (b) **giấy ấm**: kem `#F7F0E3`, giấy be `#E9DCC0` với nhấn cam `#F26B4F`, xanh `#2D6CDF`
  (r1s1, r1s3, r2s3); thêm biến thể **giấy ấm in lụa**: giấy `#D9D8B7`, xanh lá `#467D57`, đỏ son `#A93146`, xanh rêu `#19372B` (r4s4 "Rất thích"). Bảng rực vòng 4: hồng `#FB8CA7`, đỏ `#E23225`, vàng `#FEE38B` trên đen `#101316` (r4s1 "Rất thích"). Nền đen được khi có một màu nhấn rực và năng lượng cao (lime `#9BE15D` trên đen, r3s6).
  Chưa đủ tin cậy để thành rule cứng; tránh đơn sắc đen trắng và màu nhạt nét mảnh.
### Bố cục
- Nhiều lớp tạo chiều sâu (4,45 trên 6 mẫu, tin cậy vừa), có thể tràn viền (4,2); bạn bấm + bố cục dày đặc của r3s2. · cả hai
### Kiểu hình
- Minh hoạ 2D có texture hoặc nét tay; cel shading phẳng có hạt nhẹ (r3s1). Bạn bấm + kiểu hình của r3s1, r1s5, r2s3. · cả hai
### Cấu trúc
- Mạch kể gọn trong **60-90 s**: hook → 2-4 đoạn → kết; nhân vật hoặc sản phẩm đi qua nhiều thế giới (r3s1, r3s2, r2s3).

## Tránh
- **Nhân vật 2D kiểu công ty an toàn**: flat vector dáng dài, minh hoạ "Corporate Memphis", nhiều khoảng trắng (r3s3
  "Không thích", r3s4 style − và kiểu hình −). · cả hai
- **UI sản phẩm / app promo** (`ui_promo` 1,0 và `ui_san_pham` 1,0 trên 2 mẫu). (r1s4, r3s4)
- **Trừu tượng** không có chủ thể (2,0 trên 2 mẫu). (r1s2, r3s7)
- **Liệt kê máy móc** từng màn/từng tính năng (2,0 trên 7 mẫu, tin cậy cao).
- **Chữ tĩnh trên nền trống**, font pixel, slide. (r2s1, r2s8)
- **Hoà tan / mờ dần**; khung đứng yên lâu; chữ nhỏ mảnh khó đọc.
- **Không khí tối, bí ẩn** (1,5 trên 2 mẫu).
- **Đen trắng đơn sắc** (đơn sắc 2,6 trên 5 mẫu).
- **3D**: chưa có nhu cầu; không dùng trừ khi bạn yêu cầu.

## Đang theo dõi
- `character_2d` nói chung 3,95 trên 9 mẫu (mâu thuẫn): điểm phụ thuộc kiểu nhân vật, xem rule Style.
- Retro: thích game 80s (r3s1), ghét rubber hose 1920s đen trắng (r3s5). Hoạt hình kiểu 1930 **có màu** (Vipps r4s5) chỉ "Bình thường": luật cứng nhắm vào đen trắng, không phải mọi hoạt hình cổ; nhưng kiểu cổ nhịp chậm, màu tối cũng không phải gu.
- Anime game màu xanh ngọc tím, khổ vuông, ~1,7 s/cảnh (Pokimane r4s3): "Thích".
- Flat vector 3,0 trên 6 mẫu: chỉ ổn khi có cá tính và nhịp nhanh.
- AGES (r3s7, hình học không nhân vật) "Bình thường".
- **Âm thanh** (vòng 4, chưa có điểm riêng cho âm thanh, chỉ suy từ điểm tổng): hai mẫu "Rất thích" đều **không dựa vào giọng đọc**: nhạc salsa dày tiếng nhấn dẫn cả phim (r4s1) và nhạc cinematic mở nhỏ rồi dâng lên, beat rõ (r4s4). Mẫu có giọng đọc + SFX dày, âm nén đều được "Thích" (r4s3). Tiếng lọc cổ kiểu đĩa than "Bình thường" (r4s5). Giả thuyết: nhạc có nhịp rõ dẫn dắt hình > giọng đọc. Cần bạn chấm riêng category Âm thanh để thành rule.
- **Phụ đề:** chưa có dữ liệu.

## Câu hỏi còn mở
3. Video của bạn có **giọng đọc** không, và có **phụ đề** không? Nếu có phụ đề, bạn thích kiểu nào (hiện từng từ, chữ to giữa khung, một dòng nhỏ)? Đây là yêu cầu trực tiếp, trả lời một lần là đủ.
4. The Bystanders (r4s2) chưa được chấm: bỏ qua cố ý hay quên?
1. Dancing on Osees (r2s4): bạn chấm + cho style, màu và nhịp nhưng tổng chỉ "Bình thường". Điều gì kéo nó xuống?
2. Pipedrive (r3s4) "Thích" nhưng bạn bấm − cho style và kiểu hình. Bạn thích riêng chuyển cảnh và chuyển động của nó
   (hình khối biến thành cảnh, UI trượt vào), đúng không?

## Lịch sử thay đổi
| Vòng | Thay đổi |
|---|---|
| AB1 | (2026-11-23) Thử nghiệm A/B mù đầu tiên: bản theo gu 2, bản mặc định 4. Thêm mục "Bài học từ video Claude làm" (trọng số cao): hoàn thiện trước style, không giả vẽ tay bằng code, giải thích rõ, camera bám vật + match cut. Rule vẽ tay/collage chỉ áp khi có tài sản hình. |
| 4 | Thêm category `muc_dich` (10 mục đích) và `references/purposes.md`; gắn mục đích cho cả 29 mẫu; thêm mục "Theo mục đích". Quảng cáo là mục đích được thích nhất (4,3, tin cậy cao). Theo ý bạn (vòng 4): mục đích chỉ để gợi ý style, không bắt buộc. |
| 4 | 28 mẫu (r4s2 chưa chấm). Mở rộng Nên: collage gồm cả minh hoạ in lụa giấy ấm (r4s4), hand_drawn mảng phẳng theo nhạc (r4s1). Rule nhịp thêm ngoại lệ: cảnh dài tới ~4 s được nếu hình biến liên tục theo phách. Làm rõ luật cứng rubber hose: chỉ đen trắng (r4s5 có màu "Bình thường"). Âm thanh vẫn Đang theo dõi vì chưa có điểm category. |
| 1 | Bộ rule đầu tiên từ 8 mẫu; 2 luật cứng; 3D đánh dấu "chưa có nhu cầu". |
| 1 | Mẫu tham khảo từ vòng 2 chỉ lấy video dài dưới 1,5 phút (≤ 90 s). |
| 3 | 24 mẫu, nhất quán 1/1. Thêm luật cứng rubber hose đen trắng. Style mặc định thu hẹp từ "2D có nhân vật" thành "2D nhân vật có cá tính, màu rực, năng động"; thêm Tránh: nhân vật kiểu công ty, UI sản phẩm, trừu tượng, đen trắng. Rule mới: hook chuyển động mạnh ngay khung 0, không khí năng động, kinetic type được khi chữ to + nét vẽ tay. Nới rule nền tối. Câu hỏi A-Trak gỡ: chữ thuần trắng đen thì không, chữ to có nét vẽ và màu nhấn thì có. |
| 2 | 16 mẫu. Thêm luật cứng về explainer chỉ có chữ. Style mặc định chuyển sang 2D có nhân vật (tin cậy cao). Gỡ 2 câu hỏi: collage giấy thì thích, stop-motion đất sét thì không; isometric có camera động thì thích. Thêm Tránh: video chỉ có chữ, icon nét mảnh màu nhạt. Nới rule nền tối. |
| 1 | Thêm yêu cầu trực tiếp: video 60-90 s, nhịp 1-2 s/cảnh. Sửa rule nhịp (trước: 3-4 s) và rule cấu trúc. Sửa nhãn nhịp r1s1, r1s3 từ `vua` thành `cham` cho đúng định nghĩa (>2 s). |

<!-- AUTO:EVIDENCE START - phần dưới đây do scripts/taste.py audit viết lại, đừng sửa tay -->
## Bảng bằng chứng
Cập nhật 2026-11-22 · 4 vòng · 28 mẫu đã chấm. Điểm = trung bình có trọng số (điểm riêng của category x1.0, điểm tổng của mẫu x0.6).

| Category | Tag | Điểm | Lệch | Số mẫu | Trạng thái | Tin cậy | Phạm vi | Mẫu |
|---|---|---|---|---|---|---|---|---|
| Style | `isometric` | 4.62 | 0.48 | 2 | Nên | vừa | cả hai | r1s8, r2s2 |
| Style | `hand_drawn` | 4.61 | 1.18 | 7 | Nên | vừa | cả hai | r1s5, r2s4, r3s2, r3s5, r3s6, r4s1, r4s4 |
| Style | `collage` | 4.44 | 1.17 | 4 | Nên | vừa | cả hai | r1s3, r1s7, r2s3, r4s4 |
| Style | `character_2d` | 4.00 | 1.55 | 12 | Mâu thuẫn | thấp | cả hai | r1s5, r2s3, r2s4, r2s5, r3s1, r3s2, r3s3, r3s4, r3s5, r4s1, r4s3, r4s5 |
| Style | `infographic` | 3.88 | 1.45 | 2 | Đang theo dõi | thấp | cả hai | r1s8, r2s7 |
| Style | `retro` | 3.50 | 1.50 | 4 | Mâu thuẫn | thấp | animation | r3s1, r3s5, r4s3, r4s5 |
| Style | `kinetic_type` | 3.24 | 1.70 | 5 | Mâu thuẫn | thấp | motion | r1s1, r2s1, r2s6, r2s8, r3s6 |
| Style | `cg_realistic` | 3.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s6 |
| Style | `flat_vector` | 3.00 | 1.62 | 6 | Mâu thuẫn | thấp | cả hai | r1s1, r2s5, r2s7, r3s3, r3s4, r3s7 |
| Style | `abstract` | 2.00 | 1.00 | 2 | Tránh | vừa | motion | r1s2, r3s7 |
| Style | `brutalist` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s6 |
| Style | `pixel_art` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s8 |
| Style | `stop_motion` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s7 |
| Style | `product_3d` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s4 |
| Style | `swiss_minimal` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s1 |
| Style | `ui_promo` | 1.00 | 0.00 | 2 | Tránh | vừa | motion | r1s4, r3s4 |
| Không khí | `nang_dong` | 4.32 | 1.02 | 6 | Nên | vừa | cả hai | r2s6, r3s1, r3s2, r3s6, r4s1, r4s3 |
| Không khí | `dien_anh` | 4.00 | 0.82 | 3 | Nên | vừa | animation | r1s6, r2s5, r4s4 |
| Không khí | `vui_tuoi` | 3.95 | 1.31 | 11 | Đang theo dõi | thấp | cả hai | r1s1, r1s3, r2s3, r2s4, r3s1, r3s2, r3s3, r3s5, r4s1, r4s3, r4s5 |
| Không khí | `nghe_thuat` | 3.76 | 1.21 | 5 | Đang theo dõi | thấp | cả hai | r1s5, r1s7, r2s4, r3s6, r3s7 |
| Không khí | `hoai_co` | 3.71 | 1.62 | 4 | Mâu thuẫn | thấp | cả hai | r1s3, r2s3, r3s5, r4s5 |
| Không khí | `thu_cong` | 3.33 | 1.25 | 3 | Đang theo dõi | thấp | animation | r1s7, r2s4, r4s4 |
| Không khí | `tram_lang` | 3.25 | 1.48 | 4 | Đang theo dõi | thấp | cả hai | r1s2, r1s5, r2s5, r3s7 |
| Không khí | `cong_nghe` | 3.09 | 1.78 | 3 | Mâu thuẫn | thấp | motion | r1s4, r2s2, r2s8 |
| Không khí | `ky_ao` | 3.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s6 |
| Không khí | `sach_gon` | 2.92 | 1.62 | 8 | Mâu thuẫn | thấp | cả hai | r1s1, r1s4, r1s8, r2s1, r2s2, r2s7, r3s3, r3s4 |
| Không khí | `toi_bi_an` | 1.50 | 0.50 | 2 | Tránh | vừa | motion | r1s2, r2s8 |
| Mục đích | `noi_dung_mxh` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r4s1 |
| Mục đích | `phim_thuong_hieu` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r3s6 |
| Mục đích | `trailer` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r4s4 |
| Mục đích | `quang_cao` | 4.33 | 0.75 | 6 | Nên | cao | cả hai | r1s3, r2s3, r3s1, r3s2, r4s3, r4s5 |
| Mục đích | `phim_ngan` | 3.25 | 1.48 | 4 | Đang theo dõi | thấp | animation | r1s5, r1s6, r2s5, r3s5 |
| Mục đích | `giai_thich` | 3.00 | 1.31 | 7 | Đang theo dõi | thấp | cả hai | r1s1, r1s8, r2s1, r2s2, r2s7, r3s4, r3s7 |
| Mục đích | `gioi_thieu_san_pham` | 3.00 | 1.58 | 4 | Mâu thuẫn | thấp | motion | r1s4, r2s7, r3s4, r3s6 |
| Mục đích | `ident_intro` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s7 |
| Mục đích | `showreel` | 2.00 | 0.00 | 2 | Tránh | vừa | cả hai | r2s8, r3s3 |
| Mục đích | `video_nhac` | 2.00 | 0.82 | 3 | Tránh | vừa | cả hai | r1s2, r2s4, r2s6 |
| Hook | `chuyen_dong_manh` | 4.22 | 1.10 | 7 | Nên | vừa | cả hai | r1s1, r2s4, r2s6, r3s1, r3s2, r3s6, r4s1 |
| Hook | `tinh_roi_bung` | 3.43 | 1.40 | 7 | Đang theo dõi | thấp | cả hai | r1s2, r1s3, r1s5, r2s5, r2s8, r3s4, r3s7 |
| Hook | `hinh_gay_soc` | 3.33 | 1.11 | 6 | Đang theo dõi | vừa | cả hai | r1s6, r1s7, r2s2, r2s3, r2s7, r3s2 |
| Hook | `chu_to` | 3.17 | 1.62 | 12 | Mâu thuẫn | thấp | cả hai | r1s1, r1s4, r2s1, r2s6, r3s1, r3s3, r3s4, r3s5, r3s6, r4s3, r4s4, r4s5 |
| Hook | `ket_qua_truoc` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s8 |
| Nhịp và cắt cảnh | `co_khoang_lang` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s5 |
| Nhịp và cắt cảnh | `vua` | 4.77 | 0.42 | 3 | Nên | vừa | animation | r2s3, r3s2, r4s1 |
| Nhịp và cắt cảnh | `nhanh` | 4.40 | 1.07 | 6 | Nên | vừa | cả hai | r2s4, r2s6, r3s1, r3s6, r4s3, r4s4 |
| Nhịp và cắt cảnh | `tang_dan` | 4.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r3s2 |
| Nhịp và cắt cảnh | `khop_beat` | 3.88 | 1.45 | 2 | Đang theo dõi | thấp | cả hai | r2s6, r4s1 |
| Nhịp và cắt cảnh | `cham` | 2.79 | 1.55 | 18 | Mâu thuẫn | thấp | cả hai | r1s1, r1s2, r1s3, r1s4, r1s5, r1s6, r1s7, r1s8, r2s1, r2s2, r2s5, r2s7, r2s8, r3s3, r3s4, r3s5, r3s7, r4s5 |
| Chuyển cảnh | `whip_pan` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r3s1 |
| Chuyển cảnh | `push` | 4.04 | 1.48 | 7 | Nên | thấp | cả hai | r1s1, r1s3, r1s4, r2s2, r2s3, r3s3, r3s4 |
| Chuyển cảnh | `mask_reveal` | 4.00 | 1.41 | 3 | Nên | thấp | cả hai | r1s3, r1s7, r4s4 |
| Chuyển cảnh | `morph` | 3.72 | 1.54 | 12 | Mâu thuẫn | thấp | cả hai | r1s1, r1s5, r1s7, r1s8, r2s4, r2s6, r2s7, r3s2, r3s4, r3s6, r3s7, r4s1 |
| Chuyển cảnh | `zoom_xuyen` | 3.71 | 1.48 | 4 | Đang theo dõi | thấp | cả hai | r1s4, r2s2, r3s2, r4s3 |
| Chuyển cảnh | `cat_thang` | 3.47 | 1.46 | 15 | Đang theo dõi | thấp | cả hai | r1s5, r1s6, r2s1, r2s3, r2s5, r2s6, r2s8, r3s1, r3s3, r3s5, r3s6, r3s7, r4s3, r4s4, r4s5 |
| Chuyển cảnh | `glitch` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s8 |
| Chuyển cảnh | `hoa_tan` | 1.67 | 0.94 | 3 | Tránh | vừa | cả hai | r1s2, r1s6, r2s1 |
| Chữ | `serif` | 4.20 | 0.98 | 5 | Nên | cao | cả hai | r1s1, r1s6, r3s6, r4s4, r4s5 |
| Chữ | `viet_tay` | 3.83 | 1.46 | 6 | Đang theo dõi | thấp | cả hai | r1s5, r2s3, r2s4, r3s2, r3s5, r3s6 |
| Chữ | `chu_to_full` | 3.67 | 1.49 | 9 | Đang theo dõi | thấp | cả hai | r1s1, r2s3, r2s6, r2s8, r3s1, r3s2, r3s5, r3s6, r4s3 |
| Chữ | `sans_grotesk` | 2.80 | 1.47 | 5 | Đang theo dõi | thấp | cả hai | r1s1, r2s1, r2s5, r2s6, r3s3 |
| Chữ | `sans_hinh_hoc` | 2.75 | 1.30 | 4 | Đang theo dõi | thấp | motion | r1s4, r2s2, r2s7, r3s4 |
| Chữ | `condensed` | 2.59 | 1.82 | 5 | Mâu thuẫn | thấp | cả hai | r1s2, r1s3, r1s8, r2s6, r3s1 |
| Chữ | `chu_nho_tinh` | 2.24 | 1.35 | 5 | Đang theo dõi | thấp | cả hai | r1s2, r1s8, r2s2, r2s5, r2s7 |
| Chữ | `kinetic_tung_tu` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s6 |
| Chữ | `mono` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s8 |
| Chuyển động | `parallax` | 5.00 | 0.00 | 3 | Nên | vừa | cả hai | r1s3, r2s3, r4s4 |
| Chuyển động | `camera_dong` | 4.31 | 1.19 | 9 | Nên | vừa | cả hai | r1s3, r1s4, r1s6, r2s2, r2s5, r3s1, r3s6, r4s1, r4s3 |
| Chuyển động | `lo_xo_nay` | 4.21 | 1.20 | 10 | Nên | vừa | cả hai | r1s1, r2s3, r2s4, r3s1, r3s2, r3s4, r3s5, r4s1, r4s3, r4s5 |
| Chuyển động | `motion_blur` | 3.50 | 1.94 | 2 | Mâu thuẫn | thấp | cả hai | r1s2, r3s1 |
| Chuyển động | `ease_muot` | 3.35 | 1.54 | 12 | Mâu thuẫn | thấp | cả hai | r1s1, r1s3, r1s4, r1s6, r1s8, r2s1, r2s2, r2s5, r2s7, r3s3, r3s4, r3s7 |
| Chuyển động | `giat_nhanh` | 3.20 | 1.25 | 6 | Đang theo dõi | thấp | cả hai | r1s7, r2s4, r2s6, r2s8, r3s2, r3s6 |
| Chuyển động | `cham_chill` | 3.00 | 1.41 | 4 | Đang theo dõi | thấp | cả hai | r1s2, r1s5, r1s6, r3s7 |
| Chuyển động | `tinh` | 2.50 | 1.50 | 4 | Mâu thuẫn | thấp | cả hai | r1s5, r1s7, r1s8, r2s1 |
| Màu | `am` | 4.16 | 1.20 | 10 | Nên | thấp | cả hai | r1s3, r1s6, r1s7, r2s3, r2s4, r3s1, r3s2, r3s3, r4s1, r4s4 |
| Màu | `tuong_phan_cao` | 4.06 | 1.17 | 10 | Nên | vừa | cả hai | r1s1, r2s4, r2s6, r2s8, r3s1, r3s2, r3s6, r3s7, r4s1, r4s3 |
| Màu | `pastel` | 3.50 | 1.50 | 4 | Mâu thuẫn | thấp | cả hai | r1s5, r1s7, r2s3, r2s7 |
| Màu | `film_grade` | 3.40 | 1.50 | 5 | Đang theo dõi | thấp | cả hai | r1s3, r1s6, r2s3, r3s5, r4s5 |
| Màu | `nen_sang` | 3.22 | 1.60 | 10 | Mâu thuẫn | thấp | cả hai | r1s1, r1s4, r1s8, r2s1, r2s4, r2s7, r3s2, r3s3, r3s4, r4s4 |
| Màu | `lanh` | 3.00 | 1.53 | 6 | Mâu thuẫn | thấp | cả hai | r1s2, r1s4, r1s5, r2s2, r2s5, r3s7 |
| Màu | `nen_toi` | 3.00 | 1.41 | 6 | Đang theo dõi | thấp | cả hai | r1s2, r2s2, r2s5, r2s6, r2s8, r3s6 |
| Màu | `toi` | 3.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r4s5 |
| Màu | `trung_tinh` | 2.71 | 1.48 | 7 | Đang theo dõi | thấp | cả hai | r1s3, r1s7, r1s8, r2s1, r2s5, r3s4, r3s5 |
| Màu | `don_sac` | 2.60 | 1.62 | 5 | Mâu thuẫn | thấp | cả hai | r1s2, r1s5, r2s2, r2s6, r3s5 |
| Bố cục | `nhieu_lop` | 4.57 | 0.94 | 8 | Nên | cao | cả hai | r1s1, r1s3, r1s8, r2s2, r2s3, r3s2, r4s1, r4s4 |
| Bố cục | `full_bleed` | 4.47 | 1.14 | 5 | Nên | vừa | cả hai | r2s6, r3s1, r3s2, r4s1, r4s4 |
| Bố cục | `bat_doi_xung` | 3.40 | 1.62 | 5 | Mâu thuẫn | thấp | cả hai | r1s2, r1s5, r1s7, r2s5, r3s1 |
| Bố cục | `ngang_16_9` | 3.33 | 1.49 | 22 | Đang theo dõi | thấp | cả hai | r1s1, r1s2, r1s3, r1s4, r1s5, r1s6, r1s7, r1s8, r2s1, r2s2, r2s3, r2s4, r2s5, r2s6, r2s7, r2s8, r3s1, r3s2, r3s3, r3s4, r3s6, r3s7 |
| Bố cục | `luoi_swiss` | 3.20 | 1.17 | 5 | Đang theo dõi | vừa | cả hai | r1s1, r1s8, r2s2, r2s8, r3s7 |
| Bố cục | `chinh_giua` | 2.95 | 1.45 | 14 | Đang theo dõi | thấp | cả hai | r1s3, r1s4, r1s6, r2s1, r2s3, r2s4, r2s6, r2s7, r3s3, r3s5, r3s6, r3s7, r4s3, r4s5 |
| Bố cục | `nhieu_khoang_trong` | 2.57 | 1.40 | 7 | Đang theo dõi | thấp | cả hai | r1s2, r1s5, r2s1, r2s4, r2s7, r3s3, r3s4 |
| Bố cục | `vuong` | 2.50 | 1.50 | 2 | Mâu thuẫn | thấp | animation | r3s5, r4s3 |
| Kiểu hình | `minh_hoa` | 4.17 | 1.26 | 14 | Nên | thấp | cả hai | r1s5, r1s8, r2s2, r2s3, r2s4, r2s5, r3s1, r3s2, r3s3, r3s5, r3s6, r4s1, r4s3, r4s4 |
| Kiểu hình | `collage` | 4.12 | 1.23 | 5 | Nên | thấp | cả hai | r1s1, r1s3, r1s7, r2s3, r2s4 |
| Kiểu hình | `2d_phang` | 3.73 | 1.45 | 13 | Đang theo dõi | thấp | cả hai | r1s1, r1s5, r1s8, r2s2, r2s5, r2s7, r3s1, r3s2, r3s3, r3s4, r3s7, r4s1, r4s3 |
| Kiểu hình | `texture_hat` | 3.66 | 1.57 | 13 | Mâu thuẫn | thấp | cả hai | r1s1, r1s2, r1s3, r1s5, r1s7, r2s3, r2s4, r2s8, r3s1, r3s3, r3s5, r4s4, r4s5 |
| Kiểu hình | `typography_only` | 2.50 | 1.50 | 4 | Mâu thuẫn | thấp | motion | r2s1, r2s6, r2s8, r3s6 |
| Kiểu hình | `3d_render` | 2.00 | 1.00 | 2 | Tránh | vừa | cả hai | r1s4, r1s6 |
| Kiểu hình | `footage_that` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s2 |
| Kiểu hình | `ui_san_pham` | 1.00 | 0.00 | 2 | Tránh | vừa | motion | r1s4, r3s4 |
| Âm thanh | `nhac_cinematic` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r4s4 |
| Âm thanh | `nhac_nhay` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r4s1 |
| Âm thanh | `sfx_it` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r4s1 |
| Âm thanh | `voice_over` | 4.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r4s3 |
| Âm thanh | `sfx_day` | 3.50 | 0.50 | 2 | Đang theo dõi | vừa | animation | r4s3, r4s5 |
| Âm thanh | `am_thanh_co` | 3.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r4s5 |
| Phụ đề | `khong_co` | 3.35 | 1.41 | 26 | Đang theo dõi | thấp | cả hai | r1s1, r1s3, r1s4, r1s5, r1s6, r1s7, r1s8, r2s1, r2s2, r2s3, r2s4, r2s5, r2s6, r2s7, r2s8, r3s1, r3s2, r3s3, r3s4, r3s5, r3s6, r3s7, r4s1, r4s3, r4s4, r4s5 |
| Phụ đề | `gian_don` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s2 |
| Cấu trúc | `tren_60s` | 4.60 | 0.80 | 5 | Nên | cao | cả hai | r1s1, r1s3, r1s5, r1s6, r4s4 |
| Cấu trúc | `ke_chuyen` | 4.07 | 1.12 | 15 | Nên | vừa | cả hai | r1s1, r1s3, r1s5, r1s6, r2s2, r2s3, r2s5, r3s1, r3s2, r3s5, r3s7, r4s1, r4s3, r4s4, r4s5 |
| Cấu trúc | `15_30s` | 3.60 | 1.36 | 5 | Đang theo dõi | thấp | cả hai | r1s8, r2s3, r2s6, r3s1, r3s2 |
| Cấu trúc | `cta_ro` | 3.45 | 1.44 | 11 | Đang theo dõi | thấp | cả hai | r1s4, r2s1, r2s2, r2s3, r2s7, r3s1, r3s2, r3s4, r3s6, r4s3, r4s5 |
| Cấu trúc | `30_60s` | 2.76 | 1.35 | 17 | Đang theo dõi | thấp | cả hai | r1s2, r1s4, r1s7, r2s1, r2s2, r2s4, r2s5, r2s7, r2s8, r3s3, r3s4, r3s5, r3s6, r3s7, r4s1, r4s3, r4s5 |
| Cấu trúc | `loop` | 2.33 | 0.47 | 3 | Đang theo dõi | vừa | cả hai | r1s8, r2s4, r2s6 |
| Cấu trúc | `liet_ke` | 2.00 | 0.93 | 7 | Tránh | cao | cả hai | r1s4, r1s8, r2s1, r2s7, r2s8, r3s3, r3s4 |

Kiểm tra nhất quán: r3s8 (chiếu lại r2s5): 4 rồi 3
<!-- AUTO:EVIDENCE END -->
