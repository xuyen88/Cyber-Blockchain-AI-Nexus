import os

# 1. Khai báo tên thư mục
folder_name = "Python_Labs"

# 2. Tạo thư mục nếu nó chưa tồn tại
if not os.path.exists(folder_name):
    os.makedirs(folder_name)
    print(f"--- Đã tạo thư mục: {folder_name} ---")

# 3. Vòng lặp tạo 10 file .txt đánh số từ 1 đến 10
for i in range(1, 11):
    file_name = f"lab_exercise_{i}.txt"
    file_path = os.path.join(folder_name, file_name)
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Bài thực hành số {i}\n")
        f.write("Được tạo tự động bởi kịch bản Python Day 04.")
    
    print(f"Đã tạo: {file_name}")

print("\n--- Hoàn tất thử thách Day 04 ---")
