# 🎬 Video Demo Script — SmartFlow AgriSCM

**Thời lượng mục tiêu:** 4 phút 30 giây — 5 phút  
**Người thuyết trình:** Nguyễn Trường Sang  
**Người quay/chỉnh sửa:** Tống Bình Minh  
**Thiết bị:** Màn hình 1080p, mic tốt (không có tiếng ồn nền)  
**Quay ngày:** Sáng thứ 3, 08/07/2026

---

## Chuẩn bị trước khi quay

### 1. Chuẩn bị môi trường demo
- [ ] Mở tab browser sẵn: Live URL Railway + Jira Board + Confluence Home + GitHub README
- [ ] Đăng nhập sẵn tài khoản `admin@smartflow.demo`
- [ ] Seed đủ dữ liệu: ≥ 5 nông hộ, ≥ 3 đơn hàng đã duyệt, ≥ 2 lô hàng trong kho
- [ ] Tắt hết thông báo desktop, đặt trình duyệt fullscreen
- [ ] Độ phân giải màn hình: 1920×1080 (hoặc 1440×900)
- [ ] Kiểm tra âm thanh micro

### 2. Công cụ quay
- OBS Studio (free) hoặc QuickTime Player (Mac)
- Xuất file: MP4, 1080p, 30fps

---

## Script chi tiết theo từng mốc

### [00:00 – 00:30] — Giới thiệu (30 giây)
**Màn hình:** Confluence Home Page (landing page đẹp)

**Lời thoại:**
> "Chào Thầy/Cô, nhóm SmartFlow xin giới thiệu hệ thống quản lý chuỗi cung ứng nông sản — giải quyết 4 vấn đề nghiêm trọng mà các hợp tác xã lúa gạo tại Đắk Lắk đang gặp phải: không truy xuất được nguồn gốc, thất thoát kho bãi, thiếu minh bạch giá cả, và quy trình thủ công tốn thời gian. Hệ thống được xây dựng bằng Laravel và MySQL, triển khai tại Railway.app."

**Action:** Scroll qua Confluence Home → click vào Live URL

---

### [00:30 – 01:00] — Tổng quan Dashboard (30 giây)
**Màn hình:** Dashboard sau khi đăng nhập (tài khoản Quản lý HTX)

**Lời thoại:**
> "Đây là Dashboard của Quản lý HTX — giao diện tập trung hiển thị số lô hàng trong kho, tổng đơn hàng tháng này, cảnh báo tồn kho, và biểu đồ sản lượng theo tuần. Tất cả cập nhật real-time."

**Action:** Di chuột chỉ vào từng widget, hover để thấy tooltip

---

### [01:00 – 02:00] — Luồng nghiệp vụ chính (60 giây)
**Màn hình:** Module Quản lý Đơn hàng

**Lời thoại:**
> "Luồng chính của hệ thống: nông hộ [chuyển sang tài khoản nongho] đăng nhập và đăng ký lô hàng 500kg lúa ST24. Hệ thống ghi nhận thông tin ruộng, giống lúa, ngày thu hoạch."

**Action:** [Login nongho] → Tạo đơn đăng ký lô hàng → Submit

> "Phía thương lái hoặc HTX [chuyển sang tài khoản admin] nhận được đề nghị và phê duyệt. Trạng thái đơn hàng chuyển sang 'Đã duyệt' ngay lập tức."

**Action:** [Login admin] → Vào danh sách đơn hàng → Duyệt đơn vừa tạo

---

### [02:00 – 02:45] — Nhập kho & Sinh QR (45 giây)
**Màn hình:** Module Kho bãi

**Lời thoại:**
> "Sau khi đơn được duyệt, thủ kho nhập lô hàng vào kho — hệ thống tự động sinh mã QR cho lô hàng này. Mỗi QR code chứa toàn bộ thông tin: nông hộ, ruộng, giống lúa, ngày nhập, số lô."

**Action:** [Vào module kho] → Nhập kho cho đơn vừa duyệt → Hiển thị QR code vừa sinh

> "Tôi quét thử QR này bằng điện thoại..."

**Action:** [Dùng điện thoại quét QR — hiện trang truy xuất nguồn gốc]

---

### [02:45 – 03:30] — Dashboard & Báo cáo PDF (45 giây)
**Màn hình:** Dashboard tồn kho → Xuất PDF

**Lời thoại:**
> "Dashboard tồn kho cập nhật ngay sau khi nhập: tổng tồn 1.200 kg, trong đó ST24 là 700kg và Đài Thơm 8 là 500kg. Cảnh báo màu đỏ xuất hiện khi tồn xuống dưới ngưỡng tối thiểu. Thủ kho có thể xuất báo cáo PDF ngay trong một cú click."

**Action:** Click 'Xuất báo cáo PDF' → PDF hiện ra, scroll qua nhanh

---

### [03:30 – 04:15] — Truy xuất nguồn gốc (45 giây)
**Màn hình:** Trang truy xuất nguồn gốc (public — không cần đăng nhập)

**Lời thoại:**
> "Điểm nổi bật nhất của SmartFlow là tính năng truy xuất nguồn gốc. Người tiêu dùng chỉ cần quét QR trên bao bì — hệ thống hiển thị đầy đủ hành trình 'từ đồng ruộng đến bàn ăn': nông hộ nào trồng, ruộng ở đâu, ngày thu hoạch, quy trình kiểm định, ngày nhập kho, ngày xuất kho. Đây là giải pháp trực tiếp cho Pain Point số 1 — minh bạch hóa chuỗi cung ứng."

**Action:** Mở trang public truy xuất → nhập mã lô → hiển thị timeline hành trình

---

### [04:15 – 04:30] — Kết luận (15 giây)
**Màn hình:** Confluence Home Page (quay lại)

**Lời thoại:**
> "SmartFlow đã giải quyết hoàn toàn 4 Pain Points ban đầu. Toàn bộ tài liệu dự án theo PMBOK — từ Project Charter, WBS, PERT, EVM đến thiết kế hệ thống — có tại Confluence Space và GitHub Repo đã được chia sẻ trong email. Xin cảm ơn Thầy/Cô."

---

## Checklist sau khi quay xong

- [ ] Xem lại video: âm thanh rõ, không có vùng tối, text đọc được
- [ ] Cắt bỏ khoảng pause quá dài (nếu có)
- [ ] Thêm intro/outro nhẹ (logo SmartFlow + tên nhóm)
- [ ] Xuất MP4 final ≥ 1080p
- [ ] Upload YouTube:
  - Visibility: **Unlisted** (KHÔNG phải Private)
  - Title: `SmartFlow AgriSCM — Demo Hệ thống | ITS344_252_1_D01`
  - Description: Copy timestamps từ email template
- [ ] Copy link YouTube → điền vào `EMAIL_NOP_BAI_TEMPLATE.md`
- [ ] Copy link YouTube → cập nhật README.md dòng "Video Demo"
- [ ] Copy link YouTube → cập nhật Confluence Home Page dòng Video

---

## Mẹo quay video chuyên nghiệp

1. **Nói chậm hơn bình thường** — giọng đọc video cần chậm hơn 20% so với nói chuyện
2. **Chuẩn bị sẵn dữ liệu** — không tạo dữ liệu live trên camera (dễ lỗi, chậm)
3. **Dùng chuột to** — bật tính năng highlight chuột trong OBS
4. **Không apologize** — nếu nhấn nhầm, tiếp tục bình thường, đừng nói "ôi xin lỗi"
5. **Luyện 1 lần trước** — record thử không cần hoàn hảo, chỉ để biết timing
