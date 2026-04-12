from app import app
import pytest
from unittest.mock import patch

#create test client
client = app.test_client()

#reset state helpers for clean tests -> every run
@pytest.fixture(autouse=True)
def reset_inventory():
    import inventory
    inventory.inventory.clear()
    inventory.current_id = 1

#Get all items
def test_get_inventory_empty():
    response = client.get("/inventory")
    assert response.status_code == 200
    assert response.get_json() == []

#Create an item
def test_create_item():
    response = client.post("/inventory", json={
        "name": "Milk",
        "brand": "Brookside",
        "price": 120,
        "stock": 10,
        "barcode": "12345"
    })
    data = response.get_json()
    assert response.status_code == 201
    assert data["name"] == "Milk"
    assert data["id"] == 1

#Get single item
def test_get_single_item():
    client.post("/inventory", json={
        "name": "Bread",
        "brand": "SuperLoaf",
        "price": 50,
        "stock": 5,
        "barcode": "222"
    })
    response = client.get("/inventory/1")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Bread"

#Update an item
def test_update_item():
    client.post("/inventory", json={
        "name": "Sugar",
        "brand": "Mumias",
        "price": 200,
        "stock": 5,
        "barcode": "333"
    })
    response = client.patch("/inventory/1", json={
        "price": 250
    })
    data = response.get_json()
    assert response.status_code == 200
    assert data["price"] == 250

#Delete an item
def test_delete_item():
    client.post("/inventory", json={
        "name": "Salt",
        "brand": "Kensalt",
        "price": 30,
        "stock": 20,
        "barcode": "444"
    })
    response = client.delete("/inventory/1")
    assert response.status_code == 200
    assert response.get_json()["message"] == "Item deleted"

#Get non-existent item
def test_item_not_found():
    response = client.get("/inventory/999")
    assert response.status_code == 404