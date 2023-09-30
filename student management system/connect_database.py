from tkinter import *
from tkinter import ttk, messagebox
import pymysql

def connect_database():

    # Function to handle connect button click
    def connect():
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