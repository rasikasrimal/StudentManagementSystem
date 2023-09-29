from tkinter import *
import time
import ttkthemes
from tkinter import ttk

count = 0
text = ''
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

connectButton = ttk.Button(root, text='Connect Database')
connectButton.place(x=980, y=0)

leftFrame = Frame(root, relief=RIDGE)
leftFrame.place(x=10, y=70, width=300, height=600)

logo_image = PhotoImage(file='images/student2.png')
logo_label = Label(leftFrame, image=logo_image)
logo_label.grid(row=0, column=0, padx=10, pady=10)

addstudentButton = ttk.Button(leftFrame, text='Add Student', width=25)
addstudentButton.grid(row=1, column=0, padx=10, pady=0)

searchstudentButton = ttk.Button(leftFrame, text='Search Student', width=25)
searchstudentButton.grid(row=2, column=0, padx=10, pady=0)

deletestudentButton = ttk.Button(leftFrame, text='Delete Student', width=25)
deletestudentButton.grid(row=3, column=0, padx=10, pady=0)

updatestudentButton = ttk.Button(leftFrame, text='Update Student', width=25)
updatestudentButton.grid(row=4, column=0, padx=10, pady=0)

showstudentButton = ttk.Button(leftFrame, text='Show Student', width=25)
showstudentButton.grid(row=5, column=0, padx=10, pady=0)

exportDataButton = ttk.Button(leftFrame, text='Export Data', width=25)
exportDataButton.grid(row=6, column=0, padx=10, pady=0)

exitButton = ttk.Button(leftFrame, text='Exit', width=25)
exitButton.grid(row=7, column=0, padx=10, pady=0)

rightframe = Frame(root, bg='white', relief=RIDGE)
rightframe.place(x=320, y=70, width=800, height=550)

ScrollbarX = Scrollbar(rightframe, orient=HORIZONTAL)
ScrollbarY = Scrollbar(rightframe, orient=VERTICAL)

student_table = ttk.Treeview(rightframe, columns=('ID', 'Name', 'Mobile No', 'Email', 'Address', 'Gender',
                                  'DOB', 'Added Date', 'Added Time' ),
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
