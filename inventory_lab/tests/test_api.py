from app import app

def test_get_inventory():
    client = app.test_client()
    response = client.get("/inventory")
    assert response.status_code == 200