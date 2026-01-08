import psutil
import platform
import time
from .base import Monitor

class disk_Monitor(Monitor):

    def getDisk(self):
        return psutil.disk_usage('/').percent

    def getInstantDiskRead(self):
        io = psutil.disk_io_counters(perdisk=False)
        return round(io.read_bytes/(1024 ** 2), 2)
    
    def getInstantDiskWrite(self):
        io = psutil.disk_io_counters(perdisk=False)
        return round(io.write_bytes/(1024 ** 2), 2)
    
    def printInfo(self):
        io = psutil.disk_io_counters(perdisk=False)
        print("Disk Drive %: " + psutil.disk_usage('/').percent)
        print("Disk Written (MB/S): " + round(io.read_bytes/(1024 ** 2), 2))
        print("Disk Read (MB/S): " + round(io.write_bytes/(1024 ** 2), 2))


#Testing mainQ  
def main():
    diskmonitor = disk_Monitor("diskMonitor", 5)
    print("Disk Drive Percentage: " + str(diskmonitor.getDisk()))
    diskmonitor.start()

if __name__ == "__main__":
    main()