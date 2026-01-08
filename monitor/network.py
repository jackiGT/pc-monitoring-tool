import psutil
import time
from .base import Monitor

# Instantaneous network speed per minute
class network_Monitor(Monitor):

    def printNetworkInstant(self):

        #network sent and recieved (in KB)
        networkSentB = psutil.net_io_counters().bytes_sent
        networkRecvB = psutil.net_io_counters().bytes_recv
        time.sleep(1)
        networkSentA = psutil.net_io_counters().bytes_sent
        networkRecvA = psutil.net_io_counters().bytes_recv

        netUploadSpeed = abs(networkSentB-networkSentA)
        netDownloadSpeed = abs(networkRecvB-networkRecvA)

        print("Instant Upload Speed (KB/s): ", round(netUploadSpeed/1024, 2))
        print("Instant Download Speed (KB/s): ", round(netDownloadSpeed/1024, 2))

    # Average network speed per minute
    def printNetworkAvg(self):

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
    
    def getNetworkDownload(self):
        #network sent and recieved (in KB)
        networkRecvB = psutil.net_io_counters().bytes_recv
        time.sleep(1)
        networkRecvA = psutil.net_io_counters().bytes_recv

        netDownloadSpeed = abs(networkRecvB-networkRecvA)

        return round(netDownloadSpeed/1024, 2)
    
    def getNetworkUpload(self):
        #network sent and recieved (in KB)
        networkSentB = psutil.net_io_counters().bytes_sent
        time.sleep(1)
        networkSentA = psutil.net_io_counters().bytes_sent


        netUploadSpeed = abs(networkSentB-networkSentA)

        return round(netUploadSpeed/1024, 2)

    def getInstant(self):
        #network sent and recieved (in KB)
        networkSentB = psutil.net_io_counters().bytes_sent
        time.sleep(1)
        networkSentA = psutil.net_io_counters().bytes_sent


        netUploadSpeed = abs(networkSentB-networkSentA)

        return "Instant Upload Speed (KB/s): " + str(round(netUploadSpeed/1024, 2))   



#Testing main
def main():
    netmonitor = network_Monitor("NetworkMonitor1", 5)

if __name__ == "__main__":
    main()