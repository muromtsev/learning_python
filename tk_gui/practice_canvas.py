from tkinter import Tk, Canvas
 
def click(event):
  c.x = event.x + c.radius
  c.y = event.y + c.radius
  motion()
 
def motion():
  x = c.coords(c.ball)[2]
  y = c.coords(c.ball)[3]
  if c.x == x and c.y == y:
    return
  if c.x < x:
    c.move(c.ball,-1, 0)
  if c.x > x:
    c.move(c.ball, 1, 0)
  if c.y < y:
    c.move(c.ball, 0,-1)
  if c.y > y:
    c.move(c.ball, 0, 1)
  root.after(10, motion)
 
root = Tk()
c = Canvas(root, width=300, height=200, bg="white")
c.pack()
c.radius = 20
c.ball = c.create_oval(0, 100, c.radius*2, 100+c.radius*2, fill='green')
c.bind("<Button-1>", click)
root.mainloop()