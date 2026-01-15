# Day 008: Xử lý tệp tin và Ngoại lệ (Files & Exceptions)

## 🎯 Mục tiêu

Học cách tương tác với hệ thống tệp tin (đọc/ghi file) và sử dụng cấu trúc `try-except` để xử lý lỗi thông minh, giúp chương trình không bị dừng đột ngột khi gặp sự cố.

---

## 🛠 Các bước thực hiện (20 phút)

### 1. Chuẩn bị môi trường:
* Mở thư mục `Nexus_Test` bằng **VS Code**.
* Tạo một tệp mới tên là: `day_08_files.py`.

### 2. Viết mã nguồn (Scripting):
Copy và dán đoạn mã sau vào file `day_08_files.py`:

```python
def quan_ly_nhat_ky(ten_file, noi_dung):
    try:
        # Mở file ở chế độ 'a' (append) để ghi thêm vào cuối file
        with open(ten_file, "a", encoding="utf-8") as f:
            f.write(noi_dung + "\n")
        print(f"✅ Đã ghi nội dung vào {ten_file} thành công.")
    
    except Exception as e:
        print(f"❌ Có lỗi xảy ra khi ghi file: {e}")

# 1. Ghi nhật ký học tập
quan_ly_nhat_ky("nexus_log.txt", "Day 008: Đã học cách ghi file và xử lý lỗi.")
quan_ly_nhat_ky("nexus_log.txt", "Trạng thái hệ thống: Hoạt động ổn định.")

# 2. Đọc lại nội dung file vừa ghi
print("\n--- Nội dung file nhật ký hiện tại ---")
try:
    with open("nexus_log.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("⚠️ Lỗi: Không tìm thấy file nhật ký để đọc!")
```

### ⚡ Thử thách nâng cao (Input Validation)
Tạo file day_08_challenge.py để thực hiện hàm tính toán có kiểm tra lỗi nhập liệu:
```python
def tinh_tong_an_toan():
    try:
        so_1 = input("Nhập số thứ nhất: ")
        so_2 = input("Nhập số thứ hai: ")
        
        # Thử chuyển đổi sang số thực
        tong = float(so_1) + float(so_2)
        print(f"✅ Kết quả: {so_1} + {so_2} = {tong}")
        
    except ValueError:
        print("⚠️ Lỗi: Vui lòng chỉ nhập số, không nhập chữ!")

tinh_tong_an_toan()
