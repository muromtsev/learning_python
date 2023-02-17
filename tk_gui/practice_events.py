from tkinter import *

root = Tk()

def change(event):
    n1 = e1.get()
    n2 = e2.get()
    t.configure(width=n1, height=n2)

def change_color(event):
    t.configure(bg='lightgrey')

def bg_white(event):
    t.configure(bg='white')

e1 = Entry(width=3)
e1.pack()
e2 = Entry(width=3)
e2.pack()

f = Frame()
f.pack()

btn = Button(f, text='Change')
btn.pack()

t = Text(width=10, height=3)
t.pack(side=BOTTOM)

btn.bind('<Button-1>', change)
btn.bind('<Return>', change)

t.bind('<FocusIn>', change_color)
t.bind('<FocusOut>', bg_white)

root.mainloop()