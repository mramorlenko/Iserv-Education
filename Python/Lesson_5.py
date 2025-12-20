#Задача 1
# proiz = 1
# PrP = 1
# while(PrP != 0):
#     proiz *= PrP
#     PrP = int(input("Введите число: "))
# print(f"Произведени ваших чисел равна: {proiz}")

#Задача 2
# for i in range(1, 100):
#     if(i % 3 != 0 and i % 5 != 0):
#         print(i, end=" ")

#Задача 3
# Str = str(input("Введите любой текст: "))
# A = int(input("Введите первое число: "))
# B = int(input("Введите второе число: "))

# print(Str[A:B])

#Задача 4
# SRt = str(input("Введите слово палиндром: "))

# tRS = SRt[::-1]
# if(SRt == tRS):
#     print("Да вы ввели палиндром")
# else:
#     print("Это не палиндром")

#Задача 5

SrT = str(input("Введите какое-нибудь предложение: "))
SrT = SrT.replace("!", "")
SrT = SrT.replace(".", "")
SrT = SrT.replace(",", "")
SrT = SrT.replace("?", "")
print(SrT)