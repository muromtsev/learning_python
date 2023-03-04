import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.tableview import Tableview
from tkinter import messagebox as mb

root = ttk.Window()
root.geometry('500x500')
root.title('Address Book v.1.0')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = (w//2) - 200
h = (h//2) - 200
root.geometry(f'+{w}+{h}')
style = ttk.Style("darkly")
root.resizable(False, False)
ttk.Style().configure("TButton", font="TkFixedFont 10")

fname_var = ttk.StringVar()
lname_var = ttk.StringVar()
email_var = ttk.StringVar()
phone_var = ttk.StringVar()


def reset_var():
    fname_var.set(value='')
    lname_var.set(value='')
    email_var.set(value='')
    phone_var.set(value='')

def add_new_person(event):
    new_fname = fname_var.get()
    new_lname = lname_var.get()
    new_email = email_var.get()
    new_phone = phone_var.get()
    if new_fname != '' and new_lname != '' and new_email != '' and new_phone != '':
        dt.insert_row('end', values=[new_fname, new_lname, new_email, new_phone])
        dt.load_table_data()
        reset_var()
    else:
        mb.showerror(title='Error', message='There are empty fields!!!')

# First name widgets
ttk.Label(text='First name').grid(row=0, column=0, padx=10, pady=10, sticky=W)
first_name = ttk.Entry(bootstyle='primary', textvariable=fname_var, width=30)
first_name.grid(row=0, column=1, sticky=W+E)
# Last name widgets
ttk.Label(text='Last name').grid(row=1, column=0, padx=10, pady=10, sticky=W)
last_name = ttk.Entry(bootstyle='primary', textvariable=lname_var)
last_name.grid(row=1, column=1, sticky=W+E)
# Email widgets
ttk.Label(text='Email').grid(row=2, column=0, padx=10, pady=10, sticky=W)
email = ttk.Entry(bootstyle='primary', textvariable=email_var)
email.grid(row=2, column=1, sticky=W+E)
# Phone widgets
ttk.Label(text='Phone').grid(row=3, column=0, padx=10, pady=10, sticky=W)
phone = ttk.Entry(bootstyle='primary', textvariable=phone_var)
phone.grid(row=3, column=1, sticky=W+E)
# Button
btn_add = ttk.Button(text='Add', bootstyle='success-outline')
btn_add.grid(row=4, column=0, padx=10, pady=10, sticky=W)
btn_add.bind('<Button-1>', lambda event: add_new_person(event))
# Table
coldata = [
    {"text": "First name", "width": 100},
    {"text": "Last name", "width": 100},
    {"text": "Email", "width": 120},
    {"text": "Phone", "width": 120},
]

rowdata = [
    ('John', 'Do', 'john@example.com', '1 22 333 4 555 66')
]

dt = Tableview(
    master=root,
    coldata=coldata,
    rowdata=rowdata,
    bootstyle=PRIMARY,
)
dt.grid(row=5, columnspan=2, padx=5, pady=5, sticky=W)

root.mainloop()
