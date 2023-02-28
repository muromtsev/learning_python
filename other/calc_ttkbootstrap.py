import ttkbootstrap as ttk
from ttkbootstrap.constants import *


root = ttk.Window()
root.geometry('250x300')
style = ttk.Style("darkly")
root.resizable(False, False)
ttk.Style().configure("TButton", font="TkFixedFont 10")


display_var = ttk.StringVar(value=0)
x = ttk.DoubleVar()
y = ttk.DoubleVar()
operator = ttk.StringVar(value='+')


def on_btn_pressed(txt):
    display = display_var.get()

    if len(display) > 0:
        if display in ['/', '*', '-', '+']:
            display = display[1:]

    if isinstance(txt, int):
        press_num(display, txt)
    elif txt in ['C', 'CE']:
        display_var.set('')
        res_var()
    elif txt == '.' and '.' not in display:
        display_var.set(f"{display}{txt}")
    elif txt == '±':
        press_inverse(display)
    elif txt in ['/', '*', '+', '-']:
        press_oper(txt)
    elif txt == '=':
        press_eq(display)


def res_var():
    x.set(value=0)
    y.set(value=0)
    operator.set(value='+')
    lbl['text'] = 0


def press_num(display, txt):
    if display == '0':
        display_var.set(txt)
    else:
        display_var.set(f"{display}{txt}")
    lbl['text'] = display_var.get()


def press_inverse(display):
    if display.startswith("-"):
        if len(display) > 1:
            display_var.set(display[1:])
        else:
            display_var.set("")
    else:
        display_var.set(f"-{display}")
    lbl['text'] = display_var.get()


def press_oper(txt):
    operator.set(txt)
    display = float(display_var.get())
    if x.get() != 0:
        y.set(display)
    else:
        x.set(display)
    display_var.set(txt)
    lbl['text'] = display_var.get()


def press_eq(display):
    if x.get() != 0:
        y.set(display)
    else:
        x.set(display)
    one = x.get()
    two = y.get()
    op = operator.get()
    print(one, two, op)
    if all([one, two, op]):
        result = eval(f"{one}{op}{two}")
        display_var.set(result)
        res_var()
        lbl['text'] = display_var.get()


# Frame Label
frame_lbl = ttk.Frame()
frame_lbl.grid(row=0, column=0)
# Label
lbl = ttk.Label(frame_lbl, text=display_var.get(), bootstyle="inverse-secondary", font='TkFixedFont 15', padding=10, width=20, anchor=E)
lbl.grid(row=0, column=0, padx=2, pady=2)

# Frame Clear
frame_clear = ttk.Frame()
frame_clear.grid(row=1, column=0)
# C, clear, % , /
btn_about = ttk.Button(frame_clear, text='C', bootstyle='dark', width=5, padding=10, command=lambda txt='C': on_btn_pressed(txt))
btn_about.grid(row=0, column=0, sticky=NSEW, padx=1, pady=1)
btn_clear = ttk.Button(frame_clear, text='CE', bootstyle='info', width=5, padding=10, command=lambda txt='CE': on_btn_pressed(txt))
btn_clear.grid(row=0, column=1, sticky=NSEW, padx=1, pady=1)
btn_percent = ttk.Button(frame_clear, text='%', width=5, padding=10, bootstyle='success', command=lambda txt='%': on_btn_pressed(txt))
btn_percent.grid(row=0, column=2, sticky=NSEW, padx=1, pady=1)
btn_division = ttk.Button(frame_clear, text='/', width=5, padding=10, bootstyle='success', command=lambda txt='/': on_btn_pressed(txt))
btn_division.grid(row=0, column=3, sticky=NSEW, padx=1, pady=1)

# Frame Buttons
frame_btns = ttk.Frame()
frame_btns.grid(row=2, columnspan=4)
# 7, 8, 9, *
btn_seven = ttk.Button(frame_btns, text='7', width=5, padding=10, command=lambda txt=7: on_btn_pressed(txt))
btn_seven.grid(row=0, column=0, sticky=NSEW, padx=1, pady=1)
btn_eight = ttk.Button(frame_btns, text='8', width=5, padding=10, command=lambda txt=8: on_btn_pressed(txt))
btn_eight.grid(row=0, column=1, sticky=NSEW, padx=1, pady=1)
btn_nine = ttk.Button(frame_btns, text='9', width=5, padding=10, command=lambda txt=9: on_btn_pressed(txt))
btn_nine.grid(row=0, column=2, sticky=NSEW, padx=1, pady=1)
btn_multi = ttk.Button(frame_btns, text='*', width=5, padding=10, bootstyle='success', command=lambda txt='*': on_btn_pressed(txt))
btn_multi.grid(row=0, column=3, sticky=NSEW, padx=1, pady=1)
# 4, 5, 6, -
btn_four = ttk.Button(frame_btns, text='4', width=5, padding=10, command=lambda txt=4: on_btn_pressed(txt))
btn_four.grid(row=1, column=0, sticky=NSEW, padx=1, pady=1)
btn_five = ttk.Button(frame_btns, text='5', width=5, padding=10, command=lambda txt=5: on_btn_pressed(txt))
btn_five.grid(row=1, column=1, sticky=NSEW, padx=1, pady=1)
btn_six = ttk.Button(frame_btns, text='6', width=5, padding=10, command=lambda txt=6: on_btn_pressed(txt))
btn_six.grid(row=1, column=2, sticky=NSEW, padx=1, pady=1)
btn_diff = ttk.Button(frame_btns, text='-', width=5, padding=10, bootstyle='success', command=lambda txt='-': on_btn_pressed(txt))
btn_diff.grid(row=1, column=3, sticky=NSEW, padx=1, pady=1)
# 1, 2, 3, +
btn_one = ttk.Button(frame_btns, text='1', width=5, padding=10, command=lambda txt=1: on_btn_pressed(txt))
btn_one.grid(row=2, column=0, sticky=NSEW, padx=1, pady=1)
btn_two = ttk.Button(frame_btns, text='2', width=5, padding=10, command=lambda txt=2: on_btn_pressed(txt))
btn_two.grid(row=2, column=1, sticky=NSEW, padx=1, pady=1)
btn_three = ttk.Button(frame_btns, text='3', width=5, padding=10, command=lambda txt=3: on_btn_pressed(txt))
btn_three.grid(row=2, column=2, sticky=NSEW, padx=1, pady=1)
btn_add = ttk.Button(frame_btns, text='+', width=5, padding=10, bootstyle='success', command=lambda txt='+': on_btn_pressed(txt))
btn_add.grid(row=2, column=3, sticky=NSEW, padx=1, pady=1)
# +\- 0 . =
btn_symbol = ttk.Button(frame_btns, text='±', width=5, padding=10, bootstyle='secondary', command=lambda txt='±': on_btn_pressed(txt))
btn_symbol.grid(row=3, column=0, sticky=NSEW, padx=1, pady=1)
btn_zero = ttk.Button(frame_btns, text='0', width=5, padding=10, command=lambda txt=0: on_btn_pressed(txt))
btn_zero.grid(row=3, column=1, sticky=NSEW, padx=1, pady=1)
btn_dot = ttk.Button(frame_btns, text='.', width=5, padding=10, bootstyle='secondary', command=lambda txt='.': on_btn_pressed(txt))
btn_dot.grid(row=3, column=2, sticky=NSEW, padx=1, pady=1)
btn_eq = ttk.Button(frame_btns, text='=', width=5, padding=10, bootstyle='success', command=lambda txt='=': on_btn_pressed(txt))
btn_eq.grid(row=3, column=3, sticky=NSEW, padx=1, pady=1)

root.mainloop()
