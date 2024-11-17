from DATABASE.database_management import create_device_data
from DATABASE.stats import retrieve_global_stats


async def receive_data(device):
    var, reason = await create_device_data(device)
    if var:
        return {"status": "success"}
    else:
        return {"status": "failed",
                "reason": reason}


def api_global_stats():
    global_stats = retrieve_global_stats()
    return global_stats
