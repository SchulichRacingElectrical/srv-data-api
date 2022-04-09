from api.database import Session


def get_db():
    """
    Generate a database session.
    """
    try:
        db = Session()
        yield db
    finally:
        db.close()
