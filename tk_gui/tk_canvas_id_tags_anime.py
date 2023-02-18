from tkinter import *

root = Tk()

c = Canvas(width=460, height=100, bg='grey80')
# c.focus_set()
c.pack()

# ball = c.create_oval(140, 140, 160, 160, fill='green')
# c.bind('<Up>', lambda event: c.move(ball, 0, -2))
# c.bind('<Down>', lambda event: c.move(ball, 0, 2))
# c.bind('<Left>', lambda event: c.move(ball, -2, 0))
# c.bind('<Right>', lambda event: c.move(ball, 2, 0))

# rect = c.create_rectangle(80, 80, 120, 120, fill='lightgreen')

# def inFocus(event):
#     c.itemconfig(rect, fill='green', width=2)
#     c.coords(rect, 70, 70, 130, 130)

# c.bind('<FocusIn>', inFocus)
# print(rect)

# oval = c.create_oval(30, 10, 130, 80, tag='g1')
# c.create_line(10, 100, 450, 100, tag='g1')

# def color(event):
#     c.itemconfig('g1', fill='red', width=3)

# c.bind('<Button-3>', color)


oval = c.create_oval(30, 10, 130, 80, fill='orange')
c.create_rectangle(180, 10, 230, 80, tag='rect', fill='lightgreen')
trian = c.create_polygon(330, 80, 380, 10, 430, 80, fill='white', outline='black')

def oval_func(event):
    c.delete(oval)
    c.create_text(80, 50, text='Circle')
def rect_func(event):
    c.delete("rect")
    c.create_text(230, 50, text='Rectangle')
def triangle(event):
    c.delete(trian)
    c.create_text(380, 50, text='Triangle')

c.tag_bind(oval, '<Button-1>', oval_func)
c.tag_bind("rect", '<Button-1>', rect_func)
c.tag_bind(trian, '<Button-1>', triangle)


root.mainloop()