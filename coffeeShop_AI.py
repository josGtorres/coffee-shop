"""
Project name: coffeeShop.py
Author: Josue Garcia
Date: 8/31/26

Project that contains an ordering system for a coffee shop.
It asks for customer's name, amount of items, and displays the total price.
"""

# Menu: item name -> unit price
MENU = {
    "coffee": 4.50,
    "pastry": 3.00,
}


def get_customer_name():
    """Ask for the customer's name, re-prompting if left blank."""
    while True:
        name = input("Please enter your name >> ").strip()
        if name:
            return name
        print("Name can't be empty. Please try again.\n")


def get_quantity(item_name):
    """Ask how many of an item the customer wants.
    Re-prompts until a valid, non-negative whole number is entered."""
    while True:
        raw_value = input(f"How many {item_name}(s) do you want to order? >> ")
        try:
            quantity = int(raw_value)
        except ValueError:
            print("Please enter a whole number (e.g. 2).\n")
            continue

        if quantity < 0:
            print("Quantity can't be negative. Please try again.\n")
            continue

        return quantity


def get_order():
    """Collect the customer's name and quantities for every item in MENU.
    Returns (customer_name, {item_name: quantity})."""
    customer_name = get_customer_name()
    order = {}
    for item_name in MENU:
        order[item_name] = get_quantity(item_name)
    return customer_name, order


def calculate_subtotals(order):
    """Turn {item_name: quantity} into {item_name: (quantity, unit_price, subtotal)}."""
    subtotals = {}
    for item_name, quantity in order.items():
        unit_price = MENU[item_name]
        subtotals[item_name] = (quantity, unit_price, quantity * unit_price)
    return subtotals


def print_receipt(customer_name, subtotals):
    """Display a formatted receipt with per-item breakdown and grand total."""
    print(f"\nOrder for {customer_name}!")
    print("-" * 35)

    grand_total = 0.0
    for item_name, (quantity, unit_price, subtotal) in subtotals.items():
        print(
            f"{item_name.capitalize():<10} qty: {quantity:<3} "
            f"@ ${unit_price:.2f} each -- Subtotal: ${subtotal:.2f}"
        )
        grand_total += subtotal

    print("-" * 35)
    print(f"Your total is: ${grand_total:.2f}")
    print("Enjoy!")


def main():
    customer_name, order = get_order()
    subtotals = calculate_subtotals(order)
    print_receipt(customer_name, subtotals)
    input("\nPress ENTER to quit")


if __name__ == "__main__":
    main()
