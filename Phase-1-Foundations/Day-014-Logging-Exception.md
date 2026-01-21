# Day 014: Xử lý biệt lệ nâng cao và Ghi nhật ký (Logging)

## 🎯 Mục tiêu
Chuyển đổi từ việc hiển thị lỗi ra màn hình sang việc ghi lại lỗi vào file hệ thống một cách chuyên nghiệp.

## 🛠 Thực hành
* Sử dụng `try - except - finally` để kiểm soát luồng lỗi.
* Cấu hình thư viện `logging` để ghi log ra file `system_monitor.log`.
* Phân cấp mức độ lỗi: `INFO`, `WARNING`, `ERROR`, `CRITICAL`.

### Mã nguồn minh họa:
```python
import logging
from datetime import datetime

# 1. Cấu hình hệ thống Logging
logging.basicConfig(
    filename='system_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def thuc_thi_tac_vu_nguy_hiem():
    logging.info("🚀 Bắt đầu tiến trình kiểm tra hệ thống.")
    
    try:
        # Giả lập một lỗi chia cho 0 hoặc truy cập file không tồn tại
        print("Đang tính toán dữ liệu...")
        ket_qua = 10 / 0 
        
    except ZeroDivisionError as e:
        logging.error(f"❌ Lỗi toán học: {e}")
        print("Có lỗi xảy ra, vui lòng kiểm tra file log.")
        
    except Exception as e:
        logging.critical(f"🚨 Lỗi nghiêm trọng không xác định: {e}")
        
    finally:
        # Khối này luôn chạy dù có lỗi hay không
        logging.info("🏁 Kết thúc tiến trình (Cleanup).")
        print("Tiến trình đã đóng an toàn.")

# Chạy chương trình
if __name__ == "__main__":
    thuc_thi_tac_vu_nguy_hiem()
```
### ⚡ Thử thách Day 014 (Giám sát tệp tin)
Hãy kết hợp kiến thức Day 013 (OS) và Day 014 (Logging):

1. Viết một script yêu cầu người dùng nhập tên một file.

2. Sử dụng os.path.exists() để kiểm tra file đó có trong thư mục Nexus_Test không.

3. Nếu có: Ghi vào file log: INFO: File [tên file] đã được tìm thấy.

4. Nếu không: Ghi vào file log: WARNING: Truy cập thất bại! File [tên file] không tồn tại.

5. Đảm bảo file log của bạn lưu lại được lịch sử của tất cả các lần chạy trước đó.

```python
import os
import logging

# 1. Cấu hình Logging (Ghi vào file access_monitor.log)
logging.basicConfig(
    filename='access_monitor.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    encoding='utf-8'
)

def kiem_tra_truy_cap_file():
    print("--- 🛡️ NEXUS FILE MONITOR ---")
    file_name = input("🔍 Nhập tên file cần kiểm tra: ")
    
    # 2. Logic kiểm tra và ghi log
    try:
        if os.path.exists(file_name):
            # Nếu tìm thấy file
            thong_bao = f"File [{file_name}] đã được tìm thấy tại hệ thống."
            logging.info(thong_bao)
            print(f"✅ Thành công: {thong_bao}")
        else:
            # Nếu không tìm thấy file
            canh_bao = f"Truy cập thất bại! File [{file_name}] không tồn tại."
            logging.warning(canh_bao)
            print(f"⚠️ Cảnh báo: {canh_bao}")
            
    except Exception as e:
        # Xử lý các lỗi phát sinh khác (ví dụ: lỗi quyền truy cập)
        logging.error(f"🚨 Lỗi hệ thống khi kiểm tra file: {e}")
        print("Đã xảy ra lỗi kỹ thuật. Vui lòng kiểm tra log.")

if __name__ == "__main__":
    # Chạy thử vài lần để tạo lịch sử trong file log
    while True:
        kiem_tra_truy_cap_file()
        tiep_tuc = input("\nBạn có muốn kiểm tra file khác không? (y/n): ")
        if tiep_tuc.lower() != 'y':
            print("Đang đóng hệ thống giám sát...")
            break
```

### Phân tích kỹ thuật (Dành cho Kỹ sư bảo mật):
1. Chế độ Append: Thư viện `logging` mặc định sẽ ghi tiếp (append) vào cuối file thay vì ghi đè. Điều này cực kỳ quan trọng để giữ lại bằng chứng (Forensics) nếu có sự cố xảy ra.

2. `encoding='utf-8'`: Đảm bảo nhật ký ghi tiếng Việt không bị lỗi font khi bạn mở bằng Notepad hoặc VS Code.

3. Mức độ nghiêm trọng (Level):

      INFO: Dùng cho các sự kiện bình thường (người dùng tìm thấy file).

      WARNING: Dùng cho các sự việc bất thường nhưng chưa làm sập hệ thống (người dùng nhập sai tên file).

      ERROR: Dùng cho các lỗi mã nguồn hoặc lỗi hệ điều hành.
