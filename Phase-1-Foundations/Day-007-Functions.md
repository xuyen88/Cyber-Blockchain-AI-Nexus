# **Day 007: Hàm (Functions) trong Python**

## **🎯 Mục tiêu**
Học cách sử dụng `def` để tạo các khối mã có thể tái sử dụng, giúp quản lý chương trình hiệu quả hơn.

---

## **🛠 Thực hành**
* Tạo hàm `thong_bao_nhiem_vu` để in thông tin người dùng.

  ```python
1. Định nghĩa hàm (Khai báo chiếc hộp công cụ)
def thong_bao_nhiem_vu(ten, ngay_hoc):
    print(f"--- [NEXUS SYSTEM MONITOR] ---")
    print(f"Chào học viên: {ten}")
    print(f"Bạn đang thực hiện: Day {ngay_hoc}")
    print(f"Trạng thái: Hoạt động bình thường.")
    print("-" * 30 + "\n")

 2. Gọi hàm (Lấy công cụ ra dùng)
thong_bao_nhiem_vu("Xuyen", "007")
thong_bao_nhiem_vu("AI Assistant", "999")
  ```
* Tạo hàm `tinh_tong` để thực hiện phép cộng toán học.

### **Mã nguồn chính:**
```python
def tinh_tong(a, b):
    print(f"Tổng là: {a + b}")

tinh_tong(10, 20)
