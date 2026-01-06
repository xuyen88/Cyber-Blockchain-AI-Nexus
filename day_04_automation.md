import os

# 1. Khai báo tên thư mục cần tạo
folder_name = "Python_Labs"

# 2. Kiểm tra: Nếu thư mục chưa tồn tại thì tiến hành tạo mới
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"--- Đã tạo thư mục: {folder_name} ---")

# 3. Sử dụng vòng lặp để tạo ra 10 file bài tập tự động
# range(1, 11) sẽ chạy từ số 1 đến số 10
for i in range(1, 11):
    file_name = f"lab_exercise_{i}.txt"
    file_path = os.path.join(folder_name, file_name)
    
    # Mở file và ghi nội dung vào bên trong
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Ngày học số 4: Thực hành Python Automation.\n")
        f.write(f"Đây là tệp tin thứ {i} được tạo ra hoàn toàn tự động.")
    
    print(f"Đã tạo thành công: {file_name}")

print("\n--- Chúc mừng! Bạn đã hoàn thành bài thực hành Day 04 ---")
