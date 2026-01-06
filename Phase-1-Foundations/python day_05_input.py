# **Day 005: Xử lý dữ liệu nhập từ người dùng (User Input & Logic)**

## **🎯 Mục tiêu**
Học cách tương tác với người dùng thông qua hàm `input()`, xử lý kiểu dữ liệu và sử dụng cấu trúc điều kiện `if-else` để đưa ra phản hồi thông minh.

---

## **🛠 Các bước thực hiện (15 phút)**

### **1. Chuẩn bị môi trường:**
* Mở thư mục `Nexus_Test` bằng **VS Code**.
* Tạo một tệp mới tên là: `day_05_input.py`.

### **2. Viết mã nguồn (Scripting):**
Copy và dán đoạn mã sau vào file `day_05_input.py`:

```python
# Nhận dữ liệu từ bàn phím
name = input("Nhập tên của bạn: ")
age_str = input("Nhập tuổi của bạn: ")

# Chuyển đổi dữ liệu từ chữ sang số (Integer)
age = int(age_str)

print(f"\nChào {name}!")

# Kiểm tra điều kiện logic
if age >= 18:
    print("✅ Bạn đã đủ tuổi truy cập hệ thống nâng cao.")
else:
    print(f"⚠️ Bạn cần thêm {18 - age} năm nữa để đủ tuổi.")

print("\n--- Hoàn thành bài thực hành Day 05 ---")
