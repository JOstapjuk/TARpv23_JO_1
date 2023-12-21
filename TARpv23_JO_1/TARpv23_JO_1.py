#1
#print("Hello world!")
#name=input("What is your name? ")
#age=int(input("How old are you? ")) #float()->2.5
#print("Tere tulemast! "+name+". Sa oled "+str(age)+" aastat vana")
#print("Tere tulemast!",name,".Sa oled",age,"aastat vana")
#print("Tere tulemast! {0}. Sa oled {1} aastat vana".format(name,age))
#print("Muutuja vanus=",age,",tüüp on",type(age))
#2
#vanus = 18
#eesnimi = "Jaak"
#pikkus = 16.5
#kas_käib_koolis = True
#print("Muutuja vanus=",vanus,",tüüp on",type(vanus))
#print("Muutuja vanus=",eesnimi,",tüüp on",type(eesnimi))
#print("Muutuja vanus=",pikkus,",tüüp on",type(pikkus))
#print("Muutuja vanus=",kas_käib_koolis,",tüüp on",type(kas_käib_koolis))
#3
from random import *
candies=randint(10,100)
    print("Candies: ",candies)
    mitu=int(input("How many candies you want to take?"))
    candies-=mitu
    print("On the table",candies,"candies")
