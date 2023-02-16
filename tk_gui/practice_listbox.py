from tkinter import *

root = Tk()

s = 'apple bananas carrot bread butter meat popato pineapple'
lst = s.split(' ')

def move_right():
    select = list(lbox_left.curselection())
    if len(select) < 2:
        elem = lbox_left.get(select)
        lbox_right.insert(END, elem)
        lbox_left.delete(select)
    else:
        for el in select:
            elem = lbox_left.get(el)
            lbox_right.insert(END, elem)
            lbox_left.delete(el)
    
    
    
    
    

lbox_left = Listbox(selectmode=EXTENDED)
lbox_left.pack(side=LEFT)

for i in lst:
    lbox_left.insert(END, i)

f = Frame()
f.pack(side=LEFT)

btn_right = Button(f, text='>>>', command=move_right)
btn_right.pack()

btn_left = Button(f, text='<<<')
btn_left.pack()

lbox_right = Listbox(selectmode=EXTENDED)
lbox_right.pack(side=RIGHT)

root.mainloop()