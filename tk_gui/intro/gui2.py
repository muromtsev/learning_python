import sys
from tkinter import *
# widget = Button(None, text='Hello GUI world!', command=sys.exit)
root = Tk()
widget = Button(None, text='press', command=root.quit)
# side - расположение кнопки относительно окна
# expand - расположить кнопку в центра окна
# fill - растягивание кнопки на всю горизонталь окна
widget.pack(side=LEFT, expand=YES, fill=X)
widget.mainloop()