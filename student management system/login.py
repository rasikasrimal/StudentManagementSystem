from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

# Function to handle login button click
def login():
    if usernameEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    elif usernameEntry.get() == 'snow' and passwordEntry.get() == '1234':
        messagebox.showinfo('Success', 'Login Successful')
    else :
        messagebox.showerror('Error', 'Invalid Username or Password')
    window.destroy()
    import sms
    

# Create the main window
window = Tk()
window.geometry('1280x700')
window.title('Login - Student Management System')

# Load the background image
background_image = ImageTk.PhotoImage(file='images/bg.jpg')

# Create a label to display the background image
bg_label = Label(window, image=background_image)
bg_label.place(x=0, y=0)

# Create the login frame
login_frame = Frame(window, bg='white')
login_frame.place(x=400, y=150)

# Load the logo image
logo_image = Image.open('images/logo.png')
logo_photo = ImageTk.PhotoImage(logo_image)

# Create an image label to display the logo
logo_label = Label(login_frame, image=logo_photo)
logo_label.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

# Username
usernameImage = PhotoImage(file='images/user.png')
usernameLabel = Label(
    login_frame, 
    image=usernameImage, 
    text='Username', 
    compound=LEFT, 
    font=('Helvetica', 20, 'bold')
)
usernameLabel.grid(row=1, column=0, padx=20, pady=10)

usernameEntry = Entry(login_frame, font=('Helvetica', 20, 'bold'), bd=5, fg='royalblue', bg='lightgray')
usernameEntry.grid(row=1, column=1, padx=20, pady=10)

# Password
passwordImage = PhotoImage(file='images/password.png')
passwordLabel = Label(
    login_frame, 
    image=passwordImage, 
    text='Password', 
    compound=LEFT, 
    font=('Helvetica', 20, 'bold')
)
passwordLabel.grid(row=2, column=0, padx=20, pady=10)

passwordEntry = Entry(login_frame, font=('Helvetica', 20, 'bold'), bd=5, fg='royalblue', bg='lightgray', show='*')
passwordEntry.grid(row=2, column=1, padx=20, pady=10)

# Login Button
LoginButton = Button(
    login_frame, 
    text='Login', 
    font=('Helvetica', 20, 'bold'), 
    width=15, 
    fg='white', 
    bg='cornflowerblue', 
    command=login
)
LoginButton.grid(row=3, column=1, padx=20, pady=10)

# Start the main loop
window.mainloop()
