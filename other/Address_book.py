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
users = {}
count = 0

def create_notes(parent, first, last, email, phone, num):
    info['text'] = f'Added'
    return ttk.Label(parent, text=f'{first} {last} {email} {phone}').grid(row=num, column=0)



def reset():
    fname_var.set('')
    lname_var.set('')
    email_var.set('')
    phone_var.set('')


def add_new_person(event):
    global count
    new_fname = fname_var.get()
    new_lname = lname_var.get()
    new_email = email_var.get()
    new_phone = phone_var.get()

    frame = ttk.Frame(width=50, height=10)
    frame.grid(row=7, columnspan=2, padx=5, pady=5)

    if '' not in (new_fname, new_lname, new_phone, new_email):
        count += 1
        users[count] = {
            'firstname': new_fname,
            'lastname': new_lname,
            'email': new_email,
            'phone': new_phone
        }
        c = create_notes(frame, new_fname, new_lname, new_email, new_phone, count)
        reset()

    else:
        print('ERROR')

    print(f'user: {count}')
    print(users)


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
