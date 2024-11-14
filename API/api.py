from DATABASE.database_management import create_device_data


async def receive_data(device):
    var = await create_device_data(device)
    if var:
        return {"status": "success"}
    else:
        return {"status": "failed"}