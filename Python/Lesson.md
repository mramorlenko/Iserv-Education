# Мой конспект

## Мой первый калькулятор:
```
print("Введите первое число: ")
numberA = int(input())
print("Введите второе число: ")
numberB = int(input())
print(f"Сумма чисел:  {numberA} + {numberB} равна {numberA + numberB}")
print(f"Разность чисел:  {numberA} - {numberB} равна {numberA - numberB}")
print(f"Произведение чисел:  {numberA} * {numberB} равна {numberA * numberB}")
print(f"Частность чисел:  {numberA} : {numberB} равна {numberA // numberB}")
```

## Вещественный калькулятор

```
number_int = int(input())
number_float = float(input())
number_str = "30"


print("целое + вещемтвенное")
print(number_int + number_float)
print(type((number_int + number_float)))
print('-' * 30)

print("\nцелое - вешественное")
print(number_int - number_float)
print(type((number_int - number_float)))
print('-' * 30)

print("\nцелое / вешественное")
print(number_int / number_float)
print(type((number_int / number_float)))
print('-' * 30)

print("\nцелое * вешественное")
print(number_int * number_float)
print(type((number_int * number_float)))
print('-' * 30)
```

## Оприделитель возраста

```
print("Введите год вашего рождения: ")
birth_day = input()
curent_year = 2025
print(f"В этом году вам исполниться +  {curent_year - birth_day} лет")
```

## Операторы сравнение

```
a = 12*3
b = 18*2

print(a , b)
print('_' * 50)
print("a == b:", a == b)#равно
print("a != b:", a != b)#не равно
print("a < b:", a < b)#меньше
print("a > b:", a > b)#больше
print("a <= b:", a <= b)#меньше или равно
print("a >= b:", a >= b)#больше или равно
```

## Логические операторы

```
not, or, and, 
```

## Дополнительные операторы

### // -  целочисленное деление
### /* - деление состатком
### ** - Возведение в X степень

## Условная конструкция

```
age = int(input("Введите ваш возраст: "))
if(age < 18):
    print("Вы еще слишком молоды")
elif(age >= 18 and age <= 30):
    print("Вы подписаны на рассылку повестки")
else:
    print("За пенсией не сюда!")
```

## Практика с циклом WHILE

```
proiz = 1
PrP = 1
while(PrP != 0):
    proiz *= PrP
    PrP = int(input("Введите число: "))
print(f"Произведени ваших чисел равна: {proiz}")
```

## Практика с циклом FOR

```
for i in range(1, 100):
    if(i % 3 != 0 and i % 5 != 0):
        print(i, end=" ")
```

## Практика со срезами

```
Str = str(input("Введите любой текст: "))
A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))

print(Str[A:B])
```

## Практика со исключением

```
SrT = str(input("Введите какое-нибудь предложение: "))
SrT = SrT.replace("!", "")
SrT = SrT.replace(".", "")
SrT = SrT.replace(",", "")
SrT = SrT.replace("?", "")
print(SrT)
```

# Занятие 6

## Задание 1

```
fruits = ["aple", "banana", "cherry"]
fruits.append("orange")
fruits.insert(1, "lemon")
fruits.remove("banana")
Fr_len = len(fruits)
print(f"Фрукты: {fruits}. Кол-во фруктов: {Fr_len}")
```

## Модуль MATH

```
import math

part_1_1 = math.cos(math.pi/3) + math.log2(16)
part_1_2 = sum([math.factorial(n) + 1 for n in range(0,4)])
part_1 = part_1_1 * part_1_2
print(part_1)

part_2 = (math.sqrt(25) - abs(-5)) ** math.sin(math.pi/2)

print(part_2)

part_3 = (3 ** 2 + 4 ** 2) / 5 * (math.tan(0) + 1)

print(part_3)

result = part_1 + part_2 - part_3
print(result)
```

## Создание подпольного казино
```
import random

life = 5
rand_num = random.randint(1,50)
isWin = False

print("Было закадано число от 1 до 50, Попробуй угадать!")
while life != 0:
    num = int(input("Введите число: "))

    if num == rand_num:
        print("Вы победили!")
        isWin = True
        break

    elif num < rand_num:
        print("Загаданное число больше.")
        life -= 1

    elif num > rand_num:
        print("Загаданное число меньше.")
        life -= 1
if(not isWin):
    print("Вы проиграли!")
```

## Создание человеческой рожи

```
import turtle

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("lightblue")
screen.title("Веселый смайлик - Изучаем Turtle")

t = turtle.Turtle()
t.speed(5)
t.width(3)

t.penup()
t.goto(0, -100)
t.pendown()
t.color("black", "yellow")
t.begin_fill()
t.circle(100)
t.end_fill()

t.penup()
t.goto(-40, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(40, 30)
t.pendown()
t.color("black", "white")
t.begin_fill()
t.circle(20)
t.end_fill()

t.penup()
t.goto(-40, 40)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()

t.penup()
t.goto(40, 40)
t.pendown()
t.color("black", "black")
t.begin_fill()
t.circle(10)
t.end_fill()


t.penup()
t.goto(-60, -20)
t.pendown()
t.color("black")
t.begin_fill()
t.width(5)
t.setheading(-60)
t.circle(70, 120)

t.hideturtle
screen.exitonclick()
```