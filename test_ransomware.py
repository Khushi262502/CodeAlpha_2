import os
import time

def simulate_ransomware():

    print("Starting Ransomware Simulation...")

    time.sleep(5)

    for i in range(10):

        filename = f"test/file{i}.txt"

        with open(filename, "w") as f:

            f.write("encrypted data")

        print(f"Modified: {filename}")

        time.sleep(0.5)

    print("Simulation Finished")