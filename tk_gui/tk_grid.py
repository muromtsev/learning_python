from tkinter import *

root = Tk()

Label(text='Name:').grid(row=0, column=0, sticky=W, pady=10, padx=10)
table_name = Entry(width=30)
table_name.grid(row=0, column=1, columnspan=3, sticky=W+E, padx=10)

Label(text='Columns:').grid(row=1, column=0, sticky=W, padx=10, pady=10)
table_column = Spinbox(width=7, from_=1, to=5)
table_column.grid(row=1, column=1, padx=10)

Label(text="Rows:").grid(row=1, column=2, sticky=E)
table_row = Spinbox(width=7, from_=1, to=100)
table_row.grid(row=1, column=3, sticky=E, padx=10)

Button(text='Help').grid(row=2, column=0, pady=10, padx=10)
Button(text='Add').grid(row=2, column=2)
Button(text='Cancel').grid(row=2, column=3, padx=10)


root.mainloop()