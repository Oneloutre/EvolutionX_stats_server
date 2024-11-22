<div style="text-align: center;">

![banner](banner.png)

# EvolutionX stats server.
### This repo contains the code used to manage the statistics of the EvolutionX ROM.


![fastapi](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff&style=plastic) ![python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=plastic) ![docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=plastic) ![postgresql](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=plastic) ![github](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=plastic)

</div>

## API Documentation

> `/api/stats` - GET

This endpoint returns the global statistics of the EvolutionX ROM.   
It will return a json object with the following keys:


```json
{
	"all_time_downloads": 8356439,
	"total_unique_devices": 10000,
	"total_devices": 100,
	"total_countries": 100,
	"total_carrier": 14,
	"total_distinct_evo_versions": 14
}
```

- `all_time_downloads`: The total number of downloads of the EvolutionX ROM. (fetched directly from sourceforge)
- `total_unique_devices`: The total number of people that have installed the EvolutionX ROM.
- `total_devices`: The total number of devices that have installed the EvolutionX ROM.
- `total_countries`: The total number of countries where the EvolutionX ROM is installed.
- `total_carrier`: The total number of carriers on phones with the EvolutionX ROM installed.
- `total_distinct_evo_versions`: The total number of distinct EvolutionX versions installed on devices.

Difference between `total_unique_devices` and `total_devices`:
`total_unique_devices` is the number of EvoX installations, when `total_devices` is the total of devices that received EvoX. A device is determined by its codename.

---

> `/api/stats` - POST

A POST request to this endpoint will add a new entry to the database.  
Here is the json object that should be sent in the request body:

```json
{
    "device_unique_id": "AnUniqueIdRandomlyGenerated",
    "device_codename": "Lynx",
    "device_evo_version": "9.5",
    "device_country": "US",
    "device_carrier": "Verizon"
}
```

An entry will be added to the database with those information.

---
### The `per-` request.

> `/api/stats/per-$keyword` - GET

With this endpoint, depending on what keyword is used, you can get the statistics of the EvolutionX ROM per that keyword.
it returns a json object, ordered in the descending order of the keyword.
Example: `/api/v2/stats/per-country` will return the country with the most installations of the ROM.

```json
{
    "US": 1000,
    "BR": 500,
    "IN": 300,
    "FR": 200,
    "DE": 100
}
```

here are the available keywords:

- `per-device`: Returns the devices with the most installations.
- `per-country`: Returns the countries with the most installations.
- `per-carrier`: Returns the carriers with the most installations.
- `per-version`: Returns the EvolutionX versions with the most installations.

---

## Data collected

We use [Lineage's default stats APP](https://github.com/lineageos-infra/tribble-tracker) so we grab the same informations as them.
Here the data we collect, according to their github:


Devices check in (roughly) daily with the following data:

- Device ID: The sha256 of Settings.Secure.ANDROID_ID. This ID is reset every time the device is wiped.
- Device model, taken from ro.cm.device.
- Device version, taken from ro.cm.version.
- Device country, as reported by the SIM card.
- Device carrier, as reported by the SIM card.

Additionally, we record the following:

- Current time the request was made.

