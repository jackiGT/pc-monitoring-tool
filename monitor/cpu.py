import psutil
import platform
import time
from base import Monitor

class CPU_Monitor(Monitor):
    def update(self):
        interval = super().getInterval()
        starttime = time.monotonic()
        while self.running:
            print("CPU usage (%):", psutil.cpu_percent(interval=1))
            time.sleep(interval - ((time.monotonic() - starttime) % interval))

    def getCores(self, logic):
        return psutil.cpu_count(logical=logic)


#Testing mainQ  
def main():
    cpuMonitor = CPU_Monitor("cpuMonitor", 5)
    print(cpuMonitor.getCores(True))
    cpuMonitor.start()

if __name__ == "__main__":
    main()


