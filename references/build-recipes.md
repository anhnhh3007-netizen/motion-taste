# Công thức dựng theo style

File này nói **làm thế nào** để dựng một style bằng pipeline của Motion studio (Remotion, chỉ code, có thể kèm tài sản
hình). `styles.md` nói style **trông thế nào**; file này là công thức để làm ra nó.

**Quy tắc chọn (yêu cầu trực tiếp của người dùng, 2026-11-23):**
- **Mặc định luôn là `code_polished`** (mục 0 bên dưới), kể cả khi gu chấm cao vẽ tay hay collage.
- Chỉ dùng công thức khác khi người dùng **nói rõ** muốn style đó trong brief ("làm kiểu vẽ tay", "collage giấy cắt").
  Không tự đề xuất đổi style.
- Style người dùng chọn cần tài sản hình (ảnh sinh, hình vẽ sẵn): báo số ảnh và credit, chờ duyệt trước khi sinh.
  Người dùng không cho sinh ảnh thì nói rõ mức làm được (cột "Chỉ code") trước khi dựng.

Thứ tự ưu tiên vẫn giữ: luật cứng > yêu cầu trực tiếp > bài học từ video Claude làm > công thức này > rule chung.

Mỗi công thức gồm:
- **Tài sản:** cần gì ngoài code.
- **Dựng:** kỹ thuật Remotion cụ thể.
- **Chuyển động:** cách cử động.
- **Kiểm trước khi giao:** những lỗi làm style thành rẻ tiền.
- **Mức làm được:** chỉ code / có tài sản hình.

---

## 0. code_polished - Mặc định: vector hoàn thiện dựng bằng code
Rút từ thử nghiệm AB1 (bản mặc định được chấm Thích, bản giả vẽ tay bị chấm Không thích).
- **Tài sản:** không cần. Toàn bộ là SVG/CSS trong Remotion.
- **Dựng:**
  - **Nền có chiều sâu:** gradient tỏa tròn hai tông (ví dụ xanh than `#0E1430` → chàm `#1B2B5E`), hoặc nền sáng có
    vignette nhẹ. Không dùng nền phẳng một màu suốt video.
  - **Ánh sáng:** vật chính có quầng sáng bằng 2-3 lớp cùng hình, `filter: blur()` tăng dần, opacity giảm dần. Lõi sáng
    hơn viền (Mặt Trời `#FFB23E`, lõi `#FFF4D2`).
  - **Hình:** vector sạch, đổ bóng mềm hoặc đổ sáng một phía; mỗi vật 2-3 tông. Không viền đen dày, không nét rung.
  - **Không gian:** 3-4 lớp parallax (sao/hạt xa 0,3×, vật giữa 1×, tiền cảnh 1,3×).
  - **Chữ:** một sans rất đậm cho tiêu đề (Avenir Next Heavy 800 hoặc tương đương có dấu tiếng Việt), một mono nhỏ cho
    nhãn thông tin (Menlo). Chữ chính ≥ 5% chiều cao khung.
  - **Một màu nhấn** (ví dụ xanh `#2F80ED`); các màu khác chỉ khi là nội dung (ví dụ phổ màu).
  - **Tối đa một nhân vật có mặt** (mắt đơn giản), các vật khác không gắn mặt.
- **Chuyển động:**
  - Camera bám theo vật chính; đẩy vào chi tiết ở khoảnh khắc quan trọng (va chạm, kết quả).
  - Chuyển cảnh thông minh:
    - match cut: một hình nhỏ nở thành hình của cảnh sau;
    - whip theo hướng vật đang bay;
    - một màu tràn kín khung thành nền cảnh sau.
  - Lò xo có overshoot nhỏ; chữ trồi so le qua mặt nạ.
- **Kiểm trước khi giao:**
  - Có khung nào nền phẳng không có chiều sâu?
  - Có quá 2 vệt/đường chồng nhau làm rối không?
  - Mỗi cảnh có một ý và một chủ thể rõ không?
  - Có ít nhất một thông tin thật (con số, nhãn) làm điểm tựa không?
- **Mức làm được:** tốt, chỉ bằng code.

## 1. hand_drawn - Vẽ tay (chỉ khi người dùng yêu cầu)
- **Tài sản:** **bắt buộc có hình vẽ tay thật**: ảnh sinh theo style vẽ tay (bút chì, mực, màu nước) tách lớp PNG nền
  trong, hoặc hình người dùng đưa. Mỗi nhân vật hay vật chính cần 2-4 tư thế (sprite) nếu phải cử động.
- **Dựng:**
  - Đặt ảnh vẽ sẵn; texture giấy thật (ảnh quét hoặc ảnh sinh) phủ `mix-blend-mode: multiply`.
  - **Boil nét:** dịch mỗi lớp ±1-2 px theo `random(seed)` đổi mỗi 2 khung, hoặc xoay vòng 3 bản vẽ hơi khác nhau.
  - Chạy **12 hình/giây**: chuyển động tính theo `Math.floor(t * 12) / 12`, render vẫn 60 fps.
  - Chữ: chữ viết tay **là ảnh** (sinh hoặc vẽ), không dùng font tay hệ thống.
- **Chuyển động:** thay sprite theo tư thế (2-4 hình/động tác), giữ hình lâu hơn; biến hình bằng nét tự vẽ ra.
- **Kiểm trước khi giao:**
  - Có chỗ nào là vector sạch giả vẽ tay không? Nếu có thì thay bằng ảnh.
  - Có font Marker Felt / Chalkboard không? Nếu có thì bỏ.
  - Có mặt cười trên mọi vật không?
  - Có hình que không?
- **Mức làm được:**
  - Chỉ code: **không nên làm**. AB1 cho thấy giả vẽ tay bằng code thành nghiệp dư. Nói với người dùng và đề xuất
    `code_polished`, hoặc xin dùng ảnh.
  - Có ảnh: khá, nhưng nhân vật chỉ cử động ít (đổi tư thế), không diễn xuất phức tạp.

## 2. collage - Collage giấy cắt / mixed media (chỉ khi người dùng yêu cầu)
- **Tài sản:** các mảnh ảnh hoặc giấy cắt PNG nền trong (ảnh sinh hoặc ảnh người dùng đưa): nền giấy có vân, 5-15
  mảnh vật, nhân vật tách khớp (đầu, thân, tay, chân riêng).
- **Dựng:**
  - Mỗi mảnh là `<Img>` có viền giấy trắng 4-8 px không đều (ảnh có sẵn viền, hoặc `drop-shadow` trắng 0 blur cộng mặt
    nạ xé).
  - Bóng đổ cứng lệch 6-10 px giữa các lớp (`drop-shadow(8px 10px 0 rgba(0,0,0,.18))`).
  - Mép xé bằng `clip-path` polygon nhiễu có seed.
  - Texture giấy multiply phủ toàn khung.
- **Chuyển động:**
  - Rối giấy: mảnh xoay quanh khớp (`transform-origin` tại khớp) theo lò xo.
  - Nhảy khung 12 hình/giây cho chất thủ công.
  - Chuyển cảnh bằng lớp giấy trượt vào đẩy cảnh cũ ra, hoặc lộ cảnh qua mép xé.
  - Parallax 3 lớp.
- **Kiểm trước khi giao:**
  - Viền cắt có quá sạch không?
  - Có bóng giữa các lớp không?
  - Ảnh có lẫn thời kỳ không chủ đích không?
  - Có quá nhiều mảnh nhỏ không đọc được không?
- **Mức làm được:**
  - Chỉ code (giấy vẽ bằng SVG): trung bình, dễ thành phẳng.
  - Có ảnh: **khá tốt**, đây là style hợp code nhất trong nhóm thủ công.

## 3. character_2d - Nhân vật 2D có cá tính (chỉ khi người dùng yêu cầu)
- **Tài sản:** nhân vật tách lớp (đầu, mắt, miệng, thân, tay, chân) dạng SVG vẽ bằng code hoặc PNG sinh; bảng biểu cảm
  3-5 miệng/mắt.
- **Dựng:** rig xoay quanh khớp, squash & stretch theo lò xo, đổi biểu cảm bằng thay sprite; ánh sáng cel hai tông.
- **Chuyển động:** tạo dáng phóng đại, anticipation trước động tác lớn, theo sau (tóc, áo) trễ 2-4 khung.
- **Kiểm trước khi giao:**
  - Nhân vật có trượt không trọng lượng không?
  - Tay chân có cứng không?
  - Có phải nhân vật flat dáng dài kiểu công ty không? (Tránh trong gu.)
- **Mức làm được:** vừa. Đi, nhảy, đổi góc quay phức tạp thì hạn chế.

## 4. isometric - Thế giới isometric (chỉ khi người dùng yêu cầu)
- **Tài sản:** không cần; khối dựng bằng SVG theo lưới 30°.
- **Dựng:**
  - Hàm `iso(x, y, z)` → toạ độ màn hình.
  - Mỗi khối có 3 mặt 3 tông (sáng/vừa/tối).
  - Bóng mềm dưới khối.
  - Sắp xếp vẽ theo `x + y` để không đè sai.
- **Chuyển động:** camera trượt hoặc zoom xuyên qua thành phố; khối mọc lên bằng lò xo; đường nối chạy theo trục.
- **Kiểm trước khi giao:**
  - Có lệch trục 30° không?
  - Có chi tiết quá nhỏ không đọc được trên điện thoại không?
  - Bản đồ có hiện sẵn rồi chỉ sáng dần không? Cần có camera di chuyển (gu: r1s8 bị chê, r2s2 được thích).
- **Mức làm được:** tốt, chỉ code.

## 5. kinetic_type - Chữ là nhân vật (chỉ khi người dùng yêu cầu)
- **Tài sản:** không cần.
- **Dựng:**
  - Chữ rất to (serif đậm hoặc sans heavy) tràn khung.
  - Mỗi từ là phần tử riêng; biến hình chữ qua nhiều kiểu.
  - Có thêm hình hoặc nét đi kèm, không để chữ đứng một mình trên nền trống (luật cứng: không làm slide chữ).
- **Chuyển động:** từ dập vào theo phách; chữ đổi mỗi ~0,5 s ở hook; mặt nạ trồi; khớp beat.
- **Kiểm trước khi giao:**
  - Mọi từ có vào cùng một kiểu không?
  - Có quá 2 font không?
  - Có câu sans căn giữa trên nền trắng không? (Luật cứng.)
- **Mức làm được:** tốt, chỉ code.

## 6. infographic - Dữ liệu và sơ đồ động (chỉ khi người dùng yêu cầu)
- **Tài sản:** số liệu thật từ brief.
- **Dựng:** biểu đồ SVG đúng tỉ lệ; số chạy đếm; nhãn mono; theo nền và ánh sáng của `code_polished`.
- **Chuyển động:** mỗi lúc một biểu đồ; camera đẩy vào con số chính.
- **Kiểm trước khi giao:**
  - Số liệu có trang trí sai tỉ lệ không?
  - Có nhiều biểu đồ cùng lúc không?
  - Có liệt kê máy móc không? (Tránh trong gu.)
- **Mức làm được:** tốt, chỉ code.

## 7. stop_motion - Stop-motion (chỉ khi người dùng yêu cầu)
- **Tài sản:** **bắt buộc** ảnh vật thật hoặc ảnh sinh theo kiểu chụp đất sét/giấy, nhiều tư thế.
- **Dựng:** thay ảnh theo tư thế; 12 hình/giây; rung vị trí ±1-2 px mỗi khung; ánh sáng nhấp nháy rất nhẹ.
- **Kiểm trước khi giao:** có quá mượt không (mất chất); có ánh sáng nhấp nháy không chủ đích không.
- **Mức làm được:**
  - Chỉ code: không nên.
  - Có ảnh: trung bình. Gu cũ chấm thấp stop-motion đất sét (r1s7), nên nói ra trước khi làm.

---

## Thêm công thức mới
Khi người dùng yêu cầu một style chưa có ở đây: thêm mục theo khung trên, id trùng `styles.md`. Sau video đầu tiên
dùng công thức đó, ghi điểm người dùng chấm vào `data/own/` và sửa công thức.
