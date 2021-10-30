import psycopg2

from api.database import DATABASE_URL

conn = psycopg2.connect(DATABASE_URL)
cursor = conn.cursor()

# Create sessions table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS sessions (
        id INTEGER PRIMARY KEY,
        date DATE NOT NULL
    )
    """
)

# Create runs table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS runs (
        id INTEGER PRIMARY KEY,
        session_id INTEGER NOT NULL,
        start_time TIMESTAMP NOT NULL,
        end_time TIMESTAMP NOT NULL,
        CONSTRAINT fk_session
        FOREIGN KEY(session_id)
        REFERENCES sessions(id)
    )
    """
)

# Create data table
cursor.execute(
    """
    CREATE TABLE IF NOT EXISTS data (
        id INTEGER PRIMARY KEY,
        run_id INTEGER NOT NULL,
        timestamp TIMESTAMP NOT NULL,
        CONSTRAINT fk_run
        FOREIGN KEY(run_id)
        REFERENCES runs(id)
    )
    """
)

conn.commit()
