# Day 012: Regex - Tuyệt kỹ trích xuất dữ liệu (Regular Expressions)

## 🎯 Mục tiêu
Học cách sử dụng Biểu thức chính quy (Regex) để lọc và trích xuất các thông tin có quy luật (như Email, Số điện thoại, địa chỉ IP) từ các tập dữ liệu thô và hỗn độn.

---

## 🛠 Các bước thực hiện

### 1. Chuẩn bị môi trường:
* Mở thư mục `Nexus_Test` bằng **VS Code**.
* Tạo một tệp mới tên là: `day_12_regex.py`.

### 2. Viết mã nguồn tổng hợp (Scripting):
Đoạn mã này kết hợp các kỹ thuật nâng cao để trích xuất đồng thời Email và nhiều định dạng số điện thoại khác nhau:

```python
import re

# Dữ liệu mẫu (raw data)
raw_data = """
Cảm ơn bạn đã liên hệ với Nexus System. 
Mọi thắc mắc xin gửi về email: xuyen88@example.com hoặc hỗ trợ kỹ thuật tại tech.support@nexus.org.vn.
Số điện thoại khẩn cấp: 090-123-4567 hoặc 028.1111.2222.
"""

def trich_xuat_tong_hop(text):
    print("--- 🔍 KẾT QUẢ TRÍCH XUẤT TỔNG HỢP ---")
    
    # 1. Pattern Email: Chấp nhận đa dạng ký tự trước dấu @ và đuôi tên miền dài
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    
    # 2. Pattern Số điện thoại nâng cao:
    # \d{2,3}: Chấp nhận mã vùng 2 hoặc 3 số (028 hoặc 090)
    # \d{3,4}: Chấp nhận cụm giữa 3 hoặc 4 số (123 hoặc 1111)
    # [-.]: Chấp nhận dấu gạch ngang hoặc dấu chấm làm ký tự phân cách
    phone_pattern = r'\d{2,3}[-.]\d{3,4}[-.]\d{4}'
    phones = re.findall(phone_pattern, text)
    
    print(f"📧 Danh sách Email: {emails}")
    print(f"📞 Danh sách Số điện thoại: {phones}")

if __name__ == "__main__":
    trich_xuat_tong_hop(raw_data)
```

### ⚡ Thử thách Day 012 (Thợ săn IP)
Trong an ninh mạng, bạn thường xuyên phải lọc địa chỉ IP từ file Log. Hãy tạo `file day_12_challenge.py`:

1. Cho một chuỗi dữ liệu: `"Server 1: 192.168.1.1, Server 2: 10.0.0.255, Database: 172.16.254.1"`.

2. Viết một Pattern Regex để tìm tất cả các địa chỉ IP trong chuỗi đó.

3. Gợi ý: Một địa chỉ IP có định dạng `Số.Số.Số.Số` (Mỗi phần có từ 1-3 chữ số).

   
```python
import re

log_data = "Server 1: 192.168.1.1, Server 2: 10.0.0.255, Database: 172.16.254.1"

def loc_dia_chi_ip(text):
    # Pattern: Tìm 4 cụm số (1-3 chữ số) cách nhau bởi dấu chấm thực sự (\.)
    ip_pattern = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ips = re.findall(ip_pattern, text)
    
    print("--- 🌐 DANH SÁCH IP TRÍCH XUẤT ---")
    for ip in ips:
        print(f"Detected IP: {ip}")

loc_dia_chi_ip(log_data)
```

<img width="1920" height="1140" alt="image" src="https://github.com/user-attachments/assets/c9943b5a-cfb1-4367-a24f-9b1ed3c61f9a" />

