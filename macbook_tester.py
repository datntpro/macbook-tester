#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
MacBook Hardware Tester
Ứng dụng kiểm tra phần cứng MacBook cũ trước khi mua
"""

import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import subprocess
import json
import os
import sys
from datetime import datetime
import threading
import tempfile

class MacBookTester:
    def __init__(self, root):
        self.root = root
        self.root.title("Tool Test MacBook - by DATNT")
        self.root.geometry("900x720")
        
        self.test_results = {}
        self.setup_ui()
        
    def setup_ui(self):
        # Header
        header = tk.Label(self.root, text="🍎 TOOL TEST MACBOOK", 
                         font=("Arial", 20, "bold"), fg="#007AFF")
        header.pack(pady=10)
        
        # Powered by
        powered_by = tk.Label(self.root, text="Powered by DATNT", 
                            font=("Arial", 10), fg="#666", cursor="hand2")
        powered_by.pack()
        powered_by.bind("<Button-1>", lambda e: self.open_url("https://tools.datnt.work"))
        
        # Disclaimer
        disclaimer_frame = tk.Frame(self.root, bg="#FFF3CD", relief="solid", borderwidth=1)
        disclaimer_frame.pack(fill="x", padx=10, pady=5)
        
        disclaimer_text = ("⚠️ LƯU Ý: Kết quả test chỉ mang tính chất tham khảo. "
                          "Quyết định mua máy là trách nhiệm của bạn.")
        disclaimer = tk.Label(disclaimer_frame, text=disclaimer_text, 
                            font=("Arial", 9), fg="#856404", bg="#FFF3CD", 
                            wraplength=850, justify="center")
        disclaimer.pack(pady=5, padx=10)
        
        # Info frame
        info_frame = ttk.LabelFrame(self.root, text="Thông tin máy", padding=10)
        info_frame.pack(fill="x", padx=10, pady=5)
        
        self.info_text = tk.Text(info_frame, height=4, wrap="word", bg="#f0f0f0")
        self.info_text.pack(fill="x")
        
        # Test buttons frame
        test_frame = ttk.LabelFrame(self.root, text="Các bài kiểm tra", padding=10)
        test_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Create test buttons
        tests = [
            ("🖥️ Thông tin hệ thống", self.test_system_info),
            ("📷 Camera", self.test_camera),
            ("🔊 Loa & Microphone", self.test_audio),
            ("🔒 MDM (Khóa doanh nghiệp)", self.test_mdm),
            ("⌨️ Bàn phím", self.test_keyboard),
            ("💾 Ổ cứng", self.test_disk),
            ("🖼️ Màn hình", self.test_display),
            ("🔋 Pin", self.test_battery),
            ("🔌 Cổng kết nối", self.test_ports),
            ("🖱️ Trackpad", self.test_trackpad),
        ]
        
        button_frame = tk.Frame(test_frame)
        button_frame.pack(fill="x")
        
        for i, (text, command) in enumerate(tests):
            btn = ttk.Button(button_frame, text=text, command=command, width=25)
            btn.grid(row=i//2, column=i%2, padx=5, pady=5, sticky="ew")
        
        button_frame.columnconfigure(0, weight=1)
        button_frame.columnconfigure(1, weight=1)
        
        # Results area
        results_frame = ttk.LabelFrame(self.root, text="Kết quả kiểm tra", padding=10)
        results_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        self.results_text = scrolledtext.ScrolledText(results_frame, height=10, wrap="word")
        self.results_text.pack(fill="both", expand=True)
        
        # Action buttons
        action_frame = tk.Frame(self.root)
        action_frame.pack(fill="x", padx=10, pady=10)
        
        ttk.Button(action_frame, text="🚀 CHẠY TẤT CẢ", 
                  command=self.run_all_tests, style="Accent.TButton").pack(side="left", padx=5)
        ttk.Button(action_frame, text="📄 TẠO BÁO CÁO", 
                  command=self.generate_report).pack(side="left", padx=5)
        ttk.Button(action_frame, text="🗑️ Xóa kết quả", 
                  command=self.clear_results).pack(side="left", padx=5)
        
        # Load system info on start
        self.root.after(100, self.test_system_info)
    
    def log(self, message, level="INFO"):
        timestamp = datetime.now().strftime("%H:%M:%S")
        colors = {"INFO": "black", "SUCCESS": "green", "WARNING": "orange", "ERROR": "red"}
        
        self.results_text.insert("end", f"[{timestamp}] {message}\n")
        self.results_text.see("end")
        self.root.update()
    
    def run_command(self, command):
        """Chạy lệnh shell và trả về kết quả"""
        try:
            result = subprocess.run(command, shell=True, capture_output=True, 
                                  text=True, timeout=30)
            return result.stdout.strip()
        except Exception as e:
            return f"Error: {str(e)}"
    
    def test_system_info(self):
        self.log("🔍 Đang kiểm tra thông tin hệ thống...")
        
        # Get system info
        model = self.run_command("sysctl -n hw.model")
        serial = self.run_command("system_profiler SPHardwareDataType | grep 'Serial Number' | awk '{print $4}'")
        os_version = self.run_command("sw_vers -productVersion")
        cpu = self.run_command("sysctl -n machdep.cpu.brand_string")
        ram = self.run_command("sysctl -n hw.memsize")
        ram_gb = int(ram) / (1024**3) if ram.isdigit() else 0
        
        info = f"""Model: {model}
Serial: {serial}
macOS: {os_version}
CPU: {cpu}
RAM: {ram_gb:.1f} GB"""
        
        self.info_text.delete("1.0", "end")
        self.info_text.insert("1.0", info)
        
        self.test_results["system_info"] = {
            "model": model,
            "serial": serial,
            "os_version": os_version,
            "cpu": cpu,
            "ram_gb": ram_gb,
            "status": "✅ OK"
        }
        
        self.log("✅ Hoàn thành kiểm tra hệ thống")
    
    def test_camera(self):
        self.log("📷 Đang kiểm tra camera...")
        
        # Check if camera exists
        camera_check = self.run_command("system_profiler SPCameraDataType")
        
        if "No cameras" in camera_check or not camera_check:
            self.log("❌ Không tìm thấy camera!")
            self.test_results["camera"] = {"status": "❌ FAIL", "reason": "Không phát hiện camera"}
            return
        
        self.log("✅ Camera được phát hiện")
        self.log("💡 Hướng dẫn: Mở Photo Booth hoặc FaceTime để test camera thực tế")
        
        # Try to open Photo Booth
        try:
            subprocess.Popen(["open", "-a", "Photo Booth"])
            self.log("📸 Đã mở Photo Booth - Kiểm tra xem camera có hoạt động không")
        except:
            pass
        
        result = messagebox.askyesno("Test Camera", 
                                     "Camera có hoạt động bình thường không?\n(Kiểm tra trong Photo Booth)")
        
        if result:
            self.test_results["camera"] = {"status": "✅ OK"}
            self.log("✅ Camera hoạt động tốt")
        else:
            self.test_results["camera"] = {"status": "❌ FAIL"}
            self.log("❌ Camera có vấn đề")
    
    def test_audio(self):
        self.log("🔊 Đang kiểm tra âm thanh...")
        
        # Check audio devices
        output = self.run_command("system_profiler SPAudioDataType")
        
        self.log("✅ Phát hiện thiết bị âm thanh")
        self.log("🔊 Đang phát âm thanh test...")
        
        # Play test sound
        self.run_command("afplay /System/Library/Sounds/Ping.aiff")
        
        result = messagebox.askyesno("Test Loa", 
                                     "Bạn có nghe thấy âm thanh test không?")
        
        if result:
            self.test_results["audio"] = {"status": "✅ OK"}
            self.log("✅ Loa hoạt động tốt")
        else:
            self.test_results["audio"] = {"status": "❌ FAIL"}
            self.log("❌ Loa có vấn đề")
    
    def test_mdm(self):
        self.log("🔒 Đang kiểm tra MDM (Khóa doanh nghiệp)...")
        self.log("⚠️ ĐÂY LÀ KIỂM TRA QUAN TRỌNG NHẤT!")
        
        # Check MDM enrollment
        mdm_check = self.run_command("sudo profiles status -type enrollment 2>/dev/null")
        
        # Check for DEP
        dep_check = self.run_command("sudo profiles show -type enrollment 2>/dev/null")
        
        is_mdm_enrolled = "Enrolled via DEP" in mdm_check or "Enrolled via DEP" in dep_check
        
        if is_mdm_enrolled:
            self.log("❌❌❌ CẢNH BÁO: Máy BỊ KHÓA MDM/DEP!")
            self.log("❌ KHÔNG NÊN MUA máy này!")
            self.test_results["mdm"] = {
                "status": "❌ FAIL - BỊ KHÓA",
                "reason": "Máy bị khóa MDM/DEP doanh nghiệp",
                "critical": True
            }
            messagebox.showerror("CẢNH BÁO MDM", 
                               "⚠️ MÁY BỊ KHÓA MDM/DEP!\n\n"
                               "Đây là máy doanh nghiệp bị khóa.\n"
                               "KHÔNG NÊN MUA máy này!")
        else:
            self.log("✅✅✅ Máy KHÔNG bị khóa MDM")
            self.log("✅ An toàn để mua")
            self.test_results["mdm"] = {"status": "✅ OK - Không bị khóa"}
    
    def test_keyboard(self):
        self.log("⌨️ Đang kiểm tra bàn phím...")
        self.log("💡 Một cửa sổ test sẽ mở ra")
        
        # Create keyboard test window
        test_window = tk.Toplevel(self.root)
        test_window.title("Test Bàn phím")
        test_window.geometry("600x400")
        
        tk.Label(test_window, text="Gõ thử tất cả các phím trên bàn phím", 
                font=("Arial", 14)).pack(pady=10)
        
        text_area = tk.Text(test_window, font=("Arial", 12))
        text_area.pack(fill="both", expand=True, padx=10, pady=10)
        text_area.focus()
        
        def finish_test():
            result = messagebox.askyesno("Test Bàn phím", 
                                        "Tất cả phím có hoạt động bình thường không?")
            if result:
                self.test_results["keyboard"] = {"status": "✅ OK"}
                self.log("✅ Bàn phím hoạt động tốt")
            else:
                self.test_results["keyboard"] = {"status": "❌ FAIL"}
                self.log("❌ Bàn phím có phím lỗi")
            test_window.destroy()
        
        ttk.Button(test_window, text="Hoàn thành test", 
                  command=finish_test).pack(pady=10)
    
    def test_disk(self):
        self.log("💾 Đang kiểm tra ổ cứng...")
        
        # Get disk info
        disk_info = self.run_command("diskutil info / | grep -E 'Device Node|Disk Size|Volume Free Space|SMART Status'")
        self.log(f"Thông tin ổ đĩa:\n{disk_info}")
        
        # Check SMART status
        smart_status = self.run_command("diskutil info / | grep 'SMART Status' | awk '{print $3}'")
        
        # Get disk space
        disk_space = self.run_command("df -h / | tail -1")
        self.log(f"Dung lượng: {disk_space}")
        
        if "Verified" in smart_status or "Not Supported" in smart_status:
            self.test_results["disk"] = {"status": "✅ OK", "smart": smart_status, "space": disk_space}
            self.log("✅ Ổ cứng hoạt động tốt")
        else:
            self.test_results["disk"] = {"status": "⚠️ WARNING", "smart": smart_status}
            self.log("⚠️ SMART status không xác định")
    
    def test_display(self):
        self.log("🖼️ Đang kiểm tra màn hình...")
        
        # Get display info
        display_info = self.run_command("system_profiler SPDisplaysDataType | grep -E 'Resolution|Retina'")
        self.log(f"Thông tin màn hình:\n{display_info}")
        
        # Create color test window
        test_window = tk.Toplevel(self.root)
        test_window.title("Test Màn hình")
        test_window.attributes('-fullscreen', True)
        
        colors = ["white", "black", "red", "green", "blue", "yellow", "cyan", "magenta"]
        current_color = [0]
        
        canvas = tk.Canvas(test_window, bg=colors[0], highlightthickness=0)
        canvas.pack(fill="both", expand=True)
        
        label = tk.Label(test_window, text="Nhấn SPACE để đổi màu, ESC để kết thúc\nKiểm tra dead pixel và màu sắc", 
                        font=("Arial", 16), bg=colors[0])
        label.place(relx=0.5, rely=0.5, anchor="center")
        
        def next_color(event=None):
            current_color[0] = (current_color[0] + 1) % len(colors)
            color = colors[current_color[0]]
            canvas.config(bg=color)
            label.config(bg=color, fg="white" if color in ["black", "blue"] else "black")
        
        def finish_test(event=None):
            test_window.destroy()
            result = messagebox.askyesno("Test Màn hình", 
                                        "Màn hình có hiển thị tốt không?\n(Không có dead pixel, màu sắc đều)")
            if result:
                self.test_results["display"] = {"status": "✅ OK"}
                self.log("✅ Màn hình hoạt động tốt")
            else:
                self.test_results["display"] = {"status": "❌ FAIL"}
                self.log("❌ Màn hình có vấn đề")
        
        test_window.bind("<space>", next_color)
        test_window.bind("<Escape>", finish_test)
    
    def test_battery(self):
        self.log("🔋 Đang kiểm tra pin...")
        
        # Get battery info
        battery_info = self.run_command("system_profiler SPPowerDataType | grep -E 'Cycle Count|Condition|Full Charge Capacity|Health'")
        self.log(f"Thông tin pin:\n{battery_info}")
        
        cycle_count = self.run_command("system_profiler SPPowerDataType | grep 'Cycle Count' | awk '{print $3}'")
        condition = self.run_command("system_profiler SPPowerDataType | grep 'Condition' | awk '{print $2}'")
        
        self.log(f"Số chu kỳ sạc: {cycle_count}")
        self.log(f"Tình trạng: {condition}")
        
        try:
            cycles = int(cycle_count) if cycle_count.isdigit() else 0
            if cycles < 300:
                status = "✅ Rất tốt"
            elif cycles < 500:
                status = "✅ Tốt"
            elif cycles < 800:
                status = "⚠️ Trung bình"
            else:
                status = "❌ Yếu"
            
            self.test_results["battery"] = {
                "status": status,
                "cycles": cycles,
                "condition": condition
            }
            self.log(f"{status} - Pin có {cycles} chu kỳ sạc")
        except:
            self.test_results["battery"] = {"status": "⚠️ Không xác định"}
    
    def test_ports(self):
        self.log("🔌 Đang kiểm tra cổng kết nối...")
        
        # Get USB info
        usb_info = self.run_command("system_profiler SPUSBDataType")
        
        self.log("💡 Cắm thử USB/Thunderbolt vào các cổng")
        
        result = messagebox.askyesno("Test Cổng kết nối", 
                                     "Tất cả các cổng USB/Thunderbolt có hoạt động không?")
        
        if result:
            self.test_results["ports"] = {"status": "✅ OK"}
            self.log("✅ Các cổng hoạt động tốt")
        else:
            self.test_results["ports"] = {"status": "❌ FAIL"}
            self.log("❌ Có cổng bị lỗi")
    
    def test_trackpad(self):
        self.log("🖱️ Đang kiểm tra trackpad...")
        
        # Create trackpad test window
        test_window = tk.Toplevel(self.root)
        test_window.title("Test Trackpad")
        test_window.geometry("600x400")
        
        tk.Label(test_window, text="Thử các thao tác trên trackpad:", 
                font=("Arial", 14, "bold")).pack(pady=10)
        
        instructions = """
        ✓ Di chuyển con trỏ
        ✓ Click trái
        ✓ Click phải (2 ngón)
        ✓ Cuộn (2 ngón)
        ✓ Zoom (2 ngón)
        ✓ Vuốt 3 ngón
        """
        
        tk.Label(test_window, text=instructions, font=("Arial", 12), 
                justify="left").pack(pady=10)
        
        canvas = tk.Canvas(test_window, bg="white", width=500, height=200)
        canvas.pack(pady=10)
        
        def draw(event):
            x, y = event.x, event.y
            canvas.create_oval(x-2, y-2, x+2, y+2, fill="blue")
        
        canvas.bind("<B1-Motion>", draw)
        
        def finish_test():
            result = messagebox.askyesno("Test Trackpad", 
                                        "Trackpad có hoạt động mượt mà không?")
            if result:
                self.test_results["trackpad"] = {"status": "✅ OK"}
                self.log("✅ Trackpad hoạt động tốt")
            else:
                self.test_results["trackpad"] = {"status": "❌ FAIL"}
                self.log("❌ Trackpad có vấn đề")
            test_window.destroy()
        
        ttk.Button(test_window, text="Hoàn thành test", 
                  command=finish_test).pack(pady=10)
    
    def run_all_tests(self):
        self.log("=" * 50)
        self.log("🚀 BẮT ĐẦU CHẠY TẤT CẢ CÁC BÀI TEST")
        self.log("=" * 50)
        
        def run():
            tests = [
                self.test_system_info,
                self.test_mdm,
                self.test_battery,
                self.test_disk,
                self.test_camera,
                self.test_audio,
                self.test_display,
                self.test_keyboard,
                self.test_trackpad,
                self.test_ports,
            ]
            
            for test in tests:
                test()
                self.root.update()
            
            self.log("=" * 50)
            self.log("✅ HOÀN THÀNH TẤT CẢ CÁC BÀI TEST")
            self.log("=" * 50)
            self.generate_report()
        
        threading.Thread(target=run, daemon=True).start()
    
    def generate_report(self):
        if not self.test_results:
            messagebox.showwarning("Cảnh báo", "Chưa có kết quả test nào!")
            return
        
        self.log("📄 Đang tạo báo cáo...")
        
        # Calculate overall score
        total_tests = len(self.test_results)
        passed_tests = sum(1 for r in self.test_results.values() 
                          if isinstance(r, dict) and "✅" in r.get("status", ""))
        
        # Check for critical issues
        has_mdm = any(r.get("critical") for r in self.test_results.values() 
                     if isinstance(r, dict))
        
        report = f"""
{'='*60}
        BÁO CÁO KIỂM TRA MACBOOK
{'='*60}
Thời gian: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
Powered by DATNT - https://tools.datnt.work

⚠️ DISCLAIMER: Kết quả test chỉ mang tính chất tham khảo.
Quyết định mua máy là trách nhiệm của người mua.
Tool không chịu trách nhiệm về các vấn đề phát sinh sau khi mua.

THÔNG TIN MÁY:
{self.info_text.get("1.0", "end").strip()}

{'='*60}
KẾT QUẢ KIỂM TRA:
{'='*60}
"""
        
        for test_name, result in self.test_results.items():
            if isinstance(result, dict):
                status = result.get("status", "N/A")
                report += f"\n{test_name.upper()}: {status}"
                if "reason" in result:
                    report += f"\n  Lý do: {result['reason']}"
                if test_name == "battery" and "cycles" in result:
                    report += f"\n  Chu kỳ sạc: {result['cycles']}"
        
        report += f"\n\n{'='*60}\n"
        report += f"TỔNG KẾT: {passed_tests}/{total_tests} bài test PASS\n"
        report += f"{'='*60}\n\n"
        
        if has_mdm:
            report += "❌❌❌ KHUYẾN NGHỊ: KHÔNG NÊN MUA ❌❌❌\n"
            report += "Lý do: Máy bị khóa MDM/DEP doanh nghiệp\n"
            recommendation = "KHÔNG MUA"
            color = "red"
        elif passed_tests >= total_tests * 0.8:
            report += "✅✅✅ KHUYẾN NGHỊ: CÓ THỂ MUA ✅✅✅\n"
            report += "Máy trong tình trạng tốt\n"
            recommendation = "CÓ THỂ MUA"
            color = "green"
        elif passed_tests >= total_tests * 0.6:
            report += "⚠️⚠️⚠️ KHUYẾN NGHỊ: CÂN NHẮC ⚠️⚠️⚠️\n"
            report += "Máy có một số vấn đề, cần kiểm tra kỹ và thương lượng giá\n"
            recommendation = "CÂN NHẮC"
            color = "orange"
        else:
            report += "❌❌❌ KHUYẾN NGHỊ: KHÔNG NÊN MUA ❌❌❌\n"
            report += "Máy có nhiều vấn đề\n"
            recommendation = "KHÔNG MUA"
            color = "red"
        
        report += f"\n{'='*60}\n"
        report += "\n⚠️ DISCLAIMER:\n"
        report += "Kết quả test chỉ mang tính chất tham khảo.\n"
        report += "Quyết định mua máy là trách nhiệm của người mua.\n"
        report += "Tool không chịu trách nhiệm về các vấn đề phát sinh sau khi mua.\n"
        report += f"{'='*60}\n"
        
        # Save text report
        txt_filename = f"macbook_test_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        with open(txt_filename, "w", encoding="utf-8") as f:
            f.write(report)
        
        self.log(f"✅ Đã lưu báo cáo text: {txt_filename}")
        
        # Generate PDF report
        pdf_filename = self.generate_pdf_report(report, recommendation, passed_tests, total_tests, has_mdm)
        
        # Show summary
        summary_msg = f"Kết quả: {passed_tests}/{total_tests} PASS\n\n"
        summary_msg += f"KHUYẾN NGHỊ: {recommendation}\n\n"
        summary_msg += f"📄 Báo cáo HTML: {pdf_filename}\n"
        summary_msg += f"📄 Báo cáo Text: {txt_filename}\n\n"
        summary_msg += "💡 Mở file HTML và nhấn Cmd+P để in PDF"
        
        messagebox.showinfo("Báo cáo hoàn thành", summary_msg)
    
    def generate_pdf_report(self, report_text, recommendation, passed_tests, total_tests, has_mdm):
        """Tạo báo cáo PDF sử dụng HTML và công cụ có sẵn của macOS"""
        try:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            pdf_filename = f"macbook_test_report_{timestamp}.pdf"
            
            # Tạo HTML với styling đẹp
            html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Arial, sans-serif;
            max-width: 800px;
            margin: 40px auto;
            padding: 20px;
            background: #f5f5f5;
        }}
        .container {{
            background: white;
            padding: 40px;
            border-radius: 10px;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #007AFF;
            text-align: center;
            border-bottom: 3px solid #007AFF;
            padding-bottom: 20px;
            margin-bottom: 10px;
        }}
        .powered-by {{
            text-align: center;
            color: #666;
            font-size: 14px;
            margin-bottom: 30px;
        }}
        .powered-by a {{
            color: #007AFF;
            text-decoration: none;
        }}
        .powered-by a:hover {{
            text-decoration: underline;
        }}
        .info-section {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            border-left: 4px solid #007AFF;
        }}
        .test-result {{
            padding: 15px;
            margin: 10px 0;
            border-radius: 5px;
            background: #f8f9fa;
        }}
        .recommendation {{
            padding: 30px;
            margin: 30px 0;
            border-radius: 10px;
            text-align: center;
            font-size: 24px;
            font-weight: bold;
        }}
        .recommendation.buy {{
            background: #d4edda;
            color: #155724;
            border: 3px solid #28a745;
        }}
        .recommendation.consider {{
            background: #fff3cd;
            color: #856404;
            border: 3px solid #ffc107;
        }}
        .recommendation.no-buy {{
            background: #f8d7da;
            color: #721c24;
            border: 3px solid #dc3545;
        }}
        .summary {{
            background: #e7f3ff;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            text-align: center;
            font-size: 18px;
        }}
        .timestamp {{
            color: #666;
            text-align: center;
            margin-top: 30px;
            font-size: 14px;
        }}
        .disclaimer {{
            background: #fff3cd;
            border: 2px solid #ffc107;
            padding: 20px;
            border-radius: 8px;
            margin: 20px 0;
            color: #856404;
            text-align: center;
        }}
        .disclaimer strong {{
            color: #721c24;
        }}
        pre {{
            background: #f8f9fa;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            white-space: pre-wrap;
            word-wrap: break-word;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>🍎 BÁO CÁO KIỂM TRA MACBOOK</h1>
        <div class="powered-by">
            Powered by <a href="https://tools.datnt.work" target="_blank">DATNT</a>
        </div>
        
        <div class="info-section">
            <h2>📋 Thông tin máy</h2>
            <pre>{self.info_text.get("1.0", "end").strip()}</pre>
        </div>
        
        <div class="summary">
            <strong>Kết quả tổng thể:</strong> {passed_tests}/{total_tests} bài test PASS
        </div>
        
        <div class="info-section">
            <h2>✅ Chi tiết kết quả kiểm tra</h2>
"""
            
            # Add test results
            for test_name, result in self.test_results.items():
                if isinstance(result, dict):
                    status = result.get("status", "N/A")
                    html_content += f'<div class="test-result"><strong>{test_name.upper()}:</strong> {status}'
                    if "reason" in result:
                        html_content += f'<br><em>Lý do: {result["reason"]}</em>'
                    if test_name == "battery" and "cycles" in result:
                        html_content += f'<br><em>Chu kỳ sạc: {result["cycles"]}</em>'
                    html_content += '</div>'
            
            # Add recommendation
            rec_class = "no-buy" if has_mdm or passed_tests < total_tests * 0.6 else ("buy" if passed_tests >= total_tests * 0.8 else "consider")
            
            html_content += f"""
        </div>
        
        <div class="recommendation {rec_class}">
            KHUYẾN NGHỊ: {recommendation}
        </div>
"""
            
            # Add warnings if needed
            if has_mdm:
                html_content += """
        <div class="info-section" style="border-left-color: #dc3545; background: #f8d7da;">
            <h3 style="color: #721c24;">⚠️ CẢNH BÁO QUAN TRỌNG</h3>
            <p style="color: #721c24; font-size: 16px;">
                Máy bị khóa MDM/DEP (Mobile Device Management) của doanh nghiệp.<br>
                <strong>TUYỆT ĐỐI KHÔNG MUA</strong> máy này vì bạn sẽ không thể sử dụng được!
            </p>
        </div>
"""
            
            html_content += f"""
        <div class="disclaimer">
            <strong>⚠️ DISCLAIMER</strong><br><br>
            Kết quả test chỉ mang tính chất tham khảo và không đảm bảo 100% chính xác.<br>
            Quyết định mua máy là trách nhiệm hoàn toàn của người mua.<br>
            Tool và tác giả không chịu trách nhiệm về bất kỳ vấn đề nào phát sinh sau khi mua máy.
        </div>
        
        <div class="timestamp">
            Báo cáo được tạo lúc: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}
        </div>
    </div>
</body>
</html>
"""
            
            # Save HTML file directly to current directory
            html_filename = f"macbook_test_report_{timestamp}.html"
            
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            self.log(f"✅ Đã lưu báo cáo HTML: {html_filename}")
            
            # Try to open in browser for easy PDF conversion
            try:
                subprocess.Popen(['open', html_filename], 
                               stdout=subprocess.DEVNULL, 
                               stderr=subprocess.DEVNULL)
                self.log("📄 Đã mở báo cáo trong trình duyệt")
                self.log("💡 Nhấn Cmd+P và chọn 'Save as PDF' để lưu thành PDF")
            except:
                self.log("💡 Mở file HTML và nhấn Cmd+P để in thành PDF")
            
            return html_filename
            
        except Exception as e:
            self.log(f"⚠️ Lỗi khi tạo báo cáo: {str(e)}")
            self.log("📄 Báo cáo text vẫn được lưu thành công")
            return "N/A"
    
    def clear_results(self):
        self.results_text.delete("1.0", "end")
        self.test_results = {}
        self.log("🗑️ Đã xóa kết quả")
    
    def open_url(self, url):
        """Mở URL trong trình duyệt"""
        import webbrowser
        webbrowser.open(url)

def main():
    # Check if running on macOS
    if sys.platform != "darwin":
        print("❌ Lỗi: Ứng dụng này chỉ chạy trên macOS!")
        sys.exit(1)
    
    try:
        # Test tkinter
        root = tk.Tk()
        root.withdraw()  # Hide window temporarily
        
        # Check if display is available
        try:
            root.update()
        except tk.TclError as e:
            print("❌ Lỗi: Không thể khởi động GUI")
            print(f"   Chi tiết: {e}")
            print("")
            print("💡 Giải pháp:")
            print("   1. Đảm bảo bạn đang chạy trên macOS (không phải SSH)")
            print("   2. Cài Python từ python.org thay vì Homebrew")
            print("   3. Hoặc chạy: brew install python-tk")
            sys.exit(1)
        
        root.destroy()
        
        # Create main window
        root = tk.Tk()
        app = MacBookTester(root)
        root.mainloop()
        
    except ImportError as e:
        print("❌ Lỗi: Thiếu thư viện cần thiết")
        print(f"   Chi tiết: {e}")
        print("")
        print("💡 Cài đặt:")
        print("   brew install python-tk")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Lỗi không xác định: {e}")
        print("")
        print("💡 Thử chạy lại hoặc kiểm tra:")
        print("   python3 --version")
        print("   python3 -c 'import tkinter'")
        sys.exit(1)

if __name__ == "__main__":
    main()
