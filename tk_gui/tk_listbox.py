from tkinter import *

root = Tk()

def addItem():
    lbox.insert(END, e.get())
    e.delete(0, END)

def delList():
    select = list(lbox.curselection())
    select.reverse()
    for i in select:
        lbox.delete(i)

def saveList():
    f = open('list000.txt', 'w')
    f.writelines("\n".join(lbox.get(0, END)))
    f.close()


lbox = Listbox(selectmode=EXTENDED)
lbox.pack(side=LEFT)

scroll = Scrollbar(command=lbox.yview)
scroll.pack(side=LEFT, fill=Y)

lbox.config(yscrollcommand=scroll.set)

f = Frame()
f.pack(side=LEFT, padx=10)

e = Entry(f)
e.pack(anchor=N)

btn_a = Button(f, text='Add', command=addItem)
btn_a.pack(fill=X)

btn_d = Button(f, text='Delete', command=delList)
btn_d.pack(fill=X)

btn_s = Button(f, text='Save', command=saveList)
btn_s.pack(fill=X)


root.mainloop()