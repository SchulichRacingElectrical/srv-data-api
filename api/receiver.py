# Copyright Schulich Racing FSAE
# Written By Joey Van Lierop

import os
import redis
import time
import threading
import json

from sqlalchemy import insert

from api.models import Reading
from api.dependencies import get_db

db = get_db()


class Batcher(threading.Thread):
    def __init__(self):
        self.batch = []

    def add_message(self, message: dict):
        self.batch.append(message)

    def run(self):
        stmt = insert(Reading).values(self.batch).on_conflict_do_nothing()
        db.execute(stmt)
        db.commit()
        self.batch = []
        time.sleep(5)


class Receiver:
    def __init__(self):
        self.receivers = []
        self.redis_db = redis.Redis(
            host=os.getenv("REDIS_URL"),
            port=os.getenv("REDIS_PORT"),
            username=os.getenv("REDIS_USERNAME"),
            password=os.getenv("REDIS_PASSWORD"),
        )
        self.batcher = Batcher()

    def run(self):
        self.batcher.start()
        sub = self.redis_db.pubsub()
        sub.subscribe("messages")
        for message in sub.listen():
            self.handle_message(message)

    def handle_message(self, message):
        if message and not message["data"] == 1:
            json_message = json.loads(message["data"].decode("utf-8"))
            if "active" in json_message:
                if json_message["error"]:
                    # Error message
                    pass
                elif json_message["active"]:
                    # Either connection or disconnection message
                    pass
                else:
                    # Snapshot message
                    # Forward message to data api
                    # Add message to batcher
                    pass
