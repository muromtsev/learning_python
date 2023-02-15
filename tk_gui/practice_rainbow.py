from tkinter import *

root = Tk()

def red_change():
    l['text']='Red'
    e.delete(0, END)
    e.insert(0, "#ff0000")
def orange_change():
    l['text']='Orange'
    e.delete(0, END)
    e.insert(0, '#ff7d00')
def yellow_change():
    l['text']='Yellow'
    e.delete(0, END)
    e.insert(0, '#ffff00')
def green_change():
    l['text']='Green'
    e.delete(0, END)
    e.insert(0, '#00ff00')
def blue_change():
    l['text']='Blue'
    e.delete(0, END)
    e.insert(0, '#007dff')
def dark_blue_change():
    l['text']='Dark blue'
    e.delete(0, END)
    e.insert(0, '#0000ff')
def indigo_change():
    l['text']='Indigo'
    e.delete(0, END)
    e.insert(0, '#7d00ff')

l = Label(text='Выбери цвет')
e = Entry(justify='center')
b = Button(bg='#ff0000', width=15, height=1, command=red_change)
b2 = Button(bg='#ff7d00', width=15, height=1, command=orange_change)
b3 = Button(bg='#ffff00', width=15, height=1, command=yellow_change)
b4 = Button(bg='#00ff00', width=15, height=1, command=green_change)
b5 = Button(bg='#007dff', width=15, height=1, command=blue_change)
b6 = Button(bg='#0000ff', width=15, height=1, command=dark_blue_change)
b7 = Button(bg='#7d00ff', width=15, height=1, command=indigo_change)

e.insert(0, 'white')

l.pack()
e.pack()

b.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
root.mainloop()