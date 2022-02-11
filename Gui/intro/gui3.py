import sys
from tkinter import *

# def quit():
#     print('Hello, I must be going...')
#     sys.exit()

def handler(x, y=2):
    print(x + y)
    sys.exit()
# def temp():
#     handler(2)

# widget = Button(None, text='Hello event world', command=quit)
# widget = Button(None, text='Hello event world', command=(lambda: print('Hello, lambda world') or sys.exit()))
widget = Button(None, text='Hello event world', command=(lambda: handler(3)))
widget.pack()
widget.mainloop()