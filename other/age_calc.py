from tkinter import *
import datetime
root = Tk()

root.geometry('350x250')
root.title('How old are y?')
dt = datetime.date.today()

def calc(event):
    lbl['text'] = ''
    n = name.get()
    a = age.get()
    lst = [int(l) for l in a.split('-')]
    d = datetime.date(year=lst[0], month=lst[1], day=lst[2])
    r = dt.year - d.year
    lbl['text'] = f'{n}, you are {r} today'


Label(text=f'Today: {dt}', bg='white', font='Arial 10').grid(row=0, column=0, padx=10, pady=5)

Label(text='You name:', bg='white', font='Arial 10').grid(row=1, column=0, padx=5, pady=5)
name = Entry(width=15, bg='white', font="Arial 12")
name.insert(0, 'Lenin')
name.grid(row=1, column=1, padx=10, pady=10)

Label(text='You Birthday:', bg='white', font='Arial 10').grid(row=2, column=0, padx=5, pady=5)
age = Entry(width=15, bg='white', font="Arial 10")
age.insert(0, '1870-4-22')
age.grid(row=2, column=1, padx=10, pady=2)

lbl = Label(text='Lenin is 153 today..', bg='white', font='Arial 10')
lbl.grid(row=3, columnspan=2, padx=10, pady=30)

btn = Button(text='Calculate')
btn.grid(row=4, column=1, padx=10, pady=10)
btn.bind('<Button-1>', calc)
root.mainloop()