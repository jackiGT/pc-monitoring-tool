import psutil
import platform
import time
from base import Monitor

class RAM_Monitor(Monitor):

    def update(self):
        interval = super().getInterval()
        starttime = time.monotonic()
        while self.running:
            ram = psutil.virtual_memory()
            print("RAM usage (%):", ram.percent)
            print("RAM used (GB):", round(ram.used / 1e9, 2))
            time.sleep(interval - ((time.monotonic() - starttime) % interval))


#Testing mainQ  
def main():
    RAMmonitor = RAM_Monitor("RAMmonitor", 5)
    RAMmonitor.start()

if __name__ == "__main__":
    main()