## Inventory Management System

## Project Overview

This is a Flask-based Inventory Management System that allows users to:

- Manage inventory items (CRUD operations)
- Fetch real product data from the OpenFoodFacts API
- Add products manually
- Interact through a CLI (Command Line Interface)
- Run automated tests using pytest

## Features

# Inventory Management(CRUD)
- Create Inventory items
- View all inventory
- Update item details like price.
- Delete Items

# External API Integration
- Search Products by name
- Fetch product by barcode
- Add fetched products to inventory

# CLI Interface
- Interactive menu system
- Adds items manually
- Search products
- Update and delete items

# Testing
- Full API endpoint testing
- CLI function testing
- External API mocking using unittest.mock

## Project Structure

inventory_lab/
│
├── app.py                # Flask REST API
├── inventory.py          # In-memory database 
├── api.py                # External API integration (OpenFoodFacts)
├── main.py               # CLI application
│
├── tests/
│   ├── test_api.py       # Flask API tests
│   ├── test_cli.py       # CLI tests
│
├── requirements.txt
├── README.md

## Installation & Setup

- git fork & clone <link>
- cd inventory_lab
- Create & activate virtual environment
    - python3 -m venv venv
    - source venv/bin/activate
- pip install -r requirements.txt

## Running the project
- Run python3 main.py

## API Endpoints

| Method | Endpoint        | Description    |
| ------ | --------------- | -------------- |
| GET    | /inventory      | Get all items  |
| GET    | /inventory/<id> | Get item by ID |
| POST   | /inventory      | Add new item   |
| PATCH  | /inventory/<id> | Update item    |
| DELETE | /inventory/<id> | Delete item    |

## External API Routes

| Method | Endpoint                          | Description            |
| ------ | ------------------------------    | ---------------------- |
| GET    | /products/search?q=name           | Search products        |
| GET    | /products/barcode/<barcode>       | Get product by barcode |
| POST   | /inventory/from-barcode/<barcode> | Add product from API   |


## CLI Usage

---------------------
Inventory Management
---------------------
1. View Inventory
2. Add Item
3. Update Item
4. Delete Item
5. Search Product
6. Exit

## Search by name sample
- milk
- nutella
- coca cola
- oreo
- bread
## Search by Barcode
- 737628064502
- 3017620422003
- 5449000000996
- 7622210449283
- 7622300449283
## Running Tests
Run all tests by:
    - pytest

## Author

# Patrick Mutua
