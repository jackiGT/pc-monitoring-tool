"""
Author: Jackie Liu
Date: 1/8/2026
Desc: GPU monitor subclass, 
      specifically for NVIDIA GPUs (GPUtil).
Note: Can only be used for NVIDIA GPUs.
"""

import GPUtil
from .base import Monitor


class GPU_Monitor(Monitor):
    def __init__(self, name, interval, data=None):
        super().__init__(name, interval)

        try: 
            self.gpus = GPUtil.getGPUs()

        # Exception if no Nvidia GPUs detected
        except Exception:
            print("No NVIDIA driver found.")
            self.GPUCount = 0
            self.GPUAvailable = False

        else:
            self.GPUCount = len(self.gpus)
    
    # GPU static information - information not changing with time
    def getGPUStatic(self):
        gpus_list = []
        for gpu in self.gpus:

            # Call each gpu instance variables to store the information
            gpu_id = gpu.id
            gpu_name = gpu.name
            gpu_uuid = gpu.uuid

            gpu_total_mem = gpu.memoryTotal

            gpus_list.append({"id": gpu_id,
                                "model": gpu_name,
                                "total memory": gpu_total_mem,
                                "UUID": gpu_uuid})
        return gpus_list


     # GPU dynamic information - information changing with time
    def getGPUDynamic(self):
        gpus = GPUtil.getGPUs()
        gpus_list = []

        for gpu in gpus:

            gpu_load = gpu.load*100

            gpu_free_mem = gpu.memoryFree
            gpu_used_mem = gpu.memoryUsed
            
            gpu_temp = gpu.temperature

            gpus_list.append({"usage percentage": gpu_load, 
                                       "free memory": gpu_free_mem, 
                                       "used memory": gpu_used_mem, 
                                       "temp": gpu_temp})
        return gpus_list
    
    # GPU information full view
    def getGPUTotal(self):
        gpusStatic = self.getGPUStatic()
        gpusDynamic = self.getGPUDynamic()
        gpu_info_static = []
        gpu_info_dynamic = []
        gpus_list = {}

        for id in gpusStatic:

            gpu_name = id.get("model")
            gpu_total_mem = id.get("total memory")
            gpu_uuid = id.get("UUID")

            gpu_info_static.append({"model": gpu_name, 
                                       "total memory": gpu_total_mem, 
                                       "UUID": gpu_uuid})
            
        for id in gpusDynamic:
            gpu_load = id.get("usage percentage")

            gpu_free_mem = id.get("free memory")
            gpu_used_mem = id.get("used memory")
            
            gpu_temp = id.get("temp")

            gpu_info_dynamic.append({"usage percentage": gpu_load,
                                        "free memory": gpu_free_mem, 
                                        "used memory": gpu_used_mem, 
                                        "temp": gpu_temp})
            
        for i in range(len(gpusStatic)):
            gpus_list.update({"static": gpu_info_static[i], 
                              "dynamic": gpu_info_dynamic[i]})

        return [gpus_list]
    

