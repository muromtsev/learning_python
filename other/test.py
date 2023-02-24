import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()

secvar = ttk.StringVar()
SEC = 0

def counter():
    global SEC
    if SEC > 3:
        SEC = 0
    secvar.set(SEC)
    l['text'] = secvar.get()

    SEC += 1
    root.after(1000, counter)


def start(event):
    root.after(1, counter)


l = ttk.Label(text='0', font="Arial 20")
l.pack()
bstart = ttk.Button(text='Start')
bstart.pack(padx=10, pady=10)
bstart.bind('<Button-1>', start)

bstop = ttk.Button(text='Stop')
bstop.pack(padx=10, pady=10)
bstop.bind('<Button-1>', stop)

root.mainloop()
