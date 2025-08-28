

class Monitor(object):
    def __init__(self, name, data, status, interval, running):
        self.name = name
        self.interval = interval
        self.data = None
        self.status = "Inactive"
        self.running = False

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

    def start(self):
        self.running = True
        self.status = "Active"

    

    
        
    