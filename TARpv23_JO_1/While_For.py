﻿
#1 Вводят 15 чисел. Определить, сколько среди них целых.

#2 Запросите у пользователя число А и найдите сумму всех натуральных чисел от 1 до А.
# A = int(input("sisseta number A: "))
# summa = 0
# schet = 1
# while schet <= A:
#     summa += schet
#     schet += 1
# print("Looduslike numbrite summa 1 kuni ",A,": ", summa)
#3 Вводят 8 чисел. Найти их произведение (только положительных).
# korrutis = 1
# schet = 0
# while schet < 8:
#     arv = float(input("Введите положительное число: "))
    
#     if arv > 0:
#         korrutis *= arv
#         schet += 1
#     else:
#         print("Введено не положительное число. Пожалуйста, введите положительное число.")
# print("Произведение положительных чисел:", korrutis)
#4 Составьте программу, выводящую на экран квадраты чисел от 10 до 20.
# for i in range(10, 21):
#     square = i ** 2
#     print("Numbriruut ",i,":",square)
#5 Составьте программу, которая вычисляет сумму только отрицательных из N чисел. Значение N вводится с клавиатуры.
# N = int(input("Введите количество чисел N: "))
# negativ = 0
# schet = 0
# while schet < N:
#     user_input = float(input("Введите число: "))
#     if user_input < 0:
#         negativ += user_input
#     schet += 1
# print("Сумма отрицательных чисел: ",negativ)
#6 С клавиатуры вводятся N чисел.
# Составьте программу, которая определяет количество отрицательных,
# количество положительных и количество нулей среди введенных чисел.  
# Значение N вводится с клавиатуры.
# N = int(input("Введите количество чисел N: "))
# positive = 0
# negative = 0
# zero = 0
# schet = 0
# while schet < N:
#     andmed = float(input("Введите число: "))
#     if andmed > 0:
#         positive += 1
#     elif andmed < 0:
#         negative += 1
#     else:
#         zero += 1
#     schet += 1
# print("Количество положительных чисел: ", positive)
# print("Количество отрицательных чисел: ", negative)
# print("Количество нулей: ", zero)
#7 !!!!
# A = int(input("Введите начальное значение A: "))
# B = int(input("Введите конечное значение B: "))
# K = int(input("Введите значение K: "))
# print("Числа, кратные",K,", в промежутке от ",A," до ",B,":")
# for number in range(A, B):
#     if number % K == 0:
#         print(number)
#8
# for i in range(1, 21):
#     duim=i*2.5
#     print(i,"дюймов = ",duim)
#9 !!!!
# S = float(input("Введите начальную сумму вклада (в евро): "))
# N = int(input("Введите количество лет: "))
# protsent = 0.3
# while N > 0:
#     summ=S*protsent*N
# print("Сумма вклада через",N,"лет составит: ",summ,"евро")
#10 Ввести с клавиатуры 10 пар чисел.  Сравнить числа в каждой паре и напечатать большие из них.
# schet = 0
# while schet < 10:
#     число1 = float(input("Введите первое число: "))
#     число2 = float(input("Введите второе число: "))
#     if число1 > число2:
#         print("Большее число: ",число1)
#     elif число2 > число1:
#         print("Большее число: ",число2)
#     else:
#         print("Числа равны.")
#     schet += 1