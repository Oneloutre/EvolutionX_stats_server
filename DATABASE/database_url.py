import os


def get_database_url():
    user = os.getenv("POSTGRES_USER")
    password = os.getenv("POSTGRES_PASSWORD")
    host = os.getenv("POSTGRES_HOST")
    port = os.getenv("POSTGRES_PORT")
    db = os.getenv("POSTGRES_DB")
    db_url = f"postgresql://{user}:{password}@{host}:{port}/{db}"
    return db_url
