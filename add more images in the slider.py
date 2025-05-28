import tkinter as tk
from PIL import Image, ImageTk

# Create the main window
window = tk.Tk()
window.title("Image Slider")

# List of image files
images = ["image1.png", "image2.png", "image3.png"]  # Add more if you want!

# Load images
loaded_images = [ImageTk.PhotoImage(Image.open(img).resize((300, 200))) for img in images]

# Current image index
index = 0

# Label to display the image
image_label = tk.Label(window, image=loaded_images[index])
image_label.pack()

# Function to go to the next image
def next_image():
    global index
    index = (index + 1) % len(loaded_images)
    image_label.config(image=loaded_images[index])

# Function to go to the previous image
def prev_image():
    global index
    index = (index - 1) % len(loaded_images)
    image_label.config(image=loaded_images[index])

# Buttons to change images
btn_prev = tk.Button(window, text="Previous", command=prev_image)
btn_prev.pack(side="left", padx=10)

btn_next = tk.Button(window, text="Next", command=next_image)
btn_next.pack(side="right", padx=10)

# Run the app
window.mainloop()
