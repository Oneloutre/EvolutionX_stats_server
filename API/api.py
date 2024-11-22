from DATABASE.database_management import create_device_data
from DATABASE.stats import retrieve_global_stats, retrieve_per_keyword


async def receive_data(device):
    var, reason = await create_device_data(device)
    if var:
        return {"status": "success"}
    else:
        return {"status": "failed",
                "reason": reason}


def api_global_stats():
    total_downloads, total_unique_devices, total_devices, total_countries, total_carrier, total_distinct_evo_versions = retrieve_global_stats()
    return total_downloads, total_unique_devices, total_devices, total_countries, total_carrier, total_distinct_evo_versions


def stats_per(keyword):
    if keyword == "device":
        results = retrieve_per_keyword("device_codename")
    elif keyword == "country":
        results = retrieve_per_keyword("device_country")
    elif keyword == "carrier":
        results = retrieve_per_keyword("device_carrier")
    elif keyword == "evo_version":
        results = retrieve_per_keyword("device_evo_version")
    else:
        results = {"status": "failed",
                "reason": "Invalid keyword."}
    return results
