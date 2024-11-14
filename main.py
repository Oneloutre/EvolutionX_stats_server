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


#@app.get("/api/global_stats")
#async def global_stats():
#return await api.global_stats()


class DeviceData(BaseModel):
    device_name: str
    device_model: str
    device_brand: str
    device_codename: str
    device_country: str
    device_carrier: str
    device_android_version: int
    device_evo_version: float


@app.post("/api/device_receive")
async def device_receive(device: DeviceData):
    return await receive_data(device)


if __name__ == "__main__":
    init_device_data_table()
    uvicorn.run(app, host="0.0.0.0", port=8000)
