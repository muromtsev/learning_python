from tkinter import *
import random
root = Tk()

f = Frame()

def change():
    if cvar.get() == 0:
        l['text'] = 'USER 1'
    elif cvar.get() == 1:
        l['text'] = 'USER 2'
    elif cvar.get() == 2:
        l['text'] = 'USER 3'

cvar = IntVar()
cvar.set(0)

c1 = Radiobutton(f, text='user 1', variable=cvar, value=0, indicatoron=0, width=20, height=5, command=change)
c2 = Radiobutton(f, text='user 2', variable=cvar, value=1, indicatoron=0, width=20, height=5, command=change)
c3 = Radiobutton(f, text='user 3', variable=cvar, value=2, indicatoron=0, width=20, height=5, command=change)
l = Label(width=50, height=20, bg='#ffffff')
f.pack(side=LEFT)
l.pack(side=RIGHT)
c1.pack()
c2.pack()
c3.pack()


root.mainloop()