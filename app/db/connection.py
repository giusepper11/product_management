from decouple import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_HOST = config("POSTGRES_HOST")
DB_USER = config("POSTGRES_USER")
DB_PASSWORD = config("POSTGRES_PASSWORD")
DB_NAME = config("POSTGRES_DB")
CONN_STR = f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

engine = create_engine(CONN_STR, pool_pre_ping=True)
LocalSession = sessionmaker(bind=engine)
