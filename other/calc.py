from tkinter import *

root = Tk()
root.geometry('300x300')
root.title('Calc')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

w = w//2
h = h//2
w = w - 200
h = h - 200
root.geometry(f'+{w}+{h}')

table = Label(text='0', font=("Verdana", 14), bg='white', width=10, justify=LEFT)
table.grid(row=0, column=0, padx=10, pady=10, ipadx=5, ipady=5)



btn_clear = Button(text='Clear', bg='#cccccc', width=4, height=2)
btn_clear.grid(row=1, column=0, pady=2)

btn_plus = Button( text='+', bg='#cccccc', width=4, height=2)
btn_plus.grid(row=1, column=3, pady=2)

btn_minus = Button(text='-', bg='#cccccc', width=4, height=2)
btn_minus.grid(row=2, column=3, pady=2)

btn_multy = Button(text='*', bg='#cccccc', width=4, height=2)
btn_multy.grid(row=3, column=3, pady=2)


btn_one = Button(text='1', bg='#cccccc', width=4, height=2)
btn_one.grid(row=1, column=0, pady=2)

btn_two = Button( text='2', bg='#cccccc', width=4, height=2)
btn_two.grid(row=1, column=1, pady=2)

btn_three = Button(text='3', bg='#cccccc', width=4, height=2)
btn_three.grid(row=1, column=2, pady=2)

btn_module = Button(text='/', bg='#cccccc', width=4, height=2)
btn_module.grid(row=4, column=3, pady=2)


btn_four = Button(text='4', bg='#cccccc', width=4, height=2)
btn_four.grid(row=2, column=0, pady=2)

btn_five = Button( text='5', bg='#cccccc', width=4, height=2)
btn_five.grid(row=2, column=1, pady=2)

btn_six = Button(text='6', bg='#cccccc', width=4, height=2)
btn_six.grid(row=2, column=2, pady=2)

# btn_b = Button( text=' ', bg='#cccccc', width=4, height=2)
# btn_b.grid(row=2, column pady=2)


btn_seven = Button(text='7', bg='#cccccc', width=4, height=2)
btn_seven.grid(row=3, column=0, pady=2)

btn_eight = Button(text='8', bg='#cccccc', width=4, height=2)
btn_eight.grid(row=3, column=1, pady=2)

btn_nine = Button(text='9', bg='#cccccc', width=4, height=2)
btn_nine.grid(row=3, column=2, pady=2)

# btn_b1 = Button(f3, text=' ', bg='#cccccc', width=4, height=2)
# btn_b1.pack(side=LEFT, pady=2)


btn_pm = Button( text='+/-', bg='#cccccc', width=4, height=2)
btn_pm.grid(row=5, column=0, pady=2)

btn_zero = Button(text='0', bg='#cccccc', width=4, height=2)
btn_zero.grid(row=5, column=1, pady=2)

btn_dote = Button( text='.', bg='#cccccc', width=4, height=2)
btn_dote.grid(row=5, column=2, pady=2)

btn_eq = Button(text='=', bg='#cccccc', width=4, height=2)
btn_eq.grid(row=5, column=3, pady=2)


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