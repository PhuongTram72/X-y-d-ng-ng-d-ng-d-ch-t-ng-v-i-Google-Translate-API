1. Cơ sở dữ liệu:
Hệ quản trị cơ sở dữ liệu: MySQL
Bảng:
Bảng "Translations":
translation_id (PK): ID của bản dịch.
original_text: Văn bản gốc cần dịch.
translated_text: Văn bản đã được dịch.
source_language: Ngôn ngữ nguồn.
target_language: Ngôn ngữ đích.
timestamp: Thời điểm thực hiện dịch.
Ghi chú:
Bảng "Translations" lưu trữ các bản dịch với thông tin về văn bản gốc, văn bản đã dịch và thông tin ngôn ngữ.
Có quan hệ khóa ngoại (FK) giữa cột "source_language" và "target_language" với bảng "Languages" để đảm bảo tính nhất quán của dữ liệu ngôn ngữ.
Stored Procedures (SP):
SP_InsertTranslation: Chèn thông tin bản dịch mới vào bảng "Translations".
SP_GetTranslation: Truy vấn thông tin bản dịch từ bảng "Translations" dựa trên các tham số như ngôn ngữ nguồn và ngôn ngữ đích.

2. Module đọc dữ liệu:
Mô tả:
Sử dụng Python và FastAPI để tạo một API cho việc dịch văn bản tự động sử dụng Google Translate API.
Thu thập dữ liệu từ ứng dụng hoặc website cung cấp văn bản cần dịch.
Kết hợp Python với FastAPI để tạo ra một API cho ứng dụng khác có thể truy cập để dịch văn bản.
Thuật toán:
Người dùng gửi yêu cầu dịch văn bản qua API.
API gửi yêu cầu dịch văn bản đến Google Translate API.
Sau khi nhận được kết quả dịch từ Google Translate API, API trả về kết quả cho người dùng.
Đóng gói thành service:
Sử dụng NSSM để đóng gói module thành một dịch vụ Windows có thể chạy liên tục trên máy chủ.

3. Nodered:
Mô tả:
Chu trình tự động gọi API Python để lấy về dữ liệu dịch từ Google Translate API.
Sau đó, dữ liệu dịch được gửi đến cơ sở dữ liệu MySQL để lưu trữ.
Hành động:
Gọi API Python để dịch văn bản từ ngôn ngữ nguồn sang ngôn ngữ đích.
Sau đó, gọi node tương tác với cơ sở dữ liệu MySQL để chèn dữ liệu dịch vào bảng "Translations" bằng cách sử dụng Stored Procedures.

4. Web:
Mô tả:
Xây dựng một ứng dụng web cho phép người dùng nhập văn bản cần dịch và xem kết quả dịch.
Chức năng:
Người dùng nhập văn bản cần dịch và chọn ngôn ngữ nguồn và ngôn ngữ đích.
Ứng dụng sử dụng API để dịch văn bản và hiển thị kết quả dịch trên giao diện web.
Người dùng có thể xem lịch sử các bản dịch trước đó từ cơ sở dữ liệu và hiển thị trên giao diện web, có thể là biểu đồ thống kê hoặc danh sách.
