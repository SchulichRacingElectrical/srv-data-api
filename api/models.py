"""
Models for defining the database tables.
"""

from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from api.database import Base

class Organization(Base):
    __tablename__ = "organizations"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False, unique=True)

    collections = relationship("Collection", backref="organization")

class Collection(Base):
    __tablename__ = "collections"
    id = Column(Integer, primary_key=True)
    organization_id = Column(Integer, ForeignKey("organizations.id"), nullable=False)
    datestamp = Column(Date, nullable=False)

    sessions = relationship("Session", backref="collection")


class Session(Base):
    __tablename__ = "sessions"
    id = Column(Integer, primary_key=True)
    collection_id = Column(Integer, ForeignKey("collections.id"), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)


class Sensor(Base):
    __tablename__ = "sensors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)


class Reading(Base):
    __tablename__ = "readings"
    id = Column(Integer, primary_key=True)
    session_id = Column(Integer, ForeignKey("sessions.id"), nullable=False)
    sensor_id = Column(Integer, ForeignKey("sensors.id"), nullable=False)
    timestamp = Column(DateTime, nullable=False)
    value = Column(Float, nullable=False)

    session = relationship("Session", backref="readings")
    sensor = relationship("Sensor", backref="readings")
