# # search_operations.py

# def search_data(mycursor, student_table, idEntry, nameEntry, emailEntry, mobileEntry, genderEntry, dobEntry):
#     query = 'SELECT * FROM student WHERE id=%s or Name=%s or Email=%s or mobile=%s or gender=%s or dob=%s' #or address=%s'

#     mycursor.execute(query, (
#         idEntry.get(),
#         nameEntry.get(),
#         emailEntry.get(),
#         mobileEntry.get(), 
#         # addressEntry.get(),
#         genderEntry.get(), 
#         dobEntry.get() 
#         ))
#     student_table.delete(*student_table.get_children())
#     fetched_data = mycursor.fetchall()
#     for data in fetched_data:
#         student_table.insert('', END, values=data)
