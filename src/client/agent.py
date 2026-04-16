"""
Author: Jackie Liu
Date: 1/8/2026
Desc: Agent class, supervises all monitor subclasses and threads them, 
      looks at data at given intervals and then returns them in json format to be documented.
"""

import json
import threading
import socket
import time
import requests
from monitor import *

class Agent():
    def __init__(self, interval=60):
        self.interval = interval # interval of agent payload sent 
        self.deviceId = socket.gethostname() #grabs device ID of host

        # intializing all monitors for pc data
        self.gpu = GPU_Monitor("gpu", 5)
        self.cpu = CPU_Monitor("cpu", 5)
        self.disk = disk_Monitor("disk", 5)
        self.memory = RAM_Monitor("memory", 5)
        self.network = network_Monitor("network", 5)
        self.ping = ping_Monitor("ping", 5)

        # static values go directly to data (no need for constant monitoring)
        self.cpu.data["cores"] = self.cpu.getCores(False)
        self.cpu.data["log_cores"] = self.cpu.getCores(True)

        # registering monitor functions (dynamic values)
        self.gpu.register("gpus", self.gpu.getGPUTotal)

        self.cpu.register("usage_percent", self.cpu.getInstantCPUPercent)

        self.disk.register("read", self.disk.getInstantDiskRead)
        self.disk.register("write", self.disk.getInstantDiskWrite)
        self.disk.register("drive_percent", self.disk.getDisk)

        self.memory.register("usage_percent", self.memory.getRAMPercent)
        self.memory.register("usage_bytes", self.memory.getRAM)

        self.network.register("upload", self.network.getNetworkUpload)
        self.network.register("download", self.network.getNetworkDownload)

        self.ping.register("internet", self.ping.getPing)
        self.ping.register("local", self.ping.getLocalPing)

        # setting up thread objects for all monitors & set them all to daemons
        # daemon thread makes it not block program exiting
        self.gpuThread = threading.Thread(target=self.gpu.start, daemon=True)
        self.cpuThread = threading.Thread(target=self.cpu.start, daemon=True)
        self.diskThread = threading.Thread(target=self.disk.start, daemon=True)
        self.memoryThread = threading.Thread(target=self.memory.start, daemon=True)
        self.networkThread = threading.Thread(target=self.network.start, daemon=True)
        self.pingThread = threading.Thread(target=self.ping.start, daemon=True)
 
    # collection of data and put into payload
    def collect(self):
        payload = {"time": time.time(), 
                   "device_id": self.deviceId, 
                   "cpu": self.cpu.getData(), #grabs data(dict) of each monitor 
                   "gpu": self.gpu.getData(), 
                   "disk": self.disk.getData(), 
                   "memory": self.memory.getData(), 
                   "network": self.network.getData(), 
                   "ping": self.ping.getData()}
        return payload
    
    def run(self):
        # starts all monitor threads
        self.gpuThread.start()
        self.cpuThread.start()
        self.diskThread.start()
        self.memoryThread.start()
        self.networkThread.start()
        self.pingThread.start()

        # infinite loop till user terminates (ctrl+c)
        try:
            while True:
                payload = self.collect()
                #r = requests.post('http://127.0.0.1:8000/api/data', json=payload) #prints it for now
                #print(r.status_code)
                print(self.gpu.getData())
                print(json.dumps(payload, indent=4))
                time.sleep(self.interval)
        except KeyboardInterrupt: #ctrl + c
            print("Shutdown intiated.")

        except Exception as e: #error catcher
            print(f"Critical Error: {e}")
            
if __name__ == "__main__":
    agent = Agent()
    agent.run()