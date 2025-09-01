import time

class Monitor(object):
    def __init__(self, name, interval, start_time=time.monotonic(), data=None, status="Inactive", running=False):
        self.name = name
        self.interval = interval
        self.data = data
        self.status = status
        self.running = running
        self.start_time = start_time

    def getData(self):
        return self.data
    
    def getStatus(self):
        return self.status
    
    def getInterval(self):
        return self.interval
    
    def update(self):
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
        starttime = time.monotonic() # time information necessary!

        while self.running:
            self.update()
            sleepTime = max(0, interval - ((time.monotonic() - starttime) % interval))
            time.sleep(sleepTime)

    

    
        
    