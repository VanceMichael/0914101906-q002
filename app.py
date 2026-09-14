import os
import sqlite3
from fastapi import FastAPI

app = FastAPI(title="电影栏目片段授权簿")

def database_path() -> str:
    return os.getenv("REHEARSAL_PLAN_DB_PATH", "rehearsal-plan.db")

@app.get("/health")
def health():
    with sqlite3.connect(database_path()) as conn:
        conn.execute("select 1")
    return {"status": "ok"}
