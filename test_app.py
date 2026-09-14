from fastapi.testclient import TestClient
from app import app

def test_health(tmp_path, monkeypatch):
    monkeypatch.setenv("REHEARSAL_PLAN_DB_PATH", str(tmp_path / "rehearsal-plan.db"))
    assert TestClient(app).get("/health").json()["status"] == "ok"
