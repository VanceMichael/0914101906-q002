# 剧目合成排期裁决器

这是一个 FastAPI 纯后端项目，数据保存在本地 SQLite 文件。默认文件为 `film.db`，也可通过 `FILM_DB_PATH` 指定路径。

初始化：`python migrate.py`。启动：`uvicorn app:app --host 0.0.0.0 --port 8080`，健康检查为 `/health`。测试：`pytest`。容器运行：`docker build -t film-rights-ledger . && docker run --rm -p 8080:8080 film-rights-ledger`。
