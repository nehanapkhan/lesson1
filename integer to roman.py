def int_to_roman(num):
    # Define the mapping of integers to Roman numerals
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4, 1
    ]
    
    syms = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV", "I"
    ]
    
    roman = ""
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman += syms[i]
            num -= val[i]
        i += 1
    return roman

# Ask user for a number
number = int(input("Enter an integer (1 to 3999): "))

# Validate and convert
if 1 <= number <= 3999:
    print(f"Roman numeral: {int_to_roman(number)}")
else:
    print("Please enter a number between 1 and 3999.")
