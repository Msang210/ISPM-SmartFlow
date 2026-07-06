#!/usr/bin/env python3
"""
SmartFlow Jira Populator
Creates Epics + Tasks for the ISPM-SmartFlow project (SF)
reflecting the actual 8-chapter PMBOK report structure.
"""

import requests
import json
import time
from requests.auth import HTTPBasicAuth

# ---- Config ----
with open(".env") as f:
    lines = f.read().strip().splitlines()
API_TOKEN = lines[0].strip()
EMAIL = lines[1].strip()
DOMAIN = lines[2].strip()

BASE_URL = f"https://{DOMAIN}/rest/api/3"
AUTH = HTTPBasicAuth(EMAIL, API_TOKEN)
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}
PROJECT_KEY = "SF"

# Issue type IDs
EPIC_TYPE = "10006"
TASK_TYPE = "10009"
STORY_TYPE = "10010"

created = {"epics": [], "tasks": []}
errors = []

def create_issue(payload):
    resp = requests.post(f"{BASE_URL}/issue", auth=AUTH, headers=HEADERS, json=payload)
    if resp.status_code in (200, 201):
        data = resp.json()
        print(f"  ✅ Created: {data['key']} — {payload['fields'].get('summary','')[:60]}")
        time.sleep(0.3)
        return data["key"], data["id"]
    else:
        print(f"  ❌ FAILED ({resp.status_code}): {resp.text[:200]}")
        errors.append(resp.text)
        return None, None


# ─────────────────────────────────────────────
# DEFINE EPICS AND THEIR CHILD TASKS
# ─────────────────────────────────────────────
EPICS_AND_TASKS = [
    {
        "epic_summary": "C1 — Tích hợp & Project Charter",
        "epic_color": "#0052CC",
        "tasks": [
            ("Viết Project Charter — Bối cảnh & Mục tiêu kinh doanh", "Sang", "Done"),
            ("Xác định Bảng thông tin định danh dự án", "Sang", "Done"),
            ("Phân tích Ràng buộc & Giả định (Constraints & Assumptions)", "Sang", "Done"),
            ("Xây dựng Bảng Mục tiêu SMART (5 mục tiêu đo lường được)", "Sang", "Done"),
            ("Nhận diện 10 Bên liên quan & Vẽ Power-Interest Grid", "Thiên", "Done"),
            ("Lập Kế hoạch Tích hợp & Vòng đời dự án (Predictive)", "Sang", "Done"),
            ("Lập Bảng Công cụ làm việc nhóm (Jira/Confluence/GitHub)", "Sang", "Done"),
        ]
    },
    {
        "epic_summary": "C2 — Quản lý Phạm vi (Scope)",
        "epic_color": "#36B37E",
        "tasks": [
            ("Thu thập yêu cầu: Phân loại FR vs NFR (bảng đầy đủ)", "Thiên", "Done"),
            ("Viết Scope Statement & Product Description (5 phân hệ)", "Thiên", "Done"),
            ("Vẽ Sơ đồ cây WBS (Mermaid Mindmap) — 3 cấp phân rã", "Sang", "Done"),
            ("Viết Quy trình tạo và duy trì WBS (Draw.io)", "Sang", "Done"),
            ("Xây dựng Work Package Dictionary (mô tả 10 gói công việc)", "Thiên", "In Progress"),
            ("Kiểm soát Phạm vi: Change Control Process", "Thiên", "In Progress"),
        ]
    },
    {
        "epic_summary": "C3 — Quản lý Thời gian (Schedule)",
        "epic_color": "#FF991F",
        "tasks": [
            ("Viết Kế hoạch Quản lý Tiến độ (Schedule Management Plan)", "Nam", "Done"),
            ("Lập Danh sách 15 Hoạt động (ID, Tên, Deliverable, Milestone)", "Nam", "Done"),
            ("Lập Bảng Phụ thuộc: FS/SS/FF + Lag time", "Nam", "Done"),
            ("Tính PERT: O/M/P → tE + σ cho 15 hoạt động", "Nam", "Done"),
            ("Vẽ Sơ đồ mạng PDM (Network Diagram)", "Nam", "Done"),
            ("Xác định Đường Tới hạn (Critical Path Method)", "Nam", "Done"),
            ("Điền Bảng ES/EF/LS/LF/TF/FF cho 15 hoạt động", "Nam", "Done"),
            ("Vẽ Biểu đồ Gantt (16 tuần, 15 hoạt động)", "Bình Minh", "Done"),
            ("Tính các chỉ số EVM: PV, EV, AC, SV, CV, SPI, CPI, EAC, VAC", "Nam", "Done"),
            ("Ví dụ minh họa EVM thực tế tại Checkpoint 2", "Nam", "Done"),
        ]
    },
    {
        "epic_summary": "C4 — Quản lý Chi phí (Cost)",
        "epic_color": "#6554C0",
        "tasks": [
            ("Viết Nguyên tắc & Phương pháp ước lượng chi phí (Bottom-up)", "Sang", "Done"),
            ("Lập Bảng Phân loại 4 loại chi phí dự án", "Sang", "Done"),
            ("Bảng Ước lượng Chi phí WP Level (từ WBS)", "Sang", "Done"),
            ("Tính Three-Point Estimating PERT cho Chi phí", "Sang", "Done"),
            ("Xác định Ngưỡng Kiểm soát ±10% Cost Baseline", "Sang", "Done"),
            ("Lập Cost Baseline & S-Curve dự kiến", "Sang", "In Progress"),
        ]
    },
    {
        "epic_summary": "C5 — Quản lý Chất lượng & Nguồn Nhân lực",
        "epic_color": "#00B8D9",
        "tasks": [
            ("Viết Quality Management Plan (QMP)", "Bình Minh", "In Progress"),
            ("Lập Ma trận RACI đầy đủ (9 deliverable × 5 thành viên)", "Bình Minh", "Done"),
            ("Vẽ Org Chart 5 thành viên + sơ đồ vai trò PMBOK", "Bình Minh", "Done"),
            ("Vẽ Resource Histogram (giờ công 5 thành viên × 16 tuần)", "Bình Minh", "Done"),
            ("Phát triển Nhóm: Tuckman 4 giai đoạn + Maslow + Theory Y", "Bình Minh", "Done"),
            ("Kiểm soát Chất lượng: Checklist & QC Metrics", "Bình Minh", "In Progress"),
        ]
    },
    {
        "epic_summary": "C6 — Quản lý Rủi ro & Truyền thông",
        "epic_color": "#FF5630",
        "tasks": [
            ("Viết Communications Management Plan (kênh, tần suất, người nhận)", "Thiên", "Done"),
            ("Viết Quản lý & Kiểm soát Truyền thông", "Thiên", "Done"),
            ("Viết Risk Management Plan (thang P×I: 0.1 → 0.9)", "Duy", "Done"),
            ("Nhận diện & phân tích định tính 8 rủi ro (Risk Register)", "Duy", "In Progress"),
            ("Lập kế hoạch ứng phó rủi ro (Risk Response Strategies)", "Duy", "In Progress"),
            ("Giám sát & Kiểm soát Rủi ro (Risk Monitoring)", "Duy", "To Do"),
        ]
    },
    {
        "epic_summary": "C7 — Quản lý Mua sắm & Các Bên liên quan",
        "epic_color": "#403294",
        "tasks": [
            ("Lập Kế hoạch Mua sắm: Make-or-Buy 6 hạng mục", "Duy", "Done"),
            ("Phân tích quyết định: Không phát sinh chi phí mua sắm", "Duy", "Done"),
            ("Cập nhật Stakeholder Register (vai trò, ảnh hưởng, kỳ vọng)", "Thiên", "Done"),
            ("Xây dựng Stakeholder Engagement Matrix", "Thiên", "In Progress"),
            ("Lập Stakeholder Communication Strategy cho từng nhóm", "Thiên", "To Do"),
        ]
    },
    {
        "epic_summary": "C8 — Phân tích & Thiết kế Hệ thống",
        "epic_color": "#172B4D",
        "tasks": [
            ("Phân tích Quy trình AS-IS (BPMN — chuỗi cung ứng lúa gạo thủ công)", "Sang", "Done"),
            ("Thiết kế Quy trình TO-BE (BPMN — SmartFlow tự động hóa)", "Sang", "Done"),
            ("Vẽ Use Case Diagram Tổng thể (3 actor, 5 phân hệ)", "Bình Minh", "Done"),
            ("Vẽ ERD (Entity Relationship Diagram) — Module Interactions", "Nam", "Done"),
            ("Vẽ Module Architecture Diagram (Laravel MVC)", "Nam", "Done"),
            ("Vẽ Sequence Diagram: Luồng Login (MVC flow)", "Nam", "Done"),
            ("Vẽ Sequence Diagram: Tổng thể hệ thống AgriSCM", "Nam", "Done"),
            ("Thiết kế kiến trúc hệ thống: 3-tier + Tech Stack", "Sang", "Done"),
            ("Đặc tả API endpoints chính (nhập kho, sinh QR, truy xuất)", "Nam", "In Progress"),
            ("Thiết kế Wireframe UI (5 màn hình chính)", "Bình Minh", "In Progress"),
        ]
    },
    {
        "epic_summary": "Triển khai & Nộp bài",
        "epic_color": "#00875A",
        "tasks": [
            ("Tổng hợp & hoàn thiện Báo cáo DOCX chính thức", "Sang", "In Progress"),
            ("Deploy hệ thống lên Railway.app (production)", "Duy + Nam", "To Do"),
            ("Seed dữ liệu mẫu & tạo tài khoản demo (3 role)", "Duy", "To Do"),
            ("Nâng cấp Confluence Home Page — Landing page đẹp", "Sang + Bình Minh", "In Progress"),
            ("Nâng cấp GitHub README.md — Professional với badges & screenshots", "Sang", "In Progress"),
            ("Quay & chỉnh sửa Video Demo 4-5 phút", "Bình Minh + Sang", "To Do"),
            ("Upload video lên YouTube (Unlisted) + thêm Timestamps", "Bình Minh", "To Do"),
            ("Kiểm tra toàn bộ links trước khi nộp", "Sang", "To Do"),
            ("Soạn & gửi Email nộp bài professional", "Sang", "To Do"),
        ]
    },
]

STATUS_MAP = {
    "Done": "Done",
    "In Progress": "In Progress",
    "To Do": "To Do",
}

print("=" * 60)
print("🚀 SmartFlow Jira Populator")
print("=" * 60)

for epic_data in EPICS_AND_TASKS:
    print(f"\n📋 EPIC: {epic_data['epic_summary']}")

    # Create Epic
    epic_payload = {
        "fields": {
            "project": {"key": PROJECT_KEY},
            "summary": epic_data["epic_summary"],
            "issuetype": {"id": EPIC_TYPE},
            "description": {
                "type": "doc",
                "version": 1,
                "content": [{
                    "type": "paragraph",
                    "content": [{"type": "text", "text": f"Epic bao gồm các tasks thuộc {epic_data['epic_summary']} của dự án SmartFlow AgriSCM."}]
                }]
            }
        }
    }
    epic_key, epic_id = create_issue(epic_payload)
    if epic_key:
        created["epics"].append(epic_key)

    # Create Tasks under this Epic
    for task_summary, assignee, status in epic_data["tasks"]:
        task_payload = {
            "fields": {
                "project": {"key": PROJECT_KEY},
                "summary": task_summary,
                "issuetype": {"id": TASK_TYPE},
                "description": {
                    "type": "doc",
                    "version": 1,
                    "content": [{
                        "type": "paragraph",
                        "content": [{"type": "text", "text": f"Người phụ trách: {assignee}. Thuộc epic: {epic_data['epic_summary']}."}]
                    }]
                }
            }
        }
        if epic_key:
            task_payload["fields"]["parent"] = {"key": epic_key}

        task_key, task_id = create_issue(task_payload)
        if task_key:
            created["tasks"].append(task_key)

            # Try to transition to appropriate status
            if status != "To Do":
                # Get available transitions
                trans_resp = requests.get(f"{BASE_URL}/issue/{task_key}/transitions", auth=AUTH, headers=HEADERS)
                if trans_resp.status_code == 200:
                    transitions = trans_resp.json().get("transitions", [])
                    target_name = status
                    for t in transitions:
                        if target_name.lower() in t["name"].lower():
                            requests.post(
                                f"{BASE_URL}/issue/{task_key}/transitions",
                                auth=AUTH, headers=HEADERS,
                                json={"transition": {"id": t["id"]}}
                            )
                            break
                time.sleep(0.2)

print("\n" + "=" * 60)
print("✅ DONE!")
print(f"  Epics created:  {len(created['epics'])}")
print(f"  Tasks created:  {len(created['tasks'])}")
print(f"  Errors:         {len(errors)}")
if errors:
    print("\nErrors:")
    for e in errors:
        print(f"  - {e[:100]}")
print("=" * 60)
