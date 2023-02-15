from tkinter import *

# root = Tk()

# e = Entry(width=20)
# b = Button(text='Преобразовать')
# l = Label(bg='black', fg='white', width=20)

# def strToSortlist(event):
#     s = e.get()
#     s = s.split()
#     s.sort()
#     l['text'] = ' '.join(s)

# b.bind('<Button-1>', strToSortlist)

# e.pack()
# b.pack()
# l.pack()
# root.mainloop()


class Block():
    def __init__(self, master):
        self.e = Entry(master, width=20)
        self.b =  Button(master, text='Change')
        self.l = Label(master, bg='black', fg='white', width=20)
        # self.b['command'] = self.strToSortlist
        self.e.pack()
        self.b.pack()
        self.l.pack()
    def setFunc(self, func):
        self.b['command'] = eval('self.' + func)
    def strToSortlist(self):
        s = self.e.get()
        s = s.split()
        s.sort()
        self.l['text'] = ' '.join(s)
    def strReverse(self):
        s = self.e.get()
        s = s.split()
        s.reverse()
        self.l['text'] = ' '.join(s)

root = Tk()

first_block = Block(root)
first_block.setFunc('strToSortlist')

second_block = Block(root)
second_block.setFunc('strReverse')

root.mainloop()