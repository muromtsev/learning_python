from tkinter import *

root = Tk()

root.title('Главное окно')

def about():
    a = Toplevel()
    a.geometry('200x150')
    a['bg'] = 'grey'
    a.overrideredirect(True)
    Label(a, text='About This').pack(expand=1)
    a.after(5000, lambda: a.destroy())

Button(text='Button', width=20).pack()
Label(text='Label', width=20, height=3).pack()
Button(text='About', width=20, command=about).pack()



# Button(text='btn', width=20).pack()
# Label(text='Lbl', width=20, height=3).pack()
# Button(text='Btn', width=20).pack()
# # Метод update_idletasks() позволяет перезагрузить данные об окне после размещения на нем виджетов
# root.update_idletasks()
# s = root.geometry()
# print(s)
# s = s.split('+')
# print(s)
# s = s[0].split('x')
# print(s)

# width_root = int(s[0])
# height_root = int(s[1])

# w = root.winfo_screenwidth()
# h = root.winfo_screenheight()

# w = w//2
# h = h//2
# w = w - 200
# h = h - 200
# root.geometry(f'+{w}+{h}')

root.mainloop()