🎯 Mục tiêu bài học
Hiểu lý do Python là ngôn ngữ hàng đầu cho Cyber Security và AI.

Học cách sử dụng thư viện os để điều khiển hệ thống tệp tin.

Viết kịch bản (Script) đầu tiên để tự động tạo cấu trúc dữ liệu hàng loạt.

📖 Lý thuyết cốt lõi
Automation (Tự động hóa): Là việc sử dụng mã code để thay thế các thao tác thủ công lặp đi lặp lại.

Vòng lặp for: Cho phép máy tính thực hiện một hành động nhiều lần với độ chính xác tuyệt đối.

Thư viện os: Thư viện tiêu chuẩn của Python dùng để tương tác với hệ điều hành (Windows, Linux, macOS).

🛠 Hướng dẫn thực hành (A-Z)
Bước 1: Chuẩn bị tệp tin
Mở thư mục dự án Nexus_Test trong VS Code.

Tạo file mới đặt tên là: day_04_automation.py.

Bước 2: Mã nguồn thực thi
Dán đoạn mã sau vào file vừa tạo. Đoạn code này sẽ tự động tạo một thư mục chứa 10 tệp tin bài tập:

Python

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
Bước 3: Chạy chương trình
Mở Terminal và gõ lệnh sau để thực thi:

Bash

python day_04_automation.py
📝 Nhật ký thực hành
Trạng thái: Đã hoàn thành.

Kết quả: Thư mục Python_Labs được tạo với 10 file bài tập bên trong.

Lệnh Git đã dùng:

git add .

git commit -m "Hoàn thành bài tập Day 4: Python Automation"

git push origin master
