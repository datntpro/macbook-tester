#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script chuyển đổi HTML report sang PDF
Sử dụng: python3 convert_to_pdf.py <file.html>
"""

import sys
import os
import subprocess

def convert_html_to_pdf(html_file):
    """Convert HTML to PDF using macOS tools"""
    
    if not os.path.exists(html_file):
        print(f"❌ Không tìm thấy file: {html_file}")
        return False
    
    pdf_file = html_file.replace('.html', '.pdf')
    
    print(f"🔄 Đang chuyển đổi {html_file} sang PDF...")
    print("")
    
    # Method 1: Try using wkhtmltopdf if installed
    try:
        result = subprocess.run(['which', 'wkhtmltopdf'], 
                              capture_output=True, text=True)
        if result.returncode == 0:
            print("✅ Sử dụng wkhtmltopdf...")
            subprocess.run(['wkhtmltopdf', html_file, pdf_file], check=True)
            print(f"✅ Đã tạo: {pdf_file}")
            return True
    except:
        pass
    
    # Method 2: Use Safari to print
    print("📄 Đang mở trong Safari...")
    print("")
    print("Vui lòng:")
    print("  1. Nhấn Cmd+P (hoặc File > Print)")
    print("  2. Click 'PDF' ở góc dưới bên trái")
    print("  3. Chọn 'Save as PDF'")
    print(f"  4. Lưu với tên: {pdf_file}")
    print("")
    
    subprocess.run(['open', '-a', 'Safari', html_file])
    
    return False

def main():
    if len(sys.argv) < 2:
        print("╔════════════════════════════════════════════════════════╗")
        print("║          CHUYỂN ĐỔI HTML SANG PDF                     ║")
        print("╚════════════════════════════════════════════════════════╝")
        print("")
        print("Cách dùng:")
        print("  python3 convert_to_pdf.py <file.html>")
        print("")
        print("Hoặc kéo thả file HTML vào script này")
        print("")
        
        # Find HTML reports in current directory
        html_files = [f for f in os.listdir('.') if f.startswith('macbook_test_report') and f.endswith('.html')]
        
        if html_files:
            print("📄 Tìm thấy các báo cáo:")
            for i, f in enumerate(html_files, 1):
                print(f"  {i}. {f}")
            print("")
            
            try:
                choice = input("Chọn số (hoặc Enter để thoát): ").strip()
                if choice and choice.isdigit():
                    idx = int(choice) - 1
                    if 0 <= idx < len(html_files):
                        convert_html_to_pdf(html_files[idx])
            except KeyboardInterrupt:
                print("\n\nĐã hủy")
        
        return
    
    html_file = sys.argv[1]
    convert_html_to_pdf(html_file)

if __name__ == "__main__":
    main()
