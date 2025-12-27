class Cat:
    def __init__(self, poroda, color, name):
        self.poroda = poroda
        self.color = color
        self.name = name
        self.cond = False
        self.weight = 70

    def printInfo(self):
        print("Meow")
        print("=" * 10)

    def wake_up(self):
        if self.cond == False:
            print("Кошка еще не спит!")
            return
        self.cond = True
        print("Вы разбудили кошкку (Она не давольна!).")

    def lull(self):
        if self.cond == True:
            print("Кошка уже спит!")
            return
        self.cond = False
        print("Вы убаюкали кошкку (Она давольна).")

    def feeding(self):
        feed = int(input("На сколько вы хотите покормить кота?"))
        if self.weight < 0:
            print("Кошка не может похудеть от еды!")
            return
        if self.weight == 0:
            print("Ваше кошка улетела")
        print(F"Теперь ваша кошка весит: {self.weight + feed} ньютонов.")
        