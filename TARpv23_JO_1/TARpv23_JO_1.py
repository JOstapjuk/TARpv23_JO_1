#1
# print("Hello world!")
# name=input("What is your name? ")
# age=int(input("How old are you? ")) #float()->2.5
# print("Tere tulemast! "+name+". Sa oled "+str(age)+" aastat vana")
# print("Tere tulemast!",name,".Sa oled",age,"aastat vana")
# print("Tere tulemast! {0}. Sa oled {1} aastat vana".format(name,age))
# print("Muutuja vanus=",age,",tüüp on",type(age))
#2
# vanus = 18
# eesnimi = "Jaak"
# pikkus = 16.5
# kas_käib_koolis = True
# print("Muutuja vanus=",vanus,",tüüp on",type(vanus))
# print("Muutuja vanus=",eesnimi,",tüüp on",type(eesnimi))
# print("Muutuja vanus=",pikkus,",tüüp on",type(pikkus))
# print("Muutuja vanus=",kas_käib_koolis,",tüüp on",type(kas_käib_koolis))
# #3
# from random import *
# candies=randint(10,100)
# print("Candies: ",candies)
# mitu=int(input("How many candies you want to take?"))
# candies-=mitu
#4
# import math
# obhvat = float(input("Sisesta puu ümbermõõt sentimeetrites: "))
# diametr = obhvat/math.pi
# print(f"Диаметр дерева: {diametr:.1f} см")
#5
# N = float(input("Sisesta krundi pikkus meetrites (N): "))
# M = float(input("Sisesta krundi laius meetrites (M): "))
# diagonal_dlinna =(N**2 + M**2)
# print(f"Krundi diagonaali pikkus: {diagonal_dlinna:.1f} meeter")
#6
# aeg = float(input("Mitu tundi kulus sõiduks? "))
# teepikkus = float(input("Mitu kilomeetrit sõitsid? "))
# kiirus = aeg / teepikkus

# print("Sinu kiirus oli " + str(kiirus) + " km/h")
#7
# arv_1 = int(input("Sisesta esimene täisarv: "))
# arv_2 = int(input("Sisesta teine täisarv: "))
# arv_3 = int(input("Sisesta kolmas täisarv: "))
# arv_4 = int(input("Sisesta neljas täisarv: "))
# arv_5 = int(input("Sisesta viies täisarv: "))
# keskmine = (arv_1 + arv_2 + arv_3 + arv_4 + arv_5) / 5
# print(f"Aritmeetiline keskmine on: {keskmine}")
#8
# print("   @..@")
# print("  (----)")
# print(" ( \\__/ )")
# print(" ^^ \"\" ^^")
#9
# a = int(input("Sisesta esimese külje pikkus a: "))
# b = int(input("Sisesta teise külje pikkus b: "))
# c = int(input("Sisesta kolmanda külje pikkus c: "))
# umbermoot = a + b + c
# print(f"Kolmnurga ümbermõõt on: {umbermoot}")
#10
# pitsa_hind = 12.90
# jootraha_protsent = 10
# jootraha = (jootraha_protsent / 100) * pitsa_hind
# kogusumma = pitsa_hind + jootraha
# inimesi = 2
# maksma_kazdi = kogusumma / inimesi
# print(f"Igaüks peab maksma {maksma_kazdi:.2f} eurot.")