import math

# Ask the user for the radius
radius = float(input("Enter the radius of the circle: "))

# Calculate area and perimeter
area = math.pi * radius ** 2
perimeter = 2 * math.pi * radius  # also called circumference

# Show the results
print(f"Area of the circle: {area:.2f}")
print(f"Perimeter (Circumference) of the circle: {perimeter:.2f}")
