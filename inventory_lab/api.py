import requests

# Base endpoints for OpenFoodFacts API
BARCODE_URL = "https://world.openfoodfacts.org/api/v0/product/"
SEARCH_URL = "https://world.openfoodfacts.org/cgi/search.pl"

#function to fetch product details using a barcode
def get_product_by_barcode(barcode):

    url = f"{BARCODE_URL}{barcode}.json"
    response = requests.get(url)
    if response.status_code != 200:
        return None
    data = response.json()
    # If product does not exist
    if data["status"] != 1:
        return None
    product = data["product"]
    #extract only useful fields
    return {
        "name": product.get("product_name"),
        "brand": product.get("brands"),
        "ingredients": product.get("ingredients_text"),
        "barcode": barcode
    }

#function to search products using a product name
def search_product_by_name(product_name):

    params = {
        "search_terms": product_name,
        "search_simple": 1,
        "action": "process",
        "json": 1
    }
    response = requests.get(SEARCH_URL, params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    results = []

    for product in data.get("products", [])[:5]:  # limit to first 5 results
        results.append({
            "name": product.get("product_name"),
            "brand": product.get("brands"),
            "barcode": product.get("code")
        })
    return results