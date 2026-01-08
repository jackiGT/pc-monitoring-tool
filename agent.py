import json
import socket
from monitor import *

class Agent():
    def __init__(self, interval=10):
        self.interval = interval
        self.deviceId = socket.gethostname()

        self.gpu = GPU_Monitor("gpu", interval)
        self.cpu = CPU_Monitor("cpu", interval)
        self.disk = disk_Monitor("disk", interval)
        self.memory = RAM_Monitor("memory", interval)
        self.network = network_Monitor("network", interval)
        self.ping = ping_Monitor("ping", interval)

    def collect(self):
        raise NotImplementedError