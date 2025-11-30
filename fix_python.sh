#!/bin/bash
# Script tự động sửa lỗi Python/tkinter trên macOS

echo "╔════════════════════════════════════════════════════════╗"
echo "║          🔧 SỬA LỖI PYTHON/TKINTER - MACOS            ║"
echo "╚════════════════════════════════════════════════════════╝"
echo ""

echo "⚠️  Phát hiện lỗi: Python hệ thống không tương thích với tkinter"
echo ""
echo "Lỗi: 'macOS 26 (2601) or later required, have instead 16 (1601)'"
echo ""
echo "Nguyên nhân: Python 3.9.6 từ /usr/bin/python3 quá cũ"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Check if Homebrew is installed
if command -v brew &> /dev/null; then
    echo "✅ Homebrew đã có sẵn"
    echo ""
    echo "🔧 Đang cài Python mới qua Homebrew..."
    echo "   (Quá trình này mất 2-3 phút)"
    echo ""
    
    brew install python@3.11 || brew install python3
    
    echo ""
    echo "🔧 Đang cài tkinter..."
    brew install python-tk@3.11 2>/dev/null || brew install python-tk
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Cài đặt thành công!"
        echo ""
        
        # Find new Python - try multiple locations
        NEW_PYTHON=""
        for py_path in \
            "/opt/homebrew/bin/python3" \
            "/opt/homebrew/bin/python3.11" \
            "/opt/homebrew/bin/python3.12" \
            "/usr/local/bin/python3" \
            "/usr/local/bin/python3.11" \
            "/usr/local/bin/python3.12" \
            "$(brew --prefix)/bin/python3" \
            "$(which python3.11 2>/dev/null)" \
            "$(which python3.12 2>/dev/null)"; do
            
            if [ -f "$py_path" ] && [ "$py_path" != "/usr/bin/python3" ]; then
                NEW_PYTHON="$py_path"
                break
            fi
        done
        
        if [ -z "$NEW_PYTHON" ]; then
            echo "⚠️  Không tìm thấy Python mới"
            echo "Đang tìm kiếm..."
            NEW_PYTHON=$(find /opt/homebrew /usr/local -name "python3*" -type f 2>/dev/null | grep -v "/usr/bin" | head -1)
        fi
        
        if [ -n "$NEW_PYTHON" ] && [ -f "$NEW_PYTHON" ]; then
            echo "Python mới: $NEW_PYTHON"
            echo "Version: $($NEW_PYTHON --version)"
            echo ""
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo "🚀 Đang chạy MacBook Tester với Python mới..."
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo ""
            
            $NEW_PYTHON macbook_tester.py
            exit 0
        else
            echo "❌ Không tìm thấy Python sau khi cài"
            echo "Thử chạy: brew list python@3.11"
        fi
    else
        echo "❌ Cài đặt thất bại"
    fi
else
    echo "⚠️  Homebrew chưa được cài đặt"
    echo ""
    echo "📦 Đang cài đặt Homebrew..."
    echo "   (Quá trình này mất 5-10 phút)"
    echo ""
    
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    
    if [ $? -eq 0 ]; then
        echo ""
        echo "✅ Homebrew đã được cài đặt"
        echo ""
        echo "🔧 Đang cài Python..."
        
        # Add Homebrew to PATH
        if [ -d "/opt/homebrew/bin" ]; then
            export PATH="/opt/homebrew/bin:$PATH"
        fi
        
        brew install python@3.11 || brew install python3
        
        # Find new Python
        NEW_PYTHON=""
        for py_path in \
            "/opt/homebrew/bin/python3" \
            "/opt/homebrew/bin/python3.11" \
            "/usr/local/bin/python3" \
            "$(brew --prefix)/bin/python3"; do
            
            if [ -f "$py_path" ] && [ "$py_path" != "/usr/bin/python3" ]; then
                NEW_PYTHON="$py_path"
                break
            fi
        done
        
        if [ -n "$NEW_PYTHON" ] && [ -f "$NEW_PYTHON" ]; then
            echo ""
            echo "✅ Hoàn thành!"
            echo "Python: $NEW_PYTHON"
            echo ""
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo "🚀 Đang chạy MacBook Tester..."
            echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
            echo ""
            
            $NEW_PYTHON macbook_tester.py
            exit 0
        else
            echo "❌ Không tìm thấy Python sau khi cài"
        fi
    fi
fi

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "❌ Không thể tự động sửa lỗi"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 Vui lòng cài Python thủ công:"
echo ""
echo "CÁCH 1: Tải từ python.org (Dễ nhất)"
echo "   1. Truy cập: https://www.python.org/downloads/"
echo "   2. Tải 'Python 3.11' hoặc mới hơn"
echo "   3. Mở file .pkg và cài đặt"
echo "   4. Chạy lại: ./install_and_run.sh"
echo ""
echo "CÁCH 2: Dùng Homebrew"
echo "   1. Cài Homebrew:"
echo "      /bin/bash -c \"\$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\""
echo "   2. Cài Python:"
echo "      brew install python@3.11"
echo "   3. Chạy lại: ./install_and_run.sh"
echo ""
