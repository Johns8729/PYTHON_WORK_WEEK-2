# calculations.py: Functions for calculating inventory statistics
# Uses for loop to traverse the list and calculate totals

def calculate(inventory):
    # Check if there are products
    if not inventory:
        print("No products available.")
        return

    total_value = 0  # Total inventory value
    total_quantity = 0  # Total number of units

    # for loop to calculate statistics
    for product in inventory:
        # price * quantity added to total
        total_value += product["price"] * product["quantity"]
        total_quantity += product["quantity"]

    # Show clear results
    print("\n=== STATISTICS ===")
    print("Total inventory value: $%.2f" % total_value)
    print("Total product quantity: %d" % total_quantity)
