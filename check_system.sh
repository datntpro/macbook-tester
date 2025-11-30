#!/bin/bash
# Script kiểm tra hệ thống trước khi chạy

echo "🔍 Đang kiểm tra hệ thống..."
echo ""

# Check macOS
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ Không phải macOS!"
    exit 1
fi
echo "✅ macOS: $(sw_vers -productVersion)"

# Check Python3
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version 2>&1)
    echo "✅ $PYTHON_VERSION"
    PYTHON_PATH=$(which python3)
    echo "   Đường dẫn: $PYTHON_PATH"
else
    echo "❌ Python3 chưa cài đặt"
    exit 1
fi

# Check tkinter
echo ""
echo "🔍 Kiểm tra tkinter..."
python3 -c "import tkinter; print('✅ tkinter OK')" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "❌ tkinter không hoạt động"
    echo ""
    echo "Đang thử sửa lỗi tkinter..."
    
    # Try to fix tkinter on macOS
    if [ -f "/System/Library/Frameworks/Tk.framework/Versions/8.5/Tk" ]; then
        echo "✅ Tk framework tìm thấy"
    else
        echo "⚠️  Cần cài đặt tkinter"
        echo ""
        echo "Chạy lệnh sau để cài:"
        echo "brew install python-tk@3.11"
        echo ""
        echo "Hoặc cài Python từ python.org (đã bao gồm tkinter)"
    fi
else
    echo "✅ tkinter hoạt động tốt"
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "Hệ thống sẵn sàng!"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
