from tkinter import *

root = Tk()

def open_file():
    filename = e1.get()
    
    with open(f'{filename}', encoding='utf-8') as file:
        f = file.readlines()

    e2.insert(1.0, f)

def save_file():
    txt = e2.get(1.0, END)
    filename = e1.get()

    with open(f'{filename}', 'w', encoding='utf-8') as file:
        file.write(txt)

f1 = Frame()
e1 = Entry(f1, width=50)
btn_open = Button(f1, text='Open', bg='#ccc', command=open_file)
btn_save = Button(f1, text='Save',bg='#eee', command=save_file)
e2 = Text(width=50, height=10)


f1.pack()
e1.pack(side=LEFT, padx=5, pady=5)
btn_open.pack(side=LEFT, padx=5, pady=5)
btn_save.pack(side=LEFT, padx=5, pady=5)
e2.pack(side=BOTTOM)
root.mainloop()