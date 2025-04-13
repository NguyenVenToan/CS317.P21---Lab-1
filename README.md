<p align="center">
  <a href="https://www.uit.edu.vn/" title="Trường Đại học Công nghệ Thông tin" style="border: 5;">
    <img src="https://i.imgur.com/WmMnSRt.png" alt="Trường Đại học Công nghệ Thông tin | University of Information Technology">
  </a>
</p>

<!-- Title -->
<h1 align="center"><b>CS317.P21 - PHÁT TRIỂN VÀ VẬN HÀNH HỆ THỐNG MÁY HỌC</b></h1>

## GIỚI THIỆU MÔN HỌC
<a name="gioithieumonhoc"></a>
* *Tên môn học*: Phát triển và vận hành hệ thống máy học
* *Mã môn học*: CS317.P21
* *Ngày bắt đầu*: 17/02/2025
* *Năm học*: 2024-2025

## GIẢNG VIÊN HƯỚNG DẪN
<a name="giangvien"></a>
* *Đỗ Văn Tiến* - tiendv@uit.edu.vn
* *Lê Trần Trọng Khiêm* - khiemltt@uit.edu.vn

## THÀNH VIÊN NHÓM
<a name="thanhvien"></a>
* Nguyễn Vẹn Toàn - 22521492
* Đào Văn Tuân - 22521599
* Vũ Anh Tuấn - 22521614 

---

## Hướng dẫn cài đặt và chạy project bằng WSL + VS Code
Dưới đây là phiên bản hoàn chỉnh, đã thêm phần hướng dẫn **nếu chỉ muốn xem log bằng MLflow UI**:

### 1. Cài đặt các công cụ cần thiết

#### Bước 1: Cài đặt Visual Studio Code (VS Code)
- Tải VS Code tại: https://code.visualstudio.com/

#### Bước 2: Cài đặt WSL (Windows Subsystem for Linux)
- Mở **Command Prompt** với quyền **Administrator**, sau đó chạy:
  ```bash
  wsl --install
  ```
- Khởi động lại máy sau khi cài đặt nếu được yêu cầu.

#### Bước 3: Cài đặt Ubuntu từ Microsoft Store
- Mở Microsoft Store, tìm và cài **Ubuntu 22.04.5 LTS**.

#### Bước 4: Cài đặt Extension WSL trong VS Code
- Mở VS Code → Extensions (Ctrl+Shift+X)
- Tìm `WSL` (biểu tượng chim cánh cụt) và cài đặt extension do **Microsoft phát triển**.

#### Bước 5: Khởi động Ubuntu lần đầu
- Chạy Ubuntu → Đặt username và password theo hướng dẫn.

---

### 2. Cài đặt môi trường phát triển

#### Bước 6: Cập nhật và cài Python
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-venv -y
```

#### Bước 7: Kết nối Ubuntu (WSL) với VS Code
- Mở VS Code → Nhấn `F1` → Chọn **WSL: Connect to Ubuntu**

#### Bước 8: Tạo môi trường ảo Python
```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

### 3. Chạy project từ đầu đến cuối

#### Bước 9: Di chuyển đến thư mục chứa mã nguồn
```bash
cd /mnt/c/Users/toann/Downloads/breast-cancer-metaflow/flow
```

#### Bước 10: Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

#### Bước 11: Chạy pipeline
```bash
python3 breast_cancer_flow.py run
```

#### Bước 12: Xem log bằng MLflow
```bash
mlflow ui
```
- Truy cập: http://127.0.0.1:5000 để xem giao diện MLflow.
- Nhấn `Ctrl + C` để thoát.

---

### ✅ Nếu chỉ muốn xem log bằng MLflow (không cần chạy lại pipeline)

#### Bước 1: Kích hoạt môi trường ảo
```bash
source .venv/bin/activate
```

#### Bước 2: Mở giao diện MLflow UI
```bash
mlflow ui
```
- Truy cập: http://127.0.0.1:5000 để xem log các lần chạy trước đó.

---

