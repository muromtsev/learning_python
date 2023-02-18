from tkinter import *

root = Tk()
root.geometry('300x300')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

w = w//2
h = h//2
w = w - 200
h = h - 200
root.geometry(f'+{w}+{h}')

table = Label(text='Calc', font=("Verdana", 14), bg='white', width=200)
table.pack(padx=10, pady=10, ipadx=5, ipady=5)


f0 = Frame()
f0.pack()

btn_clear = Button(f0, text='CE', bg='#cccccc', width=4, height=2)
btn_clear.pack(side=LEFT, pady=2)

btn_plus = Button(f0, text='+', bg='#cccccc', width=4, height=2)
btn_plus.pack(side=LEFT, pady=2)

btn_minus = Button(f0, text='-', bg='#cccccc', width=4, height=2)
btn_minus.pack(side=LEFT, pady=2)

btn_multy = Button(f0, text='*', bg='#cccccc', width=4, height=2)
btn_multy.pack(side=LEFT, pady=2)


f1 = Frame()
f1.pack()

btn_one = Button(f1, text='1', bg='#cccccc', width=4, height=2)
btn_one.pack(side=LEFT, pady=2)

btn_two = Button(f1, text='2', bg='#cccccc', width=4, height=2)
btn_two.pack(side=LEFT, pady=2)

btn_three = Button(f1, text='3', bg='#cccccc', width=4, height=2)
btn_three.pack(side=LEFT, pady=2)

btn_module = Button(f1, text='/', bg='#cccccc', width=4, height=2)
btn_module.pack(side=LEFT, pady=2)

f2 = Frame()
f2.pack()

btn_four = Button(f2, text='4', bg='#cccccc', width=4, height=2)
btn_four.pack(side=LEFT, pady=2)

btn_five = Button(f2, text='5', bg='#cccccc', width=4, height=2)
btn_five.pack(side=LEFT, pady=2)

btn_six = Button(f2, text='6', bg='#cccccc', width=4, height=2)
btn_six.pack(side=LEFT, pady=2)

btn_b = Button(f2, text=' ', bg='#cccccc', width=4, height=2)
btn_b.pack(side=LEFT, pady=2)

f3 = Frame()
f3.pack()

btn_seven = Button(f3, text='7', bg='#cccccc', width=4, height=2)
btn_seven.pack(side=LEFT, pady=2)

btn_eight = Button(f3, text='8', bg='#cccccc', width=4, height=2)
btn_eight.pack(side=LEFT, pady=2)

btn_nine = Button(f3, text='9', bg='#cccccc', width=4, height=2)
btn_nine.pack(side=LEFT, pady=2)

btn_b1 = Button(f3, text=' ', bg='#cccccc', width=4, height=2)
btn_b1.pack(side=LEFT, pady=2)

f4 = Frame()
f4.pack()

btn_pm = Button(f4, text='+/-', bg='#cccccc', width=4, height=2)
btn_pm.pack(side=LEFT, pady=2)

btn_zero = Button(f4, text='0', bg='#cccccc', width=4, height=2)
btn_zero.pack(side=LEFT, pady=2)

btn_dote = Button(f4, text='.', bg='#cccccc', width=4, height=2)
btn_dote.pack(side=LEFT, pady=2)

btn_eq = Button(f4, text='=', bg='#cccccc', width=4, height=2)
btn_eq.pack(side=LEFT, pady=2)


def deleteTable(event):
    table['text'] = ''

def writeOne(event):
    table['text'] += btn_one['text']



def writeTable(event, var):
    table['text'] += var

def writeEq(event):
    s = table['text']
    table['text'] = ''
    table['text'] = eval(s)

btn_clear.bind('<Button-1>', deleteTable)
btn_one.bind('<Button-1>', lambda event, var = btn_one['text']: writeTable(event, var))
btn_two.bind('<Button-1>', lambda event, var = btn_two['text']: writeTable(event, var))
btn_three.bind('<Button-1>', lambda event, var = btn_three['text']: writeTable(event, var))
btn_four.bind('<Button-1>', lambda event, var = btn_four['text']: writeTable(event, var))
btn_five.bind('<Button-1>', lambda event, var = btn_five['text']: writeTable(event, var))
btn_six.bind('<Button-1>', lambda event, var = btn_six['text']: writeTable(event, var))
btn_seven.bind('<Button-1>', lambda event, var = btn_seven['text']: writeTable(event, var))
btn_eight.bind('<Button-1>', lambda event, var = btn_eight['text']: writeTable(event, var))
btn_nine.bind('<Button-1>', lambda event, var = btn_nine['text']: writeTable(event, var))
btn_zero.bind('<Button-1>', lambda event, var = btn_zero['text']: writeTable(event, var))



btn_plus.bind('<Button-1>', lambda event, var=btn_plus['text']: writeTable(event, var))
btn_minus.bind('<Button-1>', lambda event, var=btn_minus['text']: writeTable(event, var))
btn_multy.bind('<Button-1>', lambda event, var=btn_multy['text']: writeTable(event, var))
btn_module.bind('<Button-1>', lambda event, var=btn_module['text']: writeTable(event, var))
btn_eq.bind('<Button-1>', writeEq)



root.mainloop()