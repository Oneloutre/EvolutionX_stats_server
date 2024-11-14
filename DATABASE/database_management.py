from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DATABASE.init_table import DeviceData

# test credentials for now. Will be replaced with environment variables.
DATABASE_URL = "postgresql://testuser:testpassword@localhost:5432/testdb"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


async def create_device_data(data: DeviceData):
    db = SessionLocal()
    try:
        new_device_data = DeviceData(
            device_name=data.device_name,
            device_model=data.device_model,
            device_brand=data.device_brand,
            device_codename=data.device_codename,
            device_country=data.device_country,
            device_carrier=data.device_carrier,
            device_android_version=data.device_android_version,
            device_evo_version=data.device_evo_version
        )
        db.add(new_device_data)
        db.commit()
        db.refresh(new_device_data)
        return True
    except Exception as e:
        db.rollback()
        print(e)
        return False
    finally:
        db.close()
