# export_operations.py

from tkinter import filedialog, messagebox
import pandas as pd

def export_data(student_table):
    url = filedialog.asksaveasfilename(defaultextension='.csv')
    if url:
        indexing = student_table.get_children()
        data_list = []

        for index in indexing:
            content = student_table.item(index)
            datalist = content['values']
            data_list.append(datalist)

        table = pd.DataFrame(data_list, columns=['ID', 'Name', 'Mobile No', 'Email', 'Address', 'Gender', 'DOB', 'Added Date', 'Added Time'])
        table.to_csv(url, index=False)
        messagebox.showinfo('Success', 'Data Exported Successfully')
