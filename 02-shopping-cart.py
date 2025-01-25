def calculate_cart_total(items, quantities):
    """
    Calculate the total cost of items in a shopping cart.

    Args:
        items: List of item prices
        quantities: List of quantities for each item

    Returns:
        total_cost: Total cost of all items
    """
    # Initialize the running total
    total_cost = 0

    # Bug 1: List index error will occur if lists are different lengths
    for i in range(len(items)):
        # Bug 2: Calculation error in the total
        # Correct calculation should be: price * quantity
        # Current calculation adds instead of multiplies
        item_cost = items[i] + quantities[i]
        total_cost += item_cost

    return round(total_cost, 2)


# Test the function
def test_shopping_cart():
    # Test case 1: Simple cart
    prices = [10.00, 5.00, 3.00]
    quantities = [2, 1]  # Missing one quantity - will cause index error

    print("Shopping Cart Contents:")
    print("----------------------")
    for i in range(len(prices)):
        print(
            f"Item {i + 1}: ${prices[i]} (Quantity: {quantities[i] if i < len(quantities) else '?'})"
        )

    print("\nCalculating total...")
    total = calculate_cart_total(prices, quantities)
    print(f"Total cost: ${total}")


if __name__ == "__main__":
    test_shopping_cart()
