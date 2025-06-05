from fastapi import FastAPI, HTTPException
from .models import Device

app = FastAPI(title="MCP Server API", version="1.0.0")

# in-memory device store
DEVICES: dict[int, Device] = {}

@app.get("/devices", response_model=list[Device])
async def list_devices() -> list[Device]:
    return list(DEVICES.values())

@app.post("/devices", response_model=Device, status_code=201)
async def create_device(device: Device) -> Device:
    device.id = len(DEVICES) + 1
    DEVICES[device.id] = device
    return device

@app.get("/devices/{device_id}", response_model=Device)
async def get_device(device_id: int) -> Device:
    device = DEVICES.get(device_id)
    if not device:
        raise HTTPException(status_code=404, detail="Device not found")
    return device
