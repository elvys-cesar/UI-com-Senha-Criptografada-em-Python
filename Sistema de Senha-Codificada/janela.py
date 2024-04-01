from tkinter import *

root = Tk()

img = PhotoImage(file="image/bem.png")

Label_img =Label(root, image=img).pack()

root.mainloop()