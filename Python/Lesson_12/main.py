from tkinter import *
import funcs

root = Tk()
root.geometry("500x500")
root.resizable(False, False)
root.title("Приложение для теста")

text1 = Label(text="Введите ваш текст!", font=("Arial", 16))
text1.place(anchor="center,", relx=0.5, rely=0.1)

entry = Entry(width=30, font=("Arial", 14))
entry.place(anchor="center", relx=0.5, rely=0.3)

text2 = Label(text="", font=("Arial", 16), fg="red")
text2.place(anchor="center,", relx=0.5, rely=0.6)

but = Button(text="Ввести", font=("Arial", 16), width=10, height=1,
            command = lambda: funcs.print_text(text2, entry.get()))
but.place(anchor="center", relx=0.5, rely=0.4)

root.mainloop()

