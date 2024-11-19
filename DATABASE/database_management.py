from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DATABASE.init_table import DeviceData

# test credentials for now. Will be replaced with environment variables.
DATABASE_URL = "postgresql://testuser:testpassword@localhost:5432/testdb"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
db = SessionLocal()


def is_device_unique_id_present(device_unique_id: str, database: db) -> bool:
    return database.query(DeviceData).filter(DeviceData.device_unique_id == device_unique_id).first() is not None


async def create_device_data(data: DeviceData):
    received_unique_id = data.device_unique_id
    device_codename = data.device_codename
    device_evo_version = data.device_evo_version
    device_country = data.device_country
    device_carrier = data.device_carrier
    try:
        if not received_unique_id:
            reason = "device_unique_id is not provided."
            return False, reason
        if not device_codename:
            reason = "device_codename is not provided."
            return False, reason
        if not device_evo_version:
            reason = "device_evo_version is not provided."
            return False, reason
        if not device_country:
            reason = "device_country is not provided."
            return False, reason
        if not device_carrier:
            reason = "device_carrier is not provided."
            return False, reason
        if is_device_unique_id_present(received_unique_id, db):
            reason = "device_unique_id already exists in the database."
            return False, reason
        else:
            try:
                new_device_data = DeviceData(
                    device_unique_id=data.device_unique_id,
                    device_codename=data.device_codename,
                    device_evo_version=data.device_evo_version,
                    device_country=data.device_country,
                    device_carrier=data.device_carrier
                )
                db.add(new_device_data)
                db.commit()
                db.refresh(new_device_data)
                return True, None
            except Exception as e:
                db.rollback()
                print(e)
                return False
            finally:
                db.close()
                return True, None

    except Exception as e:
        print(e)
        return False
    print(uniqueid)
