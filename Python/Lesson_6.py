# fruits = ["aple", "banana", "cherry"]
# fruits.append("orange")
# fruits.insert(1, "lemon")
# fruits.remove("banana")
# Fr_len = len(fruits)
# print(f"Фрукты: {fruits}. Кол-во фруктов: {Fr_len}")

import math

# part_1_1 = math.cos(math.pi/3) + math.log2(16)
# part_1_2 = sum([math.factorial(n) + 1 for n in range(0,4)])
# part_1 = part_1_1 * part_1_2
# print(part_1)

# part_2 = (math.sqrt(25) - abs(-5)) ** math.sin(math.pi/2)

# print(part_2)

# part_3 = (3 ** 2 + 4 ** 2) / 5 * (math.tan(0) + 1)

# print(part_3)

# result = part_1 + part_2 - part_3
# print(result)

# import random

# life = 5
# rand_num = random.randint(1,50)
# isWin = False

# print("Было закадано число от 1 до 50, Попробуй угадать!")
# while life != 0:
#     num = int(input("Введите число: "))

#     if num == rand_num:
#         print("Вы победили!")
#         isWin = True
#         break

#     elif num < rand_num:
#         print("Загаданное число больше.")
#         life -= 1

#     elif num > rand_num:
#         print("Загаданное число меньше.")
#         life -= 1
# if(not isWin):
#     print("Вы проиграли!")

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