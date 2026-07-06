#!/usr/bin/env python3
"""
SmartFlow Confluence Home Page Updater
Updates the SW Space Home page with a professional landing page layout.
"""

import requests
import json
from requests.auth import HTTPBasicAuth

# ---- Config ----
with open(".env") as f:
    lines = f.read().strip().splitlines()
API_TOKEN = lines[0].strip()
EMAIL = lines[1].strip()
DOMAIN = lines[2].strip()

BASE_URL = f"https://{DOMAIN}/wiki/rest/api"
AUTH = HTTPBasicAuth(EMAIL, API_TOKEN)
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}

HOME_PAGE_ID = "1015985"

# ─────────────────────────────────────────────────────────────
# CONFLUENCE STORAGE FORMAT — HOME PAGE CONTENT
# ─────────────────────────────────────────────────────────────
HOME_CONTENT = """<ac:layout>
  <ac:layout-section ac:type="full_width" ac:breakout-mode="full-width">
    <ac:layout-cell>
      <ac:structured-macro ac:name="panel" ac:schema-version="1">
        <ac:parameter ac:name="bgColor">#0052CC</ac:parameter>
        <ac:parameter ac:name="titleColor">#FFFFFF</ac:parameter>
        <ac:parameter ac:name="borderColor">#0052CC</ac:parameter>
        <ac:rich-text-body>
          <h1 style="color: #FFFFFF; text-align: center;">🌾 SmartFlow — AgriSCM</h1>
          <p style="color: #FFFFFF; text-align: center; font-size: 16px;">Hệ thống Quản lý Chuỗi cung ứng Nông sản | ITS344_252_1_D01 | HK2 – 2025/2026</p>
          <p style="color: #FFFFFF; text-align: center; font-size: 14px;">
            📍 Khu vực: Buôn Triết, Lắk, Đắk Lắk &nbsp;|&nbsp; 🌾 Sản phẩm: Lúa gạo đặc sản ST24, Đài Thơm 8
          </p>
        </ac:rich-text-body>
      </ac:structured-macro>
    </ac:layout-cell>
  </ac:layout-section>
  <ac:layout-section ac:type="four_equal" ac:breakout-mode="default">
    <ac:layout-cell>
      <ac:structured-macro ac:name="panel" ac:schema-version="1">
        <ac:parameter ac:name="bgColor">#E3FCEF</ac:parameter>
        <ac:parameter ac:name="borderColor">#00875A</ac:parameter>
        <ac:rich-text-body>
          <p style="text-align:center; font-size: 24px;">📊</p>
          <p style="text-align:center;"><strong>Jira Board</strong></p>
          <p style="text-align:center;"><a href="https://sangminhnguyen210.atlassian.net/jira/software/projects/SF/boards">SF Board →</a></p>
        </ac:rich-text-body>
      </ac:structured-macro>
    </ac:layout-cell>
    <ac:layout-cell>
      <ac:structured-macro ac:name="panel" ac:schema-version="1">
        <ac:parameter ac:name="bgColor">#EAE6FF</ac:parameter>
        <ac:parameter ac:name="borderColor">#6554C0</ac:parameter>
        <ac:rich-text-body>
          <p style="text-align:center; font-size: 24px;">💻</p>
          <p style="text-align:center;"><strong>GitHub Repo</strong></p>
          <p style="text-align:center;"><a href="https://github.com/">SmartFlow-ITS344 →</a></p>
        </ac:rich-text-body>
      </ac:structured-macro>
    </ac:layout-cell>
    <ac:layout-cell>
      <ac:structured-macro ac:name="panel" ac:schema-version="1">
        <ac:parameter ac:name="bgColor">#FFFAE6</ac:parameter>
        <ac:parameter ac:name="borderColor">#FF991F</ac:parameter>
        <ac:rich-text-body>
          <p style="text-align:center; font-size: 24px;">🎬</p>
          <p style="text-align:center;"><strong>Video Demo</strong></p>
          <p style="text-align:center;"><em>(Sẽ cập nhật 08/07)</em></p>
        </ac:rich-text-body>
      </ac:structured-macro>
    </ac:layout-cell>
    <ac:layout-cell>
      <ac:structured-macro ac:name="panel" ac:schema-version="1">
        <ac:parameter ac:name="bgColor">#FFEBE6</ac:parameter>
        <ac:parameter ac:name="borderColor">#FF5630</ac:parameter>
        <ac:rich-text-body>
          <p style="text-align:center; font-size: 24px;">🚀</p>
          <p style="text-align:center;"><strong>Live Demo</strong></p>
          <p style="text-align:center;"><em>(Deploy 07/07)</em></p>
        </ac:rich-text-body>
      </ac:structured-macro>
    </ac:layout-cell>
  </ac:layout-section>
  <ac:layout-section ac:type="two_equal" ac:breakout-mode="default">
    <ac:layout-cell>
      <h2>📋 Trạng thái Dự án</h2>
      <table data-table-width="760" data-layout="default">
        <tbody>
          <tr>
            <th>Hạng mục</th>
            <th>Trạng thái</th>
            <th>Ghi chú</th>
          </tr>
          <tr>
            <td>📄 Báo cáo DOCX</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Yellow</ac:parameter><ac:parameter ac:name="title">Đang làm</ac:parameter></ac:structured-macro></td>
            <td>Hoàn thành 07/07</td>
          </tr>
          <tr>
            <td>🌐 Confluence Wiki</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">Hoàn thành</ac:parameter></ac:structured-macro></td>
            <td>50+ trang, 8 chương</td>
          </tr>
          <tr>
            <td>📊 Jira Board</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">Hoàn thành</ac:parameter></ac:structured-macro></td>
            <td>9 Epics, 60+ Tasks</td>
          </tr>
          <tr>
            <td>💻 GitHub Repo</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">Hoàn thành</ac:parameter></ac:structured-macro></td>
            <td>README + Docs + Diagrams</td>
          </tr>
          <tr>
            <td>🚀 Live Deploy</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Blue</ac:parameter><ac:parameter ac:name="title">Kế hoạch</ac:parameter></ac:structured-macro></td>
            <td>Railway.app – 07/07</td>
          </tr>
          <tr>
            <td>🎬 Video Demo</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Blue</ac:parameter><ac:parameter ac:name="title">Kế hoạch</ac:parameter></ac:structured-macro></td>
            <td>Quay 08/07 sáng</td>
          </tr>
        </tbody>
      </table>
    </ac:layout-cell>
    <ac:layout-cell>
      <h2>👥 Đội ngũ Dự án</h2>
      <table data-table-width="760" data-layout="default">
        <tbody>
          <tr>
            <th>#</th>
            <th>Thành viên</th>
            <th>Vai trò</th>
            <th>Chương phụ trách</th>
          </tr>
          <tr>
            <td>1</td>
            <td><strong>Nguyễn Trường Sang</strong></td>
            <td>Project Manager / SA</td>
            <td>C1, C2, C4, C8</td>
          </tr>
          <tr>
            <td>2</td>
            <td><strong>Thiên</strong></td>
            <td>Business Analyst / QC</td>
            <td>C2 yêu cầu, C6 TT, C7</td>
          </tr>
          <tr>
            <td>3</td>
            <td><strong>Tống Bình Minh</strong></td>
            <td>UI/UX Designer</td>
            <td>C5, Design</td>
          </tr>
          <tr>
            <td>4</td>
            <td><strong>Nam</strong></td>
            <td>Senior Backend Dev</td>
            <td>C3, Database, API</td>
          </tr>
          <tr>
            <td>5</td>
            <td><strong>Trần Anh Duy</strong></td>
            <td>Backend Dev / DevOps</td>
            <td>C6 rủi ro, Deploy</td>
          </tr>
        </tbody>
      </table>
    </ac:layout-cell>
  </ac:layout-section>
  <ac:layout-section ac:type="full_width" ac:breakout-mode="default">
    <ac:layout-cell>
      <h2>📚 Điều hướng Nội dung Wiki</h2>
      <table data-table-width="1200" data-layout="default">
        <tbody>
          <tr>
            <th>Chương</th>
            <th>Nội dung</th>
            <th>Trang con chính</th>
            <th>Phụ trách</th>
            <th>Trạng thái</th>
          </tr>
          <tr>
            <td><strong>C1</strong></td>
            <td>Tích hợp &amp; Project Charter</td>
            <td>Project Charter, SMART Goals, Stakeholder Register, Power-Interest Grid</td>
            <td>Sang</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">✅ Hoàn thành</ac:parameter></ac:structured-macro></td>
          </tr>
          <tr>
            <td><strong>C2</strong></td>
            <td>Quản lý Phạm vi (Scope)</td>
            <td>FR/NFR, Scope Statement, WBS Mindmap, Work Packages</td>
            <td>Thiên + Sang</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Yellow</ac:parameter><ac:parameter ac:name="title">🔄 Đang làm</ac:parameter></ac:structured-macro></td>
          </tr>
          <tr>
            <td><strong>C3</strong></td>
            <td>Quản lý Thời gian (Schedule)</td>
            <td>15 hoạt động, PERT, CPM, Gantt 16 tuần, EVM</td>
            <td>Nam</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Green</ac:parameter><ac:parameter ac:name="title">✅ Hoàn thành</ac:parameter></ac:structured-macro></td>
          </tr>
          <tr>
            <td><strong>C4</strong></td>
            <td>Quản lý Chi phí (Cost)</td>
            <td>Bottom-up Estimating, PERT Chi phí, Cost Baseline</td>
            <td>Sang</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Yellow</ac:parameter><ac:parameter ac:name="title">🔄 Đang làm</ac:parameter></ac:structured-macro></td>
          </tr>
          <tr>
            <td><strong>C5</strong></td>
            <td>Chất lượng &amp; Nguồn Nhân lực</td>
            <td>QMP, RACI Matrix, Org Chart, Resource Histogram, Tuckman</td>
            <td>Bình Minh</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Yellow</ac:parameter><ac:parameter ac:name="title">🔄 Đang làm</ac:parameter></ac:structured-macro></td>
          </tr>
          <tr>
            <td><strong>C6</strong></td>
            <td>Rủi ro &amp; Truyền thông</td>
            <td>Communications Plan, Risk Register (8 rủi ro), Risk Response</td>
            <td>Thiên + Duy</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Yellow</ac:parameter><ac:parameter ac:name="title">🔄 Đang làm</ac:parameter></ac:structured-macro></td>
          </tr>
          <tr>
            <td><strong>C7</strong></td>
            <td>Mua sắm &amp; Các Bên liên quan</td>
            <td>Make-or-Buy Analysis, Stakeholder Engagement Matrix</td>
            <td>Thiên + Duy</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Yellow</ac:parameter><ac:parameter ac:name="title">🔄 Đang làm</ac:parameter></ac:structured-macro></td>
          </tr>
          <tr>
            <td><strong>C8</strong></td>
            <td>Phân tích &amp; Thiết kế Hệ thống</td>
            <td>BPMN As-Is/To-Be, Use Case, ERD, Architecture, Sequence Diagrams</td>
            <td>Sang + Nam + Bình Minh</td>
            <td><ac:structured-macro ac:name="status"><ac:parameter ac:name="colour">Yellow</ac:parameter><ac:parameter ac:name="title">🔄 Đang làm</ac:parameter></ac:structured-macro></td>
          </tr>
        </tbody>
      </table>
    </ac:layout-cell>
  </ac:layout-section>
  <ac:layout-section ac:type="two_equal" ac:breakout-mode="default">
    <ac:layout-cell>
      <h2>🎯 Mục tiêu SMART Dự án</h2>
      <ac:structured-macro ac:name="panel" ac:schema-version="1">
        <ac:parameter ac:name="bgColor">#EAE6FF</ac:parameter>
        <ac:rich-text-body>
          <ul>
            <li>✅ <strong>S1:</strong> Xây dựng hệ thống web với 5 phân hệ hoàn chỉnh trong 16 tuần</li>
            <li>✅ <strong>S2:</strong> Truy xuất nguồn gốc bằng QR — thời gian tra cứu &lt; 3 giây</li>
            <li>✅ <strong>S3:</strong> Giảm tỷ lệ thất thoát kho xuống còn ≤ 2% (từ 5–8%)</li>
            <li>✅ <strong>S4:</strong> Minh bạch giá cả 100% — nông dân thấy giá thị trường real-time</li>
            <li>✅ <strong>S5:</strong> Chi phí triển khai &lt; 50 triệu VNĐ, vận hành trên server miễn phí</li>
          </ul>
        </ac:rich-text-body>
      </ac:structured-macro>
    </ac:layout-cell>
    <ac:layout-cell>
      <h2>🏗️ Kiến trúc Hệ thống</h2>
      <ac:structured-macro ac:name="panel" ac:schema-version="1">
        <ac:parameter ac:name="bgColor">#E3FCEF</ac:parameter>
        <ac:rich-text-body>
          <p><strong>Tech Stack:</strong></p>
          <ul>
            <li>🔴 <strong>Backend:</strong> PHP Laravel 10.x (MVC Pattern)</li>
            <li>🐬 <strong>Database:</strong> MySQL 8.0</li>
            <li>🎨 <strong>Frontend:</strong> Bootstrap 5 + Vanilla JS</li>
            <li>🔐 <strong>Auth:</strong> Laravel Sanctum</li>
            <li>📦 <strong>QR:</strong> simplesoftwareio/simple-qrcode</li>
            <li>📄 <strong>PDF:</strong> barryvdh/laravel-dompdf</li>
            <li>☁️ <strong>Deploy:</strong> Railway.app</li>
          </ul>
        </ac:rich-text-body>
      </ac:structured-macro>
    </ac:layout-cell>
  </ac:layout-section>
  <ac:layout-section ac:type="full_width" ac:breakout-mode="default">
    <ac:layout-cell>
      <ac:structured-macro ac:name="panel" ac:schema-version="1">
        <ac:parameter ac:name="bgColor">#DEEBFF</ac:parameter>
        <ac:parameter ac:name="borderColor">#0052CC</ac:parameter>
        <ac:rich-text-body>
          <p style="text-align:center;">
            <strong>📅 Deadline nộp bài: Thứ 4, ngày 08/07/2026 lúc 23:59</strong>
          </p>
          <p style="text-align:center;">
            📄 Báo cáo DOCX &nbsp;|&nbsp; 🌐 Confluence (trang này) &nbsp;|&nbsp; 📊 Jira Board &nbsp;|&nbsp; 💻 GitHub &nbsp;|&nbsp; 🚀 Live Demo &nbsp;|&nbsp; 🎬 Video 4 phút
          </p>
        </ac:rich-text-body>
      </ac:structured-macro>
    </ac:layout-cell>
  </ac:layout-section>
</ac:layout>"""

def get_current_version():
    resp = requests.get(f"{BASE_URL}/content/{HOME_PAGE_ID}?expand=version", auth=AUTH, headers=HEADERS)
    return resp.json().get("version", {}).get("number", 1)

def update_home_page():
    current_version = get_current_version()
    print(f"Current version: {current_version}")
    
    payload = {
        "id": HOME_PAGE_ID,
        "type": "page",
        "title": "SmartFlow Wiki — 🌾 AgriSCM Project Hub",
        "version": {"number": current_version + 1},
        "body": {
            "storage": {
                "value": HOME_CONTENT,
                "representation": "storage"
            }
        }
    }
    
    resp = requests.put(
        f"{BASE_URL}/content/{HOME_PAGE_ID}",
        auth=AUTH,
        headers=HEADERS,
        json=payload
    )
    
    if resp.status_code == 200:
        data = resp.json()
        print(f"✅ Home page updated successfully!")
        print(f"   Title: {data.get('title')}")
        print(f"   Version: {data.get('version',{}).get('number')}")
        print(f"   URL: https://{DOMAIN}/wiki{data.get('_links',{}).get('webui','')}")
    else:
        print(f"❌ Failed ({resp.status_code}): {resp.text[:500]}")

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 SmartFlow Confluence Home Page Updater")
    print("=" * 60)
    update_home_page()
