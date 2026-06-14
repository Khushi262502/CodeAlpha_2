import socket
import time

def start_test_scan():

    target = "127.0.0.1"

    print("Starting Port Scan Test...")

    for port in range(1, 50):

        try:

            s = socket.socket()

            s.settimeout(0.1)

            s.connect(
                (target, port)
            )

        except:

            pass

        finally:

            s.close()

    print("Scan Completed")