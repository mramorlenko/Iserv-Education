from tkinter import *

mainWindow = Tk()
width = 400
height = 200
mainWindow.title("Викторина")

screen_width = mainWindow.winfo_screenwidth()
screen_height = mainWindow.winfo_screenheight()

x_offset = (screen_width - width) // 2
y_offset = (screen_height - height) // 2

mainWindow.geometry(f"{width}x{height}+{x_offset}+{y_offset}")

QUEST = Label(text="", font=("Arial", 16))
QUEST.place(anchore="centre",relx=0.5,rely=0.15)

info = Label(text="", font=("Arial", 16))
info.place(anchore="centre",relx=0.5,rely=0.25)

buttons=[]

for i in range(1, 5):
    btn = Button(width=50, height=1, font=("Arial", 14))
    btn.place(anchor="centre", relx=0.5, rely=0.25+0.15*i)
    buttons.append(btn)

mainWindow.mainloop()