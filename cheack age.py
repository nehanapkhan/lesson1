from datetime import date

def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year

def check_age_group(age):
    if age < 0:
        return "Invalid age entered."
    elif age < 18:
        return "You are a minor."
    elif age < 65:
        return "You are an adult."
    else:
        return "You are a senior."

if __name__ == "__main__":
    try:
        birth_year = int(input("Enter your birth year: "))
        age = calculate_age(birth_year)
        print(f"You are {age} years old.")
        print(check_age_group(age))
    except ValueError:
        print("Invalid input. Please enter a valid year.")
