# def sum_squares_nums(list):
#     n_list = []
#     for i in list:
#         n_list.append(i ** 2)

#     result = sum(n_list)
#     return result

# list1 = [23, 57, 13, 67, 75]

# result = sum_squares_nums(list1)
# print(result)
# #----------------------------

# list2 = [14, 49, 49, 6, 64]

# result = sum_squares_nums(list2)
# print(result)
# #----------------------------

# list3 = [8, 90, 55, 83, 1, 22]

# result = sum_squares_nums(list3)
# print(result)

# import random
# import string

# def passward_generation(lenPas, isNumms, isUpAlfa):
#     symbols = string.ascii_lowercase
#     password = ""

#     if isUpAlfa:
#         symbols += string.ascii_uppercase
#     if isNumms:
#         symbols += "1234567890"
    

#     for _ in range(lenPas):
#         password += random.choice(symbols)

#     return password

# print("---Программа для генерации пароля---")
# lenPas = int(input("Введите длину пароля: "))
# isNumms = input("Нужны ли цифры в пароле? Y/n: ")
# isUpAlfa = input("Нужны ли заглавные буквы в пароле? Y/n: ")

# if isNumms.lower() == "y":
#     isNumms = True
# else:
#     isNumms = False

# if isUpAlfa.lower() == "y":
#     isUpAlfa = True
# else:
#     isUpAlfa = False

# password = passward_generation(lenPas, isNumms, isUpAlfa)
# print(password)

# def isEven(number):

#     if number % 2 == 0:
#         return True
#     if number % 2 != 0:
#         return False

# def CountVoulsSymbols(text):
#     voelSymbols = "аеуоюияы"
#     count = 0
#     for i in text:
#         if voelSymbols.count(i) > 0:
#             count += voelSymbols.count(i)

#     return count

# def SummaCifrChisla(num):
#     strin = str(num)

#     summ = 0

#     for i in strin:
#         summ += int(i)
#     return summ

# print(SummaCifrChisla(781))
