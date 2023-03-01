import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()
root.geometry('400x500')
root.title('Address Book v.1.0')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 200
h = h - 200
root.geometry(f'+{w}+{h}')
style = ttk.Style("darkly")
root.resizable(False, False)
ttk.Style().configure("TButton", font="TkFixedFont 10")

# First name widgets
ttk.Label(text='First name').grid(row=0, column=0)
first_name = ttk.Entry(bootstyle='primary')
first_name.grid(row=0, column=1)
# Last name widgets
ttk.Label(text='Last name').grid(row=1, column=0)
last_name = ttk.Entry(bootstyle='primary')
last_name.grid(row=1, column=1)
# Email widgets
ttk.Label(text='Email').grid(row=2, column=0)
email = ttk.Entry(bootstyle='primary')
email.grid(row=2, column=1)
# Phone widgets
ttk.Label(text='Phone').grid(row=3, column=0)
phone = ttk.Entry(bootstyle='primary')
phone.grid(row=3, column=1)


root.mainloop()