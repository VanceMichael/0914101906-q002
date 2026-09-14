from fastapi.testclient import TestClient
from app import app

def test_health(tmp_path, monkeypatch):
    monkeypatch.setenv("FILM_DB_PATH", str(tmp_path / "film.db"))
    assert TestClient(app).get("/health").json()["status"] == "ok"
