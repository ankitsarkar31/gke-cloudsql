import mysql.connector
import os
import time

def get_db():
    last_error = None

    for i in range(10):
        try:
            return mysql.connector.connect(
                host=os.getenv("DB_HOST", "127.0.0.1"),
                user=os.environ["DB_USER"],
                password=os.environ["DB_PASSWORD"],
                database=os.environ["DB_NAME"],
                port=int(os.getenv("DB_PORT", "3306")),
                connection_timeout=5
            )
        except mysql.connector.Error as e:
            last_error = e
            print(f"[DB RETRY {i+1}/10] {e}")
            time.sleep(2)

    raise Exception("Could not connect to database") from last_error

