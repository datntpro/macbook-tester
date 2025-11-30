#!/bin/bash
# Script tự động cài đặt và chạy MacBook Tester
# Dành cho người không rành công nghệ

echo "╔════════════════════════════════════════════════════════╗"
echo "║     🍎 MACBOOK HARDWARE TESTER - TỰ ĐỘNG CÀI ĐẶT     ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

# Kiểm tra xem có đang chạy trên macOS không
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ Lỗi: Script này chỉ chạy trên macOS!"
    exit 1
fi

echo "✅ Đang chạy trên macOS $(sw_vers -productVersion)"
echo ""

# Kiểm tra Python3
echo "🔍 Kiểm tra Python3..."
PYTHON_CMD=""

# Try different Python commands
for cmd in python3 /usr/bin/python3 /usr/local/bin/python3; do
    if command -v $cmd &> /dev/null; then
        PYTHON_CMD=$cmd
        break
    fi
done

if [ -z "$PYTHON_CMD" ]; then
    echo "⚠️  Python3 chưa được cài đặt"
    echo ""
    echo "📦 Đang cài đặt Python3..."
    echo ""
    
    # Check if Homebrew is installed
    if command -v brew &> /dev/null; then
        echo "✅ Homebrew đã có, đang cài Python..."
        brew install python3
        PYTHON_CMD="python3"
    else
        echo "⏳ Đang cài đặt Xcode Command Line Tools..."
        echo "   (Một cửa sổ popup sẽ xuất hiện)"
        echo ""
        
        # Install Xcode Command Line Tools
        xcode-select --install 2>/dev/null || true
        
        echo ""
        echo "⏳ Vui lòng:"
        echo "   1. Click 'Install' trong popup"
        echo "   2. Đợi cài đặt hoàn tất (3-5 phút)"
        echo "   3. Nhấn Enter để tiếp tục..."
        read -r
        
        # Check again
        if command -v python3 &> /dev/null; then
            PYTHON_CMD="python3"
            echo "✅ Cài đặt thành công!"
        else
            echo ""
            echo "❌ Không thể cài đặt tự động"
            echo ""
            echo "📝 Vui lòng cài thủ công:"
            echo "   1. Truy cập: https://www.python.org/downloads/"
            echo "   2. Tải Python 3.x cho macOS"
            echo "   3. Cài đặt và chạy lại script này"
            echo ""
            exit 1
        fi
    fi
else
    PYTHON_VERSION=$($PYTHON_CMD --version 2>&1)
    echo "✅ Python đã có sẵn: $PYTHON_VERSION"
fi

# Check tkinter
echo ""
echo "🔍 Kiểm tra tkinter (GUI library)..."
$PYTHON_CMD -c "import tkinter" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "⚠️  tkinter không hoạt động"
    echo ""
    echo "🔧 Đang thử sửa lỗi..."
    
    # Try to install tkinter
    if command -v brew &> /dev/null; then
        echo "Đang cài python-tk qua Homebrew..."
        brew install python-tk 2>/dev/null || true
    fi
    
    # Check again
    $PYTHON_CMD -c "import tkinter" 2>/dev/null
    if [ $? -ne 0 ]; then
        echo ""
        echo "❌ Không thể sửa lỗi tkinter tự động"
        echo ""
        echo "📝 Giải pháp:"
        echo "   1. Cài Homebrew: /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
        echo "   2. Chạy: brew install python-tk"
        echo "   3. Hoặc tải Python từ python.org (đã bao gồm tkinter)"
        echo ""
        exit 1
    fi
fi

echo "✅ tkinter OK"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "🚀 Đang khởi động MacBook Tester..."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Try to find better Python if system Python is too old
if [[ "$PYTHON_CMD" == "/usr/bin/python3" ]]; then
    echo "⚠️  Đang dùng Python hệ thống (có thể gặp lỗi tkinter)"
    echo "🔍 Đang tìm Python tốt hơn..."
    echo ""
    
    # Try to find Homebrew Python with tkinter
    FOUND_BETTER=false
    for alt_python in \
        /opt/homebrew/bin/python3.11 \
        /opt/homebrew/bin/python3.12 \
        /opt/homebrew/bin/python3 \
        /usr/local/bin/python3.11 \
        /usr/local/bin/python3.12 \
        /usr/local/bin/python3 \
        /Library/Frameworks/Python.framework/Versions/3.*/bin/python3; do
        
        if [ -f "$alt_python" ]; then
            # Test if tkinter works
            $alt_python -c "import tkinter" 2>/dev/null
            if [ $? -eq 0 ]; then
                echo "✅ Tìm thấy Python phù hợp: $alt_python"
                PYTHON_CMD="$alt_python"
                echo "   Version: $($PYTHON_CMD --version)"
                FOUND_BETTER=true
                break
            fi
        fi
    done
    
    if [ "$FOUND_BETTER" = false ]; then
        echo "❌ Không tìm thấy Python phù hợp"
        echo ""
        echo "Đang chạy script sửa lỗi..."
        chmod +x fix_python.sh
        ./fix_python.sh
        exit $?
    fi
    echo ""
fi

# Run the application
$PYTHON_CMD macbook_tester.py

EXIT_CODE=$?

# If crashed with tkinter error, run fix script
if [ $EXIT_CODE -eq 134 ] || [ $EXIT_CODE -eq 6 ]; then
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "⚠️  Phát hiện lỗi tkinter!"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    echo "Đang chạy script sửa lỗi tự động..."
    echo ""
    
    chmod +x fix_python.sh
    ./fix_python.sh
    exit $?
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [ $EXIT_CODE -eq 0 ]; then
    echo "✅ Hoàn thành!"
    echo "📄 Báo cáo đã được tạo trong thư mục hiện tại"
else
    echo "⚠️  Ứng dụng đã đóng"
    echo "📄 Kiểm tra file báo cáo nếu có"
fi

echo ""
echo "Cảm ơn bạn đã sử dụng MacBook Tester! 🍎"
echo ""
