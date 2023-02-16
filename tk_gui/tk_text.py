from tkinter import *

root = Tk()

text = Text(width=25, height=5, bg='darkgreen', fg='white', wrap=WORD)
# значение WORD опции wrap позволяет переносить слова на новую строку целиком
print(text['width'], text['height'])
text.pack(side=LEFT)

scroll = Scrollbar(command=text.yview)
scroll.pack(side=LEFT, fill=Y)

text.config(yscrollcommand=scroll.set)


root.mainloop()