# 剧目合成排期裁决器

这是一个 FastAPI 纯后端项目，排练安排使用本地 SQLite 文件保存。默认文件为 `rehearsal-plan.db`，可通过 `REHEARSAL_PLAN_DB_PATH` 指定。

初始化：`python migrate.py`。启动：`uvicorn app:app --host 0.0.0.0 --port 8080`，健康检查为 `/health`。测试：`pytest`。容器运行：`docker build -t rehearsal-plan . && docker run --rm -p 8080:8080 rehearsal-plan`。
