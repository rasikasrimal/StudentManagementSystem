# delete_operations.py

from tkinter import messagebox

def delete_student(mycursor, con, student_table):
    indexing = student_table.focus()
    content = student_table.item(indexing)
    content_id = content['values'][0]
    query = 'DELETE FROM student WHERE id=%s'
    mycursor.execute(query, (content_id,))
    con.commit()
    messagebox.showinfo('DELETED', f'User {content_id} is DELETED Successfully')
    query = 'SELECT * FROM student'
    mycursor.execute(query)
    fetched_data = mycursor.fetchall()
    student_table.delete(*student_table.get_children())
    for data in fetched_data:
        data_list = list(data)
        student_table.insert('', 'end', values=data_list)
