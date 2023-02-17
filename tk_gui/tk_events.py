from tkinter import *

root = Tk()

def exitWin(event):
    root.destroy()

def inLabel(event):
    t = ent.get()
    lbl.configure(text=t)

def selectAll(event):
    root.after(10, select_all, event.widget)

def select_all(widget):
    widget.selection_range(0, END)
    widget.icursor(END)

ent = Entry(width=40)
ent.focus_set()
ent.pack()

lbl = Label(height=3, fg='orange', bg='darkgreen', font="Verdana 24")
lbl.pack(fill=X)

ent.bind('<Return>', inLabel)
ent.bind('<Control-a>', selectAll)
root.bind('<Control-q>', exitWin)



root.mainloop()


# def b1(event):
#     root.title('Left btn')

# def b3(event):
#     root.title('Right btn')

# def move(event):
#     x = event.x
#     y = event.y
#     s = f'{x} - {y}'

#     root.title(s)

# root.minsize(width=500, height=400)

# root.bind('<Button-1>', b1)
# root.bind('<Button-3>', b3)
# root.bind('<Motion>', move)

# root.mainloop()