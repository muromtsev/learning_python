from tkinter import *

root = Tk()

def from_Entry(event):
    txt = e.get()
    e.delete(0, END)
    lst = txt.split(' ')
    for l in lst:
        lbox.insert(END, l)

def from_List(event):
    select = list(lbox.curselection())
    select.reverse()
    
    e.insert(END, lbox.get(select[0])+' ')

    for i in select:
        lbox.delete(i)
    
e = Entry(width=50)
e.insert(0, 'Text from Entry')
e.bind('<Return>', from_Entry)
e.pack()

lbox = Listbox(width=50)
lbox.bind('<Double-Button-1>', from_List)
lbox.pack()

root.mainloop()