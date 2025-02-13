# Simple Birthday Storage Program

# Dictionary to store birthdays
birthdays = {}

# Function to add a birthday
def add_birthday():
    name = input("Enter name: ")
    date = input("Enter birthday (DD/MM/YYYY): ")
    birthdays[name] = date
    print(f"Birthday of {name} added successfully!\n")

# Function to get a birthday
def get_birthday():
    name = input("Enter name to search: ")
    print(birthdays.get(name, "Birthday not found!\n"))

# Function to display all birthdays
def display_birthdays():
    if birthdays:
        print("\nStored Birthdays:")
        for name, date in birthdays.items():
            print(f"{name}: {date}")
    else:
        print("No birthdays stored yet.\n")

# Main loop
while True:
    print("\n1. Add Birthday\n2. Get Birthday\n3. Display All Birthdays\n4. Exit")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_birthday()
    elif choice == "2":
        get_birthday()
    elif choice == "3":
        display_birthdays()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice! Please try again.\n")
