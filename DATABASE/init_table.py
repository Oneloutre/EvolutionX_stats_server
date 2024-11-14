from sqlalchemy import create_engine, Column, Integer, String, DateTime, inspect
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

# test credentials for now. Will be replaced with environment variables.
DATABASE_URL = "postgresql://testuser:testpassword@localhost:5432/testdb"
engine = create_engine(DATABASE_URL)
Base = declarative_base()


class DeviceData(Base):
    __tablename__ = "device_data"

    id = Column(Integer, primary_key=True, index=True)
    device_name = Column(String(100))
    device_model = Column(String(50))
    device_brand = Column(String(50))
    device_codename = Column(String(50))
    device_country = Column(String(50))
    device_carrier = Column(String(50))
    device_android_version = Column(String(10))
    device_evo_version = Column(String(10))
    created_at = Column(DateTime, default=datetime.utcnow)


def init_device_data_table():
    inspector = inspect(engine)
    if not inspector.has_table("device_data"):
        Base.metadata.create_all(engine)
        print("Table device_data successfully initated.")
    else:
        print("Table device_data already exists. No action needed..")
