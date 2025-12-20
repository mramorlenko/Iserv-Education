#Задача 1

# SRt = "Я люблю какашке"
# count = 1

# while count < 11:
#     print(SRt)
#     count += 1

#Задача 2

# shopping_cost = 20
# money = 110

# while( money > shopping_cost):
#     money -= shopping_cost
#     print("Вы купили товар")

# print(F"У вас осталось {money} деняг")

#Задача 3

# random = 0
# input_number = int(input("Угадай какое число я загадал: "))

# while(input_number != random):
#     print("Не правильно!!!")
#     if(input_number < random):
#         print("Ваше число меньше моего")
#     elif(input_number > random):
#         print("Ваше число больше моего")
#     input_number = int(input("Угадай какое число я загадал: "))

# print("Ура ты угадал!!!")

#Задача 4

# for i in range(0, 51):
#     print(i)

#Задача 5

cifra = int(input("Введите любое число: "))
summa = 0

for i in range(0, cifra + 1):
    summa += i
print(f"Держите: {summa}")

cifra_1 = int(input("Введите любое число: "))
summa_1 = 1

for i in range(0, cifra_1 + 1):
    summa_1 *= i
print(f"Держите: {summa}")