from tkinter import *
import time
import ttkthemes
from tkinter import ttk, messagebox
import pymysql

count = 0
text = ''

def search_student():

    def search_data():
        query = ' SELECT * FROM student WHERE id=%s or Name=%s or mobile=%s or Email=%s or address=%s or gender=%s or dob=%s or date=%s or time=%s'

        mycursor.execute(query, (
            idEntry.get(), 
            nameEntry.get(), 
            emailEntry.get(), 
            mobileEntry.get(), 
            addressEntry.get(), 
            genderEntry.get(), 
            dobEntry.get() ))
        student_table.delete(*student_table.get_children())
        fetched_data = mycursor.fetchall()
        for data in fetched_data:
            student_table.insert('', END, values=data)
                 
        

    search_windows = Toplevel()
    search_windows.grab_set()
    search_windows.title('Search Student')
    search_windows.resizable(False, False)
    idlable = Label(search_windows, text='ID', font=('Helvetica', 15, 'bold'))
    idlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    idEntry = Entry(search_windows, font=('Helvetica', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    namelable = Label(search_windows, text='Name', font=('Helvetica', 15, 'bold'))
    namelable.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    nameEntry = Entry(search_windows, font=('Helvetica', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=10)

    mobilelable = Label(search_windows, text='Mobile', font=('Helvetica', 15, 'bold'))
    mobilelable.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    mobileEntry = Entry(search_windows, font=('Helvetica', 15, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, padx=10, pady=10)

    emaillable = Label(search_windows, text='Email', font=('Helvetica', 15, 'bold'))
    emaillable.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    emailEntry = Entry(search_windows, font=('Helvetica', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=10, pady=10)

    addresslable = Label(search_windows, text='Address', font=('Helvetica', 15, 'bold'))
    addresslable.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    addressEntry = Entry(search_windows, font=('Helvetica', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=10, pady=10)

    genderlable = Label(search_windows, text='Gender', font=('Helvetica', 15, 'bold'))
    genderlable.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    genderEntry = Entry(search_windows, font=('Helvetica', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=10, pady=10)

    doblable = Label(search_windows, text='DOB', font=('Helvetica', 15, 'bold'))
    doblable.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    dobEntry = Entry(search_windows, font=('Helvetica', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=10)

    search_student_button = ttk.Button(search_windows, text='Search Student', width=25, command=search_data)
    search_student_button.grid(row=9, columnspan=2, padx=10, pady=10)


#################################################################################################

def add_student():
    def add_data():
        if (
            idEntry.get() == '' or
            nameEntry.get() == '' or
            mobileEntry.get() == '' or
            emailEntry.get() == '' or
            addressEntry.get() == '' or
            genderEntry.get() == '' or
            dobEntry.get() == ''
        ):
            messagebox.showerror('Error', 'All fields are required', parent=add_windows)
        else:
            currentdate = time.strftime('%Y:%m:%d')
            currenttime = time.strftime('%H:%M:%S')
            query = 'INSERT INTO student VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)'
            try:
                mycursor.execute(query, (
                    idEntry.get(),
                    nameEntry.get(),
                    mobileEntry.get(),
                    emailEntry.get(),
                    addressEntry.get(), 
                    genderEntry.get(), 
                    dobEntry.get(), 
                    currentdate,
                    currenttime
                ))
                con.commit()
                result = messagebox.askyesnocancel('Success', 'Do you want to clear the form?')
                if result:
                    idEntry.delete(0, END)
                    nameEntry.delete(0, END)
                    mobileEntry.delete(0, END)
                    emailEntry.delete(0, END)
                    addressEntry.delete(0, END)
                    genderEntry.delete(0, END)
                    dobEntry.delete(0, END)
            except Exception as e:
                print(f"Error: {e}")
                messagebox.showerror('Error', 'This ID is already taken', parent=search_windows)
                return

        query = 'SELECT * FROM student'
        mycursor.execute(query)
        fetched_data = mycursor.fetchall()
        student_table.delete(*student_table.get_children())
        for data in fetched_data:
            data_list = list(data)
            student_table.insert('', END, values=data_list)

    add_windows = Toplevel()
    add_windows.grab_set()
    add_windows.resizable(False, False)
    idlable = Label(add_windows, text='ID', font=('Helvetica', 15, 'bold'))
    idlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')
    idEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
    idEntry.grid(row=0, column=1, padx=10, pady=10)

    namelable = Label(add_windows, text='Name', font=('Helvetica', 15, 'bold'))
    namelable.grid(row=1, column=0, padx=10, pady=10, sticky='w')
    nameEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
    nameEntry.grid(row=1, column=1, padx=10, pady=10)

    mobilelable = Label(add_windows, text='Mobile', font=('Helvetica', 15, 'bold'))
    mobilelable.grid(row=2, column=0, padx=10, pady=10, sticky='w')
    mobileEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
    mobileEntry.grid(row=2, column=1, padx=10, pady=10)

    emaillable = Label(add_windows, text='Email', font=('Helvetica', 15, 'bold'))
    emaillable.grid(row=3, column=0, padx=10, pady=10, sticky='w')
    emailEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
    emailEntry.grid(row=3, column=1, padx=10, pady=10)

    addresslable = Label(add_windows, text='Address', font=('Helvetica', 15, 'bold'))
    addresslable.grid(row=4, column=0, padx=10, pady=10, sticky='w')
    addressEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
    addressEntry.grid(row=4, column=1, padx=10, pady=10)

    genderlable = Label(add_windows, text='Gender', font=('Helvetica', 15, 'bold'))
    genderlable.grid(row=5, column=0, padx=10, pady=10, sticky='w')
    genderEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
    genderEntry.grid(row=5, column=1, padx=10, pady=10)

    doblable = Label(add_windows, text='DOB', font=('Helvetica', 15, 'bold'))
    doblable.grid(row=6, column=0, padx=10, pady=10, sticky='w')
    dobEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
    dobEntry.grid(row=6, column=1, padx=10, pady=10)

    add_student_button = ttk.Button(add_windows, text='Add Student', width=25, command=add_data)
    add_student_button.grid(row=9, columnspan=2, padx=10, pady=10)

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
        global mycursor, con
        try:
            con = pymysql.connect(host='localhost', user='root', password='1234')
            # con = pymysql.connect(host=hostEntry.get(), user=userEntry.get(), password=PasswordEntry.get())
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
            mycursor.execute(query)
        except:
                query = 'USE studentmanagementsystem'
                mycursor.execute(query)

        # con.commit()
        # con.close()

        messagebox.showinfo('Success', 'Connected to Database')
        connectWindow.destroy()
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

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25, state=DISABLED, command=add_student)
addstudentButton.grid(row=1, column=0, padx=10, pady=0)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25, state=DISABLED, command=search_student)
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
