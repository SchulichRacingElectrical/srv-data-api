"""
Models for validating types in requests/responses for the API.
"""

from datetime import date, datetime

from pydantic import BaseModel


class SessionBase(BaseModel):
    date: date = date.today()

    class Config:
        orm_mode = True


class RunBase(BaseModel):
    session_id: int
    start_time: datetime
    end_time: datetime

    class Config:
        orm_mode = True


class SensorBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class ReadingBase(BaseModel):
    run_id: int
    sensor_id: int
    timestamp: datetime = datetime.now()
    value: float

    class Config:
        orm_mode = True
