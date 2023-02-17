from tkinter import *

root = Tk()

s = 'apple bananas carrot bread butter meat popato pineapple'
lst = s.split(' ')

def move_right():
    select = list(lbox_left.curselection())
    select.reverse()
    for el in select:        
        lbox_right.insert(END, lbox_left.get(el))
        lbox_left.delete(el)
    

def move_left():
    select = list(lbox_right.curselection())
    select.reverse()
    for el in select:
        lbox_left.insert(END, lbox_right.get(el))
        lbox_right.delete(el)

lbox_left = Listbox(selectmode=EXTENDED)
lbox_left.pack(side=LEFT)

for i in lst:
    lbox_left.insert(END, i)

f = Frame()
f.pack(side=LEFT)

btn_right = Button(f, text='>>>', command=move_right)
btn_right.pack()

btn_left = Button(f, text='<<<', command=move_left)
btn_left.pack()

lbox_right = Listbox(selectmode=EXTENDED)
lbox_right.pack(side=RIGHT)

root.mainloop()