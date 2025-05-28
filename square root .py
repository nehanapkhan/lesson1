import math

# Ask the user for a number
num = float(input("Enter a number to find its square root: "))

# Check for non-negative input
if num < 0:
    print("Sorry, square root of negative numbers is not supported.")
else:
    sqrt = math.sqrt(num)
    print(f"The square root of {num} is {sqrt:.4f}")
