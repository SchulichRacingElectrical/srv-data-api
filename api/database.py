"""
Handles database connection.
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from api.config import DATABASE_URL

engine = create_engine(DATABASE_URL, future=True)

Session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()  # Base class for all models
