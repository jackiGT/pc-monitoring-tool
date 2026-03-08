"""
Author: Jackie Liu
Date: 1/8/2026
Desc: RAM monitor subclass, collections on ram usage.
"""

import psutil
from .base import Monitor

class RAM_Monitor(Monitor):

    def getRAMPercent(self):
        ram = psutil.virtual_memory()
        return ram.percent

    def getRAM(self):
        ram = psutil.virtual_memory()
        return round(ram.used / 1e9, 2)

    def getInstant(self):
        ram = psutil.virtual_memory()
        print("RAM usage (%): " + str(ram.percent))


#Testing mainQ  
def main():
    RAMmonitor = RAM_Monitor("RAMmonitor", 5)
    RAMmonitor.start()

if __name__ == "__main__":
    main()