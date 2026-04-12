from unittest.mock import patch
import main



def test_menu_display(capsys):
    main.menu()
    captured = capsys.readouterr()
    assert "INVENTORY MANAGEMENT SYSTEM" in captured.out

#view inventory (mock requests)
@patch("requests.get")
def test_view_inventory(mock_get, capsys):
    mock_get.return_value.json.return_value = [
        {
            "id": 1,
            "name": "Milk",
            "brand": "Brookside",
            "price": 100,
            "stock": 10,
            "barcode": "123"
        }
    ]
    main.view_inventory()
    captured = capsys.readouterr()
    assert "Milk" in captured.out

#Delete an item
@patch("requests.delete")
@patch("builtins.input", side_effect=["1"])
def test_delete_item(mock_input, mock_delete, capsys):
    mock_delete.return_value.status_code = 200
    mock_delete.return_value.json.return_value = {
        "message": "Item deleted"
    }
    main.delete_item()
    captured = capsys.readouterr()
    assert "deleted" in captured.out.lower()