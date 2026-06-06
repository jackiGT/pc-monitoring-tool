"""
Author: Jackie Liu
Date: 4/10/2026
Desc: Basic agentAPI, grabs information and sends to pointed locations

    Note: fastapi dev *.py for running dev server (testing/debugging)
          fastapi run -h for more info on running server
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from routes.agent import router as agent_router
from os import getenv

# Instance of FastAPI class for active usage
app = FastAPI(prefix="/api", title="Main API", description="API for agent to send data to server currently", version="0.1.0")

# 
app.include_router(agent_router)

# Test posts
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

# Testing
@app.get("/", response_class=HTMLResponse, include_in_schema=False)
@app.get("/test", response_class=HTMLResponse, include_in_schema=False)
def home():
    return f"<h1>{posts}</h1>"
    
PORT = getenv("PORT", 8000)

if __name__ == "__main__":
    print("Test")
