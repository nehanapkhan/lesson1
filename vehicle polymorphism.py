# Base class
class Vehicle:
    def start(self):
        print("Vehicle is starting")

    def stop(self):
        print("Vehicle is stopping")

# Derived class 1
class Car(Vehicle):
    def start(self):
        print("Car engine is starting with a key")

    def stop(self):
        print("Car is stopping with brakes")

# Derived class 2
class Bike(Vehicle):
    def start(self):
        print("Bike engine is starting with a button")

    def stop(self):
        print("Bike is stopping using hand brakes")

# Function that uses polymorphism
def start_vehicle(vehicle):
    vehicle.start()

def stop_vehicle(vehicle):
    vehicle.stop()

# Create objects
v = Vehicle()
c = Car()
b = Bike()

# Demonstrate polymorphism
for vehicle in (v, c, b):
    start_vehicle(vehicle)
    stop_vehicle(vehicle)
    print("---")
