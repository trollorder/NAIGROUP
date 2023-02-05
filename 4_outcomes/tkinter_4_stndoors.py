import tkinter as tk
from PIL import Image, ImageTk

root= tk.Tk()
root.title("Our Approach Outcome")
# root['background'] = '#eee5e5'
root.window_start_x = (root.winfo_screenwidth())
root.window_start_y = (root.winfo_screenheight())
root.geometry("1920x768")

def change_carriage_1():
    # Load the new image
    ratio = root.window_start_x / 706
    final_x = int(706*ratio)
    final_y = int(165*ratio)
    new_image = Image.open("outcome_1.jpg")
    new_image = new_image.resize((final_x,final_y), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(new_image)

    # Update the image label
    label.config(image=new_image)
    label.image = new_image

def change_carriage_2():
    # Load the new image
    ratio = root.window_start_x / 706
    final_x = int(706*ratio)
    final_y = int(165*ratio)
    new_image = Image.open("outcome_2.jpg")
    new_image = new_image.resize((final_x,final_y), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(new_image)

    # Update the image label
    label.config(image=new_image)
    label.image = new_image

def change_carriage_3():
    # Load the new image
    ratio = root.window_start_x / 706
    final_x = int(706*ratio)
    final_y = int(165*ratio)
    new_image = Image.open("outcome_3.jpg")
    new_image = new_image.resize((final_x,final_y), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(new_image)

    # Update the image label
    label.config(image=new_image)
    label.image = new_image

def change_carriage_4():
    # Load the new image
    ratio = root.window_start_x / 706
    final_x = int(706*ratio)
    final_y = int(165*ratio)
    new_image = Image.open("outcome_4.jpg")
    new_image = new_image.resize((final_x,final_y), Image.ANTIALIAS)
    new_image = ImageTk.PhotoImage(new_image)

    # Update the image label
    label.config(image=new_image)
    label.image = new_image


# Load the first image
ratio = root.window_start_x / 706
final_x = int(706*ratio)
final_y = int(165*ratio)
image = Image.open("outcome_1.jpg")
image = image.resize((final_x,final_y), Image.ANTIALIAS)
image = ImageTk.PhotoImage(image)

# Create a label to display the image
label = tk.Label(root, image=image)
label.pack(pady=10)

# Create a button to change the image
button = tk.Button(root, text="carriage_1", command=change_carriage_1)
button.pack()
button = tk.Button(root, text="carriage_2", command=change_carriage_2)
button.pack()
button = tk.Button(root, text="carriage_3", command=change_carriage_3)
button.pack()
button = tk.Button(root, text="carriage_4", command=change_carriage_4)
button.pack()

# Start the main loop
root.mainloop()