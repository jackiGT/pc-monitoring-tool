import psutil
import platform
import time
from base import Monitor

class CPU_Monitor(Monitor):
    def update(self):
        starttime = time.monotonic()
        while self.running:
            print("CPU usage (%):", psutil.cpu_percent(interval=1))
            print("CPU Cores: ", psutil.cpu_count(logical=True))
            time.sleep(super().getInterval(self) - ((time.monotonic() - starttime) % super().getInterval(self)))


