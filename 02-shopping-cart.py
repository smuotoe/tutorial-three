def process_item(price, quantity):
    """Process a single item in the cart."""
    # This will throw TypeError when price is a string
    processed_price = price + 5  # Adding handling fee

    # This will throw ValueError for negative quantities
    if quantity <= 0:
        raise ValueError("Quantity must be positive")

    return processed_price * quantity


def calculate_cart_total(items, quantities):
    """
    Calculate the total cost of items in a shopping cart.

    Args:
        items: List of item prices
        quantities: List of quantities for each item
    """
    total_cost = 0

    # This will throw IndexError when processing last item
    for i in range(len(items) + 1):  # Intentionally one step too far
        item_cost = process_item(items[i], quantities[i])
        total_cost += item_cost

    return round(total_cost, 2)


def test_shopping_cart():
    # Test case with multiple issues:
    # - String price that will cause TypeError
    # - Negative quantity that will cause ValueError
    # - Unequal list lengths that will cause IndexError
    prices = [10.00, "5.00", 3.00]
    quantities = [2, -1, 1, 4]  # Extra quantity will contribute to index error

    print("Shopping Cart Contents:")
    print("----------------------")
    for i, price in enumerate(prices):
        print(f"Item {i + 1}: ${price}")

    print("\nCalculating total...")
    total = calculate_cart_total(prices, quantities)
    print(f"Total cost: ${total}")


if __name__ == "__main__":
    test_shopping_cart()