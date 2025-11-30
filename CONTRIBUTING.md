# 🤝 Đóng góp cho MacBook Tester

Cảm ơn bạn quan tâm đến việc đóng góp! Mọi đóng góp đều được chào đón.

## 📋 Cách đóng góp

### 1. Báo lỗi (Bug Report)

Nếu bạn tìm thấy lỗi, vui lòng tạo Issue với thông tin:

- **Mô tả lỗi**: Lỗi gì xảy ra?
- **Cách tái hiện**: Làm thế nào để gặp lỗi?
- **Môi trường**:
  - macOS version
  - Python version
  - Model MacBook đang test
- **Log lỗi**: Copy/paste error message
- **Screenshot**: Nếu có

### 2. Đề xuất tính năng (Feature Request)

Tạo Issue với:

- **Mô tả tính năng**: Tính năng gì?
- **Lý do**: Tại sao cần tính năng này?
- **Cách hoạt động**: Tính năng sẽ hoạt động như thế nào?

### 3. Pull Request

#### Quy trình:

1. **Fork** repo
2. **Clone** fork về máy:
   ```bash
   git clone https://github.com/your-username/macbook-tester.git
   cd macbook-tester
   ```

3. **Tạo branch** mới:
   ```bash
   git checkout -b feature/ten-tinh-nang
   # hoặc
   git checkout -b fix/ten-loi
   ```

4. **Thực hiện thay đổi**

5. **Test** kỹ trên macOS

6. **Commit** với message rõ ràng:
   ```bash
   git commit -m "Add: Thêm tính năng kiểm tra Bluetooth"
   # hoặc
   git commit -m "Fix: Sửa lỗi crash khi test camera"
   ```

7. **Push** lên fork:
   ```bash
   git push origin feature/ten-tinh-nang
   ```

8. **Tạo Pull Request** trên GitHub

#### Quy tắc code:

- **Python style**: Tuân theo PEP 8
- **Comments**: Viết comment bằng tiếng Việt cho dễ hiểu
- **Docstrings**: Mô tả rõ ràng function/class
- **Error handling**: Xử lý lỗi đầy đủ
- **User-friendly**: Thông báo lỗi dễ hiểu cho người dùng

#### Ví dụ code tốt:

```python
def test_battery(self):
    """Kiểm tra tình trạng pin"""
    self.log("🔋 Đang kiểm tra pin...")
    
    try:
        # Get battery info
        cycle_count = self.run_command("system_profiler SPPowerDataType | grep 'Cycle Count'")
        
        if not cycle_count:
            self.log("⚠️ Không lấy được thông tin pin")
            return
        
        # Parse and evaluate
        cycles = int(cycle_count.split()[-1])
        
        if cycles < 300:
            status = "✅ Rất tốt"
        elif cycles < 500:
            status = "✅ Tốt"
        else:
            status = "⚠️ Cần thay pin"
        
        self.test_results["battery"] = {
            "status": status,
            "cycles": cycles
        }
        
        self.log(f"{status} - Pin có {cycles} chu kỳ sạc")
        
    except Exception as e:
        self.log(f"❌ Lỗi: {str(e)}")
        self.test_results["battery"] = {"status": "❌ FAIL"}
```

## 🎯 Ý tưởng đóng góp

### Tính năng mới:

- [ ] Test Bluetooth
- [ ] Test WiFi
- [ ] Test Touch ID
- [ ] Test Face ID (MacBook mới)
- [ ] Benchmark CPU/GPU
- [ ] Test nhiệt độ
- [ ] Export báo cáo PDF trực tiếp (không qua HTML)
- [ ] Giao diện dark mode
- [ ] Đa ngôn ngữ (English, Vietnamese)

### Cải thiện:

- [ ] Tối ưu tốc độ test
- [ ] Thêm progress bar
- [ ] Lưu lịch sử test
- [ ] So sánh với test trước
- [ ] Tích hợp API kiểm tra giá MacBook
- [ ] Thêm database giá tham khảo

### Documentation:

- [ ] Video hướng dẫn
- [ ] FAQ chi tiết hơn
- [ ] Dịch sang tiếng Anh
- [ ] Thêm ảnh minh họa

## 📝 Commit Message Convention

Sử dụng prefix:

- `Add:` Thêm tính năng mới
- `Fix:` Sửa lỗi
- `Update:` Cập nhật tính năng có sẵn
- `Refactor:` Tái cấu trúc code
- `Docs:` Cập nhật documentation
- `Style:` Format code, không thay đổi logic
- `Test:` Thêm/sửa test

Ví dụ:
```
Add: Thêm test Bluetooth
Fix: Sửa lỗi crash khi test camera trên macOS 13
Update: Cải thiện UI báo cáo HTML
Docs: Thêm hướng dẫn xử lý lỗi tkinter
```

## ✅ Checklist trước khi submit PR

- [ ] Code chạy được trên macOS
- [ ] Đã test trên ít nhất 1 model MacBook
- [ ] Không có lỗi Python
- [ ] Code có comment đầy đủ
- [ ] Cập nhật README.md (nếu cần)
- [ ] Cập nhật GUIDE.md (nếu cần)
- [ ] Commit message rõ ràng

## 🙏 Cảm ơn

Cảm ơn bạn đã đóng góp cho MacBook Tester!

Mọi đóng góp, dù lớn hay nhỏ, đều giúp tool này tốt hơn.

---

**Powered by [DATNT](https://tools.datnt.work)**
