def calculate_power(base, exponent):
    """
    Calculates the power of a number.

    Args:
        base (float): The base number.
        exponent (float): The exponent.

    Returns:
        float: The result of base raised to the power of exponent.
    """
    return base ** exponent

if __name__ == "__main__":
    try:
        base = float(input("Enter the base: "))
        exponent = float(input("Enter the exponent: "))
        result = calculate_power(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}")
    except ValueError:
        print("Invalid input. Please enter numeric values.")
