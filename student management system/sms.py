from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
import pymysql

count = 0
text = ''

# Function to handle exit button click
def exit_program():
    root.destroy()

# Function to handle slider
def slider():
    global count, text
    if count == len(s):
        count = 0
        text = ''
    text = text + s[count]
    sliderLabel.config(text=text)
    count += 1
    sliderLabel.after(60, slider)

# Function to handle login button click
def clock():
    date=time.strftime('%d:%m:%Y')
    current_time = time.strftime('%H:%M:%S')
    datetimeLabel.config(text=f'{date}\n{current_time}') 
    datetimeLabel.after(1000, clock)

# Function to handle connect database button click
def connect_database():

    # Function to handle connect button click
    def connect():
        try:
            con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=PasswordEntry.get())
            mycursor = con.cursor()
        except:
            messagebox.showinfo('Success', 'Connected to Database')
            return
        try:
            query = 'CREATE DATABASE IF NOT EXISTS studentmanagementsystem'
            mycursor.execute(query)
            query = 'USE studentmanagementsystem'
            mycursor.execute(query)
            query = '''
            CREATE TABLE IF NOT EXISTS student (
                    id INT NOT NULL PRIMARY KEY, 
                    name VARCHAR(255), 
                    mobile VARCHAR(15),
                    email VARCHAR(255),
                    address TEXT,
                    gender VARCHAR(10),
                    dob DATE,
                    date DATE,
                    time TIME
                    )
                '''
        except:
                query = 'USE studentmanagementsystem'
                mycursor.execute(query)
                query = '''
                INSERT INTO student (id, name, mobile, email, address, gender, dob, date, time) VALUES
                    (1, 'John Doe', '123-456-7890', 'john.doe@example.com', '123 Main St, City', 'Male', '1990-05-15', '2023-09-08', '14:30:00'),
                    (2, 'Jane Smith', '987-654-3210', 'jane.smith@example.com', '456 Elm St, Town', 'Female', '1995-08-22', '2023-09-08', '10:15:00'),
                    (3, 'Michael Johnson', '555-555-5555', 'michael.j@example.com', '789 Oak St, Village', 'Male', '1998-03-10', '2023-09-09', '09:45:00'),
                    (4, 'Emily Davis', '777-888-9999', 'emily.d@example.com', '101 Pine St, Town', 'Female', '1993-12-05', '2023-09-09', '16:00:00'),
                    (5, 'William Brown', '111-222-3333', 'william.b@example.com', '222 Cedar St, City', 'Male', '1991-07-18', '2023-09-10', '11:30:00'),
                    (6, 'Olivia Lee', '444-333-2222', 'olivia.l@example.com', '333 Maple St, Village', 'Female', '1997-02-28', '2023-09-10', '13:45:00'),
                    (7, 'James Wilson', '999-888-7777', 'james.w@example.com', '444 Oak St, City', 'Male', '1996-09-12', '2023-09-11', '15:20:00'),
                    (8, 'Sophia Turner', '777-555-1111', 'sophia.t@example.com', '555 Birch St, Town', 'Female', '1994-11-08', '2023-09-11', '08:00:00'),
                    (9, 'Daniel Evans', '666-555-4444', 'daniel.e@example.com', '666 Willow St, Village', 'Male', '1992-04-30', '2023-09-12', '10:00:00'),
                    (10, 'Ava White', '222-333-4444', 'ava.w@example.com', '777 Pine St, City', 'Female', '1999-01-25', '2023-09-12', '14:15:00');
                '''
                mycursor.execute(query)

        # con.commit()
        # con.close()

        messagebox.showinfo('Success', 'Connected to Database')
        addstudentButton.config(state=NORMAL)
        searchstudentButton.config(state=NORMAL)
        updatestudentButton.config(state=NORMAL)
        showstudentButton.config(state=NORMAL)
        exportDataButton.config(state=NORMAL)
        deletestudentButton.config(state=NORMAL)

#############################################################

    connectWindow = Toplevel()
    connectWindow.grab_set()
    connectWindow.title('Connect Database')
    connectWindow.geometry('500x300+500+200')
    connectWindow.resizable(False, False)

    hostnameLabel = Label(connectWindow, text='Hostname', font=('Helvetica', 15, 'bold'))
    hostnameLabel.grid(row=0, column=0, padx=10, pady=10)

    hostEntry = Entry(connectWindow, font=('Helvetica', 15, 'bold'))
    hostEntry.grid(row=0, column=1, padx=10, pady=10)

    usernameLabel = Label(connectWindow, text='Username', font=('Helvetica', 15, 'bold'))
    usernameLabel.grid(row=1, column=0, padx=10, pady=10)

    userEntry = Entry(connectWindow, font=('Username', 15, 'bold'))
    userEntry.grid(row=1, column=1, padx=10, pady=10)

    PasswordLabel = Label(connectWindow, text='Password', font=('Helvetica', 15, 'bold'))
    PasswordLabel.grid(row=2, column=0, padx=10, pady=10)

    PasswordEntry = Entry(connectWindow, font=('Password', 15, 'bold'))
    PasswordEntry.grid(row=2, column=1, padx=10, pady=10)

    connectButton=ttk.Button(connectWindow, text='Connect', command=connect)
    connectButton.grid(row=3, column=0, padx=10, pady=10)

# GUI Part
root = ttkthemes.ThemedTk()
root.get_themes()
root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.resizable(False, False)
root.title('Student Management System')

datetimeLabel = Label(root, text='Hello', font=('Helvetica', 20, 'bold'))
datetimeLabel.place(x=5, y=5)
clock()

s = 'Student Management System'
sliderLabel = Label(root, font=('Helvetica', 30, 'bold'), relief=RIDGE, width=30)
sliderLabel.place(x=200, y=0)
slider()  # Start the animation

connectButton = ttk.Button(root, text='Connect Database', command=connect_database)
connectButton.place(x=980, y=0)

leftFrame = Frame(root, relief=RIDGE)
leftFrame.place(x=10, y=70, width=300, height=600)

logo_image = PhotoImage(file='images/student2.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0, padx=10, pady=10)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED)
addstudentButton.grid(row=1, column=0, padx=10, pady=0)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED)
searchstudentButton.grid(row=2, column=0, padx=10, pady=0)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=25, state=DISABLED)
deletestudentButton.grid(row=3, column=0, padx=10, pady=0)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=25, state=DISABLED)
updatestudentButton.grid(row=4, column=0, padx=10, pady=0)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=25, state=DISABLED)
showstudentButton.grid(row=5, column=0, padx=10, pady=0)

exportDataButton = ttk.Button(leftFrame, text='Export Data', width=25, state=DISABLED)
exportDataButton.grid(row=6, column=0, padx=10, pady=0)

exitButton = ttk.Button(leftFrame, text='Exit', width=25, command=exit_program)
exitButton.grid(row=7, column=0, padx=10, pady=0)

rightframe = Frame(root, bg='white', relief=RIDGE)
rightframe.place(x=320, y=70, width=800, height=550)

ScrollbarX = Scrollbar(rightframe, orient=HORIZONTAL)
ScrollbarY = Scrollbar(rightframe, orient=VERTICAL)

student_table = ttk.Treeview(rightframe, columns=(
    'ID', 'Name', 'Mobile No', 'Email', 'Address', 
    'Gender','DOB', 'Added Date', 'Added Time' ),
        xscrollcommand=ScrollbarX.set,
        yscrollcommand=ScrollbarY.set)

ScrollbarX.config(command=student_table.xview)
ScrollbarY.config(command=student_table.yview)

ScrollbarX.pack(side=BOTTOM, fill=X)
ScrollbarY.pack(side=RIGHT, fill=Y)

student_table.pack(fill=BOTH, expand=1)

student_table.heading('ID', text='ID')
student_table.heading('Name', text='Name')
student_table.heading('Mobile No', text='Mobile No')
student_table.heading('Email', text='Email')
student_table.heading('Address', text='Address')
student_table.heading('Gender', text='Gender')
student_table.heading('DOB', text='DOB')
student_table.heading('Added Date', text='Added Date')
student_table.heading('Added Time', text='Added Time')

student_table.config(show='headings')

root.mainloop()
