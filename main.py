# main.py: Main file that controls the program flow with interactive menu
from functions import add_product, show_inventory
from calculations import calculate


def summary(inventory):
    print("\n=== FINAL SUMMARY ===")
    show_inventory(inventory)
    calculate(inventory)
    print("Program finished.")


def main():
    inventory = []

    continuar = "si"  # Control del ciclo

    while continuar == "si":

        print("\n=== MAIN MENU ===")
        print("1. Add product")
        print("2. Show inventory")
        print("3. Calculate statistics")
        print("4. Exit")

        option = input("Enter an option (1-4): ").strip()

        if option == "1":
            add_product(inventory)
        elif option == "2":
            show_inventory(inventory)
        elif option == "3":
            calculate(inventory)
        elif option == "4":
            print("\nExiting the program")
            continuar = "no"  # Aquí se detiene el ciclo
        else:
            print("Invalid option. Try again.")

    if inventory:
        summary(inventory)
    else:
        print("\nInventory is empty Goodbye")


if __name__ == "__main__":
    main()