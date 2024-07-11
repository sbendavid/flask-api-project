from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config

# Assuming your config.py defines DATABASE_URL
engine = create_engine(config['development']) 
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
  with SessionLocal() as session:
    # You can test some basic database operations here (optional)
    pass
except Exception as e:
  print(f"Error connecting to database: {e}")
