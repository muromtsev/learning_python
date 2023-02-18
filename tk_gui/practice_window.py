from tkinter import *

root = Tk()
root.geometry('400x400')
w = root.winfo_screenwidth()
h = root.winfo_screenheight()

w = w//2
h = h//2
w = w - 200
h = h - 200
root.geometry(f'+{w}+{h}')


c = Canvas(width=w, height=h, bg='white')
c.pack()



def figure(event):
    t = Toplevel()
    t.geometry(f'150x150-600+{h}')
    
    f1 = Frame(t)
    f1.pack()
    lx1 = Label(f1, text='x1')
    lx1.pack(side=LEFT)
    ex1 = Entry(f1, width=5)
    ex1.pack(side=LEFT)
    ly1 = Label(f1, text='y1')
    ly1.pack(side=LEFT)
    ey1 = Entry(f1, width=5)
    ey1.pack(side=LEFT)

    f2 = Frame(t)
    f2.pack()
    lx2 = Label(f2, text='x2')
    lx2.pack(side=LEFT)
    ex2 = Entry(f2, width=5)
    ex2.pack(side=LEFT)
    ly2 = Label(f2, text='y2')
    ly2.pack(side=LEFT)
    ey2 = Entry(f2, width=5)
    ey2.pack(side=LEFT)

    rvar = IntVar()
    rvar.set(0)
    r1 = Radiobutton(t, text='Rectangele', variable=rvar, value=0)
    r1.pack()
    r2 = Radiobutton(t, text='Oval', variable=rvar, value=1)
    r2.pack()
    
    btn = Button(t, text='Draw')
    btn.pack()

    btn.bind('<Button-1>', lambda event, flag=rvar.get(): draw(event, flag))

    def draw(event, flag):
        x1 = int(ex1.get())
        y1 = int(ey1.get())
        x2 = int(ex2.get())
        y2 = int(ey2.get())

        if flag == 0:        
            c.create_rectangle(x1, y1, x2, y2, outline='black', width=3)
        elif flag == 1:
            c.create_oval(x1, y1, x2, y2, outline='black', width=3)


btn = Button(text='Добавить фигуру')
btn.pack()

btn.bind('<Button-1>', figure)

root.mainloop()