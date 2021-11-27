import json
from typing import List

import requests
from fastapi import Depends, FastAPI
from sqlalchemy import delete, insert, select, update
from sqlalchemy.orm import Session as DBSession

from api import schema
from api.database import Base, engine
from api.dependencies import get_db
from api.models import Collection, Organization, Reading, Sensor, Session

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.on_event("startup")
def startup():
    r = requests.get("http://localhost:8080/database/sensors")
    data = json.loads(r.content)
    # unfinished, should add new rows to database


# Collections
@app.post("/collections/", response_model=schema.CollectionResponse, tags=["collections"])
async def create_collection(collection: schema.CollectionBase, db: DBSession = Depends(get_db)):
    collection = Collection(**collection.dict())  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(collection)
    db.commit()
    return collection


@app.get(
    "/collections/{collection_id}", response_model=schema.CollectionResponse, tags=["collections"]
)
async def get_collection(collection_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Collection).where(Collection.id == collection_id)).scalar()


@app.get("/collections/", response_model=List[schema.CollectionResponse], tags=["collections"])
async def get_collections(db: DBSession = Depends(get_db)):
    return list(db.execute(select(Collection)).scalars())


# Sensors
@app.post("/sensors/", response_model=schema.SensorResponse, tags=["sensors"])
async def create_sensor(sensor: schema.SensorBase, db: DBSession = Depends(get_db)):
    sensor = Sensor(**sensor.dict())  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(sensor)
    db.commit()
    return sensor


@app.get("/sensors/{sensor_id}", response_model=schema.SensorResponse, tags=["sensors"])
async def get_sensor(sensor_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Sensor).where(Sensor.id == sensor_id)).scalar()


@app.get("/sensors/", response_model=List[schema.SensorResponse], tags=["sensors"])
async def get_sensors(db: DBSession = Depends(get_db)):
    return list(db.execute(select(Sensor)).scalars())


# Sessions
@app.post("/sessions/", response_model=schema.SessionResponse, tags=["sessions"])
async def create_session(session: schema.SessionBase, db: DBSession = Depends(get_db)):
    session = Session(**session.dict())  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(session)
    db.commit()
    return session


@app.get("/sessions/{session_id}", response_model=schema.SessionResponse, tags=["sessions"])
async def get_session(session_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Session).where(Session.id == session_id)).scalar()


@app.get("/sessions/", response_model=List[schema.SessionResponse], tags=["sessions"])
async def get_sessions(db: DBSession = Depends(get_db)):
    return list(db.execute(select(Session)).scalars())


# Readings
@app.post("/readings/", response_model=schema.ReadingResponse, tags=["readings"])
async def create_reading(reading: schema.ReadingBase, db: DBSession = Depends(get_db)):
    reading = Reading(**reading.dict())  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(reading)
    db.commit()
    return reading


@app.get("/readings/{reading_id}", response_model=schema.ReadingResponse, tags=["readings"])
async def get_reading(reading_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Reading).where(Reading.id == reading_id)).scalar()


@app.get("/readings/", response_model=List[schema.ReadingResponse], tags=["readings"])
async def get_readings(db: DBSession = Depends(get_db)):
    return list(db.execute(select(Reading)).scalars())


# Organizations
@app.post("/organizations/", response_model=schema.OrganizationResponse, tags=["organizations"])
async def create_organization(
    organization: schema.OrganizationBase, db: DBSession = Depends(get_db)
):
    organization = Organization(
        **organization.dict()
    )  # Convert from Pydantic obj to SQLAlchemy obj
    db.add(organization)
    db.commit()
    return organization


@app.get(
    "/organizations/{organization_id}",
    response_model=schema.OrganizationResponse,
    tags=["organizations"],
)
async def get_organization(organization_id: int, db: DBSession = Depends(get_db)):
    return db.execute(select(Organization).where(Organization.id == organization_id)).scalar()


@app.get(
    "/organizations/", response_model=List[schema.OrganizationResponse], tags=["organizations"]
)
async def get_organizations(db: DBSession = Depends(get_db)):
    return list(db.execute(select(Organization)).scalars())
