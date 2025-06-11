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

## 📑 Mục lục

- [📌 Tính năng nổi bật](#-tính-năng-nổi-bật)
- [⚙️ Công nghệ sử dụng](#️-công-nghệ-sử-dụng)
- [🔬 Mô tả các bước trong Pipeline](#-mô-tả-các-bước-trong-pipeline)
- [🧪 Bộ dữ liệu](#-bộ-dữ-liệu)
- [📁 Artifact được log vào MLflow](#-artifact-được-log-vào-mlflow)
- [💡 Điểm mới / Sáng tạo](#-điểm-mới--sáng-tạo)
- [🔧 Chú ý](#-chú-ý)
- [Hướng dẫn cài đặt và chạy project bằng WSL + VS Code](#hướng-dẫn-cài-đặt-và-chạy-project-bằng-wsl--vs-code-trên-hệ-điều-hành-windows)
  - [1. Cài đặt các công cụ cần thiết](#1-cài-đặt-các-công-cụ-cần-thiết)
  - [2. Cài đặt môi trường phát triển](#2-cài-đặt-môi-trường-phát-triển)
  - [3. Tải thư mục mã nguồn và tạo môi trường ảo](#3-tải-thư-mục-mã-nguồn-và-tạo-môi-trường-ảo)
  - [4. Cài đặt các thư viện cần thiết và chạy project](#4-cài-đặt-các-thư-viện-cần-thiết-và-chạy-project)
  - [✅ Nếu chỉ muốn xem log bằng MLflow](#-nếu-chỉ-muốn-xem-log-bằng-mlflow-không-cần-chạy-lại-pipeline)
- [🎥 Video demo training pipeline](#-video-demo)
- [Hướng dẫn cài đặt môi trường và cách chạy code API](#hướng-dẫn-cài-đặt-môi-trường-và-cách-chạy-code)
  - [1. Yêu cầu chung](#1-yêu-cầu-chung)
  - [2. Cài đặt và chạy trên máy(local)](#2-cài-đặt-và-chạy)
    - [Trường hợp 1: Dùng image có sẵn từ DockerHub](#-trường-hợp-1-dùng-image-có-sẵn-từ-dockerhub-nhanh-gọn)
    - [Trường hợp 2: Muốn tự build lại image từ mã nguồn](#-trường-hợp-2-muốn-tự-build-lại-image-từ-mã-nguồn)
  - [3. Cách chạy trên server được cấp](#3-cách-chạy-trên-server-được-cấp)
  - [4. Lưu ý](#4-lưu-ý)
- [🎥 Video demo API](#-video-demo-1)
- [📊 Monitoring & Logging Setup Guide](#-monitoring--logging-setup-guide)
  - [📁 Chuẩn bị thư mục](#-chuẩn-bị-thư-mục)
  - [🖥️ Cài đặt & chạy trên máy local](#-cài-đặt--chạy-trên-máy-local)
    - [🔹 Trường hợp 1: Dùng image có sẵn từ DockerHub *(Nhanh gọn)*](#-trường-hợp-1-dùng-image-có-sẵn-từ-dockerhub-nhanh-gọn)
    - [🔹 Trường hợp 2: Tự build image từ mã nguồn](#-trường-hợp-2-tự-build-image-từ-mã-nguồn)
    - [🔍 Kiểm tra API](#-kiểm-tra-api)
  - [🌐 Cách cài đặt trên server](#-cách-cài-đặt-trên-server)
  - [📈 Truy cập Grafana để xem Monitoring & Logging](#-truy-cập-grafana-để-xem-monitoring--logging)
  - [⚙️ Cấu hình Grafana](#-cấu-hình-grafana)
    - [🔹 Dashboard 1 - Tài nguyên hệ thống](#-dashboard-1---tài-nguyên-hệ-thống)
    - [🔹 Dashboard 2 - Ứng dụng ML](#-dashboard-2---ứng-dụng-ml)
  - [📜 Xem log với Loki](#-xem-log-với-loki)
  - [🎥 Video demo](#-video-demo-2)

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

- Nguồn: [Kaggle - Breast Cancer Wisconsin](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) (version 2)
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

## 🎥 Video demo

🎬 **Video ngắn demo cách chạy training pipeline:**  
[👉 Xem tại đây trên YouTube](https://youtu.be/2eHGDafKRcA)

Nội dung video bao gồm:

- Cách chạy pipeline 
- Quá trình tự động hóa pipeline với **Metaflow**
- **Tracking đầy đủ** trên MLflow:  
  - File log  
  - Siêu tham số (hyperparameters)  
  - Các mô hình (checkpoints)  
  - Hình ảnh đánh giá (confusion matrix)  
  - Báo cáo đánh giá (classification report)
- Trình bày giao diện trực quan của **MLflow UI**

---

## Hướng dẫn cài đặt môi trường và cách chạy code

### 1. Yêu cầu chung

* Python 3.10 (hoặc tương thích)
* Docker (phiên bản >= 20.x)
* Docker Compose (phiên bản >= 1.29.x)
* Tải đầy đủ 5 file trong thư mục deploy_api về máy, bao gồm: Dockerfile, docker-compose.yml, main.py, model_rf.pkl, requirements.txt

### 2. Cài đặt và chạy trên máy(local)

#### 🔹 Trường hợp 1: **Dùng image có sẵn từ DockerHub** (Nhanh gọn)

Không cần build lại image, chỉ cần chạy:

```bash
docker compose up
```

> 📝 Mặc định `docker-compose.yml` đã sử dụng image được push sẵn lên DockerHub (`<your-dockerhub-username>/<your-image-name>`).

---

#### 🔹 Trường hợp 2: **Muốn tự build lại image từ mã nguồn**

1. **Chỉnh sửa `docker-compose.yml`:**

   * Tìm dòng:

     ```yaml
     image: <your-dockerhub-username>/<your-image-name>
     ```
   * **Bỏ dòng này hoặc thay bằng tên image bạn muốn build**, ví dụ:

     ```yaml
     image: my-fastapi-app:latest
     ```

2. **Chạy lệnh build và khởi động ứng dụng:**

   ```bash
   docker compose up --build
   ```

> ⚠️ Nếu không sửa `image:` trong `docker-compose.yml`, Docker sẽ dùng image từ DockerHub thay vì build mới từ Dockerfile.

---
* Mở trình duyệt truy cập [http://localhost:8000/docs](http://localhost:8000/docs) để test API.

🛑 **Để thoát ứng dụng**, nhấn `Ctrl + C` trong terminal.

---

### 3. Cách chạy trên server được cấp
#### ✅ Bước 1: SSH vào server

```bash
ssh <your-username>@<server-ip>
```

---

#### ✅ Bước 2: Cài đặt Docker và Docker Compose trên server (chỉ 1 lần)

```bash
sudo apt-get update
sudo apt-get install ca-certificates curl

# Thêm key Docker GPG
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Thêm Docker repo vào sources
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "${UBUNTU_CODENAME:-$VERSION_CODENAME}") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Cài Docker và Docker Compose
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

---
#### ✅ Bước 3: Kéo image và chạy container

```bash
mkdir breast_cancer_api
cd breast_cancer_api
```

Tạo file `docker-compose.yml` với nội dung:

```yaml
version: "3.8"

services:
  api:
    image: toannguyenuit/breast_cancer_api:1.0
    ports:
      - "8000:8000"
```

Kéo image từ Docker Hub về:

```bash
docker pull toannguyenuit/breast_cancer_api:1.0
```

Chạy container:

```bash
docker compose up -d
```

Truy cập API qua:

```
http://<IP_SERVER>:8000/docs
```

---

### 4. Lưu ý

* Luôn khai báo rõ phiên bản thư viện trong `requirements.txt` để tránh lỗi do cập nhật thư viện.
* Khi cập nhật code, cần build lại image và push lên Docker Hub trước khi deploy trên server.

---
## 🎥 Video demo

🎬 **Video ngắn demo cách chạy local và trên server:**  
[👉 Xem tại đây trên YouTube](https://youtu.be/3znsc5hFSr4)

Nội dung video bao gồm:

**Trên local:**

- Chạy container từ image vừa build
- Test API trên [http://localhost:8000/docs] và xác nhận phản hồi thành công
- Push image đã bbuild lên Docker Hub
---

**Trên server:**

- SSH vào server được cấp
- Cài đặt Docker và Docker Compose
- Pull image từ Docker Hub (hoặc copy từ local lên server)
- Cấu hình Docker Compose để chạy API
- Khởi động container bằng `docker-compose`
-  Test API trên [http://localhost:8000/docs] và xác nhận phản hồi thành công
---
# 📊 Monitoring & Logging Setup Guide

## 📁 Chuẩn bị thư mục

1. **Tải folder** `Monitoring_and_Logging` cùng toàn bộ nội dung bên trong.
2. Tải file `grafana_dashboard_model.json` và đặt vào cùng thư mục `Monitoring_and_Logging`.
3. Di chuyển vào thư mục `Monitoring_and_Logging/monitoring` và tạo thư mục `loki-storage` như sau:

```bash
mkdir -p monitoring/loki-storage/{cache,chunks,compactor,index,wal}
```

---

## 🖥️ Cài đặt & chạy trên máy local

### 🔹 Trường hợp 1: Dùng image có sẵn từ DockerHub *(Nhanh gọn)*

Không cần build lại image, chỉ cần chạy:

```bash
docker compose up
```

📝 *Mặc định `docker-compose.yml` đã sử dụng image có sẵn từ DockerHub:*

```yaml
image: <your-dockerhub-username>/<your-image-name>
```

---

### 🔹 Trường hợp 2: Tự build image từ mã nguồn

1. Mở file `docker-compose.yml`
2. Tìm dòng:

```yaml
image: <your-dockerhub-username>/<your-image-name>
```

3. **Xóa dòng này** hoặc thay bằng tên image tùy chọn, ví dụ:

```yaml
image: my-fastapi-app:latest
```

4. Chạy lệnh sau để build và khởi động:

```bash
docker compose up --build
```

⚠️ *Nếu không chỉnh sửa `image:` thì Docker sẽ tiếp tục dùng image từ DockerHub.*

---

### 🔍 Kiểm tra API

Mở trình duyệt truy cập:  
👉 [http://localhost:5050/docs](http://localhost:5050/docs)

🛑 Để dừng ứng dụng:  
Nhấn `Ctrl + C` trong terminal

---

## 🌐 Cách cài đặt trên server

1. SSH vào server:

```bash
ssh mlops@<ip_server>
```

2. Trên máy cá nhân, dùng `scp` để upload toàn bộ thư mục:

```bash
scp -r "C:\Users\toann\OneDrive\Documents\MLops" mlops@192.168.28.35:/home/mlops/
```

3. Trên server:

```bash
cd /home/mlops/Monitoring_and_Logging
```

4. Cấp quyền cho thư mục `loki-storage`:

```bash
sudo chmod 755 ./monitoring/loki-storage
sudo chmod -R o+rx ./monitoring/loki-storage
```

🔁 *Hoặc (không khuyến nghị do kém an toàn):*

```bash
sudo chmod -R 777 ./monitoring/loki-storage
```

5. Build và chạy dịch vụ:

```bash
docker compose up --build -d
```

6. Truy cập API:

👉 [http://<ip_server>:5050/docs](http://<ip_server>:5050/docs)

---

## 📈 Truy cập Grafana để xem Monitoring & Logging

1. Mở trình duyệt:
   - Local: [http://localhost:3000](http://localhost:3000)
   - Server: [http://<ip_server>:3000](http://<ip_server>:3000)

2. Đăng nhập:
   - **Username:** `admin`
   - **Password:** `admin` (sẽ yêu cầu đổi mật khẩu sau lần đăng nhập đầu tiên)

---

## ⚙️ Cấu hình Grafana

1. **Thêm Data Source**
   - Vào `Connections` → `Data Sources` → `Add data source`
   - **Chọn Prometheus:**
     - Name: `prometheus`
     - URL: `http://prometheus:9090`
     - Save & Test
   - **Chọn Loki:**
     - Name: `loki`
     - URL: `http://loki:3000`
     - Save & Test

---

2. **Thêm Dashboards**

🔹 **Dashboard 1 - Tài nguyên hệ thống:**

- Vào `Dashboards` → `New` → `Import`
- Nhập ID: `1860` → Load → Load

📊 *Hiển thị: CPU usage, RAM usage, Disk space, disk IO, Network IO (Tx/Rx)*

🔹 **Dashboard 2 - Ứng dụng ML:**

- Vào `Dashboards` → `New` → `Import`
- Upload file: `grafana_dashboard_model.json` → Load

📊 *Hiển thị: Request per second, Error rate, Latency, Inference speed, Confidence score*

---

## 📜 Xem log với Loki

1. Vào một dashboard → `Add visualization`
2. Chọn **Data source:** `loki`
3. Phần `Queries` nhập một trong các dòng sau để lọc log:

```
# 1. App logs
{job="app_logfile"}

# 2. Docker stdout/stderr
{job="docker_stdout"}

# 3. Chỉ stdout
{job="docker_stdout", stream="stdout"}

# 4. Chỉ stderr
{job="docker_stdout", stream="stderr"}

# 5. Syslog
{job="syslog"}
```

Bạn có thể tùy chỉnh và lưu lại visualization theo nhu cầu.

---
## 🎥 Video demo

🎬 Video ngắn demo cách chạy trên server:  
[👉 Xem tại đây trên YouTube](https://youtu.be/lLwDTwuR3FQ)

**Nội dung video bao gồm:**

### 📡 Trên server:
- Build image
- Dashboard đã xây dựng, bao gồm các thông số trong phần yêu cầu
- Chạy script giả lập traffic request vào API, sau đó dashboard thay đổi
- Logging capture log từ API, system log
- Giả lập trường hợp API lỗi, show error log capture được và error rate trong dashboard có thay đổi
