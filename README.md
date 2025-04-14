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

# 🩺 Breast Cancer Prediction Pipeline with Metaflow & MLflow

Đây là một pipeline học máy đầy đủ, giúp **dự đoán khả năng ác tính của ung thư vú** dựa trên bộ dữ liệu [Breast Cancer Wisconsin](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data). Dự án sử dụng **Metaflow** để quản lý pipeline và **MLflow** để log mô hình, tham số và đánh giá.

---

## 📌 Tính năng nổi bật

- 🔁 Pipeline đầu-cuối (end-to-end) với **Metaflow**
- 🤖 Huấn luyện và so sánh 3 mô hình: **Random Forest**, **SVM**, và **Logistic Regression**
- 🔍 Tùy chọn **tìm siêu tham số (GridSearchCV)** cho cả 3 mô hình
- 📊 Tự động log mô hình, tham số, kết quả và file với **MLflow**
- 📁 Ghi lại thông tin bộ dữ liệu (CSV, metadata JSON)
- 📉 Tạo và lưu hình ảnh ma trận nhầm lẫn, báo cáo đánh giá dưới dạng JSON

---

## ⚙️ Công nghệ sử dụng

| Công cụ         | Mục đích                                           |
|------------------|-----------------------------------------------------|
| **Metaflow**     | Xây dựng và điều phối pipeline                     |
| **MLflow**       | Theo dõi thực nghiệm, log mô hình và kết quả       |
| **Scikit-learn** | Huấn luyện mô hình và đánh giá                     |
| **Matplotlib, Seaborn** | Vẽ biểu đồ (ma trận nhầm lẫn)             |
| **Pandas / Numpy** | Xử lý và thao tác dữ liệu                        |

---

## 🔬 Mô tả các bước trong Pipeline

### 1. `start`
- Kiểm tra tồn tại và đọc file `breast-cancer.csv`

### 2. `preprocessing`
- Xoá cột dư thừa (`id`, `Unnamed: 32`)
- Chuyển đổi nhãn: `M` → 1 (ác tính), `B` → 0 (lành tính)
- Tách features `X` và label `y`

### 3. `split`
- Tách tập huấn luyện và kiểm tra với `test_size` và `random_state` cấu hình được

### 4. `train_model`
- Khởi tạo thực nghiệm MLflow
- Ghi log các tham số, thông tin bộ dữ liệu (link, version)
- Huấn luyện 3 mô hình:
  - Nếu `hyperparameter_tuning=True`: dùng `GridSearchCV` để tìm siêu tham số tốt nhất
- Lưu mô hình bằng `mlflow.sklearn.log_model`

### 5. `evaluate`
- Dự đoán với từng mô hình và tính các chỉ số:
  - Accuracy, Precision, Recall, F1-score
- Vẽ ma trận nhầm lẫn (confusion matrix)
- Ghi log tất cả kết quả, báo cáo, và hình ảnh lên MLflow

### 6. `end`
- Thông báo kết thúc pipeline

---

## 🧪 Bộ dữ liệu

- Nguồn: [Kaggle - Breast Cancer Wisconsin](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)
- Gồm: 569 mẫu, 30 đặc trưng số, nhãn chẩn đoán là `M` hoặc `B`

---

## 📁 Artifact được log vào MLflow

- Các mô hình đã huấn luyện (Random Forest, SVM, Logistic Regression)
- Các chỉ số đánh giá: Accuracy, Precision, Recall, F1
- Hình ảnh ma trận nhầm lẫn (`confusion_matrices.png`)
- Báo cáo đánh giá dạng JSON (`classification_report_*.json`)
- File CSV dữ liệu gốc và file metadata `dataset_info.json`

---

## 💡 Điểm mới / Sáng tạo

- ✅ So sánh nhiều mô hình trong cùng pipeline
- 🔍 Dễ dàng chuyển đổi giữa chế độ huấn luyện thường và tìm siêu tham số
- 📦 Ghi lại không chỉ mô hình mà cả thông tin bộ dữ liệu để tái lập thực nghiệm
- 📊 Tự động hóa quá trình đánh giá và trực quan hóa
- 🔄 Cấu trúc linh hoạt, dễ tùy chỉnh và mở rộng

---

## 🔧 Chú ý

Tất cả các thư viện Python cần thiết, bao gồm **phiên bản cụ thể**, đã được liệt kê trong file requirements.txt.  
Vui lòng sử dụng môi trường ảo để cài đặt đúng các thư viện này và tránh xung đột với hệ thống.

---

## Hướng dẫn cài đặt và chạy project bằng WSL + VS Code (trên hệ điều hành Windows)

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
- Chạy Ubuntu → Đặt username và password.

---

### 2. Cài đặt môi trường phát triển

#### Bước 6: Cập nhật và cài Python
```bash
sudo apt update
sudo apt upgrade -y
sudo apt install python3 python3-venv -y
```

#### Bước 7: Kết nối Ubuntu (WSL) với VS Code
- Mở VS Code → Nhấn `F1` → Chọn **WSL: Connect to WSL using Distro..** → Chọn **Ubuntu-22.04**

---

### 3. Tải thư mục mã nguồn và tạo môi trường ảo

#### Bước 8: Tải thư mục code từ GitHub
- Bạn có thể **clone repository** bằng cách sử dụng Git:
  ```bash
  git clone https://github.com/NguyenVenToan/CS317.P21---Lab-1.git
  ```
- Hoặc nếu bạn không muốn sử dụng Git, bạn có thể **tải file ZIP** của repository từ GitHub:
  - Truy cập trang GitHub của dự án.
  - Bấm vào nút **Code** (nút màu xanh lá cây).
  - Chọn **Download ZIP** để tải thư mục mã nguồn về máy.

#### Bước 9: Di chuyển vào thư mục mã nguồn đã tải
- Sau khi tải về (hoặc clone), di chuyển vào thư mục dự án:
  ```bash
  cd /mnt/path/to/your/cloned/project
  ```
- Ví dụ:
  ```bash
  cd /mnt/c/Users/toann/Downloads/breast-cancer-metaflow/flow
  ```

#### Bước 10: Tạo môi trường ảo Python
```bash
# Nếu chưa có môi trường ảo
python3 -m venv .venv

# Kích hoạt môi trường ảo
source .venv/bin/activate
```

---

### 4. Cài đặt các thư viện cần thiết và chạy project

#### Bước 11: Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

**Bước 12**: (Tuỳ chọn) Chỉnh sửa đường dẫn trong `mlruns`  
Để đảm bảo MLflow log đúng các artifacts, bạn cần sửa lại đường dẫn trong `mlruns` nếu project đã được copy từ máy khác hoặc chuyển từ Windows sang WSL.

- Vào thư mục:
```bash
cd mlruns/<experiment_id>/
```

- Mở file `meta.yaml` trong thư mục experiment và các run con:
  - Sửa trường `artifact_location` và `artifact_uri` thành đúng đường dẫn thực tế trong hệ thống Ubuntu, ví dụ:
    ```yaml
    artifact_location: file:///home/toan/breast-cancer-metaflow/mlruns/0
    ```
  - Sửa `user_id` thành **username** bạn đã đặt khi cài Ubuntu.

✅ *Việc này rất quan trọng vì nếu không sửa, MLflow sẽ không hiển thị hoặc lưu đúng artifact như mô hình, hình ảnh, checkpoints,...*

#### Bước 13: Chạy pipeline
```bash
python3 breast_cancer_flow.py run
```

#### Bước 14: Xem log bằng MLflow
```bash
mlflow ui
```
- Truy cập: http://127.0.0.1:5000 để xem giao diện MLflow.
- Nếu **port 5000** đã bị chiếm, bạn có thể chỉ định port khác bằng cách thêm `--port`:
  ```bash
  mlflow ui --port 5001
  ```
- Nhấn `Ctrl + C` để thoát.

---

### ✅ Nếu chỉ muốn xem log bằng MLflow (không cần chạy lại pipeline)

#### Bước 1: Kích hoạt môi trường ảo
```bash
# Nếu chưa có môi trường ảo
python3 -m venv .venv

# Kích hoạt môi trường ảo
source .venv/bin/activate
```
```bash
# Nếu chưa có môi trường ảo
pip install -r requirements.txt
```
#### Bước 2: Chỉnh sửa đường dẫn trong `mlruns`(Bắt buộc) 
Để đảm bảo MLflow log đúng các artifacts, bạn cần sửa lại đường dẫn trong `mlruns` nếu project đã được copy từ máy khác hoặc chuyển từ Windows sang WSL.

- Vào thư mục:
```bash
cd mlruns/<experiment_id>/
```

- Mở file `meta.yaml` trong thư mục experiment và các run con:
  - Sửa trường `artifact_location` và `artifact_uri` thành đúng đường dẫn thực tế trong hệ thống Ubuntu, ví dụ:
    ```yaml
    artifact_location: file:///home/toan/breast-cancer-metaflow/mlruns/0
    ```
  - Sửa `user_id` thành **username** bạn đã đặt khi cài Ubuntu.

✅ *Việc này rất quan trọng vì nếu không sửa, MLflow sẽ không hiển thị hoặc lưu đúng artifact như mô hình, hình ảnh, checkpoints,...*

#### Bước 3: Mở giao diện MLflow UI
```bash
mlflow ui
```
- Truy cập: http://127.0.0.1:5000 (hoặc port tùy chỉnh nếu có xung đột) để xem log các lần chạy trước đó.

---
### 📥 Link Dataset Public (Nếu muốn tìm hiểu thêm)

- Dataset **Breast Cancer Wisconsin (Diagnostic)** được sử dụng trong dự án này có thể tải từ Kaggle tại:  
  [Breast Cancer Wisconsin Data](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data)  (version 2)
  
- Tuy nhiên, bạn cũng có thể tìm dataset này đã được bao gồm trong thư mục dự án, không cần phải tải lại từ Kaggle.

---


