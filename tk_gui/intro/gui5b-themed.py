from tkinter import *

class ThemedButton(Button):
    def __init__(self, parent=None, **configs):
        Button.__init__(self, parent, **configs)
        self.pack()
        self.config(fg='red', bg='black', font=('courier', 12), relief=RAISED, bd=5)


def onSpam(): print('Spam')


b1 = ThemedButton(text='spam', command=onSpam)
b2 = ThemedButton(text='eggs')
b2.pack(expand=YES, fill=BOTH)
mainloop()