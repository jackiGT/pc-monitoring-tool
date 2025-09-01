import psutil
import time
from base import Monitor
import ping3
import socket

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


# Monitors local and internet ping, prints out both pings every 5 seconds
class ping_Monitor(Monitor):
    
    def update(self, local):
        ping = ping3.ping("8.8.8.8") #Google DNS
        pingLocal = ping3.ping(getRouterIP())

        if local:
            if pingLocal != None:
                print("Local Ping (ms): ", round((pingLocal * 1000), 2))
            else:
                print("Local Ping (ms): Timed out")
        else:
            if ping != None:
                print("Ping (ms): ", round((ping * 1000), 2))
            else:
                print("Ping (ms): Timed out")
        
        print("")
    
    def start(self, local):
        self.running = True
        self.status = "Active"

        interval = self.getInterval()
        starttime = time.monotonic() # time information necessary!

        while self.running:
            self.update(local)
            sleepTime = max(0, interval - ((time.monotonic() - starttime) % interval))
            time.sleep(sleepTime)
    


#Testing mainQ  
def main():
    pingMonitor = ping_Monitor("pingMonitor", 5)
    pingMonitor.start(local=False)

if __name__ == "__main__":
    main()