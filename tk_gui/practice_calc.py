from tkinter import *

root = Tk()

num1 = Entry(width=20)
num2 = Entry(width=20)
button_plus = Button(text='+')
button_minus = Button(text='-')
button_multy = Button(text='*')
button_module = Button(text='/')
b = Button(text='Вычислить')
l = Label(bg='black', fg='white', width=20)

def func_plus(event):
    n1 = num1.get()
    
    n2 = num2.get()
    if n1.isdigit() and n2.isdigit():
        result = int(n1) + int(n2)
        l['text'] = result
    else:
        l['text'] = 'Error'

def func_minus(event):
    n1 = num1.get()
    n2 = num2.get()
    if n1.isdigit() and n2.isdigit():
        result = int(n1) - int(n2)
        l['text'] = result
    else:
        l['text'] = 'Error'

def func_multy(event):
    n1 = num1.get()
    n2 = num2.get()
    if n1.isdigit() and n2.isdigit():
        result = int(n1) * int(n2)
        l['text'] = result
    else:
        l['text'] = 'Error'

def func_module(event):
    n1 = num1.get()
    n2 = num2.get()
    if n1.isdigit() and n2.isdigit():
        result = int(n1) / int(n2)
        l['text'] = result
    else:
        l['text'] = 'Error'

button_plus.bind('<Button-1>', func_plus)
button_minus.bind('<Button-1>', func_minus)
button_multy.bind('<Button-1>', func_multy)
button_module.bind('<Button-1>', func_module)

num1.pack()
num2.pack()
button_plus.pack()
button_minus.pack()
button_multy.pack()
button_module.pack()
b.pack()
l.pack()
root.mainloop()