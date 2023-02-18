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

def deleteText(event):
   
    txt.delete(1.0, END)

x = 0
y = 0

def popup(event):
    global x, y
    x = event.x
    y = event.y
    menu.post(event.x_root, event.y_root)
    deleteText(event)

root = Tk()

mainmenu = Menu(root)
root.config(menu=mainmenu)

mainmenu.add_command(label='Open', command=insertText)
mainmenu.add_command(label='Save', command=extractText)


txt = Text(width=50, height=25)
txt.grid(columnspan=2)

menu = Menu(txt, tearoff=0)
menu.add_command(label='Clear')

txt.bind('<Button-3>', popup)


root.mainloop()