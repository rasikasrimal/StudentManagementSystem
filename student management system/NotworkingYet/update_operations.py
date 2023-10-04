# # update_operations.py

# from tkinter import messagebox
# import time

# def update_data(mycursor, con, idEntry, nameEntry, mobileEntry, emailEntry, addressEntry, genderEntry, dobEntry, student_table):
#     currentdate = time.strftime('%d:%m:%Y')
#     currenttime = time.strftime('%H:%M:%S')

#     query = 'update student set name=%s, mobile=%s, email=%s, address=%s, gender=%s, dob=%s, date=%s, time=%s where id=%s'
#     mycursor.execute(query, (
#         nameEntry.get(),
#         mobileEntry.get(),
#         emailEntry.get(),
#         addressEntry.get(),
#         genderEntry.get(),
#         dobEntry.get(),
#         currentdate,
#         currenttime,
#         idEntry.get()
#     ))
#     con.commit()
#     messagebox.showinfo('Success', 'Student Updated Successfully', parent=student_table)
#     show_student(mycursor, student_table)
