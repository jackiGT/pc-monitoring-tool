"""
Author: Jackie Liu
Date: 1/8/2026
Desc: RAM monitor subclass, collections on RAM (memory) usage.
"""

import psutil
from .base import Monitor

class RAM_Monitor(Monitor):

    # Ram used in percent
    def getRAMPercent(self):
        ram = psutil.virtual_memory()
        return ram.percent

    # Ram used in GB
    def getRAM(self):
        ram = psutil.virtual_memory()
        return round(ram.used / 1e9, 2)

    # Ram used in percent
    def getInstant(self):
        ram = psutil.virtual_memory()
        print("RAM usage (%): " + str(ram.percent))


#Testing mainQ  
def main():
    RAMmonitor = RAM_Monitor("RAMmonitor", 5)
    RAMmonitor.start()

if __name__ == "__main__":
    main()