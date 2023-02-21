from tkinter import *
import zipfile
import os

zfiles = [filename for filename in os.listdir('.') if zipfile.is_zipfile(filename)]


size_zipfile = os.path.getsize('test.zip')


def convert_bytes(size):
    """Конвертер байт в большие единицы"""
    if size < 1000:
        return f'{size} B'
    elif 1000 <= size < 1000000:
        return f'{round(size / 1024)} KB'
    elif 1000000 <= size < 1000000000:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'


def func(event):
    lbl['text'] = ''
    names = ''
    with zipfile.ZipFile(f"{lbox.get(lbox.curselection())}") as zfile:
        info = zfile.namelist()
        for el in info:
            names += el + '\n'
    lbl['text'] = names

root = Tk()
# определяем размер окна по центру экрана
root.geometry('800x600')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = w//2
h = h//2
w = w - 400
h = h - 300
root.geometry(f'+{w}+{h}')

fr1 = Frame()
fr1.grid(row=0, column=0)
Label(fr1, text='Доступные файлы', font="Verdana 10").grid(row=0, column=0, padx=10, pady=10)

lbox = Listbox(fr1, bg='white', font="Verdana 12")
lbox.grid(row=1, column=0, padx=10, pady=10)

for idx, el in enumerate(zfiles):
    lbox.insert(idx+1, el)


btn = Button(fr1, text='Button')
btn.grid(row=2, column=0, pady=10)
btn.bind('<Button-1>', func)

lbl = Label(text='Информация о файле...', width=50, height=30, bg='white', justify=LEFT)
lbl.grid(row=0, column=1, padx=10, pady=10)


root.mainloop()




root.mainloop()