# Day 010: Xử lý Thời gian và Tự động hóa (Datetime & Time)

## 🎯 Mục tiêu
Học cách quản lý thời gian trong Python để phục vụ việc ghi Log (nhật ký) và điều khiển tốc độ thực thi của chương trình.

## 🛠 Thực hành
* Sử dụng `datetime.now()` để lấy mốc thời gian thực tế.
* Sử dụng `strftime` để định dạng hiển thị thời gian theo ý muốn.
* Ứng dụng `time.sleep()` để tạo khoảng nghỉ giữa các tác vụ tự động.

### Mã nguồn minh họa:
```python
from datetime import datetime
import time

def he_thong_checkin():
    print("--- 🛡️ NEXUS SECURITY MONITOR ---")
    
    # 1. Lấy thời gian hiện tại
    bay_gio = datetime.now()
    
    # 2. Định dạng thời gian: Ngày/Tháng/Năm Giờ:Phút:Giây
    dinh_dang = bay_gio.strftime("%d/%m/%Y %H:%M:%S")
    
    print(f"🔔 Bắt đầu giám sát hệ thống lúc: {dinh_dang}")
    
    # 3. Giả lập một tiến trình quét hệ thống (delay 3 giây)
    print("🚀 Đang quét các cổng mạng (Port Scanning)...")
    time.sleep(3) 
    
    ket_thuc = datetime.now()
    print(f"✅ Hoàn thành lúc: {ket_thuc.strftime('%H:%M:%S')}")
    print(f"⏱️ Tổng thời gian thực hiện: {(ket_thuc - bay_gio).seconds} giây.")

# Chạy chương trình
he_thong_checkin()
```

### ⚡ Thử thách Day 010 (Kỹ sư hệ thống)
Hãy kết hợp kiến thức Day 009 (JSON) và Day 010 (Time):

1. Viết một hàm khi chạy sẽ yêu cầu nhập "Nội dung công việc".

2. Lưu "Nội dung công việc" kèm theo thời gian chính xác lúc nhập vào một file history_log.json.

3. File JSON phải có cấu trúc dạng danh sách các object để lưu lại lịch sử nhiều ngày.
```python
import json
import os
from datetime import datetime

def ghi_nhat_ky_cong_viec():
    file_name = "history_log.json"
    
    # 1. Nhập nội dung công việc
    noi_dung = input("📝 Nhập nội dung công việc hôm nay: ")
    
    # 2. Lấy thời gian hiện tại và định dạng
    thoi_gian = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # 3. Tạo object dữ liệu mới
    entry_moi = {
        "timestamp": thoi_gian,
        "content": noi_dung
    }
    
    # 4. Logic đọc và cập nhật file JSON
    lich_su = []
    
    # Kiểm tra nếu file tồn tại thì nạp dữ liệu cũ
    if os.path.exists(file_name):
        try:
            with open(file_name, "r", encoding="utf-8") as f:
                lich_su = json.load(f)
        except Exception:
            lich_su = [] # Nếu file lỗi hoặc trống, khởi tạo list rỗng
            
    # Thêm mục mới vào danh sách
    lich_su.append(entry_moi)
    
    # 5. Ghi ngược lại vào file JSON
    try:
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(lich_su, f, indent=4, ensure_ascii=False)
        print(f"✅ Đã lưu vào nhật ký lúc {thoi_gian}!")
    except Exception as e:
        print(f"❌ Lỗi ghi file: {e}")

# Chạy thử thách
if __name__ == "__main__":
    ghi_nhat_ky_cong_viec()
```

### Phân tích kỹ thuật (Dành cho Kỹ sư hệ thống):
1. Cấu trúc dữ liệu: File JSON sẽ lưu dưới dạng một Mảng các Đối tượng (Array of Objects). Điều này cho phép bạn dễ dàng truy vấn hoặc lọc dữ liệu theo thời gian sau này.

Ví dụ cấu trúc file: [{"timestamp": "...", "content": "..."}, {...}].

2. Tính toàn vẹn của dữ liệu: Sử dụng os.path.exists đảm bảo bạn không xóa mất nhật ký của những ngày trước đó khi chạy script vào ngày hôm sau.

3. Định dạng chuẩn: Việc dùng strftime("%d/%m/%Y %H:%M:%S") giúp log của bạn có thể đọc được bởi cả con người và các hệ thống phân tích dữ liệu khác.
