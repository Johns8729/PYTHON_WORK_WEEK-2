# main.py: Main file that controls the program flow with interactive menu
# Uses conditional statements (if/elif/else) to process options and while loop for persistence

# Import functions from other modules
from functions import add_product, show_inventory
from calculations import calculate


def summary(inventory):
    # Final program summary
    print("\n=== FINAL SUMMARY ===")

    # Show all products
    show_inventory(inventory)

    # Show statistics
    calculate(inventory)

    print("Program finished.")


def main():
    # Main function that runs the program

    inventory = []  # Empty list for inventory (list of dictionaries)

    # Main while loop for interactive menu until 'Exit'
    while True:

        print("\n=== MAIN MENU ===")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Calculate statistics")
        print("4. Exit")

        # User selects option with validation
        option = input("Enter an option (1-4): ").strip()

        # Process option using if/elif/else conditionals
        if option == "1":
            add_product(inventory)
        elif option == "2":
            show_inventory(inventory)
        elif option == "3":
            calculate(inventory)
        elif option == "4":
            print("\nExiting the program!")
            break  # Exit the while loop
        else:
            print(" Invalid option. Try again.")
            # The while loop automatically reprompts the menu

    # Show summary if there are products
    if inventory:
        summary(inventory)
    else:
        print("\nInventory is empty. Goodbye!")


# Start the program
if __name__ == "__main__":
    main()

# WEEKLY OBJECTIVE: Manage multiple products in inventory via interactive menu, using
# conditionals (if/elif/else), loops (while and for), lists and dictionaries for storage,
# data validation, and basic statistics.
