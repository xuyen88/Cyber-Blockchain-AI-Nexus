# Day 013: Quản lý hệ thống với Thư viện OS

## 🎯 Mục tiêu
Sử dụng thư viện `os` để tương tác với hệ điều hành, quản lý tập tin và thư mục tự động.

## 🛠 Thực hành
* `os.getcwd()`: Lấy đường dẫn thư mục hiện tại.
* `os.listdir()`: Liệt kê danh sách file.
* `os.makedirs()`: Tạo thư mục mới một cách an toàn.

### Mã nguồn minh họa:
```python
import os

def kiem_tra_he_thong():
    print("--- 🖥️ THÔNG TIN HỆ THỐNG NEXUS ---")
    
    # 1. Lấy thư mục làm việc hiện tại
    thu_muc_hien_tai = os.getcwd()
    print(f"📍 Bạn đang ở: {thu_muc_hien_tai}")
    
    # 2. Liệt kê toàn bộ file trong thư mục Nexus_Test
    print("\n📂 Danh sách file đang quản lý:")
    danh_sach_file = os.listdir(".")
    for filename in danh_sach_file:
        print(f"  - {filename}")
    
    # 3. Thử tạo một thư mục mới để lưu Backup
    ten_thu_muc = "Nexus_Backup"
    if not os.path.exists(ten_thu_muc):
        os.makedirs(ten_thu_muc)
        print(f"\n✅ Đã tạo thư mục mới: {ten_thu_muc}")
    else:
        print(f"\n⚠️ Thư mục {ten_thu_muc} đã tồn tại.")

# Chạy chương trình
if __name__ == "__main__":
    kiem_tra_he_thong()
```

### ⚡ Thử thách Day 013 (Sắp xếp hệ thống)
Hãy viết một file `day_13_challenge.py` thực hiện nhiệm vụ sau:

1. Liệt kê toàn bộ các file trong thư mục `Nexus_Test`.

2. Sử dụng kiến thức Day 012 (Regex) hoặc hàm `.endswith()` để lọc ra danh sách các file có đuôi `.json`.

3. In ra màn hình: "Tìm thấy [số lượng] file dữ liệu quan trọng (.json)".

```python
import os
import re

def quet_file_du_lieu():
    # 1. Xác định thư mục mục tiêu (dấu "." nghĩa là thư mục hiện tại)
    target_dir = "."
    
    print(f"🔍 Đang quét thư mục: {os.path.abspath(target_dir)}")
    
    # 2. Lấy danh sách toàn bộ file
    all_files = os.listdir(target_dir)
    
    # --- CÁCH 1: Dùng hàm .endswith() (Đơn giản) ---
    json_files_simple = [f for f in all_files if f.endswith(".json")]
    
    # --- CÁCH 2: Dùng Regex (Chuyên nghiệp - học từ Day 012) ---
    # Pattern: \.json$ (Tìm các file kết thúc bằng .json)
    json_pattern = r'.*\.json$'
    json_files_regex = []
    
    for f in all_files:
        if re.match(json_pattern, f):
            json_files_regex.append(f)
    
    # 3. In kết quả
    print(f"\n📂 Danh sách file tìm thấy:")
    for index, name in enumerate(json_files_regex, 1):
        print(f"  {index}. {name}")
    
    print(f"\n📊 Kết luận: Tìm thấy {len(json_files_regex)} file dữ liệu quan trọng (.json)")

if __name__ == "__main__":
    quet_file_du_lieu()
```
### Giải thích kỹ thuật cho Kỹ sư hệ thống:
1. `os.path.abspath(target_dir)`: Hàm này giúp bạn in ra đường dẫn đầy đủ từ ổ đĩa (C:...), rất hữu ích khi bạn cần kiểm tra chính xác vị trí mình đang thao tác.

2. `re.match(json_pattern, f)`:

    `.*`: Nghĩa là bất kỳ ký tự nào, lặp lại bao nhiêu lần cũng được.

    `\.json`: Tìm đúng cụm chữ `.json`.

    `$`: Ký hiệu neo (anchor) trong Regex, bắt buộc chuỗi phải kết thúc tại đó. Điều này giúp tránh trường hợp file tên là `test.json.txt` bị nhận nhầm.

3. `enumerate(..., 1)`: Một mẹo nhỏ để đánh số thứ tự danh sách bắt đầu từ số 1 khi in ra màn hình.
   
<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/88e38482-b7c6-4742-a50e-386c24c1484b" />
