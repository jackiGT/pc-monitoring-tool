import psutil
import platform
import time
from base import Monitor

io = psutil.disk_io_counters(perdisk=False)
class disk_Monitor(Monitor):

    def DiskUsage():
        print("Disk drive usage (%):", psutil.disk_usage('/').percent)

    def update(self):
        starttime = time.monotonic()
        while disk_Monitor.running:
            print("Disk Activity (MB read):", round(io.read_bytes/(1024 ** 2), 2))
            print("Disk Activity (MB write):", round(io.write_bytes/(1024 ** 2), 2))
            time.sleep(super().getInterval(self) - ((time.monotonic() - starttime) % super().getInterval(self)))