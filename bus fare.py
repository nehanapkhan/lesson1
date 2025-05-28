# Base fare per kilometer
fare_per_km = 2.0

# Discounts
discounts = {
    "student": 0.5,   # 50% off
    "senior": 0.3,    # 30% off
    "adult": 0.0      # no discount
}

# Get input
distance = float(input("Enter distance (in km): "))
passenger_type = input("Enter passenger type (student/senior/adult): ").lower()

# Check if passenger type is valid
if passenger_type in discounts:
    discount = discounts[passenger_type]
    fare = distance * fare_per_km
    final_fare = fare * (1 - discount)
    print(f"{passenger_type.capitalize()} fare for {distance} km: ${final_fare:.2f}")
else:
    print("Invalid passenger type. Please enter student, senior, or adult.")
