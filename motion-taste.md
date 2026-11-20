# Motion taste: gu video của tôi

Bộ rule rút từ các vòng chấm mẫu (skill `motion-taste`). Mỗi rule ghi phạm vi áp dụng: `motion` (motion graphics dựng
bằng code), `animation` (phim hoạt hình) hoặc `cả hai`, kèm độ tin cậy và mẫu dẫn chứng.

Trạng thái: **2 vòng · 16 mẫu đã chấm (2026-11-20).** Tạm dừng sau vòng 2; học tiếp bất cứ lúc nào bằng "vòng mẫu tiếp theo".

## Tóm tắt gu
Sau 2 vòng (16 mẫu), tín hiệu mạnh nhất là **hình minh hoạ 2D có nhân vật**: cả 4 mẫu có nhân vật 2D đều được 5 điểm
cho style (r1s5, r2s3, r2s4, r2s5). Bạn thích thế giới **vẽ tay hoặc giấy cắt có vân**, không khí **vui tươi, hơi hoài
cổ**, vật thể **nảy và chạy parallax**, câu chuyện có mạch. Ngược lại, bạn không thích video **chỉ có chữ** (kinetic
type thuần chữ, explainer slide, font pixel), explainer **liệt kê tính năng**, và không khí tối bí ẩn. 3D chưa phải nhu
cầu.

## Yêu cầu trực tiếp
Điều bạn nói thẳng (không phải suy từ điểm chấm). Ưu tiên ngay sau luật cứng, đè lên rule rút từ điểm.
- **Độ dài video: 60-90 s** (khoảng 1 phút đến 1 phút 30). Cấu trúc, số cảnh và hook phải tính cho độ dài này.
  (vòng 1, trả lời câu hỏi audit)
- **Nhịp nhanh hơn 3-4 s/cảnh:** mục tiêu khoảng **1-2 s/cảnh**, với 60-90 s là khoảng 35-60 cú cắt hoặc đổi trạng
  thái lớn. (vòng 1, trả lời câu hỏi audit)

## Luật cứng
- **Không** làm video trừu tượng tối: nền gần như đen, hình mờ trôi chậm, chữ rất nhỏ, gần như không có nội dung để
  đọc. (vòng 1, r1s2 "Không bao giờ")
- **Không** làm UI/app promo kiểu điện thoại 3D xoay trên nền gradient xanh lạnh, đi lần lượt từng màn rồi kết bằng nút
  store. (vòng 1, r1s4 "Không bao giờ")
- **Không** làm explainer chỉ có chữ kiểu slide: câu sans căn giữa trên nền trắng, chen ảnh stock, gần như không chuyển
  động. (vòng 2, r2s1 "Không bao giờ")

## Nên
### Style
- **2D có nhân vật** là lựa chọn mặc định: `character_2d` 5,0 trên 4 mẫu (tin cậy cao) - nhân vật cartoon đơn giản,
  cử động nhún nhảy, đặt trong thế giới minh hoạ. (r1s5, r2s3, r2s4, r2s5) · animation, dùng được cho motion
- `hand_drawn` (5,0, 2 mẫu): nét bút chì/bút sáp, giấy kẻ, vân màu. (r1s5, r2s4)
- `collage` **giấy cắt** (2D có vân giấy, viền cắt, bóng mềm giữa các lớp) - **không** phải stop-motion đất sét.
  (r1s3, r2s3 "Rất thích" kèm + ở 7 phần; r1s7 stop-motion "Không thích")
- `isometric` (4,6, 2 mẫu) khi **camera luôn di chuyển** và có câu chuyện; bạn chấm + cho nhịp, chuyển động, không khí
  của r2s2. (r1s8 tĩnh thì không thích)
- `flat_vector` chỉ khi có minh hoạ/nhân vật đi kèm; bản nét mảnh, nhạt, liệt kê icon thì không. (r1s1 thích, r2s7 không)
### Không khí
- **Vui tươi** (4,6 trên 4 mẫu, tin cậy cao), **hoài cổ** (5,0, 2 mẫu): ấm, dí dỏm, như truyện tranh/poster cũ.
  (r1s1, r1s3, r2s3, r2s4)
### Nhịp và cắt cảnh
- Theo yêu cầu trực tiếp: **1-2 s/cảnh**. Các mẫu bạn chấm + ở phần nhịp đều có chuyển động dày bên trong cảnh: camera
  trượt liên tục (r2s2), ~2,4 s/cảnh với nhân vật luôn cử động (r2s3), nét vẽ biến hình liên tục (r2s4). · cả hai
### Chuyển cảnh
- Cắt thẳng hoặc **đẩy/lớp giấy trượt vào** (`push` 4,1 trên 5 mẫu); hiệu ứng nằm ở vật thể trong cảnh. (r1s3, r2s3)
### Chữ
- Chữ **đi cùng hình**, không đứng một mình: chữ vẽ tay hoặc cắt giấy đậm, có thể to nửa khung ở cảnh chốt ("GRANDE
  ICED COFFEE $1.95", r2s3). `viet_tay` 4,3 trên 3 mẫu. · cả hai
### Chuyển động
- **Parallax nhiều lớp** (5,0, 2 mẫu) và **lò xo nảy** (4,5, 3 mẫu): nhân vật nhún, vật thể bật vào có overshoot.
  (r1s1, r1s3, r2s3, r2s4)
### Màu
- Nền sáng ấm (kem `#F7F0E3`, giấy be `#E9DCC0`) với 3-4 màu nhấn bão hoà vừa: cam `#F26B4F`, xanh `#2D6CDF`,
  vàng `#F5C342`, đỏ đô `#7A1E1E`, xanh cổ vịt `#1E4A5A`; grade giấy in cũ (`film_grade` 4,3). Bạn chấm + màu của r2s4:
  giấy kem với bút đỏ `#E8402A`, hồng `#F25C9B`, xanh `#2E6FD0`. (r1s1, r1s3, r2s3, r2s4)
### Bố cục
- Nhiều lớp tạo chiều sâu (4,3 trên 5 mẫu, tin cậy vừa); bạn chấm + bố cục nhiều lớp giấy của r2s3. · cả hai
### Kiểu hình
- **Minh hoạ** (4,25 trên 6 mẫu) có texture: vân giấy, bút sáp, halftone; trộn được giấy cắt. (r1s5, r2s3, r2s4, r2s5)
### Cấu trúc
- Mạch kể gọn trong **60-90 s**: hook → 2-4 đoạn phát triển → kết; có hành trình hoặc nhân vật đi qua nhiều bối cảnh
  (`ke_chuyen` 4,4 trên 7 mẫu, tin cậy cao). (r2s3, r2s5, r2s2)

## Tránh
- **Video chỉ có chữ** (`typography_only` 1,7 trên 3 mẫu): kinetic type thuần chữ dù nhịp nhanh (r2s6), font pixel
  (r2s8), explainer slide (r2s1). · motion
- **Liệt kê máy móc** từng màn/từng tính năng (`liet_ke` 1,6 trên 5 mẫu, tin cậy cao). (r1s4, r1s8, r2s1, r2s7, r2s8)
- **Chữ nhỏ, mảnh, khó đọc**. (r1s2, r1s8)
- **Khung đứng yên lâu**; biến đổi tại chỗ không có cú chuyển. (r1s2, r1s8, r2s7)
- **Hoà tan / mờ dần** (1,7 trên 3 mẫu). (r1s2, r1s6, r2s1)
- **Không khí tối, bí ẩn** (1,5 trên 2 mẫu). Nền tối không bị cấm tuyệt đối: isometric nền navy r2s2 vẫn "Thích".
- **Icon nét mảnh, màu nhạt** kiểu explainer SaaS. (r2s7)
- **3D**: chưa có nhu cầu; không dùng trừ khi bạn yêu cầu. (r1s4, r1s6 ghi chú "Tôi chưa có nhu cầu 3d")

## Đang theo dõi
- Kinetic type: 2,5 trên 4 mẫu. Thích khi chữ đi cùng đồ vật minh hoạ (r1s1), không thích khi chỉ có chữ (r2s1, r2s6, r2s8).
- Brutalist, pixel art: mỗi style 1 mẫu, 2 điểm.
- Hook: chưa rõ; cả mở chậm lẫn mở bằng chữ to đều lẫn lộn.
- Âm thanh, phụ đề: chưa đánh giá được (xem không có tiếng; mẫu gần như không có phụ đề).
- Màu nền tối khi có minh hoạ sáng (r2s2 navy được "Thích").

## Câu hỏi còn mở
1. Dancing on Osees (r2s4): bạn chấm + cho style, màu và nhịp nhưng tổng chỉ "Bình thường". Điều gì kéo nó xuống:
   không có câu chuyện, nhân vật quá kỳ dị, hay nét vẽ quá thô?
2. A-Trak (r2s6) nhịp đúng 1,5 s/cảnh nhưng "Không thích". Lý do là chỉ có chữ, hay vì trắng đen, nền đen?

## Lịch sử thay đổi
| Vòng | Thay đổi |
|---|---|
| 1 | Bộ rule đầu tiên từ 8 mẫu; 2 luật cứng; 3D đánh dấu "chưa có nhu cầu". |
| 1 | Mẫu tham khảo từ vòng 2 chỉ lấy video dài dưới 1,5 phút (≤ 90 s). |
| 2 | 16 mẫu. Thêm luật cứng về explainer chỉ có chữ. Style mặc định chuyển sang 2D có nhân vật (tin cậy cao). Gỡ 2 câu hỏi: collage giấy thì thích, stop-motion đất sét thì không; isometric có camera động thì thích. Thêm Tránh: video chỉ có chữ, icon nét mảnh màu nhạt. Nới rule nền tối. |
| 1 | Thêm yêu cầu trực tiếp: video 60-90 s, nhịp 1-2 s/cảnh. Sửa rule nhịp (trước: 3-4 s) và rule cấu trúc. Sửa nhãn nhịp r1s1, r1s3 từ `vua` thành `cham` cho đúng định nghĩa (>2 s). |

<!-- AUTO:EVIDENCE START - phần dưới đây do scripts/taste.py audit viết lại, đừng sửa tay -->
## Bảng bằng chứng
Cập nhật 2026-11-20 · 2 vòng · 16 mẫu đã chấm. Điểm = trung bình có trọng số (điểm riêng của category x1.0, điểm tổng của mẫu x0.6).

| Category | Tag | Điểm | Lệch | Số mẫu | Trạng thái | Tin cậy | Phạm vi | Mẫu |
|---|---|---|---|---|---|---|---|---|
| Style | `character_2d` | 5.00 | 0.00 | 4 | Nên | cao | animation | r1s5, r2s3, r2s4, r2s5 |
| Style | `hand_drawn` | 5.00 | 0.00 | 2 | Nên | vừa | animation | r1s5, r2s4 |
| Style | `isometric` | 4.62 | 0.48 | 2 | Nên | vừa | cả hai | r1s8, r2s2 |
| Style | `collage` | 4.18 | 1.34 | 3 | Nên | thấp | cả hai | r1s3, r1s7, r2s3 |
| Style | `flat_vector` | 4.18 | 1.34 | 3 | Nên | thấp | cả hai | r1s1, r2s5, r2s7 |
| Style | `infographic` | 3.88 | 1.45 | 2 | Đang theo dõi | thấp | cả hai | r1s8, r2s7 |
| Style | `cg_realistic` | 3.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s6 |
| Style | `kinetic_type` | 2.50 | 1.50 | 4 | Mâu thuẫn | thấp | motion | r1s1, r2s1, r2s6, r2s8 |
| Style | `brutalist` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s6 |
| Style | `pixel_art` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s8 |
| Style | `stop_motion` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s7 |
| Style | `abstract` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s2 |
| Style | `product_3d` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s4 |
| Style | `swiss_minimal` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s1 |
| Style | `ui_promo` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s4 |
| Không khí | `hoai_co` | 5.00 | 0.00 | 2 | Nên | vừa | cả hai | r1s3, r2s3 |
| Không khí | `vui_tuoi` | 4.57 | 0.82 | 4 | Nên | cao | cả hai | r1s1, r1s3, r2s3, r2s4 |
| Không khí | `dien_anh` | 3.50 | 0.50 | 2 | Đang theo dõi | vừa | animation | r1s6, r2s5 |
| Không khí | `nghe_thuat` | 3.33 | 1.25 | 3 | Đang theo dõi | thấp | animation | r1s5, r1s7, r2s4 |
| Không khí | `tram_lang` | 3.33 | 1.70 | 3 | Mâu thuẫn | thấp | cả hai | r1s2, r1s5, r2s5 |
| Không khí | `cong_nghe` | 3.09 | 1.78 | 3 | Mâu thuẫn | thấp | motion | r1s4, r2s2, r2s8 |
| Không khí | `ky_ao` | 3.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s6 |
| Không khí | `sach_gon` | 2.90 | 1.76 | 6 | Mâu thuẫn | thấp | cả hai | r1s1, r1s4, r1s8, r2s1, r2s2, r2s7 |
| Không khí | `thu_cong` | 2.50 | 0.50 | 2 | Đang theo dõi | vừa | animation | r1s7, r2s4 |
| Không khí | `nang_dong` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s6 |
| Không khí | `toi_bi_an` | 1.50 | 0.50 | 2 | Tránh | vừa | motion | r1s2, r2s8 |
| Hook | `tinh_roi_bung` | 3.40 | 1.62 | 5 | Mâu thuẫn | thấp | cả hai | r1s2, r1s3, r1s5, r2s5, r2s8 |
| Hook | `chuyen_dong_manh` | 3.33 | 1.25 | 3 | Đang theo dõi | thấp | cả hai | r1s1, r2s4, r2s6 |
| Hook | `hinh_gay_soc` | 3.20 | 1.17 | 5 | Đang theo dõi | vừa | cả hai | r1s6, r1s7, r2s2, r2s3, r2s7 |
| Hook | `chu_to` | 2.25 | 1.64 | 4 | Mâu thuẫn | thấp | motion | r1s1, r1s4, r2s1, r2s6 |
| Hook | `ket_qua_truoc` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s8 |
| Nhịp và cắt cảnh | `co_khoang_lang` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r1s5 |
| Nhịp và cắt cảnh | `vua` | 5.00 | 0.00 | 1 | Đang theo dõi | thấp | animation | r2s3 |
| Nhịp và cắt cảnh | `nhanh` | 3.88 | 1.45 | 2 | Đang theo dõi | thấp | cả hai | r2s4, r2s6 |
| Nhịp và cắt cảnh | `cham` | 2.86 | 1.69 | 13 | Mâu thuẫn | thấp | cả hai | r1s1, r1s2, r1s3, r1s4, r1s5, r1s6, r1s7, r1s8, r2s1, r2s2, r2s5, r2s7, r2s8 |
| Nhịp và cắt cảnh | `khop_beat` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s6 |
| Chuyển cảnh | `push` | 4.12 | 1.49 | 5 | Nên | thấp | cả hai | r1s1, r1s3, r1s4, r2s2, r2s3 |
| Chuyển cảnh | `mask_reveal` | 3.50 | 1.50 | 2 | Mâu thuẫn | thấp | cả hai | r1s3, r1s7 |
| Chuyển cảnh | `cat_thang` | 3.30 | 1.49 | 7 | Đang theo dõi | thấp | cả hai | r1s5, r1s6, r2s1, r2s3, r2s5, r2s6, r2s8 |
| Chuyển cảnh | `morph` | 2.70 | 1.49 | 7 | Đang theo dõi | thấp | cả hai | r1s1, r1s5, r1s7, r1s8, r2s4, r2s6, r2s7 |
| Chuyển cảnh | `zoom_xuyen` | 2.50 | 1.50 | 2 | Mâu thuẫn | thấp | motion | r1s4, r2s2 |
| Chuyển cảnh | `glitch` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s8 |
| Chuyển cảnh | `hoa_tan` | 1.67 | 0.94 | 3 | Tránh | vừa | cả hai | r1s2, r1s6, r2s1 |
| Chữ | `viet_tay` | 4.33 | 0.94 | 3 | Nên | vừa | animation | r1s5, r2s3, r2s4 |
| Chữ | `serif` | 4.00 | 1.00 | 2 | Nên | vừa | cả hai | r1s1, r1s6 |
| Chữ | `chu_to_full` | 3.50 | 1.50 | 4 | Mâu thuẫn | thấp | cả hai | r1s1, r2s3, r2s6, r2s8 |
| Chữ | `sans_grotesk` | 3.00 | 1.58 | 4 | Mâu thuẫn | thấp | cả hai | r1s1, r2s1, r2s5, r2s6 |
| Chữ | `sans_hinh_hoc` | 2.33 | 1.25 | 3 | Đang theo dõi | thấp | motion | r1s4, r2s2, r2s7 |
| Chữ | `chu_nho_tinh` | 2.24 | 1.35 | 5 | Đang theo dõi | thấp | cả hai | r1s2, r1s8, r2s2, r2s5, r2s7 |
| Chữ | `condensed` | 2.07 | 1.58 | 4 | Mâu thuẫn | thấp | cả hai | r1s2, r1s3, r1s8, r2s6 |
| Chữ | `kinetic_tung_tu` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s6 |
| Chữ | `mono` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s8 |
| Chuyển động | `parallax` | 5.00 | 0.00 | 2 | Nên | vừa | cả hai | r1s3, r2s3 |
| Chuyển động | `lo_xo_nay` | 4.45 | 0.89 | 3 | Nên | vừa | cả hai | r1s1, r2s3, r2s4 |
| Chuyển động | `camera_dong` | 3.76 | 1.48 | 5 | Đang theo dõi | thấp | cả hai | r1s3, r1s4, r1s6, r2s2, r2s5 |
| Chuyển động | `ease_muot` | 3.24 | 1.61 | 9 | Mâu thuẫn | thấp | cả hai | r1s1, r1s3, r1s4, r1s6, r1s8, r2s1, r2s2, r2s5, r2s7 |
| Chuyển động | `cham_chill` | 3.00 | 1.63 | 3 | Mâu thuẫn | thấp | cả hai | r1s2, r1s5, r1s6 |
| Chuyển động | `tinh` | 2.50 | 1.50 | 4 | Mâu thuẫn | thấp | cả hai | r1s5, r1s7, r1s8, r2s1 |
| Chuyển động | `giat_nhanh` | 2.25 | 0.43 | 4 | Đang theo dõi | cao | cả hai | r1s7, r2s4, r2s6, r2s8 |
| Chuyển động | `motion_blur` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s2 |
| Màu | `film_grade` | 4.33 | 0.94 | 3 | Nên | vừa | cả hai | r1s3, r1s6, r2s3 |
| Màu | `am` | 4.12 | 1.23 | 5 | Nên | thấp | cả hai | r1s3, r1s6, r1s7, r2s3, r2s4 |
| Màu | `tuong_phan_cao` | 3.71 | 1.48 | 4 | Đang theo dõi | thấp | cả hai | r1s1, r2s4, r2s6, r2s8 |
| Màu | `pastel` | 3.50 | 1.50 | 4 | Mâu thuẫn | thấp | cả hai | r1s5, r1s7, r2s3, r2s7 |
| Màu | `don_sac` | 3.00 | 1.58 | 4 | Mâu thuẫn | thấp | cả hai | r1s2, r1s5, r2s2, r2s6 |
| Màu | `lanh` | 3.00 | 1.67 | 5 | Mâu thuẫn | thấp | cả hai | r1s2, r1s4, r1s5, r2s2, r2s5 |
| Màu | `nen_sang` | 2.90 | 1.76 | 6 | Mâu thuẫn | thấp | cả hai | r1s1, r1s4, r1s8, r2s1, r2s4, r2s7 |
| Màu | `trung_tinh` | 2.80 | 1.47 | 5 | Đang theo dõi | thấp | cả hai | r1s3, r1s7, r1s8, r2s1, r2s5 |
| Màu | `nen_toi` | 2.60 | 1.20 | 5 | Đang theo dõi | thấp | cả hai | r1s2, r2s2, r2s5, r2s6, r2s8 |
| Bố cục | `nhieu_lop` | 4.29 | 1.13 | 5 | Nên | vừa | cả hai | r1s1, r1s3, r1s8, r2s2, r2s3 |
| Bố cục | `luoi_swiss` | 3.25 | 1.30 | 4 | Đang theo dõi | thấp | cả hai | r1s1, r1s8, r2s2, r2s8 |
| Bố cục | `ngang_16_9` | 3.02 | 1.50 | 16 | Mâu thuẫn | thấp | cả hai | r1s1, r1s2, r1s3, r1s4, r1s5, r1s6, r1s7, r1s8, r2s1, r2s2, r2s3, r2s4, r2s5, r2s6, r2s7, r2s8 |
| Bố cục | `bat_doi_xung` | 3.00 | 1.58 | 4 | Mâu thuẫn | thấp | cả hai | r1s2, r1s5, r1s7, r2s5 |
| Bố cục | `chinh_giua` | 2.92 | 1.54 | 8 | Mâu thuẫn | thấp | cả hai | r1s3, r1s4, r1s6, r2s1, r2s3, r2s4, r2s6, r2s7 |
| Bố cục | `nhieu_khoang_trong` | 2.40 | 1.50 | 5 | Đang theo dõi | thấp | cả hai | r1s2, r1s5, r2s1, r2s4, r2s7 |
| Bố cục | `full_bleed` | 2.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r2s6 |
| Kiểu hình | `minh_hoa` | 4.25 | 1.09 | 6 | Nên | vừa | cả hai | r1s5, r1s8, r2s2, r2s3, r2s4, r2s5 |
| Kiểu hình | `collage` | 4.12 | 1.23 | 5 | Nên | thấp | cả hai | r1s1, r1s3, r1s7, r2s3, r2s4 |
| Kiểu hình | `2d_phang` | 4.05 | 1.30 | 6 | Nên | thấp | cả hai | r1s1, r1s5, r1s8, r2s2, r2s5, r2s7 |
| Kiểu hình | `texture_hat` | 3.71 | 1.56 | 8 | Mâu thuẫn | thấp | cả hai | r1s1, r1s2, r1s3, r1s5, r1s7, r2s3, r2s4, r2s8 |
| Kiểu hình | `3d_render` | 2.00 | 1.00 | 2 | Tránh | vừa | cả hai | r1s4, r1s6 |
| Kiểu hình | `typography_only` | 1.67 | 0.47 | 3 | Tránh | vừa | motion | r2s1, r2s6, r2s8 |
| Kiểu hình | `footage_that` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s2 |
| Kiểu hình | `ui_san_pham` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s4 |
| Phụ đề | `khong_co` | 3.07 | 1.44 | 15 | Đang theo dõi | thấp | cả hai | r1s1, r1s3, r1s4, r1s5, r1s6, r1s7, r1s8, r2s1, r2s2, r2s3, r2s4, r2s5, r2s6, r2s7, r2s8 |
| Phụ đề | `gian_don` | 1.00 | 0.00 | 1 | Đang theo dõi | thấp | motion | r1s2 |
| Cấu trúc | `tren_60s` | 4.50 | 0.87 | 4 | Nên | cao | cả hai | r1s1, r1s3, r1s5, r1s6 |
| Cấu trúc | `ke_chuyen` | 4.43 | 0.73 | 7 | Nên | cao | cả hai | r1s1, r1s3, r1s5, r1s6, r2s2, r2s3, r2s5 |
| Cấu trúc | `15_30s` | 3.00 | 1.41 | 3 | Đang theo dõi | thấp | cả hai | r1s8, r2s3, r2s6 |
| Cấu trúc | `cta_ro` | 2.60 | 1.62 | 5 | Mâu thuẫn | thấp | cả hai | r1s4, r2s1, r2s2, r2s3, r2s7 |
| Cấu trúc | `loop` | 2.33 | 0.47 | 3 | Đang theo dõi | vừa | cả hai | r1s8, r2s4, r2s6 |
| Cấu trúc | `30_60s` | 2.22 | 1.13 | 9 | Đang theo dõi | vừa | cả hai | r1s2, r1s4, r1s7, r2s1, r2s2, r2s4, r2s5, r2s7, r2s8 |
| Cấu trúc | `liet_ke` | 1.60 | 0.49 | 5 | Tránh | cao | cả hai | r1s4, r1s8, r2s1, r2s7, r2s8 |
<!-- AUTO:EVIDENCE END -->
