from tkinter import *
import zipfile
import os

zfiles = [filename for filename in os.listdir('.') if zipfile.is_zipfile(filename)]
size_zipfile = os.path.getsize('test.zip')
current_file = ''

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


def show_file(event):
    """
        Создание списка Listbox на основе выбранного файла
    """
    if not lbox.curselection():
        file_box.insert(0, 'Выберите файл')
    else:
        file_box.delete(0)
        global current_file
        current_file = lbox.get(lbox.curselection())
        with zipfile.ZipFile(f"{current_file}") as zfile:
            info = zfile.infolist()
            for el in info:
                if not el.is_dir():
                    file_box.insert(END, el.filename)


def file_extract(event):
    """
        Извлекает ОДИН выбранный объект в директорию
    """
    if not file_box.curselection():
        pass
    else:
        elem = file_box.get(file_box.curselection())
        with zipfile.ZipFile(f"{current_file}") as zfile:
            zfile.extract(elem)


def file_extract_mark(event):
    """
        Извлекает выбранные в списке объекты в директорию
    """
    if not file_box.curselection():
        pass
    else:
        select = file_box.curselection()
        with zipfile.ZipFile(f"{current_file}") as zfile:
            for elem in select:
                zfile.extract(file_box.get(elem))

def file_extract_all(event):
    """
        Извлекает все объекты из файла
    """
    with zipfile.ZipFile(f"{current_file}") as zfile:
        zfile.extractall()


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
# первый фрейм для спискаб подписи и кнопки
fr1 = Frame()
fr1.grid(row=0, column=0)
Label(fr1, text='Доступные Zip-файлы', font="Verdana 10").grid(row=0, column=0, padx=10, pady=10)

lbox = Listbox(fr1, bg='white', font="Verdana 12")
lbox.grid(row=1, column=0, padx=10, pady=10)

# заполняем список найденных zip-файлов
for idx, el in enumerate(zfiles):
    lbox.insert(idx+1, el)

btn = Button(fr1, text='Показать содержимое')
btn.grid(row=2, column=0, pady=10)
btn.bind('<Button-1>', show_file)

# второй фрейм для подписи и списка
fr2 = Frame()
fr2.grid(row=0, column=1)

lbl_file = Label(fr2, text='Содержимое файла')
lbl_file.grid(row=0, column=0)
file_box = Listbox(fr2, selectmode=EXTENDED, bg='white', font="Verdana 10", width=45, height=20)
file_box.grid(row=1, column=0, padx=10, pady=3)

# третий фрейм для кнопок
fr3 = Frame()
fr3.grid(row=0, column=2)

btn_extract = Button(fr3, text='Извлечь')
btn_extract.grid(row=0, column=0, pady=5)

btn_extract_mark = Button(fr3, text='Извлечь выбранные')
btn_extract_mark.grid(row=1, column=0, pady=5)

btn_extract_all = Button(fr3, text='Извлечь всё')
btn_extract_all.grid(row=2, column=0, pady=5)

btn_extract.bind('<Button-1>', file_extract)
btn_extract_mark.bind('<Button-1>', file_extract_mark)
btn_extract_all.bind('<Button-1>', file_extract_all)
root.mainloop()