# Day 009: Quản lý dữ liệu dự án với JSON

## 🎯 Mục tiêu
Sử dụng định dạng JSON để lưu trữ và quản lý dữ liệu có cấu trúc, cho phép cập nhật dữ liệu mà không làm mất thông tin cũ.

## 🛠 Thực hành
* Học cách kiểm tra sự tồn tại của tệp tin bằng thư viện `os`.
* Thực hiện quy trình: **Đọc file cũ -> Cập nhật dữ liệu -> Ghi đè file mới**.

### Mã nguồn xử lý JSON:
```python
import json

# 1. Tạo dữ liệu cấu hình dưới dạng Dictionary
user_config = {
    "name": "Xuyen",
    "phase": 1,
    "day": 9,
    "status": "Active",
    "skills": ["Python", "Git", "File I/O"]
}

# 2. Ghi dữ liệu vào file JSON
try:
    with open("config.json", "w", encoding="utf-8") as f:
        # indent=4 giúp file JSON dễ đọc hơn (đẹp hơn)
        json.dump(user_config, f, indent=4)
    print("✅ Đã lưu cấu hình vào file config.json thành công.")

    # 3. Đọc dữ liệu từ file JSON
    with open("config.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        print("\n--- Dữ liệu đọc từ file JSON ---")
        print(f"Học viên: {data['name']}")
        print(f"Kỹ năng: {', '.join(data['skills'])}")

except Exception as e:
    print(f"❌ Có lỗi: {e}")
```
### ⚡ Thử thách Day 009
Hãy tạo một file tên là day_09_challenge.py. Viết một chương trình cho phép người dùng nhập Tên dự án và Ngân sách, sau đó lưu thông tin này vào một file projects.json. Nếu file đã tồn tại, hãy đọc dữ liệu cũ ra và cập nhật thêm dự án mới vào. 
```python
import json
import os

def quan_ly_du_an():
    file_name = "projects.json"
    
    # 1. Nhận thông tin từ người dùng
    ten_du_an = input("Nhập tên dự án: ")
    ngan_sach = input("Nhập ngân sách dự án (USD): ")

    # Tạo object dự án mới
    du_an_moi = {
        "ten": ten_du_an,
        "ngan_sach": ngan_sach
    }

    # 2. Xử lý logic cập nhật dữ liệu
    danh_sach_du_an = []

    # Kiểm tra nếu file đã tồn tại thì đọc dữ liệu cũ ra
    if os.path.exists(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                danh_sach_du_an = json.load(f)
        except:
            danh_sach_du_an = []

    # Thêm dự án mới vào danh sách
    danh_sach_du_an.append(du_an_moi)

    # 3. Ghi toàn bộ danh sách đã cập nhật vào lại file
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(danh_sach_du_an, f, indent=4, ensure_ascii=False)
        print(f"✅ Đã lưu dự án '{ten_du_an}' vào hệ thống!")
    except Exception as e:
        print(f"❌ Lỗi khi ghi file: {e}")

# Chạy chương trình
quan_ly_an_toan = True
while quan_ly_an_toan:
    quan_ly_du_an()
    tiep_tuc = input("Bạn có muốn nhập thêm dự án không? (y/n): ")
    if tiep_tuc.lower() != 'y':
        break
