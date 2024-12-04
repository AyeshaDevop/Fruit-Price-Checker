def calculate_total_cost(fruit_prices):
    """
    Calculates the total cost of fruits based on user input.
    Args:
        fruit_prices (dict): A dictionary where keys are fruit names and values are their prices.
    Returns:
        float: The total cost of the fruits purchased.
    """
    total_cost = 0
    print("Enter the quantity for each fruit:")
    for fruit, price in fruit_prices.items():
        try:
            amount_bought = int(input(f"How many ({fruit}) do you want to buy?: "))
            total_cost += price * amount_bought
        except ValueError:
            print("Invalid input. Please enter a number.")
    return total_cost


def main():
    """
    Main function to calculate the total cost of fruits purchased:
    - Prompts the user for quantities of each fruit.
    - Displays the total cost.
    """
    fruit_prices = {
        'apple': 1.5,
        'durian': 50,
        'jackfruit': 80,
        'kiwi': 1,
        'rambutan': 1.5,
        'mango': 5
    }

    print("Welcome to the Fruit Shop Calculator!")
    total_cost = calculate_total_cost(fruit_prices)
    print(f"Your total is ${total_cost:.2f}")

if __name__ == '__main__':
    main()