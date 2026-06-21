from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import time
from alert import generate_alert

changes = []


class RansomwareHandler(
    FileSystemEventHandler
):

    def on_modified(
        self,
        event
    ):

        if not event.is_directory:

            changes.append(
                time.time()
            )

            print(
                f"Modified: {event.src_path}"
            )

            detect_ransomware()


def detect_ransomware():

    current_time = time.time()

    recent_changes = [

        t for t in changes

        if current_time - t <= 10

    ]

    if len(recent_changes) >= 5:

        generate_alert(
            "Possible Ransomware Activity Detected",
            "CRITICAL"
        )


def start_ransomware_monitor():

    path = "test"

    observer = Observer()

    observer.schedule(
        RansomwareHandler(),
        path,
        recursive=True
    )

    observer.start()

    print(
        "Ransomware Monitor Started..."
    )

    return observer