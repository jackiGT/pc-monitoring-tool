import psutil
import time
from base import Monitor

# Instantaneous network speed per minute
class network_Monitor(Monitor):
    def __init__(self, name, interval, mode=None):
        super().__init__(name, interval)
        self.mode = mode

    def monitorNetworkInstant(self):

        #network sent and recieved (in KB)
        networkSentB = psutil.net_io_counters().bytes_sent
        networkRecvB = psutil.net_io_counters().bytes_recv
        time.sleep(1)
        networkSentA = psutil.net_io_counters().bytes_sent
        networkRecvA = psutil.net_io_counters().bytes_recv

        netUploadSpeed = abs(networkSentB-networkSentA)
        netDownloadSpeed = abs(networkRecvB-networkRecvA)

        # print every minute
        print("Instant Upload Speed (KB/s): ", round(netUploadSpeed/1024, 2))
        print("Instant Download Speed (KB/s): ", round(netDownloadSpeed/1024, 2))

    # Average network speed per minute
    def monitorNetworkAvg(self):

        starttime = time.monotonic()

        #network sent and recieved (in KB) (point B)
        networkSentB = psutil.net_io_counters().bytes_sent
        networkRecvB = psutil.net_io_counters().bytes_recv

        sleepTime = max(0, self.getInterval() - ((time.monotonic() - starttime) % self.getInterval()))
        time.sleep(sleepTime)

        #network sent and recieved (in KB) (point A)
        networkSentA = psutil.net_io_counters().bytes_sent
        networkRecvA = psutil.net_io_counters().bytes_recv

        netUploadSpeed = abs(networkSentB-networkSentA)
        netDownloadSpeed = abs(networkRecvB-networkRecvA)

        avgUploadSpeed = netUploadSpeed/60
        avgDownloadSpeed = netDownloadSpeed/60

        # print every minute
        print("Average Upload Speed (KB/s): ", round(avgUploadSpeed/1024, 2))
        print("Average Download Speed (KB/s): ", round(avgDownloadSpeed/1024, 2))

    def update(self, mode):
        self.mode = mode
        mode()

    def start(self, mode):
        self.running = True
        self.status = "Active"

        interval = self.getInterval()
        starttime = time.monotonic() # time information necessary!

        while self.running:
            self.update(mode)
            sleepTime = max(0, interval - ((time.monotonic() - starttime) % interval))
            time.sleep(sleepTime)


#Testing main
def main():
    netmonitor = network_Monitor("NetworkMonitor1", 5)
    netmonitor.start(netmonitor.monitorNetworkInstant)

if __name__ == "__main__":
    main()