from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker  

from decouple import config

DATABASE_URL = config('DATABASE_URL')

engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# session = SessionLocal()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()