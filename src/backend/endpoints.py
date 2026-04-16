"""
Author: Jackie Liu
Date: 4/10/2026
Desc: Basic API endpoints, grabs information and sends to pointed locations
"""
# Note: fastapi dev *.py for running dev server

from fastapi import FastAPI, HTTPException, Request, status, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

# instance of FastAPI class for active usage
app = FastAPI()

posts: list[dict] = [
    {"key": "val",
     "id": 0,
    "Circles": "spheres",
    "triangles": "pyramid"},

    {"key": "val",
     "id": 1,
    "sword": "claymore",
    "dagger": "knife"}
]

# Payload schemas to validate incoming json format and set guidelines
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
class Static(BaseModel): # non changing variables for GPU
    model: str
    memory: float
    UUID: str

class Dynamic(BaseModel): # changing variables for GPU
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


# Testing
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/test", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts[0]['triangles']}</h1>"

# gets POST request payload when agent sends it to server
@app.post("/api/data")
async def recievePayload(payload: Payload, request: Request):
    payload = await request.json()
    print("Safe!")
    if payload:
        return payload
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payload not found")

@app.get("/api/data")
def readPayload():
    raise NotImplementedError