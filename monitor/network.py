import psutil
import platform
import time
import ping3
import socket

# Instantaneous network speed per minute
def monitorNetworkInstant():
    starttime = time.monotonic()
    while True:
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
        time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))

# Average network speed per minute
def monitorNetworkAvg():
    starttime = time.monotonic()
    while True:
        #network sent and recieved (in MB)
        networkSentB = psutil.net_io_counters().bytes_sent
        networkRecvB = psutil.net_io_counters().bytes_recv
        time.sleep(60.0 - ((time.monotonic() - starttime) % 60.0))
        networkSentA = psutil.net_io_counters().bytes_sent
        networkRecvA = psutil.net_io_counters().bytes_recv

        netUploadSpeed = abs(networkSentB-networkSentA)
        netDownloadSpeed = abs(networkRecvB-networkRecvA)

        avgUploadSpeed = netUploadSpeed/60
        avgDownloadSpeed = netDownloadSpeed/60

        # print every minute
        print("Average Upload Speed (KB/s): ", round(avgUploadSpeed/1024, 2))
        print("Average Download Speed (KB/s): ", round(avgDownloadSpeed/1024, 2))
        
# Monitors local and internet ping, prints out both pings every 5 seconds
def monitorPing():
    starttime = time.monotonic()
       
    while True:
        ping = ping3.ping("8.8.8.8") #Google DNS
        pingLocal = ping3.ping(getRouterIP())
        if ping != None:
            print("Ping (ms): ", round((ping * 1000), 2))
        else:
            print("Ping (ms): Timed out")
        
        if pingLocal != None:
            print("Local Ping (ms): ", round((pingLocal * 1000), 2))
        else:
            print("Local Ping (ms): Timed out")
        time.sleep(5.0 - ((time.monotonic() - starttime) % 5.0)) # Every 5 seconds

# Gets the router IP dynamically
def getRouterIP():
    networks = psutil.net_if_stats()
    networkAddresses = psutil.net_if_addrs()
    networksUp = []

    for network in networks:
        if networks[network].isup:
            networksUp.append(network)
    
    for Name in networkAddresses:
        if Name in networksUp:
            for addr in networkAddresses[Name]:
                if addr.address != "127.0.0.1" and addr.family == socket.AF_INET:
                    routerIP = addr.address
                    break
    return routerIP