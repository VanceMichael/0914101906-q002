import os, sqlite3

path = os.getenv("REHEARSAL_PLAN_DB_PATH", "rehearsal-plan.db")
with sqlite3.connect(path) as conn:
    conn.execute("create table if not exists schema_version(version integer not null)")
    conn.commit()
print("数据库已初始化")
