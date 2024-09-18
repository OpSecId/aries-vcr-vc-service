from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_check():
    """Test app health check"""

    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}