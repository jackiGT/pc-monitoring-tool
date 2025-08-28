import psutil
import platform
import time
from base import Monitor

# Instantaneous network speed per minute
class network_Monitor(Monitor):
    def __init__(self, mode=None):
        super().__init__()
        self.mode = mode

    def monitorNetworkInstant(self):
        starttime = time.monotonic()
        while network_Monitor.running:
            #network sent and recieved (in MB)
            networkSentB = psutil.net_io_counters().bytes_sent
            networkRecvB = psutil.net_io_counters().bytes_recv
            time.sleep(1)
            networkSentA = psutil.net_io_counters().bytes_sent
            networkRecvA = psutil.net_io_counters().bytes_recv

            netUploadSpeed = abs(networkSentB-networkSentA)
            netDownloadSpeed = abs(networkRecvB-networkRecvA)
            # print every minute
            print("Upload Speed (KB/s): ", round(netUploadSpeed/1024, 2))
            print("Download Speed (KB/s): ", round(netDownloadSpeed/1024, 2))
            time.sleep(super().getInterval(self) - ((time.monotonic() - starttime) % super().getInterval(self)))

    # Average network speed per minute
    def monitorNetworkAvg(self):
        starttime = time.monotonic()
        while True:
            #network sent and recieved (in MB)
            networkSentB = psutil.net_io_counters().bytes_sent
            networkRecvB = psutil.net_io_counters().bytes_recv
            time.sleep(super().getInterval(self) - ((time.monotonic() - starttime) % super().getInterval(self)))
            networkSentA = psutil.net_io_counters().bytes_sent
            networkRecvA = psutil.net_io_counters().bytes_recv

            netUploadSpeed = abs(networkSentB-networkSentA)
            netDownloadSpeed = abs(networkRecvB-networkRecvA)

            avgUploadSpeed = netUploadSpeed/60
            avgDownloadSpeed = netDownloadSpeed/60

            # print every minute
            print("Average Upload Speed (KB/s): ", round(avgUploadSpeed/1024, 2))
            print("Average Download Speed (KB/s): ", round(avgDownloadSpeed/1024, 2))

    def update(self):
        self.data = self.mode()
