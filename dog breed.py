import tkinter as tk
import random

# List of dog breeds
breeds = [
    "Beagle", "Pug", "Bulldog", "Dalmatian", 
    "Labrador", "Husky", "Boxer", "Poodle"
]

# Function to show random breed
def show_random_breed():
    breed = random.choice(breeds)
    label.config(text=f"Random Dog Breed:\n{breed}")

# Create window
window = tk.Tk()
window.title("Dog Breed Viewer")
window.geometry("300x200")

# Breed label
label = tk.Label(window, text="Click the button to see a dog breed!", font=("Arial", 14), wraplength=250, justify="center")
label.pack(pady=20)

# Button
button = tk.Button(window, text="Show Random Dog Breed", command=show_random_breed)
button
