# Nhận dữ liệu từ bàn phím
name = input("Nhập tên của bạn: ")
age_str = input("Nhập tuổi của bạn: ")

# Chuyển đổi dữ liệu từ chữ sang số (Integer)
age = int(age_str)

print(f"\nChào {name}!")

# Kiểm tra điều kiện logic
if age >= 18:
    print("✅ Bạn đã đủ tuổi truy cập hệ thống nâng cao.")
else:
    print(f"⚠️ Bạn cần thêm {18 - age} năm nữa để đủ tuổi.")

print("\n--- Hoàn thành bài thực hành Day 05 ---")
