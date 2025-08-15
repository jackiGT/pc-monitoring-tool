import psutil
import platform
import time

io = psutil.disk_io_counters(perdisk=False)

def DiskUsage():
    print("Disk usage (%):", psutil.disk_usage('/').percent)

def monitorDiskActivity():
    starttime = time.monotonic()
    while True:
        print("Disk Activity (MB read):", round(io.read_bytes/(1024 ** 2), 2))
        print("Disk Activity (MB write):", round(io.write_bytes/(1024 ** 2), 2))
        time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))

DiskUsage()
monitorDiskActivity()