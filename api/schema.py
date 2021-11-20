"""
Models for validating types in requests/responses for the API.
"""

from datetime import date, datetime

from pydantic import BaseModel


class CollectionBase(BaseModel):
    datestamp: date = date.today()
    organization_id = int

    class Config:
        orm_mode = True


class CollectionResponse(CollectionBase):
    id: int


class SessionBase(BaseModel):
    collection_id: int
    start_time: datetime
    end_time: datetime

    class Config:
        orm_mode = True


class SessionResponse(SessionBase):
    id: int


class SensorBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class SensorResponse(SensorBase):
    id: int


class ReadingBase(BaseModel):
    session_id: int
    sensor_id: int
    timestamp: datetime = datetime.now()
    value: float

    class Config:
        orm_mode = True


class ReadingResponse(ReadingBase):
    id: int


class OrganizationBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class OrganizationResponse(OrganizationBase):
    id: int
