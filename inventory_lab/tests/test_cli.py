import builtins
from unittest.mock import patch
import main

def test_menu_display(capsys):
    main.menu()
    captured = capsys.readouterr()
    assert "Inventory CLI" in captured.out
    assert "1. View Inventory" in captured.out

@patch("requests.get")
def test_view_inventory(mock_get, capsys):
    mock_get.return_value.json.return_value = [
        {"id": 1, "name": "Milk", "price": 3.5}
    ]
    main.view_inventory()
    captured = capsys.readouterr()
    assert "Milk" in captured.out

@patch("requests.post")
@patch("builtins.input", side_effect=[
    "Milk",
    "BrandA",
    "3.5",
    "10",
    "123456"
])
def test_add_item(mock_input, mock_post, capsys):
    mock_post.return_value.json.return_value = {
        "id": 1,
        "name": "Milk"
    }
    main.add_item()
    captured = capsys.readouterr()
    assert "Milk" in captured.out

@patch("requests.delete")
@patch("builtins.input", side_effect=["1"])
def test_delete_item(mock_input, mock_delete, capsys):
    mock_delete.return_value.json.return_value = {
        "message": "Item deleted"
    }
    main.delete_item()
    captured = capsys.readouterr()
    assert "Item deleted" in captured.out