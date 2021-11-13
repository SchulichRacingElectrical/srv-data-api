"""
Models for validating types in requests/responses for the API.
"""

from datetime import date, datetime

from pydantic import BaseModel


class SessionBase(BaseModel):
    datestamp: date = date.today()

    class Config:
        orm_mode = True


class SessionResponse(SessionBase):
    id: int


class RunBase(BaseModel):
    session_id: int
    start_time: datetime
    end_time: datetime

    class Config:
        orm_mode = True


class RunResponse(RunBase):
    id: int


class SensorBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SensorResponse(SensorBase):
    id: int


class ReadingBase(BaseModel):
    run_id: int
    sensor_id: int
    timestamp: datetime = datetime.now()
    value: float

    class Config:
        orm_mode = True


class ReadingResponse(ReadingBase):
    id: int
