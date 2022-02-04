"""
Реализация графического интерфеса дял просмотра и изменения экземплеров класса,
хранящихся в хранилище
хранилище нахожится на том же компьютере, где выполняется сценарий в виде одного
или более локальных файлов
"""

from tkinter import *
from tkinter.messagebox import showinfo
import shelve

shelvename = 'class-shelve'
fieldnames = ('name', 'age', 'job', 'pay')

def makeWidgets():
    global entries
    window = Tk()
    window.title('People Shelve')
    form = Frame(window)
    form.pack()
    entries = {}
    for (ix, label) in enumerate(('key',) + fieldnames):
        lab = Label(form, text=label)
        ent = Entry(form)
        lab.grid(row=ix, column=0)
        ent.grid(row=ix, column=1)
        entries[label] = ent
    Button(window, text='Fetch', command=fetchRecord).pack(side=LEFT)
    Button(window, text='Update', command=updateRecord).pack(side=LEFT)
    Button(window, text="Quit", command=window.quit).pack(side=RIGHT)
    return window

def fetchRecord():
    key = entries['key'].get()
    print(f"fetchRecord => {key}")
    try:
        record = db[key]
    except:
        showinfo(title='Error', message='No such key!')
    else:
        for field in fieldnames:
            entries[field].delete(0, END)
            entries[field].insert(0, repr(getattr(record, field)))
def updateRecord():
    key = entries['key'].get()
    print(f"updateRecord => {key}")
    if key in db:
        record = db[key]
    else:
        from person_start import Person
        record = Person(name='?', age='?')
    
    for field in fieldnames:
        setattr(record, field, eval(entries[field].get()))
    db[key] = record

db = shelve.open(shelvename)
window = makeWidgets()
window.mainloop()
db.close()