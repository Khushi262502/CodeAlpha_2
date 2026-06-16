from capture import start_capture
from test_scan import start_test_scan
from log_analyzer import analyze_log

import threading
import time

capture_thread = threading.Thread(
    target=start_capture,
    daemon = True

)

capture_thread.start()
print("IDS Started...")

time.sleep(5)

start_test_scan()
analyze_log()

capture_thread.join()