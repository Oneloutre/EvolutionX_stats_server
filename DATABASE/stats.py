from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DATABASE.init_table import DeviceData
import requests
from datetime import datetime

# test credentials for now. Will be replaced with environment variables.
DATABASE_URL = "postgresql://testuser:testpassword@localhost:5432/testdb"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def retrieve_global_stats():
    db = SessionLocal()
    try:
        today = datetime.now().strftime("%Y-%m-%d")
        total_unique_devices = db.query(DeviceData).count()
        total_devices = db.query(DeviceData.device_codename).distinct().count()
        total_countries = db.query(DeviceData.device_country).distinct().count()
        total_carrier = db.query(DeviceData.device_carrier).distinct().count()
        total_distinct_evo_versions = db.query(DeviceData.device_evo_version).distinct().count()
        total_downloads_req = requests.get(f"https://sourceforge.net/projects/evolution-x/files/stats/json?start_date=2014-10-29&end_date={today}")
        total_downloads = total_downloads_req.json()["total"]
        return total_downloads, total_unique_devices, total_devices, total_countries, total_carrier, total_distinct_evo_versions
    except Exception as e:
        print(e)
    finally:
        db.close()
