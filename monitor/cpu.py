import psutil
import platform
import time
from .base import Monitor

class CPU_Monitor(Monitor):
    
    def getCores(self, logic):
        return psutil.cpu_count(logical=logic)
    
    def getInstantCPUPercent(self):
        return psutil.cpu_percent(interval=1)
    
    def getInstant(self):
        return str(psutil.cpu_percent(interval=0))
    
    def printInfo(self):
        print("Cores (#): " + psutil.cpu_count(logical=True))
        print("CPU (%): " + psutil.cpu_percent(interval=1))
        print("CPU (MB): " + psutil.cpu_percent(interval=1))

#Testing mainQ  
def main():
    cpuMonitor = CPU_Monitor("cpuMonitor", 5)
    print(cpuMonitor.getCores(True))
    cpuMonitor.printInfo()

if __name__ == "__main__":
    main()


