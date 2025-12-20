from tkinter import *
from tkinter import Tk
#from PIL import ImageTK, Image


var = IntVar()
var.set(0)
root = Tk()

root.title("Котики")
root.geometry("800x720")
root.resizable(width=False, height=False)
imgs = {1: Image.open("C:\Users\user\Desktop\Gavrilov_Andrey\Python\Lesson_9\assets\7e4cc2a69f256c2cffd07d2d74aa1ddd.jpg"),
        2: Image.open("C:\Users\user\Desktop\Gavrilov_Andrey\Python\Lesson_9\assets\780cf8d0f218041d1a76756cd84c1c8d.jpg"),
        3: Image.open("C:\Users\user\Desktop\Gavrilov_Andrey\Python\Lesson_9\assets\e326d9ad17cadccdd7798ef3aefba732.jpg"),
        3: Image.open("C:\Users\user\Desktop\Gavrilov_Andrey\Python\Lesson_9\assets\i.webp")}

img_b1 = imgs[1].resize((150, 150))
#img_b1 = ImageTk.PhotoImage(img_b1)

img_b2 = imgs[2].resize((150, 150))
#img_b2 = ImageTk.PhotoImage(img_b2)

img_b3 = imgs[3].resize((150, 150))
#img_b3 = ImageTk.PhotoImage(img_b3)

img_b4 = imgs[4].resize((150, 150))
#img_b4 = ImageTk.PhotoImage(img_b4)

varian = {1: img_b1,
          2: img_b2,
          3: img_b3,
          4: img_b4}


# b1 = Radiobutton(width=150, height=150< indicatoron=0, variable=var, value=1, image=img_b1)
# b1.place(relx=0.1, rely=0.75)

sc1 = Scale(from_=50, to=400, length=400)
sc1.place(relx=0.18, rely=0.1)

sc2 = Scale(from_=50, to=400, length=400, orient='horizontal')
sc2.place(relx=0.25, rely=0.03)

canvas = Canvas(width=50, height=50, bg="grey")
canvas.place(relx=0.25, rely=0.1)

#-----------------------------------------------------------------------
root.mainloop()