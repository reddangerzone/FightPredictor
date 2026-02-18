import api
import pandas as pd
import time
import psycopg2
import os
from datetime import datetime

load_dotenv()

# -- connect to database
def connect():
    try:
        conn = psycopg2.connect(
        host=os.getenv("DB_URL"),
        database="postgres",
        user="postgres",
        password=os.getenv("DB_PASSWORD"),
        port="5432"
        )
        
        print("✅ Database connected")

        conn.close()

    except Exception as e:
        print(f"❌ Connection failed: {e}")

