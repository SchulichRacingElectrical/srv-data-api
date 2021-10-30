import psycopg2

from api.database import DATABASE_URL

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

cursor.execute(
    """
    DROP TABLE IF EXISTS data
    """
)

cursor.execute(
    """
    DROP TABLE IF EXISTS runs
    """
)

cursor.execute(
    """
    DROP TABLE IF EXISTS sessions
    """
)

conn.commit()
