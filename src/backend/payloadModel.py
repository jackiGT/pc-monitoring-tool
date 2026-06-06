
from pydantic import BaseModel

# Payload schema to validate incoming json format (agent payload) and set guidelines
# - Different sub models for each monitor to validate data

class CPU(BaseModel):
    cores: int
    log_cores: int
    usage_percent: float

class Disk(BaseModel):
    read: float
    write: float
    drive_percent: float

class Memory(BaseModel):
    usage_percent: float
    usage_bytes: float

class Network(BaseModel):
    upload: float
    download: float

class Ping(BaseModel):
    internet: float
    local: float

## GPU sub models
class Static(BaseModel): # Non changing variables for GPU
    model: str
    memory: float
    UUID: str

class Dynamic(BaseModel): # Changing variables for GPU
    usage_percent: float
    free_mem: float
    used_mem: float
    temp: float

class GpuID(BaseModel):
    static: Static
    dynamic: Dynamic

class GPU(BaseModel): # Multiple GPUs possible
    gpus: list[GpuID]

class Payload(BaseModel):
    time: float
    device_id: str
    cpu: CPU
    gpu: GPU
    disk: Disk
    memory: Memory
    network: Network
    ping: Ping