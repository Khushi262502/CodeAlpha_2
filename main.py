from capture import start_capture
from test_scan import start_test_scan
from log_analyzer import analyze_log
from ransomware_detector import start_ransomware_monitor
from test_ransomware import simulate_ransomware
from dashboard import start_dashboard

import threading
import time


capture_thread = threading.Thread(
    target=start_capture,
    daemon=True
)

dashboard_thread = threading.Thread(
    target=start_dashboard,
    daemon=True
)

capture_thread.start()

start_ransomware_monitor()

dashboard_thread.start()

print("IDS Started...")
print("Dashboard Running at http://127.0.0.1:5000")

time.sleep(5)

start_test_scan()

analyze_log()

simulate_ransomware()

while True:

    time.sleep(1)