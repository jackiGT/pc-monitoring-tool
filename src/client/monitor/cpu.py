"""
Author: Jackie Liu
Date: 1/8/2026
Desc: CPU monitor subclass, collections on CPU usage, # cores/logical cores.
"""

import psutil
from .base import Monitor

class CPU_Monitor(Monitor):
    
    def getCores(self, logic):
        return psutil.cpu_count(logical=logic)
    
    def getInstantCPUPercent(self):
        return psutil.cpu_percent(interval=1)
    
    def printInfo(self):
        print("Cores (#): " + str(psutil.cpu_count(logical=True)))
        print("CPU (%): " + str(psutil.cpu_percent(interval=1)))

#Testing mainQ  
def main():
    cpuMonitor = CPU_Monitor("cpuMonitor", 5)
    print(cpuMonitor.getCores(True))
    cpuMonitor.printInfo()

if __name__ == "__main__":
    main()


