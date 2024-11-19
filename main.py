from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from API import api
from pydantic import BaseModel
import uvicorn

from DATABASE.init_table import init_device_data_table
from API.api import receive_data

app = FastAPI()


@app.get("/")
async def read_root():
    return RedirectResponse("https://evolution-x.org")


@app.get("/api/stats")
async def global_stats():
    total_downloads, total_unique_devices, total_devices, total_countries, total_carrier, total_distinct_evo_versions = api.api_global_stats()
    return {"all_time_downloads": total_downloads,
            "total_unique_devices": total_unique_devices,
            "total_devices": total_devices,
            "total_countries": total_countries,
            "total_carrier": total_carrier,
            "total_distinct_evo_versions": total_distinct_evo_versions}


class DeviceData(BaseModel):
    device_unique_id: str
    device_codename: str
    device_evo_version: float
    device_country: str
    device_carrier: str


@app.post("/api/stats")
async def device_receive(device: DeviceData):
    return await receive_data(device)


if __name__ == "__main__":
    init_device_data_table()
    uvicorn.run(app, host="0.0.0.0", port=8000)
