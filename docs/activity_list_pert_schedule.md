# Activity List & Milestones — SmartFlow AgriSCM

> Nguồn: Chương 3 — Quản lý Thời gian | Bảng 3.1 | PMBOK 6th Edition §6.3

| Mã HĐ | Tên hoạt động | Thời lượng | Tiền nhiệm | Milestone | Người P/T |
|:---:|---|:---:|:---:|---|:---:|
| A1 | Khởi động & Lập điều lệ dự án (Project Charter) | 1 tuần | — | M1: Project Charter signed (Tuần 1) | PM Sang |
| A2 | Thu thập & Phân tích yêu cầu (Requirements) | 1.5 tuần | A1 | — | BA Thiên |
| A3 | Phân tích hiện trạng & Thiết kế quy trình (BPMN) | 1 tuần | A2 | — | BA Thiên |
| A4 | Thiết kế cơ sở dữ liệu (ERD & Data Dictionary) | 1 tuần | A3 | — | Backend Nam |
| A5 | Thiết kế UI/UX & Wireframe | 1.5 tuần | A3 | — | Designer Bình Minh |
| A6 | Thiết kế kiến trúc hệ thống (System Architecture) | 0.5 tuần | A4 | M2: Architecture approved (Tuần 5) | PM Sang |
| A7 | Phát triển Module Kho & QR Traceability | 3 tuần | A4, A6 | — | Backend Nam + Duy |
| A8 | Phát triển Module Đơn hàng & Nông hộ | 2 tuần | A4, A6 | — | Backend Nam + Duy |
| A9 | Phát triển Dashboard & Báo cáo | 1.5 tuần | A5, A7 | — | Designer Bình Minh |
| A10 | Tích hợp Frontend – Backend | 1 tuần | A7, A8, A9 | M3: Integration complete (Tuần 12) | Cả nhóm |
| A11 | Kiểm thử (Unit Test, Integration Test) | 1.5 tuần | A10 | — | BA Thiên |
| A12 | Sửa lỗi & Tối ưu hóa (Bug Fix & Optimization) | 1 tuần | A11 | — | Backend Nam |
| A13 | Triển khai & Cấu hình server (Deployment) | 0.5 tuần | A12 | M4: Go-live (Tuần 15) | DevOps Duy |
| A14 | Viết tài liệu kỹ thuật & User Manual | 1 tuần | A13 | — | BA Thiên + PM Sang |
| A15 | Nghiệm thu & Nộp báo cáo | 0.5 tuần | A14 | M5: Project Close (Tuần 16) | PM Sang |

## Critical Path

`A1 → A2 → A3 → A4 → A6 → A7 → A10 → A11 → A12 → A13 → A14 → A15`

**Tổng thời lượng đường tới hạn:** ~14.5 tuần  
**Float của các hoạt động không găng:** A5 (2.5 tuần), A9 (1.5 tuần)

## PERT Parameters Summary

| Mã HĐ | O (Lạc quan) | M (Có khả năng) | P (Bi quan) | tE (ngày) | σ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| A1 | 4 | 5 | 8 | 5.3 | 0.67 |
| A2 | 5 | 7 | 12 | 7.5 | 1.17 |
| A3 | 4 | 5 | 9 | 5.5 | 0.83 |
| A4 | 4 | 5 | 8 | 5.3 | 0.67 |
| A5 | 5 | 7 | 12 | 7.5 | 1.17 |
| A6 | 2 | 2.5 | 4 | 2.7 | 0.33 |
| A7 | 10 | 15 | 22 | 15.3 | 2.00 |
| A8 | 8 | 10 | 16 | 10.7 | 1.33 |
| A9 | 6 | 7.5 | 12 | 7.8 | 1.00 |
| A10 | 4 | 5 | 8 | 5.3 | 0.67 |
| A11 | 6 | 7.5 | 12 | 7.8 | 1.00 |
| A12 | 4 | 5 | 9 | 5.5 | 0.83 |
| A13 | 2 | 2.5 | 4 | 2.7 | 0.33 |
| A14 | 4 | 5 | 8 | 5.3 | 0.67 |
| A15 | 2 | 2.5 | 4 | 2.7 | 0.33 |
