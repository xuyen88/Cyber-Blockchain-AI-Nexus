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
