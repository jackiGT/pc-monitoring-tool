from fastapi import HTTPException, Request, status, Body
from fastapi import APIRouter
from payloadModel import Payload

# Base API router for agent request methods
router = APIRouter()

# Empty dict to store payload for get request
stored_payload = {}

# Gets POST request payload when agent sends it to server
@router.post("/api/data")
async def recievePayload(payload: Payload, request: Request):
    payload = await request.json()
    if payload:
        stored_payload.update(payload)
        print("Payload received successfully")
        return payload
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payload not found")


@router.get("/api/data", include_in_schema=False)
async def readPayload():
    if stored_payload:
        return stored_payload
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Payload not found")