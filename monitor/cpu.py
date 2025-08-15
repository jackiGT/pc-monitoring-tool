import psutil
import platform
import time

def monitorCPU():
    starttime = time.monotonic()
    while True:
        print("CPU usage (%):", psutil.cpu_percent(interval=1))
        print("CPU Cores: ", psutil.cpu_count(logical=True))
        time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))

