from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from DATABASE.init_table import DeviceData

# test credentials for now. Will be replaced with environment variables.
DATABASE_URL = "postgresql://testuser:testpassword@localhost:5432/testdb"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def retrieve_global_stats():
    db = SessionLocal()
    try:
        data = db.query(DeviceData).count()
        return data
    except Exception as e:
        print(e)
    finally:
        db.close()