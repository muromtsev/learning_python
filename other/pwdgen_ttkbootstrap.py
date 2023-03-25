import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox as mb

import string
import random

root = ttk.Window()
root.geometry('900x500')
root.title('Password Generator')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()
w = (w//2) - 450
h = (h//2) - 250
root.geometry(f'+{w}+{h}')
style = ttk.Style("darkly")
root.resizable(False, False)


LENGHT_VAR = ttk.IntVar(value=10)
VOLUME_VAR = ttk.IntVar(value=10)
LATIN_VAR = ttk.IntVar(value=1)
DIGITS_VAR = ttk.IntVar(value=1)
SYMBOLS_VAR = ttk.IntVar(value=1)
AMBIGUOUS_VAR = ttk.IntVar()

LESS_LETTERS = ''.join([symbol for symbol in string.ascii_letters if symbol not in 'ilLoO'])
LESS_DIGITS = ''.join([symbol for symbol in string.digits if symbol not in '10'])

def create_symbols():

    dict_symbols = {
        'ascii_letters': '',
        'digits': '',
        'punctuation': '',
    }

    if AMBIGUOUS_VAR.get() == 0:
        if LATIN_VAR.get() == 1:
            if dict_symbols['ascii_letters'] == '':
                dict_symbols['ascii_letters'] = string.ascii_letters
        else:
            dict_symbols['ascii_letters'] = ''    
        if DIGITS_VAR.get() == 1:
            if dict_symbols['digits'] == '':
                dict_symbols['digits'] = string.digits
        else:
            dict_symbols['digits'] = ''
        if SYMBOLS_VAR.get() == 1:
            if dict_symbols['punctuation'] == '':
                dict_symbols['punctuation'] = string.punctuation
        else:
            dict_symbols['punctuation'] = ''

    elif AMBIGUOUS_VAR.get() == 1:
        if LATIN_VAR.get() == 1:
            if dict_symbols['ascii_letters'] == '':
                dict_symbols['ascii_letters'] = LESS_LETTERS                
        else:
            dict_symbols['ascii_letters'] = ''    
        if DIGITS_VAR.get() == 1:
            if dict_symbols['digits'] == '':
                dict_symbols['digits'] = LESS_DIGITS
        else:
            dict_symbols['digits'] = ''
    return dict_symbols


def create_list_pwd():
    DICT_SYMBOLS = create_symbols()
    vol = VOLUME_VAR.get()
    txt.delete('1.0', END)
    symbols = ''.join([val for val in DICT_SYMBOLS.values()])
    list_pwd = []
    while vol > 0:
        pwd = ''
        for i in range(LENGHT_VAR.get()):
            print(i)
            pwd += random.choice(symbols)
        txt.insert(END, pwd + '\n')
        list_pwd.append(pwd)
        vol -= 1    
    return list_pwd


def create_file():
    with open('passwords.txt', 'w', encoding='utf-8') as file:
        for pwd in create_list_pwd():
            file.write(pwd + '\n')


lbl_property = ttk.Labelframe(bootstyle="info", text='Свойства')
lbl_property.grid(row=0, columnspan=3, ipadx=10, ipady=10, padx=10, sticky=W)

ttk.Label(lbl_property, text='Длина').grid(row=1, column=0, padx=10, pady=10, sticky=W)
lenght_pwd = ttk.Entry(lbl_property, bootstyle='primary', textvariable=LENGHT_VAR, width=10)
lenght_pwd.grid(row=1, column=1, columnspan=3, sticky=W+E)

ttk.Label(lbl_property, text='Количество').grid(row=2, column=0, padx=10, pady=10, sticky=W)
volume_pwd = ttk.Entry(lbl_property, bootstyle='primary', textvariable=VOLUME_VAR, width=10)
volume_pwd.grid(row=2, column=1, columnspan=2, sticky=W+E)

ttk.Checkbutton(lbl_property, bootstyle="success-round-toggle", text="Латинские буквы", state=ACTIVE, variable=LATIN_VAR, command=create_symbols).grid(row=3, column=0, ipadx=5, ipady=5, padx=5, sticky=W)

ttk.Checkbutton(lbl_property, bootstyle="success-round-toggle", text="Цифры", state=ACTIVE, variable=DIGITS_VAR, command=create_symbols).grid(row=4, column=0, ipadx=5, ipady=5, padx=5, sticky=W)

ttk.Checkbutton(lbl_property, bootstyle="success-round-toggle", text="Символы", state=ACTIVE, variable=SYMBOLS_VAR, command=create_symbols).grid(row=5, column=0, ipadx=5, ipady=5, padx=5, sticky=W)

ttk.Checkbutton(lbl_property, bootstyle="success-round-toggle", text="Исключение (il1Lo0O)", variable=AMBIGUOUS_VAR, command=create_symbols).grid(row=6, column=0, ipadx=5, ipady=5, padx=5, sticky=W)


btn_create = ttk.Button(text='Создать', command=create_list_pwd)
btn_create.grid(row=1, column=0)

btn_write = ttk.Button(text='Создать файл', command=create_file)
btn_write.grid(row=1, column=1)

txt = ttk.ScrolledText()
txt.grid(row=0, rowspan=4, column=3, padx=10, pady=10)



root.mainloop()
