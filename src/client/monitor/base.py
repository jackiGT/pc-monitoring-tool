"""
Author: Jackie Liu
Date: 1/8/2026
Desc: Base monitor class, returns information on a given interval 
      depending on registered function metric, monitor subclass.
"""

import time
import threading

class Monitor(object):
    def __init__(self, name, interval):
        self.name = name
        self.interval = interval

        self.status = "Inactive"
        self.running = False
        
        self.start_time = time.monotonic()

        self.data = {}
        self.metrics = []

        # lock to prevent concurrent threads from accessing same source, unpredictability
        # instance level lock so each monitor can run concurrently
        self.lock = threading.Lock()

    def getData(self):
        with self.lock:
            return self.data.copy()
    
    def getStatus(self):
        return self.status
    
    def getInterval(self):
        return self.interval
    
    def register(self, name, func):
        self.metrics.append((name, func))

    def unregister(self, func):
        self.metrics.remove(func)
    
    def update(self):
        with self.lock:
            for name, func in self.metrics:
                self.data[name] = func()
    
    def getInstant(self):
        raise NotImplementedError
    
    def printInfo(self):
        raise NotImplementedError
    
    def stop(self):
        self.running = False
        self.status = "Inactive"

    def getUptime(self):
        return time.monotonic() - self.start_time

    def start(self):
        self.running = True
        self.status = "Active"

        interval = self.getInterval()
        loopStart = time.monotonic() # time information necessary!


        while self.running:
            self.update()

            # interval timer, higher accuracy with time.monotonic()
            elapsed = time.monotonic() - loopStart
            sleepTime = interval - (elapsed % interval)
            time.sleep(sleepTime)