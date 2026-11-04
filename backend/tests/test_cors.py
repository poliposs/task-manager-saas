from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# Test the health check endpoint for failure
def test_cors_allows_frontend_origin_fail():
    origin = "http://localhost:5173"
    response = client.options("/health", headers={"Origin": origin})
    assert response.headers.get("access-control-allow-origin") == origin
