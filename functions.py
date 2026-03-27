# functions.py: Functions for inventory management
# Includes data validation with conditionals and while loops

def add_product(inventory):
    # Function to add product with input validation
    name = input("Product name: ").strip()

    # Validation: name not empty (while loop)
    while name == "":
        print("Error: Name cannot be empty.")
        name = input("Product name: ").strip()

    # Price validation: float >= 0 (try/except + while)
    try:
        price = float(input("Product price: "))
        while price < 0:
            print("Error: Price cannot be negative.")
            price = float(input("Product price: "))
    except ValueError:
        print("Invalid price.")
        return

    # Quantity validation: int > 0 (try/except + while)
    try:
        quantity = int(input("Quantity: "))
        while quantity <= 0:
            print("Error: Quantity must be greater than 0.")
            quantity = int(input("Quantity: "))
    except ValueError:
        print("Invalid quantity.")
        return

    # Create product dictionary
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    # Add to inventory list
    inventory.append(product)

    print("Product added successfully.")


def show_inventory(inventory):
    # Function to display inventory using for loop
    if not inventory:
        print("Inventory is empty.")
        return

    print("\n=== INVENTORY ===")
    for product in inventory:
        # Required clear format
        print(f"Product: {product['name']} | Price: ${product['price']} | Quantity: {product['quantity']}")
