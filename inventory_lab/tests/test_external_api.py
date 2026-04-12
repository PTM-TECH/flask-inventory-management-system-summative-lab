from unittest.mock import patch
from app import app

#create client
client = app.test_client()


@patch("api.requests.get")
def test_search_product(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "products": [
            {
                "product_name": "Milk",
                "brands": "Brookside",
                "code": "123"
            }
        ]
    }
    response = client.get("/products/search?q=milk")
    assert response.status_code == 200
    assert response.get_json()[0]["name"] == "Milk"

@patch("api.requests.get")
def test_get_product_by_barcode(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Bread",
            "brands": "SuperLoaf",
            "ingredients_text": "flour"
        }
    }
    response = client.get("/products/barcode/123")
    assert response.status_code == 200
    assert response.get_json()["name"] == "Bread"

#add from barcode
@patch("api.requests.get")
def test_add_from_barcode(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        "status": 1,
        "product": {
            "product_name": "Juice",
            "brands": "DelMonte"
        }
    }
    response = client.post("/inventory/from-barcode/999", json={
        "price": 100,
        "stock": 5
    })
    data = response.get_json()
    assert response.status_code == 201
    assert data["name"] == "Juice"