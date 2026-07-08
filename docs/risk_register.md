# Risk Register — SmartFlow AgriSCM

> Nguồn: Chương 6 — Quản lý Rủi ro | Bảng 6.5 | PMBOK 6th Edition §11
> Thang đánh giá: Xác suất (P) × Tác động (I) → Điểm rủi ro (Score)

| Mã | Loại rủi ro | Mô tả | P | I | Score | Mức độ | Chiến lược ứng phó |
|:---:|---|---|:---:|:---:|:---:|:---:|---|
| R-01 | Kỹ thuật | Tích hợp module QR với Camera trình duyệt gặp lỗi tương thích | 0.5 | 0.7 | 0.35 | Cao | Mitigate: Test sớm trên nhiều thiết bị; Fallback sang nhập mã thủ công |
| R-02 | Kỹ thuật | Laravel version mismatch / dependency conflict | 0.3 | 0.5 | 0.15 | Trung bình | Mitigate: Lock version trong composer.json; dùng Docker |
| R-03 | Tiến độ | Thành viên cốt lõi rút khỏi dự án đột xuất | 0.2 | 0.9 | 0.18 | Cao | Mitigate: Backup role; tài liệu hóa toàn bộ; Contingency Reserve sẵn sàng |
| R-04 | Tiến độ | GV không phản hồi đúng hạn tại 4 Checkpoint | 0.3 | 0.5 | 0.15 | Trung bình | Accept: Tự tiến hành theo kế hoạch; ghi lại trong communication log |
| R-05 | Chi phí | Chi phí vượt Contingency Reserve (4.5M) | 0.2 | 0.7 | 0.14 | Trung bình | Mitigate: Kiểm soát EVM hàng tuần; cắt giảm tính năng Nice-to-have |
| R-06 | Bảo mật | Lỗ hổng SQL Injection / XSS trên form nhập liệu | 0.3 | 0.7 | 0.21 | Cao | Mitigate: Dùng Eloquent ORM; escaping; Laravel Validation rules |
| R-07 | Phạm vi | Scope creep sau khi Scope Baseline đã khóa | 0.4 | 0.5 | 0.20 | Trung bình | Avoid: Change Control Process nghiêm ngặt; từ chối yêu cầu ngoài RTM |
| R-08 | Kỹ thuật | Server miễn phí (Railway) bị giới hạn tài nguyên khi demo | 0.5 | 0.5 | 0.25 | Trung bình | Mitigate: Tối ưu query; Dùng DB seeder nhẹ; Upgrade khi cần thiết |
