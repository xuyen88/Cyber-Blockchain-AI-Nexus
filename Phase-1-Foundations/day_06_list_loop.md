# **Day 006: Làm việc với Danh sách (List) và Vòng lặp (For Loop)**

## **🎯 Mục tiêu**
Học cách quản lý nhiều dữ liệu cùng lúc bằng **List** và sử dụng vòng lặp **For Loop** để xử lý dữ liệu tự động thay vì thao tác thủ công.

---

## **🛠 Các bước thực hiện (15 phút)**

### **1. Chuẩn bị môi trường:**
* Tạo tệp tin thực hành: `day_06_list_loop.py`.

### **2. Viết mã nguồn (Scripting):**
Dưới đây là mã nguồn quản lý danh sách học viên và gửi thông báo tự động:

```python
# 1. Tạo một danh sách các học viên (List)
students = ["An", "Bình", "Chi", "Dũng", "Em"]

# 2. Thêm một học viên mới vào cuối danh sách
students.append("Xuyên")

print(f"Số lượng học viên hiện có: {len(students)}")

# 3. Sử dụng vòng lặp For để duyệt qua danh sách
print("\n--- Bắt đầu gửi thông báo ---")

for person in students:
    # Kiểm tra điều kiện trong vòng lặp
    if person == "Xuyên":
        print(f"⭐ Chào trưởng nhóm: {person}!")
    else:
        print(f"📩 Đã gửi tài liệu cho: {person}")

print("\n--- Tất cả thông báo đã được gửi thành công ---")
