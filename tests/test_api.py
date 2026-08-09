from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json() == {'status': 'ok'}


def test_system_endpoint():
    response = client.get('/api/system')
    assert response.status_code == 200
    body = response.json()
    assert 'hostname' in body
    assert 'cpu_percent' in body
    assert 'memory_percent' in body
    assert 'disk_percent' in body
    assert 'network' in body
