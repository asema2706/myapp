import pytest
import app
import json

@pytest.fixture
def client():
    """Фикстура для создания тестового клиента Flask"""
    app.app.config['TESTING'] = True
    with app.app.test_client() as client:
        yield client

def test_hello_endpoint(client):
    """Тест главного эндпоинта"""
    response = client.get('/')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert data['message'] == "Hello, DevOps!"

def test_health_endpoint(client):
    """Тест health-эндпоинта"""
    response = client.get('/health')
    data = json.loads(response.data)
    assert response.status_code == 200
    assert 'status' in data
    assert data['status'] == "ok"

def test_external_api(client):
    """Тест внешнего API (с моком для изоляции)"""
    response = client.get('/external')
    assert response.status_code == 200

def test_invalid_route(client):
    """Тест несуществующего маршрута"""
    response = client.get('/invalid')
    assert response.status_code == 404