# 🍎 MacBook Hardware Tester

> Công cụ kiểm tra phần cứng MacBook toàn diện - Giúp bạn đánh giá chính xác tình trạng máy trước khi mua

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![macOS](https://img.shields.io/badge/platform-macOS-lightgrey.svg)](https://www.apple.com/macos/)

**Powered by [DATNT](https://tools.datnt.work)**

---

## 📋 Tính năng

Ứng dụng kiểm tra toàn diện 10 thành phần quan trọng của MacBook:

| Thành phần | Kiểm tra |
|-----------|----------|
| 🔒 **MDM** | Phát hiện khóa doanh nghiệp (QUAN TRỌNG NHẤT) |
| 🔋 **Pin** | Số chu kỳ sạc, tình trạng pin |
| 💾 **Ổ cứng** | Dung lượng, SMART status, tốc độ |
| 📷 **Camera** | Test webcam hoạt động |
| 🔊 **Loa** | Test âm thanh output |
| 🖼️ **Màn hình** | Dead pixel, màu sắc, độ sáng |
| ⌨️ **Bàn phím** | Test từng phím |
| 🖱️ **Trackpad** | Độ nhạy, cử chỉ đa điểm |
| 🔌 **Cổng kết nối** | USB/Thunderbolt |
| 🖥️ **Hệ thống** | Model, Serial, CPU, RAM, macOS |

**Kết quả:** Báo cáo HTML/PDF đẹp với khuyến nghị rõ ràng: **MUA** / **CÂN NHẮC** / **KHÔNG MUA**

---

## 🚀 Cách sử dụng

### Cách 1: Tự động (Khuyến nghị)

```bash
# Clone repo
git clone https://github.com/yourusername/macbook-tester.git
cd macbook-tester

# Chạy script tự động
./install_and_run.sh
```

Script sẽ tự động:
- ✅ Kiểm tra và cài Python (nếu cần)
- ✅ Cài tkinter (GUI library)
- ✅ Chạy ứng dụng

### Cách 2: Chạy trực tiếp

```bash
python3 macbook_tester.py
```

### Cách 3: Double-click

```bash
# Cho phép thực thi
chmod +x START_HERE.command

# Double-click vào file START_HERE.command
```

---

## 📖 Hướng dẫn sử dụng

1. **Khởi động app** bằng một trong các cách trên
2. **Click "CHẠY TẤT CẢ"** để test tự động (hoặc test từng phần)
3. **Làm theo hướng dẫn** trên màn hình cho từng bài test
4. **Click "TẠO BÁO CÁO"** sau khi hoàn thành
5. **Xem báo cáo** HTML/PDF với khuyến nghị rõ ràng

---

## ⚠️ Lưu ý quan trọng

### 📢 DISCLAIMER

**Kết quả test chỉ mang tính chất tham khảo và không đảm bảo 100% chính xác.**

- ✅ Tool giúp phát hiện các vấn đề cơ bản
- ⚠️ Không thể phát hiện tất cả các lỗi tiềm ẩn
- 🤝 Quyết định mua máy là trách nhiệm hoàn toàn của bạn
- 🚫 Tool và tác giả không chịu trách nhiệm về bất kỳ vấn đề nào phát sinh sau khi mua

**Khuyến nghị:** Nên kiểm tra thêm bằng mắt, tai và kinh nghiệm cá nhân.

---

### 🔒 Kiểm tra MDM là QUAN TRỌNG NHẤT!

**MDM (Mobile Device Management)** là hệ thống khóa máy doanh nghiệp.

❌ **Nếu máy bị khóa MDM:**
- Không thể xóa và cài lại macOS
- Máy yêu cầu đăng nhập tài khoản công ty
- Không thể sử dụng được
- **TUYỆT ĐỐI KHÔNG MUA!**

### 📊 Đánh giá Pin

| Chu kỳ sạc | Đánh giá |
|-----------|----------|
| < 300 | ✅ Rất tốt |
| 300-500 | ✅ Tốt |
| 500-800 | ⚠️ Trung bình |
| > 800 | ❌ Cần thay pin |

### 💡 Tips khi mua MacBook

- ✅ Luôn test trước khi mua
- ✅ Kiểm tra MDM đầu tiên
- ✅ Test tất cả các phím (bàn phím MacBook dễ hỏng)
- ✅ Kiểm tra màn hình kỹ (dead pixel khó sửa)
- ✅ Xem số chu kỳ pin
- ✅ Hỏi lịch sử sửa chữa
- ✅ Kiểm tra serial trên [Apple Check Coverage](https://checkcoverage.apple.com)

---

## 📄 Báo cáo

Sau khi test, app tạo 2 file:

1. **HTML Report** (Đẹp, có màu sắc):
   - `macbook_test_report_YYYYMMDD_HHMMSS.html`
   - Mở trong trình duyệt, nhấn Cmd+P để in PDF

2. **Text Report** (Backup):
   - `macbook_test_report_YYYYMMDD_HHMMSS.txt`

**Khuyến nghị trong báo cáo:**
- 🟢 **CÓ THỂ MUA**: Máy trong tình trạng tốt
- 🟡 **CÂN NHẮC**: Có vấn đề nhỏ, cần thương lượng giá
- 🔴 **KHÔNG MUA**: Nhiều vấn đề hoặc bị khóa MDM

---

## 🔧 Yêu cầu hệ thống

- **OS**: macOS (bất kỳ phiên bản)
- **Python**: 3.9+ (script tự động cài nếu thiếu)
- **Quyền**: sudo (để kiểm tra MDM)

---

## 🐛 Xử lý lỗi

### Lỗi: "Python quit unexpectedly"

**Nguyên nhân:** Python hệ thống có tkinter cũ

**Giải pháp:**
```bash
# Chạy script sửa lỗi tự động
./fix_python.sh

# Hoặc cài Python mới từ python.org
# https://www.python.org/downloads/
```

### Lỗi: "tkinter not found"

```bash
# Cài tkinter qua Homebrew
brew install python-tk@3.11
```

### Kiểm tra hệ thống

```bash
./check_system.sh
```

---

## 📦 Cấu trúc project

```
macbook-tester/
├── macbook_tester.py       # App chính
├── install_and_run.sh      # Script cài đặt và chạy tự động
├── fix_python.sh           # Script sửa lỗi Python/tkinter
├── check_system.sh         # Script kiểm tra hệ thống
├── convert_to_pdf.py       # Chuyển HTML sang PDF
├── START_HERE.command      # Double-click để chạy
├── requirements.txt        # Dependencies (không cần cài thêm)
└── README.md              # File này
```

---

## 🤝 Đóng góp

Mọi đóng góp đều được chào đón! Vui lòng:

1. Fork repo
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

---

## 📝 License

MIT License - xem file [LICENSE](LICENSE) để biết thêm chi tiết

## ⚠️ Disclaimer

**ĐỌC KỸ TRƯỚC KHI SỬ DỤNG:** [DISCLAIMER.md](DISCLAIMER.md)

Kết quả test chỉ mang tính tham khảo. Quyết định mua máy là trách nhiệm của bạn. Tool và tác giả không chịu trách nhiệm về bất kỳ vấn đề nào phát sinh sau khi mua.

---

## 👨‍💻 Tác giả

**DATNT**
- Website: [tools.datnt.work](https://tools.datnt.work)
- GitHub: [@datntpro](https://github.com/datntpro)

---

## ⭐ Support

Nếu tool này hữu ích, hãy cho một ⭐ trên GitHub!

**Chúc bạn tìm được MacBook ưng ý! 🍎**
