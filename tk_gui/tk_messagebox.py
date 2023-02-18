from tkinter import *
from tkinter import messagebox as mb

def check():
    answer = mb.askyesno(title='Question', message='Перенести данные?')
    s = entry.get()
    if s.isdigit() == False:
        mb.showerror('Error', 'Must be a number')
    else:
        entry.delete(0, END)
        label['text'] = s
      

root = Tk()

entry = Entry()
entry.pack(pady=10)

Button(text='Передать', command=check).pack()

label = Label(height=3)
label.pack()

root.mainloop()