from sqlalchemy import create_engine, Column, Integer, String, DateTime, inspect
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
from DATABASE.database_url import get_database_url

DATABASE_URL = get_database_url()

engine = create_engine(DATABASE_URL)
Base = declarative_base()


class DeviceData(Base):
    __tablename__ = "device_data"

    id = Column(Integer, primary_key=True, index=True)
    device_unique_id = Column(String(100))
    device_codename = Column(String(50))
    device_evo_version = Column(String(10))
    device_country = Column(String(10))
    device_carrier = Column(String(50))
    created_at = Column(DateTime, default=datetime.now(timezone.utc))


def init_device_data_table():
    inspector = inspect(engine)
    if not inspector.has_table("device_data"):
        Base.metadata.create_all(engine)
        print("Table device_data successfully initated.")
    else:
        print("Table device_data already exists. No action needed..")
