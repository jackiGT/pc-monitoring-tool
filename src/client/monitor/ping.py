"""
Author: Jackie Liu
Date: 1/8/2026
Desc: Ping monitor subclass, collections on local/remote ping.
"""

import psutil
from .base import Monitor
import ping3
import socket

# Gets the local machine IP dynamically
def getlocalIP():

    # networks gives network status, 
    # networkAddresses gives addresses of networks,
    # local networks connected to computer
    networks = psutil.net_if_stats()
    networkAddresses = psutil.net_if_addrs()
    networksUp = []

    # List of all networks online locally
    for network in networks:
        if networks[network].isup:
            networksUp.append(network)
    

    # Looks though online local networks, if not localhost & is IPv4 address
    # then it is local machine IP (ping monitoring)
    for Name in networkAddresses:
        if Name in networksUp:
            for addr in networkAddresses[Name]:
                if addr.address != "127.0.0.1" and addr.family == socket.AF_INET:
                    localIP = addr.address
                    break
    return localIP


# Monitors local and internet ping, prints out both pings every 5 seconds
class ping_Monitor(Monitor):
    
    def printInfo(self, local):
        ping = ping3.ping("8.8.8.8") #Google DNS ping (standard for internet ping)
        pingLocal = ping3.ping(getlocalIP())

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
    

    def getInstant(self):
        ping = ping3.ping("8.8.8.8") #Google DNS
        return "Ping: " + str(round((ping * 1000), 2))

    def getPing(self):
        ping = ping3.ping("8.8.8.8") #Google DNS
        return round((ping * 1000), 2)
    

    def getLocalPing(self):
        pingLocal = ping3.ping(getlocalIP())
        return round((pingLocal * 1000), 2)



#Testing mainQ  
def main():
    pingMonitor = ping_Monitor("pingMonitor", 5)
    pingMonitor.start(local=False)

if __name__ == "__main__":
    main()