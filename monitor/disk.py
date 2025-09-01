import psutil
import platform
import time
from base import Monitor

io = psutil.disk_io_counters(perdisk=False)
class disk_Monitor(Monitor):

    def getDisk(self):
        return psutil.disk_usage('/').percent

    def update(self):
        interval = super().getInterval()
        starttime = time.monotonic()
        while self.running:
            print("Disk Activity (MB read):", round(io.read_bytes/(1024 ** 2), 2))
            print("Disk Activity (MB write):", round(io.write_bytes/(1024 ** 2), 2))
            time.sleep(interval - ((time.monotonic() - starttime) % interval))


#Testing mainQ  
def main():
    diskmonitor = disk_Monitor("diskMonitor", 5)
    print("Disk Drive Percentage: " + str(diskmonitor.getDisk()))
    diskmonitor.start()

if __name__ == "__main__":
    main()