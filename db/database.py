from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base

DATABASE_URL = "postgresql+psycopg://test:1234@127.0.0.1:5432/aprendiendofastapi"

engine = create_engine(
DATABASE_URL,
pool_pre_ping=True
)

Base = declarative_base()