# app.py
from fastapi import FastAPI, Request
import os
from dotenv import load_dotenv
from run_flow import run_flow
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

load_dotenv()

app = FastAPI()
app.mount("/frontend", StaticFiles(directory="frontend"), name="frontend")

@app.post("/api/run")
async def api_run(request: Request):
    data = await request.json()
    result = run_flow(data.get("input", ""))
    return result

@app.get("/")
def index():
    with open("frontend/index.html") as f:
        return HTMLResponse(f.read())
