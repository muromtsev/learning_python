import sys
from tkinter import Toplevel, Button, Label

win1 = Toplevel()
win2 = Toplevel()

Button(win1, text='Spam', command=sys.exit).pack() # два не зависимых окна
Button(win2, text='SPAM', command=sys.exit).pack() # являющихся частью одного и того же процесса

Label(text='Popups').pack() # по умолчанию добавляется в корневое окно Tk()
win1.mainloop()