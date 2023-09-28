from tkinter import *
from PIL import ImageTk

window = Tk()
window.geometry('1280x700')

# Load the background image
background_image = ImageTk.PhotoImage(file=r'C:/Users/Rasika Srimal/Documents/GitHub/DBMS-MiniProjects/student management system/images/bg.jpg')

# Create a label to display the background image
bg_label = Label(window, image=background_image)
bg_label.place(x=0, y=0)

# Create the login frame
login_frame = Frame(window)
login_frame.place(x=400, y=150)

# Load the logo image
logo_image = PhotoImage(file=r'C:/Users/Rasika Srimal/Documents/GitHub/DBMS-MiniProjects/student management system/images/logo.png')

# Create an image label to display the logo
logo_label = Label(login_frame, image=logo_image)
logo_label.grid(row=0, column=0)

window.mainloop()
