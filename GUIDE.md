# 📖 Hướng dẫn chi tiết

## ⚠️ DISCLAIMER - ĐỌC KỸ TRƯỚC KHI SỬ DỤNG

**Kết quả test từ tool này chỉ mang tính chất tham khảo.**

### Điều bạn cần biết:

- ✅ Tool giúp phát hiện các vấn đề phần cứng cơ bản
- ⚠️ Tool KHÔNG THỂ phát hiện tất cả các lỗi tiềm ẩn
- 🔍 Một số vấn đề chỉ xuất hiện sau thời gian sử dụng lâu dài
- 🤝 Quyết định mua máy là **TRÁCH NHIỆM HOÀN TOÀN** của bạn
- 🚫 Tool và tác giả **KHÔNG CHỊU TRÁCH NHIỆM** về:
  - Máy hỏng sau khi mua
  - Phát hiện lỗi mới sau khi mua
  - Tranh chấp với người bán
  - Bất kỳ tổn thất tài chính nào

### Khuyến nghị:

1. **Sử dụng tool như một công cụ hỗ trợ**, không phải quyết định duy nhất
2. **Kiểm tra thêm bằng mắt, tai** và kinh nghiệm cá nhân
3. **Hỏi ý kiến người am hiểu** về MacBook
4. **Mua từ nguồn uy tín** có chính sách bảo hành/đổi trả
5. **Không mua nếu không chắc chắn**

---

## Mục lục

- [Cài đặt](#cài-đặt)
- [Sử dụng](#sử-dụng)
- [Các bài test](#các-bài-test)
- [Đọc báo cáo](#đọc-báo-cáo)
- [Xử lý lỗi](#xử-lý-lỗi)
- [Tips mua MacBook](#tips-mua-macbook)

---

## Cài đặt

### Cách 1: Tự động (Dễ nhất)

```bash
# 1. Tải về
git clone https://github.com/yourusername/macbook-tester.git
cd macbook-tester

# 2. Chạy
./install_and_run.sh
```

### Cách 2: Thủ công

```bash
# 1. Kiểm tra Python
python3 --version

# 2. Nếu chưa có, cài từ python.org
# https://www.python.org/downloads/

# 3. Chạy app
python3 macbook_tester.py
```

---

## Sử dụng

### Bước 1: Khởi động

Chọn một trong các cách:
- Double-click `START_HERE.command`
- Chạy `./install_and_run.sh`
- Chạy `python3 macbook_tester.py`

### Bước 2: Chạy test

**Option A: Test tự động**
1. Click nút "🚀 CHẠY TẤT CẢ"
2. Làm theo hướng dẫn trên màn hình
3. Đợi hoàn thành

**Option B: Test từng phần**
1. Click vào từng nút test
2. Làm theo hướng dẫn
3. Chuyển sang test tiếp theo

### Bước 3: Tạo báo cáo

1. Click "📄 TẠO BÁO CÁO"
2. File HTML sẽ tự động mở
3. Nhấn Cmd+P để in PDF (nếu cần)

---

## Các bài test

### 1. 🔒 MDM (Khóa doanh nghiệp)

**Quan trọng nhất!**

- Kiểm tra máy có bị khóa MDM/DEP không
- Nếu bị khóa → **KHÔNG MUA**
- Cần quyền sudo để kiểm tra

**Cách test:**
- App tự động kiểm tra
- Hiển thị cảnh báo nếu bị khóa

### 2. 🔋 Pin

**Kiểm tra:**
- Số chu kỳ sạc
- Tình trạng pin (Condition)
- Dung lượng còn lại

**Đánh giá:**
- < 300 chu kỳ: Rất tốt
- 300-500: Tốt
- 500-800: Trung bình
- > 800: Cần thay pin

### 3. 💾 Ổ cứng

**Kiểm tra:**
- Dung lượng tổng/còn trống
- SMART status
- Loại ổ (SSD/HDD)

**Lưu ý:**
- SMART status phải là "Verified"
- Nếu "Failing" → Ổ cứng sắp hỏng

### 4. 📷 Camera

**Cách test:**
1. App mở Photo Booth
2. Kiểm tra camera có hoạt động không
3. Xác nhận kết quả

**Kiểm tra:**
- Camera có bật được không
- Hình ảnh có rõ nét không
- Có bị mờ/vàng không

### 5. 🔊 Loa & Microphone

**Cách test:**
1. App phát âm thanh test
2. Nghe xem có âm thanh không
3. Xác nhận kết quả

**Kiểm tra:**
- Loa có kêu không
- Âm thanh có rè/vỡ không
- Âm lượng có đủ lớn không

### 6. 🖼️ Màn hình

**Cách test:**
1. Màn hình chuyển sang fullscreen
2. Nhấn Space để đổi màu
3. Kiểm tra dead pixel
4. Nhấn ESC để kết thúc

**Kiểm tra:**
- Dead pixel (điểm chết)
- Màu sắc có đều không
- Có vệt sáng/tối không
- Độ sáng có đủ không

**Màu test:**
- Trắng, Đen, Đỏ, Xanh lá, Xanh dương, Vàng, Cyan, Magenta

### 7. ⌨️ Bàn phím

**Cách test:**
1. Cửa sổ test mở ra
2. Gõ thử TẤT CẢ các phím
3. Xác nhận kết quả

**Phím quan trọng:**
- Space, Enter, Shift, Command
- Các phím chữ cái
- Các phím số
- Các phím chức năng (F1-F12)

**Lưu ý:**
- Bàn phím MacBook dễ hỏng
- Sửa rất đắt (thay cả bàn phím + top case)

### 8. 🖱️ Trackpad

**Cách test:**
1. Di chuyển con trỏ
2. Click trái/phải
3. Cuộn 2 ngón
4. Zoom 2 ngón
5. Vuốt 3 ngón
6. Vẽ trên canvas

**Kiểm tra:**
- Độ nhạy
- Click có phản hồi không
- Cử chỉ đa điểm hoạt động không
- Có vùng chết không

### 9. 🔌 Cổng kết nối

**Cách test:**
1. Cắm USB/Thunderbolt vào từng cổng
2. Kiểm tra có nhận không
3. Xác nhận kết quả

**Kiểm tra:**
- Tất cả cổng có hoạt động không
- Có cổng lỏng không
- Sạc có vào không

### 10. 🖥️ Thông tin hệ thống

**Tự động hiển thị:**
- Model MacBook
- Serial number
- macOS version
- CPU
- RAM

---

## Đọc báo cáo

### Báo cáo HTML

File: `macbook_test_report_YYYYMMDD_HHMMSS.html`

**Cấu trúc:**
1. **Header**: Tiêu đề + Powered by DATNT
2. **Thông tin máy**: Model, Serial, CPU, RAM
3. **Kết quả tổng thể**: X/10 bài test PASS
4. **Chi tiết từng test**: Trạng thái + lý do (nếu có)
5. **Khuyến nghị**: MUA / CÂN NHẮC / KHÔNG MUA

**Màu sắc:**
- 🟢 Xanh: CÓ THỂ MUA
- 🟡 Vàng: CÂN NHẮC
- 🔴 Đỏ: KHÔNG MUA

**Chuyển sang PDF:**
1. Mở file HTML trong trình duyệt
2. Nhấn Cmd+P
3. Click "PDF" → "Save as PDF"

### Báo cáo Text

File: `macbook_test_report_YYYYMMDD_HHMMSS.txt`

- Định dạng text thuần
- Dùng để backup
- Dễ gửi qua email/chat

---

## Xử lý lỗi

### Lỗi 1: "Python quit unexpectedly"

**Nguyên nhân:** Python hệ thống có tkinter cũ

**Giải pháp:**
```bash
# Tự động sửa
./fix_python.sh

# Hoặc cài Python mới
# Tải từ: https://www.python.org/downloads/
```

### Lỗi 2: "tkinter not found"

```bash
# Cài tkinter
brew install python-tk@3.11
```

### Lỗi 3: "Permission denied"

```bash
# Cho phép thực thi
chmod +x install_and_run.sh
chmod +x START_HERE.command
```

### Lỗi 4: "MDM check failed"

**Nguyên nhân:** Không có quyền sudo

**Giải pháp:**
```bash
# Chạy với sudo
sudo python3 macbook_tester.py
```

### Kiểm tra hệ thống

```bash
./check_system.sh
```

Script này sẽ kiểm tra:
- macOS version
- Python version
- tkinter có hoạt động không

---

## Tips mua MacBook

### Trước khi gặp người bán

1. ✅ Hỏi thông tin cơ bản:
   - Model, năm sản xuất
   - Cấu hình (CPU, RAM, SSD)
   - Lý do bán
   - Giá mong muốn

2. ✅ Yêu cầu:
   - Ảnh thực tế máy
   - Ảnh About This Mac
   - Ảnh Battery Cycle Count

### Khi gặp trực tiếp

1. ✅ Địa điểm an toàn:
   - Cafe, trung tâm thương mại
   - Nơi công cộng, đông người

2. ✅ Kiểm tra ngoại hình:
   - Vỏ máy có móp méo không
   - Màn hình có trầy xước không
   - Bàn phím có bong tróc không

3. ✅ Chạy MacBook Tester:
   - Test đầy đủ 10 thành phần
   - Đặc biệt chú ý MDM và Pin

4. ✅ Kiểm tra thêm:
   - Serial trên [Apple Check Coverage](https://checkcoverage.apple.com)
   - Xem còn bảo hành không
   - Kiểm tra Find My có tắt không

### Thương lượng giá

**Nếu có vấn đề nhỏ:**
- Pin > 500 chu kỳ: Trừ 2-3 triệu (chi phí thay pin)
- Màn hình có vết nhỏ: Trừ 1-2 triệu
- Bàn phím 1-2 phím lỗi: Trừ 3-5 triệu (thay bàn phím rất đắt)

**Không mua nếu:**
- ❌ Bị khóa MDM
- ❌ Ổ cứng SMART status "Failing"
- ❌ Màn hình nhiều dead pixel
- ❌ Nhiều phím bàn phím lỗi
- ❌ Người bán không cho test kỹ

### Sau khi mua

1. ✅ Xóa máy và cài lại macOS
2. ✅ Đăng nhập iCloud của bạn
3. ✅ Cài đặt các app cần thiết
4. ✅ Backup thường xuyên

---

## Câu hỏi thường gặp

**Q: App có miễn phí không?**
A: Có, hoàn toàn miễn phí và open source.

**Q: App có thu thập dữ liệu không?**
A: Không, app chạy hoàn toàn offline.

**Q: Tôi có thể tin báo cáo 100% không?**
A: KHÔNG. Báo cáo chỉ mang tính tham khảo. Bạn vẫn cần kiểm tra thêm bằng mắt, tai và kinh nghiệm. Tool không thể phát hiện tất cả các lỗi tiềm ẩn.

**Q: Nếu báo cáo nói "CÓ THỂ MUA", tôi mua rồi máy hỏng thì sao?**
A: Tool và tác giả không chịu trách nhiệm. Quyết định mua máy là trách nhiệm của bạn. Nên mua từ nguồn có bảo hành.

**Q: App có chạy trên Windows không?**
A: Không, chỉ chạy trên macOS.

**Q: Tôi có thể sửa đổi app không?**
A: Có, app là open source (MIT License).

---

**Powered by [DATNT](https://tools.datnt.work)**
