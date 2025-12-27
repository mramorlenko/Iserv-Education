class Car:
    def __init__(self, name, color, power):
        self.name = name
        self.color = color
        self.power = power
        self.mileage = 0
        self.is_running = False

    def printInfo(self):
        print("=" * 10)
        print(f"Название машины: {self.name}")
        print(f"Цвет: {self.color}")
        print(f"Мощность: {self.power}")
        print("=" * 10)

    def start_engine(self):
        if self.is_running:
            print("Двигатель уже заведен!")
            return
        self.is_running = True
        print("Двигатель запущен.")

    def stop_engine(self):
        if not self.is_running:
            print("Двигатель уже остановлен!")
            return
        self.is_running = False
        print("Двигатель остановлен.")

    