# Cost Estimation — SmartFlow AgriSCM

> Nguồn: Chương 4 — Quản lý Chi phí | Bảng 4.2 | PMBOK 6th Edition §7

## Phương pháp: Bottom-up Estimating từ WBS

| Mã WP | Tên Work Package | Loại chi phí | Ước lượng (VNĐ) | Người P/T |
|:---:|---|---|---:|:---:|
| 1.0 | Quản lý dự án & Lập kế hoạch | Trực tiếp (Man-hour) | 3.500.000 | Sang |
| 2.0 | Phân tích và Thiết kế hệ thống | Trực tiếp (Man-hour) | 5.000.000 | Thiên, B.Minh |
| 3.1 | Setup môi trường (MAMP, Laravel) | Trực tiếp | 1.000.000 | Duy |
| 3.2 | Phát triển Module Kho | Trực tiếp | 10.000.000 | Nam |
| 3.3 | Phát triển Module Đơn hàng | Trực tiếp | 8.000.000 | Nam, Duy |
| 3.4 | Phát triển Module QR Traceability | Trực tiếp + Hữu hình | 6.000.000 | Duy |
| 3.5 | Phát triển Dashboard & UI | Trực tiếp | 3.000.000 | B.Minh |
| 4.0 | Kiểm thử, Triển khai & Tài liệu | Trực tiếp | 4.000.000 | Thiên, Sang |
| **Tổng WP** | | | **40.500.000** | |
| CR | Contingency Reserve (10%) | Dự phòng rủi ro biết trước | 4.500.000 | PM |
| **BAC** | **Budget At Completion** | **Ngân sách cơ sở** | **45.000.000** | PM |

> ⚠️ **Lưu ý:** Management Reserve 5% = 2.250.000 VNĐ **không** nằm trong BAC, thuộc Total Project Budget.

## EVM tại Checkpoint 2 (Tuần 8)

| Chỉ số | Giá trị | Diễn giải |
|:---|---:|---|
| BAC | 45.000.000 VNĐ | Ngân sách phê duyệt toàn dự án |
| PV (Planned Value) | 23.850.000 VNĐ | PV = BAC × 53% (kế hoạch Tuần 8) |
| EV (Earned Value) | 21.600.000 VNĐ | EV = BAC × 48% (thực tế hoàn thành) |
| AC (Actual Cost) | 22.500.000 VNĐ | Chi phí thực tế đã bỏ ra |
| SV (Schedule Variance) | -2.250.000 VNĐ | EV − PV = Chậm tiến độ |
| CV (Cost Variance) | -900.000 VNĐ | EV − AC = Vượt chi phí |
| SPI | 0.91 | EV/PV < 1 → Chậm hơn kế hoạch |
| CPI | 0.96 | EV/AC < 1 → Hiệu suất chi phí thấp hơn |
| EAC | 46.875.000 VNĐ | BAC / CPI = Chi phí hoàn thành dự báo |
| VAC | -1.875.000 VNĐ | BAC − EAC = Nguy cơ vượt ngân sách |
