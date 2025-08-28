import psutil
import platform
import time
from base import Monitor

class RAM_Monitor(Monitor):

    def update(self):
        starttime = time.monotonic()
        while RAM_Monitor.running:
            ram = psutil.virtual_memory()
            print("RAM usage (%):", ram.percent)
            print("RAM used (GB):", round(ram.used / 1e9, 2))
            time.sleep(super().getInterval(self) - ((time.monotonic() - starttime) % super().getInterval(self)))