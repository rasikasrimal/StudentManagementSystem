# from tkinter import *
# from tkinter import ttk

# def add_student():
#     add_windows = Toplevel()

#     idlable = Label(add_windows, text='ID', font=('Helvetica', 15, 'bold'))
#     idlable.grid(row=0, column=0, padx=10, pady=10, sticky='w')
#     idEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     idEntry.grid(row=0, column=1, padx=10, pady=10)

#     namelable = Label(add_windows, text='Name', font=('Helvetica', 15, 'bold'))
#     namelable.grid(row=1, column=0, padx=10, pady=10, sticky='w')
#     nameEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     nameEntry.grid(row=1, column=1, padx=10, pady=10)

#     mobilelable = Label(add_windows, text='Mobile', font=('Helvetica', 15, 'bold'))
#     mobilelable.grid(row=2, column=0, padx=10, pady=10, sticky='w')
#     mobileEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     mobileEntry.grid(row=2, column=1, padx=10, pady=10)

#     emaillable = Label(add_windows, text='Email', font=('Helvetica', 15, 'bold'))
#     emaillable.grid(row=3, column=0, padx=10, pady=10, sticky='w')
#     emailEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     emailEntry.grid(row=3, column=1, padx=10, pady=10)

#     addresslable = Label(add_windows, text='Address', font=('Helvetica', 15, 'bold'))
#     addresslable.grid(row=4, column=0, padx=10, pady=10, sticky='w')
#     addressEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     addressEntry.grid(row=4, column=1, padx=10, pady=10)

#     genderlable = Label(add_windows, text='Gender', font=('Helvetica', 15, 'bold'))
#     genderlable.grid(row=5, column=0, padx=10, pady=10, sticky='w')
#     genderEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     genderEntry.grid(row=5, column=1, padx=10, pady=10)

#     doblable = Label(add_windows, text='DOB', font=('Helvetica', 15, 'bold'))
#     doblable.grid(row=6, column=0, padx=10, pady=10, sticky='w')
#     dobEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     dobEntry.grid(row=6, column=1, padx=10, pady=10)

#     datelable = Label(add_windows, text='Date', font=('Helvetica', 15, 'bold'))
#     datelable.grid(row=7, column=0, padx=10, pady=10, sticky='w')
#     dateEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     dateEntry.grid(row=7, column=1, padx=10, pady=10)

#     timelable = Label(add_windows, text='Time', font=('Helvetica', 15, 'bold'))
#     timelable.grid(row=8, column=0, padx=10, pady=10, sticky='w')
#     timeEntry = Entry(add_windows, font=('Helvetica', 15, 'bold'), width=24)
#     timeEntry.grid(row=8, column=1, padx=10, pady=10)

#     add_student_button = ttk.Button(add_windows, text='Add Student', width=25)
#     add_student_button.grid(row=9, columnspan=2, padx=10, pady=10)

# if __name__ == "__main__":
#     root = Tk()
#     root.geometry("800x600")
    
#     add_button = Button(root, text="Add Student", command=add_student)
#     add_button.pack()

#     root.mainloop()