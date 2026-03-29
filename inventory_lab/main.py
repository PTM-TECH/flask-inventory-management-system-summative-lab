import requests
from api import get_product_by_barcode, search_product_by_name

# Base URL for the local Flask inventory API
BASE_URL = "http://127.0.0.1:5000/inventory"

#function to display the CLI menu options
def menu():
    print("-"*10)
    print("\nPawatech Inventory Management")
    print("-"*10)
    print("1. View Inventory")
    print("2. Add Item Manually")
    print("3. Update Item Price")
    print("4. Delete Item")
    print("5. Search Product (Barcode / Name)")
    print("6. Exit")

# Function to fetch and display all inventory items
def view_inventory():
    # Send GET request to Flask API
    response = requests.get(BASE_URL)
    items = response.json()
    # If inventory is empty
    if not items:
        print("Inventory is empty")
        return
    # Print each item
    for item in items:
        print(item)

#function to add a product manually via CLI input
def add_item_manual():
    # Collect product information from user
    name = input("Enter product name: ")
    brand = input("Enter product brand: ")
    price = float(input("Enter product price: "))
    stock = int(input("Enter stock quantity: "))
    barcode = input("Enter barcode: ")

    # Create JSON payload
    data = {
        "name": name,
        "brand": brand,
        "price": price,
        "stock": stock,
        "barcode": barcode
    }
    # Send POST request to API to create item
    response = requests.post(BASE_URL, json=data)
    print("Item added successfully:", response.json())
#function to update the price of an existing inventory item
def update_item():
    # Ask user for item ID
    item_id = input("Enter Item ID: ")
    # Ask for new price
    new_price = float(input("Enter New price: "))
    # Send PATCH request to update the item
    response = requests.patch(
        f"{BASE_URL}/{item_id}",
        json={"price": new_price}
    )
    print(response.json())

#function to delete an item from inventory
def delete_item():
    item_id = input("Enter Item ID: ")
    # Send DELETE request to API
    response = requests.delete(f"{BASE_URL}/{item_id}")
    print(response.json())

#function to search for a product using barcode OR product name
def search_product():
    query = input("Enter barcode OR product name: ")

    # If input is numeric, treat it as a barcode
    if query.isdigit():
        # Fetch product from OpenFoodFacts
        product = get_product_by_barcode(query)
        if not product:
            print("Product not found in OpenFoodFacts")
            return
        print("Product found:", product)
        # Ask user for price and stock
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        data = {
            "name": product["name"],
            "brand": product["brand"],
            "price": price,
            "stock": stock,
            "barcode": product["barcode"]
        }
        # Add product to inventory via Flask API
        response = requests.post(BASE_URL, json=data)
        print("Product added to inventory:", response.json())
    else:
        # Otherwise treat input as product name
        results = search_product_by_name(query)
        if not results:
            print("No products found")
            return
        print("\nSearch results:")

        # Display search results
        for i, product in enumerate(results):
            print(f"{i+1}. {product['name']} - {product['brand']}")
        # User selects product
        choice = int(input("Select product number: ")) - 1
        selected = results[choice]
        print("Selected product:", selected)
        # Ask for inventory details
        price = float(input("Enter price: "))
        stock = int(input("Enter stock quantity: "))
        data = {
            "name": selected["name"],
            "brand": selected["brand"],
            "price": price,
            "stock": stock,
            "barcode": selected["barcode"]
        }
        # Add selected product to inventory
        response = requests.post(BASE_URL, json=data)
        print("Product added:", response.json())

def run():
    while True:
        # Display menu
        menu()
        # Get user choice
        choice = input("Choose option: ")
        if choice == "1":
            view_inventory()
        elif choice == "2":
            add_item_manual()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            search_product()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid option")


# Start CLI when file runs
if __name__ == "__main__":
    run()