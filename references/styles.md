# Thư viện style motion & animation

**Đang dùng để dựng (skill `motion-styles`, file `ACTIVE`): `collage` và `vox`.** Các style khác ở đây chỉ để nhận diện
và gắn nhãn mẫu khi chấm gu.

Mỗi style có id (trùng tag của category `style` trong `categories.md`), cách nhận diện, ngữ pháp mặc định theo các
category, cách dựng, và những lỗi làm nó trông rẻ. Đây là **mặc định của style**, không phải gu của người dùng: khi
thiết kế, gu trong `motion-taste.md` luôn đè lên mặc định ở đây (xem SKILL.md, "Thiết kế theo một style").

Cách dựng ghi theo khả năng của studio code (Remotion / canvas): **dễ** = chỉ cần hình khối, chữ, ảnh; **vừa** = cần
asset vẽ sẵn hoặc shader; **khó** = cần phần mềm 3D, quay thật hoặc vẽ tay từng khung; khi khó, ghi cách giả lập.

Mục lục: kinetic_type · swiss_minimal · flat_vector · character_2d · hand_drawn · collage · stop_motion · cg_realistic ·
cg_stylized · product_3d · ui_promo · isometric · infographic · abstract · glitch_grunge · retro · pixel_art · brutalist

---

## kinetic_type - Kinetic typography
- **Nhận diện:** chữ là chủ thể; từ xuất hiện theo lời hoặc nhịp; ít hoặc không có hình minh hoạ.
- **Ngữ pháp:** nhịp nhanh, đổi khung theo từ/cụm từ (0,3-0,8 s); chuyển cảnh bằng chính chữ (phóng xuyên chữ, mask
  qua chữ, chữ biến hình); chữ grotesk hoặc condensed đậm, chữ to chiếm 40-80% khung; chuyển động lò xo gọn, so le
  30-60 ms giữa ký tự; 2-3 màu, tương phản cao.
- **Dựng:** dễ. Mỗi từ là một phần tử, `riseWord`/mask, khớp lưới phách.
- **Rẻ tiền khi:** mọi từ cùng một kiểu vào; dùng quá 2 font; chữ nhảy loạn không theo nhịp.

## swiss_minimal - Swiss / tối giản lưới
- **Nhận diện:** lưới rõ, căn lề trái, nhiều khoảng trống, 1 màu nhấn.
- **Ngữ pháp:** nhịp vừa, cắt trên phách mạnh; chuyển cảnh wipe/push theo trục lưới; grotesk (Helvetica, Inter, Neue
  Haas), cỡ chữ tương phản lớn; ease mượt, không nảy; nền trắng/đen + 1 màu đỏ/cam/xanh; hình học cơ bản.
- **Dựng:** dễ.
- **Rẻ tiền khi:** lệch lưới; thêm gradient, bóng đổ; nhiều màu nhấn.

## flat_vector - 2D vector phẳng / explainer
- **Nhận diện:** hình vector phẳng, màu khối, icon và đồ vật đơn giản, thường giải thích một ý.
- **Ngữ pháp:** nhịp vừa (2-3 s/ý); chuyển cảnh morph, push, vật thể bật vào; sans hình học; lò xo nảy nhẹ; 4-6 màu
  tươi trên nền sáng; thường thêm hạt nhẹ để bớt "nhựa".
- **Dựng:** dễ. SVG/canvas, path morph.
- **Rẻ tiền khi:** màu mặc định của bộ icon; mọi thứ bật vào cùng lúc; không có texture, không có bóng tối.

## character_2d - 2D nhân vật cartoon
- **Nhận diện:** có nhân vật vẽ cách điệu (vector, rubber hose, cut-out rig).
- **Ngữ pháp:** nhịp theo hành động; cắt thẳng giữa các góc máy; squash & stretch, anticipation, overshoot; màu
  khối; chữ ít.
- **Dựng:** vừa. Rig nhân vật bằng các phần tử SVG xoay quanh khớp; vẽ tay từng khung thì khó.
- **Rẻ tiền khi:** nhân vật trượt không có trọng lượng; tay chân cứng; lip-sync lệch.

## hand_drawn - 2D vẽ tay / frame-by-frame
- **Nhận diện:** nét bút chì/mực/màu nước thấy rõ, đường nét "sôi" nhẹ giữa các khung, thường 8-12 hình/giây.
- **Ngữ pháp:** nhịp chậm đến vừa, giữ hình lâu; chuyển cảnh hoà tan hoặc biến hình bằng nét; chữ viết tay; chuyển động
  tiết chế; mỗi cảnh một tông màu chủ đạo; texture giấy.
- **Dựng:** khó. Giả lập: ảnh vẽ sẵn + boil nét (dịch path vài px mỗi 2-3 khung) + texture giấy + 12 fps.
- **Rẻ tiền khi:** nét quá sạch như vector; chạy 60 fps mượt mất chất tay.

## collage - Collage / mixed media
- **Nhận diện:** ảnh cắt dán (thường ảnh cổ), giấy, băng dính, nhiều lớp chồng; nhân vật cử động kiểu rối giấy.
- **Ngữ pháp:** nhịp vừa; chuyển cảnh lớp giấy trượt vào/ra, lộ qua mép giấy; parallax nhiều lớp; chữ ít, kiểu bảng
  hiệu hoặc cắt từ báo; màu giấy cũ, be, đỏ đô, xanh cổ vịt; hạt và vết gấp.
- **Dựng:** vừa. Ảnh PNG cắt viền + bóng mềm + xoay khớp.
- **Rẻ tiền khi:** viền cắt quá sạch; ảnh hiện đại lẫn ảnh cổ không chủ đích; không có bóng giữa các lớp.

## stop_motion - Stop-motion (đất sét, giấy, vật thật)
- **Nhận diện:** vật thật chụp từng khung, rung tự nhiên, thấy vân tay/vân giấy, 10-12 hình/giây.
- **Ngữ pháp:** ít cắt, cảnh biến đổi ngay trong khung; chuyển động giật nhẹ; ánh sáng bàn mềm; màu pastel ấm; chữ làm
  bằng vật liệu thật.
- **Dựng:** khó. Giả lập: ảnh vật thật + nhảy khung 12 fps + rung vị trí ±1-2 px + thay sprite.
- **Rẻ tiền khi:** quá mượt (mất chất stop-motion); ánh sáng nhấp nháy không chủ đích.

## cg_realistic - 3D CG hiện thực / điện ảnh
- **Nhận diện:** render 3D có ánh sáng, chất liệu, độ sâu trường ảnh như phim.
- **Ngữ pháp:** nhịp chậm, cắt thưa; camera dolly/crane trôi; grade phim; chữ serif hoặc sans mảnh, ít.
- **Dựng:** khó. Cần Blender/C4D; studio code chỉ ghép footage render sẵn.
- **Rẻ tiền khi:** ánh sáng phẳng; camera quay không có lý do; thung lũng kỳ lạ ở nhân vật.

## cg_stylized - 3D cách điệu
- **Nhận diện:** 3D bo tròn, chất đất nặn/nhựa/đồ chơi, màu kẹo, ánh sáng mềm.
- **Ngữ pháp:** nhịp vừa; vật thể nảy, squash; camera xoay quanh; sans tròn; pastel bão hoà.
- **Dựng:** vừa-khó. Three.js cho cảnh đơn giản; cảnh phức tạp cần phần mềm 3D.
- **Rẻ tiền khi:** chất liệu mặc định bóng nhựa; bóng đổ cứng.

## product_3d - 3D sản phẩm
- **Nhận diện:** một sản phẩm xoay trong studio, phản chiếu, cận chi tiết.
- **Ngữ pháp:** nhịp vừa-nhanh, cắt theo beat giữa các góc cận; camera orbit, push-in; nền tối hoặc gradient; chữ
  sans mảnh, thông số nhỏ; ease chậm sang trọng.
- **Dựng:** khó (render) hoặc vừa (ảnh sản phẩm + parallax giả 3D).
- **Rẻ tiền khi:** xoay 360° liên tục không điểm nhấn; lens flare thừa.

## ui_promo - UI / app promo
- **Nhận diện:** màn hình app/web thật chuyển động, mockup thiết bị, con trỏ hoặc ngón tay.
- **Ngữ pháp:** nhịp vừa; camera bay vào màn hình, zoom vào phần tử; UI tự bấm, số nhảy; sans hình học/grotesk; ease
  mượt; nền gradient nhẹ; kết bằng CTA.
- **Dựng:** dễ-vừa. Dựng lại UI bằng HTML/canvas sẽ nét hơn quay màn hình.
- **Rẻ tiền khi:** thiết bị xoay vô cớ; UI mờ vì phóng ảnh chụp; mọi màn hình cùng một kiểu vào.

## isometric - Isometric
- **Nhận diện:** thế giới nhỏ góc 30°, khối hộp, thường là bản đồ hoặc dây chuyền.
- **Ngữ pháp:** khung cố định hoặc camera trượt chậm; khu vực sáng lên lần lượt; vòng lặp; nhãn chữ chạy theo trục;
  màu nhạt dịu.
- **Dựng:** vừa.
- **Rẻ tiền khi:** sai trục phối cảnh; quá nhiều chi tiết nhỏ không đọc được ở điện thoại.

## infographic - Infographic / data động
- **Nhận diện:** biểu đồ, số liệu, sơ đồ chuyển động là nội dung chính.
- **Ngữ pháp:** nhịp theo ý dữ liệu; số đếm lên, thanh mọc, đường vẽ dần; mono hoặc grotesk số đều; màu có nghĩa.
- **Dựng:** dễ.
- **Rẻ tiền khi:** số liệu trang trí không đúng tỉ lệ; quá nhiều biểu đồ một lúc.

## abstract - Trừu tượng
- **Nhận diện:** hình khối, chất lỏng, ánh sáng, hạt; không kể chuyện cụ thể.
- **Ngữ pháp:** nhịp theo nhạc; chuyển cảnh hoà tan/biến hình; chữ rất ít, nhỏ; chuyển động trôi, liên tục; một tông
  màu chủ đạo, thường tối.
- **Dựng:** vừa. Shader/canvas.
- **Rẻ tiền khi:** preset gradient lỏng phổ biến; không có điểm nhấn nào để mắt bám.

## glitch_grunge - Glitch / grunge
- **Nhận diện:** nhiễu số, RGB lệch, scanline, texture bẩn, flash.
- **Ngữ pháp:** nhịp rất nhanh, cắt trên phách; flash, đảo âm bản; chữ condensed/mono, méo; tương phản gắt.
- **Dựng:** dễ-vừa. Shader hoặc lớp phủ.
- **Rẻ tiền khi:** glitch ở mọi cú cắt; hiệu ứng che mất nội dung.

## retro - Retro / Y2K / VHS
- **Nhận diện:** màu và chất liệu của một thập niên cũ: VHS, chrome Y2K, poster thập niên 70.
- **Ngữ pháp:** theo thập niên được chọn; thường có hạt, viền tròn, chữ đặc trưng thời kỳ; màu ngả.
- **Dựng:** dễ-vừa.
- **Rẻ tiền khi:** trộn nhiều thập niên; lớp VHS phủ lên nội dung hiện đại mà không đổi chữ, màu.

## pixel_art - Pixel art
- **Nhận diện:** lưới pixel lớn, bảng màu giới hạn, hoạt hình ít khung.
- **Ngữ pháp:** chuyển động theo bước pixel, 8-12 fps; chữ pixel; palette 8-16 màu.
- **Dựng:** vừa. Canvas với `imageSmoothingEnabled = false`.
- **Rẻ tiền khi:** pixel không đều cỡ; xoay/scale làm vỡ lưới.

## brutalist - Brutalist
- **Nhận diện:** khối thô, chữ cực to, đường viền đen dày, màu gắt, bố cục cố ý "sai".
- **Ngữ pháp:** cắt cứng, nhanh; chữ grotesk/condensed siêu đậm tràn khung; không ease (giật); 2 màu gắt + đen.
- **Dựng:** dễ.
- **Rẻ tiền khi:** thô mà không có hệ thống; chữ khó đọc.

## vox - Video giải thích kiểu Vox (tư liệu + tài liệu + đồ hoạ chú thích)
- **Nhận diện:** ảnh tư liệu đen trắng/sepia cắt rời đặt trên nền giấy kem, đen than, màu đất phẳng hoặc xám; vệt dạ
  quang vàng tô chữ trong tài liệu; nhãn chữ hoa và nét khoanh/X/mũi tên vẽ tay đỏ hoặc vàng; bản đồ cổ, sơ đồ biến đổi.
  Ba biến thể: A flat cutout, B archive screen, C paper collage (chi tiết `motion-styles/vox/README.md`).
- **Ngữ pháp:** chữ vào theo đơn vị lời, không có hoạt cảnh ra; không dissolve, nối cảnh bằng wipe khối màu, push,
  blob-zoom, match cut hoặc cắt cứng; camera ảo zoom/pan trên ảnh tĩnh; một màu nhấn theo chức năng (vàng tô, đỏ cảnh
  báo); A/B chạy bậc 12/10 fps không vượt, C mượt có spring vượt.
- **Dựng:** vừa. Đồ hoạ, nhãn, chữ, texture làm được bằng code; ảnh tư liệu là tài sản cần có. Luật riêng, bộ file
  hướng dẫn và component ở `~/.claude/skills/motion-styles/vox/`.
- **Rẻ tiền khi:** font thiếu dấu tiếng Việt; vệt tô và nét vẽ tay xuất hiện vô cớ, không theo lời; cả khung đen trắng
  không có màu nhấn; dùng logo/giao diện thương hiệu thật; khung đứng yên quá 1 s.

---

## Thêm style mới
Khi gặp mẫu không vừa style nào: thêm một mục mới ở đây theo đúng khung trên (id viết thường, nối `_`), thêm tag cùng
id vào category `style` trong `categories.md`, và nói với người dùng là đã thêm style mới. Khi style được dùng để
dựng, tạo thư mục của nó trong `motion-styles` bằng `styles.py new <id>` và viết `STYLE.md` theo khung cố định 11 mục
(`motion-styles/SKILL.md`, mục "Khung cố định").
