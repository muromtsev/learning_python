from tkinter import *
from tkinter import filedialog as fd

def insertText():
    filename = fd.askopenfilename()
    f = open(filename)
    s = f.read()
    txt.insert(1.0, s)
    f.close()

def extractText():
    filename = fd.asksaveasfilename(filetypes=(("TXT files", "*.txt"), ("HTML files", "*.html"), ("All files", "*.*")))
    f = open(filename, 'w')
    s = txt.get(1.0, END)
    f.write(s)
    f.close

root = Tk()

txt = Text(width=50, height=25)
txt.grid(columnspan=2)

b1 = Button(text='Open', command=insertText)
b1.grid(row=1, sticky=E)

b2 = Button(text='Save', command=extractText)
b2.grid(row=1, column=1, sticky=W)

root.mainloop()