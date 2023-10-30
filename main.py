import tkinter as tk
from PIL import Image, ImageTk
import random
import os

# List of image file paths
# image_paths = ["alex_mages_bid.png", "alex_mages_pe.png","alex_mages_title.png", "bomb_defense.png","BWB.png", "bomb_defense_inv.png"]
# image_paths = [f for f in os.listdir() if os.path.isfile(f)]
image_paths = []
for filename in os.listdir():
    if filename.lower().endswith('.png'):
        image_paths.append(os.path.abspath(filename))
print(image_paths)

current_image_index = random.randint(0,len(image_paths))

# Create the main application window
app = tk.Tk()
# app.attributes('-fullscreen', True)


# Create a label to display images
image_label = tk.Label(app)
image_label.pack()

# Function to update the displayed image
def update_image():
    global current_image_index
    if current_image_index >= len(image_paths):
        current_image_index = 0

    image_path = image_paths[current_image_index]
    img = Image.open(image_path)
    img = img.resize((1280, 400))
    img_tk = ImageTk.PhotoImage(img)

    image_label.config(image=img_tk)
    image_label.image = img_tk
    current_image_index = random.randint(0,len(image_paths))
    app.after(random.randint(30000,300000), update_image)  # Schedule the next update after 60 seconds

# Initial image update
update_image()

# Start the tkinter main loop
app.mainloop()