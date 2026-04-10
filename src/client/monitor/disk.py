"""
Author: Jackie Liu
Date: 1/8/2026
Desc: Disk monitor subclass, collections on disk drive, disk read/written.
"""
import time
import psutil
from .base import Monitor

class disk_Monitor(Monitor):

    # Disk usage percentage (of total capacity)
    def getDisk(self):
        return psutil.disk_usage('/').percent

    # Disk drive read total (since last shutdown)
    def getTotalDiskRead(self):
        io = psutil.disk_io_counters(perdisk=False)
        return round(io.read_bytes/(1024 ** 2), 2)
    
    # Disk drive written total (since last shutdown)
    def getTotalDiskWrite(self):
        io = psutil.disk_io_counters(perdisk=False)
        return round(io.write_bytes/(1024 ** 2), 2)
    
    # Calculates real-time disk read/write speed in MB/s
    # Samples IO counters 0.2 seconds apart and divides
    # delta by interval to get instantaneous throughput
    def getInstantDiskWrite(self):
        interval = .2

        before = psutil.disk_io_counters(perdisk=False).write_bytes
        time.sleep(interval)
        after = psutil.disk_io_counters(perdisk=False).write_bytes

        return round(((after - before)/interval)/(1024 ** 2), 2)
    def getInstantDiskRead(self):
        interval = .2

        before = psutil.disk_io_counters(perdisk=False).read_bytes
        time.sleep(interval)
        after = psutil.disk_io_counters(perdisk=False).read_bytes

        return round(((after - before)/interval)/(1024 ** 2), 2)
    
    def printInfo(self):
        io = psutil.disk_io_counters(perdisk=False)
        print("Disk Drive %: " + psutil.disk_usage('/').percent)
        print("Disk Written (MB/S): " + round(io.read_bytes/(1024 ** 2), 2))
        print("Disk Read (MB/S): " + round(io.write_bytes/(1024 ** 2), 2))


#Testing mainQ  
if __name__ == "__main__":
    interval = .2

    before = psutil.disk_io_counters(perdisk=False).write_bytes
    time.sleep(interval)
    after = psutil.disk_io_counters(perdisk=False).write_bytes
    print(round(((after - before)/interval)/(1024 ** 2), 2))