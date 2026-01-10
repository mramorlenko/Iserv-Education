class Cat:
    def __init__(self, poroda, name, age):
        self.__poroda = poroda
        self.__name = name
        self.__age = age

    def printInfo(self):
        print("=== Информация о кошке ===")
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Порода: {self.__poroda}")
        print("=" * 30)

    def speak(self):
        print("Кошка говорит Мяу!")

class Dog:
    def __init__(self, poroda, name, age):
        self.__poroda = poroda
        self.__name = name
        self.__age = age

    def printInfo(self):
        print("=== Информация о кошке ===")
        print(f"Имя: {self.__name}")
        print(f"Возраст: {self.__age}")
        print(f"Порода: {self.__poroda}")
        print("=" * 30)

    def speak(self):
        print("Кошка говорит Гав!")

class HomeCat(Cat):
    def __init__(self, poroda, name, age, color, owner):
        super().__init__(poroda, name, age)
        self.__color = color
        self.__owner = owner
        self.__is_sleep = False

    def printInfo(self):
        super().printInfo()
        print(f"Цвет: {self.__color}")
        print(f"Владелец: {self.__owner}")
        print("=" * 30)

    def play(self):
        if self.__is_sleep:
            print("Кошка спит и не может играть.")
            return
        print("кошка начала играть!")

        