from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Test the health check endpoint
def test_health_returns_ok():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
