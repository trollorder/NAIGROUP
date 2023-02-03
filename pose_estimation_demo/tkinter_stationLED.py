from tkinter import *
from PIL import ImageTk, Image

root= Tk()
root.title("BEST GENERATOR YET")
root.geometry("800x600")
# root['background'] = '#eee5e5'
# root.window_start_x = (root.winfo_screenwidth())
# root.window_start_y = (root.winfo_screenheight())

image1 = Image.open("Platform-Screen-Doors.jpg")
image2 = ImageTk.PhotoImage(image1)

canvas = Canvas(root)
canvas.pack(fill=BOTH, expand=1)

image = canvas.create_image(0, 0, anchor=NW, image=image2)

#put in data here
# kelvinser = "red"
kelvinser = "yellow"
# kelvinser = "green"

#create left LED
line = canvas.create_line(  305, 130, 392, 130,
                            392, 130, 392, 152,
                            305, 152, 392, 152,
                            305, 130, 305, 152,
                            fill="black", width=3)

#create right LED
line = canvas.create_line(  415.5, 130, 502.5, 130, 
                            502.5, 130, 502.5, 152, 
                            415.5, 152, 502.5, 152,
                            415.5, 130, 415.5, 152, 
                            fill="black", width=3)

line = canvas.create_line(306.5, 141, 391, 141, fill=kelvinser, width=19)
line = canvas.create_line(418, 141, 501.5, 141, fill=kelvinser, width=19)

root.mainloop()