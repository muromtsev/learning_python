import ttkbootstrap as ttk
from ttkbootstrap.constants import *

root = ttk.Window()
root.geometry('250x300')
style = ttk.Style("darkly")
root.resizable(False, False)
ttk.Style().configure("TButton", font="TkFixedFont 10")
# Frame Label
frame_lbl = ttk.Frame()
frame_lbl.grid(row=0, column=0)
# Label
lbl = ttk.Label(frame_lbl, text='0', bootstyle='inverse-secondary', font='TkFixedFont 15', padding=10, width=20, anchor=E)
lbl.grid(row=0, column=0, padx=2, pady=2)

# Frame Clear
frame_clear = ttk.Frame()
frame_clear.grid(row=1, column=0)
# C, clear, % , /
btn_about = ttk.Button(frame_clear, text='C', bootstyle='dark', width=5, padding=10)
btn_about.grid(row=0, column=0, sticky=NSEW, padx=1, pady=1)
btn_clear = ttk.Button(frame_clear, text='Clear', bootstyle='info', width=5, padding=10)
btn_clear.grid(row=0, column=1, sticky=NSEW, padx=1, pady=1)
btn_percent = ttk.Button(frame_clear, text='%', width=5, padding=10, bootstyle='success')
btn_percent.grid(row=0, column=2, sticky=NSEW, padx=1, pady=1)
btn_division = ttk.Button(frame_clear, text='/', width=5, padding=10, bootstyle='success')
btn_division.grid(row=0, column=3, sticky=NSEW, padx=1, pady=1)

# Frame Buttons
frame_btns = ttk.Frame()
frame_btns.grid(row=2, columnspan=4)
# 7, 8, 9, *
btn_seven = ttk.Button(frame_btns, text='7', width=5, padding=10)
btn_seven.grid(row=0, column=0, sticky=NSEW, padx=1, pady=1)
btn_eight = ttk.Button(frame_btns, text='8', width=5, padding=10)
btn_eight.grid(row=0, column=1, sticky=NSEW, padx=1, pady=1)
btn_nine = ttk.Button(frame_btns, text='9', width=5, padding=10)
btn_nine.grid(row=0, column=2, sticky=NSEW, padx=1, pady=1)
btn_multi = ttk.Button(frame_btns, text='*', width=5, padding=10, bootstyle='success')
btn_multi.grid(row=0, column=3, sticky=NSEW, padx=1, pady=1)
# 4, 5, 6, -
btn_four = ttk.Button(frame_btns, text='4', width=5, padding=10)
btn_four.grid(row=1, column=0, sticky=NSEW, padx=1, pady=1)
btn_five = ttk.Button(frame_btns, text='5', width=5, padding=10)
btn_five.grid(row=1, column=1, sticky=NSEW, padx=1, pady=1)
btn_six = ttk.Button(frame_btns, text='6', width=5, padding=10)
btn_six.grid(row=1, column=2, sticky=NSEW, padx=1, pady=1)
btn_diff = ttk.Button(frame_btns, text='-', width=5, padding=10, bootstyle='success')
btn_diff.grid(row=1, column=3, sticky=NSEW, padx=1, pady=1)
# 1, 2, 3, +
btn_one = ttk.Button(frame_btns, text='1', width=5, padding=10)
btn_one.grid(row=2, column=0, sticky=NSEW, padx=1, pady=1)
btn_two = ttk.Button(frame_btns, text='2', width=5, padding=10)
btn_two.grid(row=2, column=1, sticky=NSEW, padx=1, pady=1)
btn_three = ttk.Button(frame_btns, text='3', width=5, padding=10)
btn_three.grid(row=2, column=2, sticky=NSEW, padx=1, pady=1)
btn_add = ttk.Button(frame_btns, text='+', width=5, padding=10, bootstyle='success')
btn_add.grid(row=2, column=3, sticky=NSEW, padx=1, pady=1)
# +\- 0 . =
btn_symbol = ttk.Button(frame_btns, text='+\-', width=5, padding=10, bootstyle='secondary')
btn_symbol.grid(row=3, column=0, sticky=NSEW, padx=1, pady=1)
btn_zero = ttk.Button(frame_btns, text='0', width=5, padding=10)
btn_zero.grid(row=3, column=1, sticky=NSEW, padx=1, pady=1)
btn_dot = ttk.Button(frame_btns, text='.', width=5, padding=10, bootstyle='secondary')
btn_dot.grid(row=3, column=2, sticky=NSEW, padx=1, pady=1)
btn_eq = ttk.Button(frame_btns, text='=', width=5, padding=10, bootstyle='success')
btn_eq.grid(row=3, column=3, sticky=NSEW, padx=1, pady=1)

root.mainloop()