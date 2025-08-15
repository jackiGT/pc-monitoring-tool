import psutil
import platform
import time


def monitorRAM():
    starttime = time.monotonic()
    while True:
        ram = psutil.virtual_memory()
        print("RAM usage (%):", ram.percent)
        print("RAM used (GB):", round(ram.used / 1e9, 2))
        time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))