# Day 011: Kết nối Internet và Thư viện Requests

## 🎯 Mục tiêu
Học cách sử dụng thư viện bên thứ ba để tương tác với các ứng dụng Web thông qua API.

## 🛠 Thực hành
* Cài đặt thư viện bằng lệnh `pip install requests`.
* Gửi yêu cầu `GET` và nhận phản hồi định dạng `JSON` từ máy chủ.

### Mã nguồn minh họa:
```python
import requests
import json

def lay_du_lieu_api():
    # Sử dụng một API giả lập để lấy danh sách người dùng
    url = "https://jsonplaceholder.typicode.com/users/1"
    
    print(f"🌐 Đang kết nối tới: {url}...")
    
    try:
        # Gửi yêu cầu lấy dữ liệu
        response = requests.get(url)
        
        # Kiểm tra nếu mã trạng thái là 200 (Thành công)
        if response.status_code == 200:
            data = response.json()
            
            print("\n--- 🛡️ KẾT QUẢ TRUY VẤN API ---")
            print(f"Tên người dùng: {data['name']}")
            print(f"Email: {data['email']}")
            print(f"Thành phố: {data['address']['city']}")
            print("------------------------------")
        else:
            print(f"⚠️ Lỗi hệ thống: Mã trạng thái {response.status_code}")
            
    except Exception as e:
        print(f"❌ Không thể kết nối Internet: {e}")

# Chạy chương trình
lay_du_lieu_api()
```
### ⚡ Thử thách Day 011 (Thợ săn dữ liệu)
Hãy kết hợp với kỹ năng ghi file của Day 008/009:

Viết một hàm lấy dữ liệu từ URL: https://jsonplaceholder.typicode.com/posts/1

Sau khi lấy được dữ liệu, hãy lưu nội dung đó vào một file tên là web_data.json.

Đừng quên sử dụng try-except để xử lý trường hợp máy tính không có kết nối mạng.

```python
import requests
import json

def san_du_lieu_web():
    # 1. URL mục tiêu
    url = "https://jsonplaceholder.typicode.com/posts/1"
    file_name = "web_data.json"
    
    print(f"📡 Đang bắt đầu săn dữ liệu từ: {url}...")
    
    try:
        # 2. Gửi yêu cầu GET tới máy chủ
        response = requests.get(url, timeout=10)
        
        # Kiểm tra nếu phản hồi thành công (Status Code 200)
        if response.status_code == 200:
            # Chuyển dữ liệu nhận được sang định dạng JSON
            data = response.json()
            
            # 3. Ghi dữ liệu vào file web_data.json
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=4, ensure_ascii=False)
            
            print(f"✅ Săn dữ liệu thành công! Đã lưu vào file: {file_name}")
            print(f"📝 Tiêu đề bài viết: {data['title']}")
        else:
            print(f"⚠️ Máy chủ phản hồi lỗi. Mã trạng thái: {response.status_code}")
            
    except requests.exceptions.ConnectionError:
        print("❌ Lỗi: Không có kết nối Internet. Vui lòng kiểm tra lại mạng!")
    except Exception as e:
        print(f"❌ Có lỗi không xác định xảy ra: {e}")

# Chạy thử thách
if __name__ == "__main__":
    san_du_lieu_web()
```
### Giải thích kỹ thuật cho "Thợ săn dữ liệu":
1. `timeout=10`: Trong thực tế, khi săn dữ liệu (Crawling), máy chủ có thể bị treo. Thêm timeout giúp chương trình của bạn không bị đợi mãi mãi nếu mạng quá chậm.

2. `requests.exceptions.ConnectionError`: Đây là cách bắt lỗi chuyên nghiệp cho việc mất kết nối mạng, giúp bạn đưa ra thông báo chính xác thay vì một lỗi chung chung.

3. Tư duy Security: Việc biết cách kéo dữ liệu từ API là bước đầu tiên để bạn viết các script tự động kiểm tra xem các thông tin nhạy cảm của hệ thống có đang bị lộ ra ngoài qua các đường dẫn API công khai hay không.
