from tkinter import *

# root = Tk()
# переменной присваивается объект типа BoolenVar
# r_var = BooleanVar()
# с помощью метода set устанавливается значение 0
# r_var.set(0)

def change():
    if var.get() == 0:
        label['bg'] = 'red'
    elif var.get() == 1:
        label['bg'] = 'green'
    elif var.get() == 2:
        label['bg'] = 'blue'

root = Tk()

var = IntVar()
var.set(0)

red = Radiobutton(text='Red', variable=var, value=0)
green = Radiobutton(text='Green', variable=var, value=1)
blue = Radiobutton(text='Blue', variable=var, value=2)

btn = Button(text='Change', command=change)

label = Label(width=20, height=10)

red.pack()
green.pack()
blue.pack()
btn.pack()
label.pack()

root.mainloop()