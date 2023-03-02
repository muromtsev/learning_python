import ttkbootstrap as ttk
from ttkbootstrap.constants import *


root = ttk.Window()
root.geometry('400x500')
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
count = 7


def reset():
    first_name.delete(0, END)
    fname_var.set('')
    lname_var.set('')
    email_var.set('')
    phone_var.set(0)


def add_new_person(event):
    global count
    user = 1
    f = fname_var.get()
    l = lname_var.get()
    e = email_var.get()
    p = phone_var.get()

    ttk.Label(text=f'{f} {l} {e} {p}').grid(row=count, column=0)
    info['text'] = f'Added'
    count += 1
    reset()


# First name widgets
ttk.Label(text='First name').grid(row=0, column=0, padx=10, pady=10)
first_name = ttk.Entry(bootstyle='primary', textvariable=fname_var)
first_name.grid(row=0, column=1)
# Last name widgets
ttk.Label(text='Last name').grid(row=1, column=0, padx=10, pady=10)
last_name = ttk.Entry(bootstyle='primary', textvariable=lname_var)
last_name.grid(row=1, column=1)
# Email widgets
ttk.Label(text='Email').grid(row=2, column=0, padx=10, pady=10)
email = ttk.Entry(bootstyle='primary', textvariable=email_var)
email.grid(row=2, column=1)
# Phone widgets
ttk.Label(text='Phone').grid(row=3, column=0, padx=10, pady=10)
phone = ttk.Entry(bootstyle='primary', textvariable=phone_var)
phone.grid(row=3, column=1)
# Button
btn_add = ttk.Button(text='Add', bootstyle='success-outline')
btn_add.grid(row=4, column=0, padx=10, pady=10)
btn_add.bind('<Button-1>', lambda event: add_new_person(event))
# Label info
info = ttk.Label(text='Add a new person', bootstyle='light', width=55)
info.grid(row=6, columnspan=2, padx=10, pady=3, ipadx=5, ipady=5)

root.mainloop()
