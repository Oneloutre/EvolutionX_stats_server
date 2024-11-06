<center>

# EvolutionX stats server.
### This repo contains the code used to manage the statistics of the EvolutionX ROM.


![fastapi](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=fff&style=plastic) ![python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff&style=plastic) ![docker](https://img.shields.io/badge/Docker-2496ED?logo=docker&logoColor=fff&style=plastic) ![postgresql](https://img.shields.io/badge/PostgreSQL-4169E1?logo=postgresql&logoColor=fff&style=plastic) ![github](https://img.shields.io/badge/GitHub-181717?logo=github&logoColor=fff&style=plastic)

</center>

## API Documentation

> `/api/v2/global_stats` - GET

This endpoint returns the global statistics of the EvolutionX ROM.   
It will return a json object with the following keys:


```json
{
    "total_downloads": 1000000,
    "total_unique_devices": 100000,
    "total_countries": 100,
    "total_carriers": 1000,
    "total_users": 10000
}
```

---

> `/api/v2/stats` - POST

A POST request to this endpoint will add a new entry to the database.  
Here is the json object that should be sent in the request body:

```json
{
    "device_name": "OnePlus 7 Pro",
    "device_model": "GM1917",
    "device_brand": "OnePlus",
    "device_codename": "guacamole",
    "device_country": "United States",
    "device_carrier": "T-Mobile",
    "device_android_version": "14",
    "device_evo_version": "9.5"
}
```

An entry will be added to the database with those informations.