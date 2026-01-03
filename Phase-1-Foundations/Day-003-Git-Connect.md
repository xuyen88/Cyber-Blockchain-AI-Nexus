# Day 003: Kết nối máy tính với GitHub (Git Push)

## 🎯 Mục tiêu
Đưa thư mục `Nexus_Test` từ máy tính cá nhân lên GitHub để lưu trữ và chia sẻ.

## 🛠 Các bước thực hiện (15 phút)

1. **Cấu hình danh tính (Chỉ làm 1 lần duy nhất):**
   Mở Terminal và gõ:
   - `git config --global user.name "TênCủaBạn"`
   - `git config --global user.email "EmailCủaBạn@example.com"`

2. **Khởi tạo và Kết nối:**
   Tại thư mục `Nexus_Test` trên máy tính, gõ các lệnh sau:
   - `git init` (Để máy tính hiểu đây là một thư mục Git).
   - `git add .` (Chuẩn bị đóng gói tất cả file trong thư mục).
   - `git commit -m "Bài tập ngày 3"` (Ghi chú cho đợt đóng gói này).

3. **Lệnh "Thần thánh":**
   Để đẩy code lên, bạn cần copy link Repo của mình (ví dụ: `https://github.com/xuyen88/Cyber-Blockchain-AI-Nexus.git`) và gõ:
   - `git remote add origin <Link_Repo_Của_Bạn>`
   - `git push -u origin main` (Đẩy mọi thứ lên mây!).

## ⚡ Thử thách
Hãy thử sửa nội dung file `hello.txt` trên máy tính, sau đó dùng lệnh `git add .`, `git commit` và `git push` để thấy sự thay đổi trên GitHub mà không cần dùng chuột.
