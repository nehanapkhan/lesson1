# Function to check if a number is odd or even
def check_odd_even():
    num = int(input("Enter a number: "))  # Get user input
    if num % 2 == 0:
        print(f"{num} is Even")  # If divisible by 2, it's even
    else:
        print(f"{num} is Odd")   # Otherwise, it's odd

# Run the function
check_odd_even()

