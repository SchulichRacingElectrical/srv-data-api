from sqlalchemy import Column, Date, DateTime, Integer
from sqlalchemy.orm import relationship

from api.database import Base


# Creates a table for Runs
class Run(Base):
    __tablename__ = "runs"
    id = Column(Integer, primary_key=True)
    datetime = Column(DateTime, unique=True, nullable=False)

    # Define other columns here
    ...


# Creates a table for Sessions, which can reference many Runs
class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    date = Column(Date, unique=True, nullable=False)

    runs = relationship("Run", backref="session")
