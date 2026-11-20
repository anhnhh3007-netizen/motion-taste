# 13 category và bộ tag chuẩn

Mỗi mẫu được tách theo các category dưới đây. Mỗi category chọn **1-3 tag** mô tả rõ nhất mẫu, cộng một
`note` bằng giá trị cụ thể. Tag là thứ script cộng điểm; note là thứ biến điểm thành rule dựng được. Thiếu note thì
rule viết ra sẽ chung chung, nên note càng cụ thể càng tốt: giây, số shot, hex, nhóm font, kiểu easing, vị trí trên khung.

Id category (dùng trong JSON) đứng trước dấu `-`. Hai category đầu (`style`, `khong_khi`) phân loại cả mẫu; 11 category
còn lại tách ngữ pháp của nó. Kỹ thuật làm hình (2D, 3D, đất sét…) nằm ở category `hinh`.

## style - Style (phong cách tổng thể)
Mẫu thuộc họ phong cách nào. Chọn 1 tag chính, thêm 1 tag phụ nếu mẫu lai. Định nghĩa đầy đủ, ngữ pháp và cách dựng
của từng style ở `references/styles.md`; tag ở đây phải trùng id trong file đó.
| Tag | Nghĩa |
|---|---|
| `kinetic_type` | Kinetic typography: chữ là nhân vật chính |
| `swiss_minimal` | Swiss / tối giản theo lưới, ít màu, chữ grotesk |
| `flat_vector` | 2D vector phẳng, explainer, đồ hoạ thương hiệu |
| `character_2d` | 2D nhân vật cartoon (vector hoặc rubber hose) |
| `hand_drawn` | 2D vẽ tay, frame-by-frame, nét bút |
| `collage` | Collage / mixed media, cắt dán ảnh và giấy |
| `stop_motion` | Stop-motion: đất sét, giấy, vật thật chụp từng khung |
| `cg_realistic` | 3D CG hướng hiện thực, điện ảnh |
| `cg_stylized` | 3D cách điệu: đồ chơi, đất nặn render, low-poly |
| `product_3d` | 3D sản phẩm bóng bẩy, studio light |
| `ui_promo` | UI / app promo, màn hình sản phẩm chuyển động |
| `isometric` | Isometric: thế giới thu nhỏ góc 30° |
| `infographic` | Infographic / data viz động |
| `abstract` | Trừu tượng: liquid, generative, hình khối, ánh sáng |
| `glitch_grunge` | Glitch, grunge, texture nặng, nhiễu số |
| `retro` | Retro / Y2K / VHS / phim cũ |
| `pixel_art` | Pixel art |
| `brutalist` | Brutalist: khối thô, chữ cực to, màu gắt |
Note: vì sao xếp vào style này (2-3 dấu hiệu nhìn thấy được).

## khong_khi - Không khí (mood)
Cảm giác mẫu để lại. Chọn 1-2 tag.
| Tag | Nghĩa |
|---|---|
| `vui_tuoi` | Vui, tươi, hài hước |
| `nang_dong` | Năng động, mạnh, nhanh |
| `tram_lang` | Trầm, lặng, chiêm nghiệm |
| `dien_anh` | Điện ảnh, hoành tráng |
| `sang_trong` | Sang trọng, cao cấp |
| `hoai_co` | Hoài cổ, vintage |
| `ky_ao` | Kỳ ảo, mơ màng |
| `cong_nghe` | Công nghệ, tương lai |
| `thu_cong` | Thủ công, mộc, thấy bàn tay người làm |
| `toi_bi_an` | Tối, bí ẩn, căng |
| `sach_gon` | Sạch, gọn, chuyên nghiệp |
| `nghe_thuat` | Nghệ thuật, thể nghiệm |
Note: một câu về cảm giác, dựa vào đâu.

## hook - Hook (2-3 giây đầu)
Điều gì giữ người xem ở lại.
| Tag | Nghĩa |
|---|---|
| `chu_to` | Một dòng chữ lớn chiếm khung ngay từ đầu |
| `hinh_gay_soc` | Hình lạ, đẹp hoặc bất ngờ trước khi có chữ |
| `cau_hoi` | Mở bằng câu hỏi hoặc vấn đề |
| `ket_qua_truoc` | Cho thấy kết quả cuối ngay từ đầu |
| `chuyen_dong_manh` | Chuyển động hoặc cú cắt mạnh ở khung đầu |
| `tinh_roi_bung` | Tĩnh hoặc chậm một nhịp rồi bùng lên |
| `nguoi_noi` | Một người nói thẳng vào camera |
Note: hook xảy ra ở giây nào, khung đầu tiên có gì.

## nhip - Nhịp và cắt cảnh
| Tag | Nghĩa |
|---|---|
| `rat_nhanh` | Shot trung bình dưới 0,5 s |
| `nhanh` | 0,5-1 s |
| `vua` | 1-2 s |
| `cham` | Trên 2 s |
| `tang_dan` | Cắt nhanh dần về cuối hoặc tới cao trào |
| `co_khoang_lang` | Có chỗ dừng hoặc giữ hình để thở |
| `khop_beat` | Cú cắt rơi đúng phách nhạc |
Note: số shot / thời lượng, độ dài shot ngắn nhất và dài nhất, chỗ đổi nhịp.

## chuyen_canh - Chuyển cảnh
| Tag | Nghĩa |
|---|---|
| `cat_thang` | Cắt cứng |
| `match_cut` | Nối theo hình dáng, màu hoặc chuyển động |
| `whip_pan` | Lia nhanh có nhoè |
| `zoom_xuyen` | Zoom xuyên vào vật thể sang cảnh mới |
| `mask_reveal` | Lộ cảnh qua mặt nạ (hình khối, chữ) |
| `morph` | Biến hình liền mạch |
| `wipe` | Gạt ngang hoặc dọc |
| `push` | Đẩy cảnh cũ ra khỏi khung |
| `glitch` | Nhiễu số, RGB lệch |
| `hoa_tan` | Hoà tan, mờ dần |
Note: kiểu nào chiếm đa số, có tiếng nhấn đi kèm không.

## chu - Chữ (typography)
| Tag | Nghĩa |
|---|---|
| `sans_hinh_hoc` | Sans hình học (Futura, Poppins…) |
| `sans_grotesk` | Grotesk hoặc neo-grotesk (Helvetica, Inter, Neue Haas…) |
| `serif` | Có chân |
| `condensed` | Hẹp, cao |
| `mono` | Đơn cách |
| `viet_tay` | Viết tay, script |
| `chu_to_full` | Chữ to chiếm gần cả khung |
| `chu_nho_tinh` | Chữ nhỏ, tinh tế, nhiều khoảng trống |
| `kinetic_tung_tu` | Chữ vào từng từ hoặc từng ký tự theo nhịp |
| `go_chu` | Kiểu gõ chữ |
| `chu_3d` | Chữ có chiều sâu hoặc đặt trong không gian 3D |
Note: độ đậm, hoa hay thường, giãn chữ, cỡ so với chiều cao khung, cách chữ vào và ra.

## chuyen_dong - Chuyển động
Cảm giác của mọi thứ khi di chuyển.
| Tag | Nghĩa |
|---|---|
| `lo_xo_nay` | Lò xo có nảy, vượt đích rồi về |
| `ease_muot` | Ease vào ra mượt, không nảy |
| `giat_nhanh` | Nhanh, gắt, gần như tức thì |
| `cham_chill` | Chậm, trôi |
| `parallax` | Nhiều lớp chạy khác tốc độ |
| `camera_dong` | Camera đẩy, xoay quanh, lia liên tục |
| `tinh` | Gần như đứng yên |
| `motion_blur` | Có nhoè chuyển động |
Note: easing ước lượng, tốc độ, so le giữa các phần tử (ms).

## mau - Màu
| Tag | Nghĩa |
|---|---|
| `tuong_phan_cao` | Đen trắng hoặc tương phản gắt |
| `don_sac` | Một màu chủ đạo cộng sắc độ của nó |
| `pastel` | Pastel, nhạt |
| `neon` | Neon, rực trên nền tối |
| `trung_tinh` | Be, xám, đất |
| `am` | Tông ấm |
| `lanh` | Tông lạnh |
| `nen_toi` | Nền tối chủ đạo |
| `nen_sang` | Nền sáng chủ đạo |
| `film_grade` | Grade kiểu phim (hạt, highlight cam, shadow xanh…) |
Note: 2-4 mã hex chính kèm vai trò (nền, chữ, nhấn), số màu nhấn.

## bo_cuc - Bố cục khung
| Tag | Nghĩa |
|---|---|
| `doc_9_16` | Dọc 9:16 |
| `ngang_16_9` | Ngang 16:9 |
| `vuong` | 1:1 hoặc 4:5 |
| `chinh_giua` | Mọi thứ đặt chính giữa |
| `luoi_swiss` | Lưới chặt, căn lề trái kiểu Swiss |
| `bat_doi_xung` | Bất đối xứng, lệch có chủ đích |
| `full_bleed` | Hình tràn viền |
| `nhieu_lop` | Nhiều lớp chồng nhau, khung dày |
| `nhieu_khoang_trong` | Nhiều khoảng trống |
Note: chủ thể ở đâu, vùng an toàn cho chữ, mật độ phần tử.

## hinh - Kiểu hình
| Tag | Nghĩa |
|---|---|
| `2d_phang` | Vector 2D phẳng |
| `3d_render` | Render 3D |
| `footage_that` | Cảnh quay thật |
| `collage` | Cắt dán, mixed media |
| `minh_hoa` | Minh hoạ vẽ tay |
| `ui_san_pham` | Giao diện app hoặc web, màn hình sản phẩm |
| `typography_only` | Chỉ có chữ và hình khối |
| `texture_hat` | Hạt, nhiễu, giấy, halftone rõ rệt |
| `ugc_dien_thoai` | Quay điện thoại kiểu người thật, không dàn dựng |
Note: chất liệu, độ chi tiết, ánh sáng.

## am_thanh - Âm thanh
Chỉ điền khi đã nghe được. Xem không có tiếng thì bỏ trống.
| Tag | Nghĩa |
|---|---|
| `nhac_dien_tu` | Electronic, beat rõ |
| `nhac_lofi` | Lofi, chill |
| `nhac_cinematic` | Cinematic, dàn nhạc, build-up |
| `nhac_trend` | Âm thanh trend mạng xã hội |
| `sfx_day` | Nhiều tiếng hiệu ứng khớp hình |
| `sfx_it` | Ít hoặc không có SFX |
| `voice_over` | Có giọng đọc |
| `am_thanh_goc` | Tiếng gốc của cảnh quay |
Note: tempo ước lượng, chỗ nhạc đổi, tiếng nhấn ở đâu.

## phu_de - Phụ đề
| Tag | Nghĩa |
|---|---|
| `khong_co` | Không có phụ đề |
| `gian_don` | Một dòng nhỏ, đơn giản |
| `highlight_tu` | Tô màu từ đang nói |
| `karaoke_tung_tu` | Hiện từng từ theo lời |
| `phu_de_lon_giua` | Phụ đề to giữa khung |
| `emoji` | Có emoji hoặc sticker |
Note: font, vị trí, số từ mỗi dòng.

## cau_truc - Cấu trúc
| Tag | Nghĩa |
|---|---|
| `duoi_15s` | Dưới 15 s |
| `15_30s` | 15-30 s |
| `30_60s` | 30-60 s |
| `tren_60s` | Trên 60 s |
| `ke_chuyen` | Có mở, thân, kết như một câu chuyện |
| `liet_ke` | Liệt kê các ý hoặc mẹo |
| `truoc_sau` | So sánh trước và sau |
| `loop` | Cuối nối liền về đầu |
| `cta_ro` | Kết bằng lời kêu gọi rõ ràng |
Note: các đoạn và mốc thời gian, cách kết.

## Khi không có tag phù hợp
Thêm tag mới (viết thường, không dấu, nối bằng `_`, ví dụ `chu_outline`) và giải thích nó trong note. Audit liệt kê
mọi tag ngoài bộ chuẩn; khi một tag mới xuất hiện ở từ 2 mẫu trở lên, thêm nó vào bảng tương ứng trong file này.
