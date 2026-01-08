import GPUtil
import platform
import time
from .base import Monitor

class GPU_Monitor(Monitor):
    def __init__(self, name, interval, data=None):
        super().__init__(name, interval)

        try:
            self.gpus = GPUtil.getGPUs()

        except Exception:
            print("No NVIDIA driver found.")
            self.GPUCount = 0
            self.GPUAvailable = False

        else:
            self.GPUCount = len(self.gpus)
    
    def getGPUStatic(self):
        dict_gpus = {}
        for gpu in self.gpus:

            gpu_id = gpu.id
            gpu_name = gpu.name
            gpu_uuid = gpu.uuid

            gpu_total_mem = gpu.memoryTotal

            dict_gpus.update({gpu_id: {"name": gpu_name,
                                       "total memory": gpu_total_mem,
                                       "UUID": gpu_uuid}})
        return dict_gpus

    def getGPUDynamic(self):
        gpus = GPUtil.getGPUs()
        dict_gpus = {}

        for gpu in gpus:

            gpu_id = gpu.id

            gpu_load = gpu.memoryFree

            gpu_free_mem = gpu.memoryFree
            gpu_used_mem = gpu.memoryUsed
            
            gpu_temp = gpu.temperature

            dict_gpus.update({gpu_id: {"usage percentage": gpu_load, 
                                       "free memory": gpu_free_mem, 
                                       "used memory": gpu_used_mem, 
                                       "temperature": gpu_temp}})
        return dict_gpus
    
    def viewGPUTotal(self):
        gpusStatic = self.getGPUStatic()
        gpusDynamic = self.getGPUDynamic()
        dict_gpus = {}

        for id in gpusStatic:

            gpu_id = id

            gpu_name = id.get("name")
            gpu_total_mem = id.get("total memory")
            gpu_uuid = id.get("UUID")

            dict_gpus.update({gpu_id: {"name": gpu_name, 
                                       "total memory": gpu_total_mem, 
                                       "UUID": gpu_uuid}})
            
        for id in gpusDynamic:
            gpu_load = id.get("usage percentage")

            gpu_free_mem = id.get("free memory")
            gpu_used_mem = id.get("used memory")
            
            gpu_temp = id.get("temperature")

            dict_gpus[id]["dynamic"] = {"usage percentage": gpu_load,
                                        "free memory": gpu_free_mem, 
                                        "used memory": gpu_used_mem, 
                                        "temperature": gpu_temp}

        return dict_gpus
