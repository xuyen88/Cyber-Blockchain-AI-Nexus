# 1. Tạo một danh sách các học viên (List)
students = ["An", "Bình", "Chi", "Dũng", "Em"]

# 2. Thêm một học viên mới vào cuối danh sách
students.append("Xuyến")

print(f"Số lượng học viên hiện có: {len(students)}")

# 3. Sử dụng vòng lặp For để gửi lời chào tự động
print("\n--- Bắt đầu gửi thông báo ---")

for person in students:
    # Logic: Nếu tên là Xuyến thì in thông báo đặc biệt
    if person == "Xuyến":
        print(f"⭐ Chào trưởng nhóm: {person}!")
    else:
        print(f"📩 Đã gửi tài liệu cho: {person}")

print("\n--- Tất cả thông báo đã được gửi thành công ---")