from capture import start_capture
from test_scan import start_test_scan
from log_analyzer import analyze_log
from ransomware_detector import start_ransomware_monitor
from test_ransomware import simulate_ransomware

import threading
import time

capture_thread = threading.Thread(
    target=start_capture,
    daemon = True

)

capture_thread.start()
ransomware_observer = (
    start_ransomware_monitor()
)
print("IDS Started...")

time.sleep(5)

start_test_scan()
analyze_log()
simulate_ransomware()

capture_thread.join()