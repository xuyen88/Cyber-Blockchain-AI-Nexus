# Day 004: Tự động hóa với Python (Python Automation)

## 🎯 Mục tiêu
Sử dụng ngôn ngữ **Python** để tự động tạo cấu trúc thư mục và tệp tin hàng loạt thay vì làm thủ công. Điều này giúp tiết kiệm thời gian và giảm thiểu sai sót khi quản lý dữ liệu lớn.

---

## 🛠 Các bước thực hiện (15 phút)

### 1. Chuẩn bị môi trường:
* Mở thư mục `Nexus_Test` bằng **VS Code**.
* Tạo một tệp mới tên là: `day_04_automation.py`.

### 2. Viết mã nguồn (Scripting):
Copy và dán toàn bộ đoạn mã sau vào file `day_04_automation.py` vừa tạo:

```python
import os

# Tạo thư mục chứa bài tập
folder = "Python_Labs"
if not os.path.exists(folder):
    os.makedirs(folder)
    print(f"--- Đã tạo thư mục: {folder} ---")

# Tự động tạo 10 file bài tập trong 1 giây
for i in range(1, 11):
    file_path = f"{folder}/lab_exercise_{i}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Bài thực hành số {i}\n")
        f.write("Hoàn thành bởi Python Automation!")
    print(f"Đã tạo: {file_path}")

print("\n--- Chúc mừng! Bạn đã hoàn thành bài thực hành Day 04 ---")```


<img width="883" height="630" alt="day004" src="https://github.com/user-attachments/assets/2b24e262-ea49-4779-8fc1-0ad72d5bdeca" />

