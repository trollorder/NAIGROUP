from tkinter import *
from PIL import ImageTk, Image
import sqlite3
from LEDInstructor import LEDinstructor

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

firstled=LEDinstructor("stationcount.db","traincount.db",1)
#put in data here
# kelvinser = "red"
# kelvinser = "yellow"
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
instruction = firstled.processinstruction()

# Anything here after will keep updating
def update():
    instruction = firstled.processinstruction()
    print(instruction)
    line = canvas.create_line(306.5, 141, 391, 141, fill=instruction, width=19)
    line = canvas.create_line(418, 141, 501.5, 141, fill=instruction, width=19)
    root.after(1000,update)



    
root.after(1000,update)
root.mainloop()