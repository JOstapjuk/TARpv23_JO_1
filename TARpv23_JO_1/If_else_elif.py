##1 if
#print("Tund on alanud")
#hilinemine=input("Kas õpilane on hilinenud?") 
## "JAH"-a.upper(), "jah"-a.lower(), "Jah"-capitalize() ,jAH
#if hilinemine.upper()=="JAH":
#    print("Õpilane ootab 30 min")
#print("Õpilane astub klassi")
##2 if else
from random import *
#arv=randint(0,100) #juhuslik täisarv vahemikust 0...100
#if arv%2==0:
#    print(arv,"on paaris arv")
#else:
#    print(arv,"on paaritu arv")
#print()
##3 if elif
#protsent=randint(-100,500) #0...100 0-59-"2",61-74-"3", 75-89-"4", 90-100-"5"
#print(protsent,"% on testi tulemus")
#if protsent<0 or protsent>100:
#    tulemus="valed andmed"
#elif protsent<60:#protsent>0 and protsent<60; 0<protsent<60
#    tulemus="hinne 2"
#elif 60<=protsent<75:
#    tulemus="hinne 3"
#elif 75<=protsent<90:
#    tulemus="hinne 4"
#else: #elif 90<=protsent<=100: 
#    tulemus="hinne 5"
#print(tulemus)
#print()

#1 Juku läheb kinno
# eesnimi=input("Mis on sinu nimi? ").capitalize()
# print("Tere",eesnimi)
# if eesnimi=="Juku":
#     print("Lähme kinno")
#     vanus=int(input("Kui vana sa oled? "))
#     if  vanus<0 or vanus>100:
#         tulemus="viga andmetega"
#     elif vanus<6:
#         tulemus="Sinu pilet on tasuta"
#     elif vanus<=14:
#         tulemus="Sinu pilet on lastepilet"
#     elif vanus<=65:
#         tulemus="Sinu pilet on täispilet"
#     elif vanus<=100:
#         tulemus="sinu pilet on sooduspilet"
#     print(tulemus) #Ilus ja õige vastus!"Vale vanus" või "On vaja osta"
# else:
#     print("Ma ootan Jukut")
#2 Pinginaabrid !!!!
# Kasutajate nimed
# pinginaaber1 = input("Mis on sinu nimi? ")
# pinginaaber2 = input("Mis on sinu nimi? ")
# print(pinginaaber1 +" "+"ja"+" " + pinginaaber2 +" on pinginaabrid täna")
#3 Remont
# pikkus = float(input("Sisesta ruumi pikkus: "))
# laius = float(input("Sisesta ruumi laius: "))
# pindala = pikkus * laius
# print("Ruumi põranda pindala on ",pindala, " ruutmeetrit.")
# remont = input("Kas soovid teha remonti (jah/ei)? ")
# if remont == "jah":
#     ruutmeetr_hind = float(input("Sisesta ruutmeetri hind: "))
#     remont_hind = pindala * ruutmeetr_hind
#     print("Põranda vahetamise hind on ",remont_hind," eurot")
# else:
#     print("Ruumi remonti ei tehta")
#4 Allahindus
# alghind=float(input("Sisesta hind:"))
# if alghind>700:
#     hindprots= alghind*0.3
#     print("Hind on:",hindprots)
# else:
#     print("Allahindlust teil ei tule. Teie hind jääb samaks")
#5 Temperatuur
# kraade=float(input("Kui palju on praegu kraade? "))
# if kraade<18:
#     print("Temperatuur on liiga madal")
# else:
#     print("Temperatuur on normaalne")
#6 Pikkus
# pikkus=float(input("Kui pikk te olete? "))
# if pikkus<165:
#     print("Teil on lühike kasv")
# elif 165<=pikkus<=180:
#     print("Teil on keskmine kasv")
# elif pikkus>180:
#     print("Teil on pikk kasv")
#7
# sugu=input("Mis teile sugu on? (naine/mees): ")
# pikkus=float(input("Kui pikk te olete? "))
# if sugu=="naine":
#     if pikkus<165:
#         print("Teil on lühike kasv")
#     elif 165<=pikkus<=180:
#         print("Teil on keskmine kasv")
#     else:
#         print("Teil on pikk kasv")
# elif sugu=="mees":
#     if pikkus<170:
#         print("Teil on lühike kasv")
#     elif 170<=pikkus<=185:
#         print("Teil on keskmine kasv")
#     else:
#         print("Teil on pikk kasv")
# else:
#     print("Palun sisesta kehtiv sugu (mees või naine)")
#8 Poes !!!!

#9 Ruut
# kulg1 = float(input("Sisesta esimese ruudu külje pikkus: "))
# kulg2 = float(input("Sisesta teise ruudu külje pikkus: "))
# if kulg1 > 0 and kulg2 > 0:
#     if kulg1 == kulg2:
#         print("Tegemist on ruuduga")
#     else:
#         print("Need küljepikkused ei moodusta ruutu")
# else:
#     print("Palun sisesta kehtivad küljepikkused")
#10 Matemaatika
# Küsi kasutajalt kaks arvu
# arv1 = float(input("Sisesta esimene arv: "))
# arv2 = float(input("Sisesta teine arv: "))
# teha = input("Vali tehe (+, -, *, /): ")
# if teha == "+":
#     tulemus = arv1 + arv2
#     print(arv1,"+",arv2,"=",tulemus)
# elif teha == "-":
#     tulemus = arv1 - arv2
#     print(arv1,"-",arv2,"=",tulemus)
# elif teha == "*":
#     tulemus = arv1 * arv2
#     print(arv1,"*",arv2,"=",tulemus)
# elif teha == "/":
#     if arv2 == "0":
#         print("Nulliga jagamine ei ole lubatud")
#     else:
#         tulemus = arv1 / arv2
#         print(arv1,"/",arv2,"=",tulemus)
# else:
#     print("Palun sisesta kehtiv tehe (+, -, *, /).")
#11 Juubel !!!!

#12 Müük
# toote_hind = float(input("Sisesta toote hind eurodes: "))
# if toote_hind <= 10:
#     allahind_summa = toote_hind * 0.1
#     lõpphind = toote_hind - allahind_summa
#     print("Allahindlusega summa: ",lõpphind)
# elif toote_hind > 10:
#     allahind_summa = toote_hind * 0.2
#     lõpphind = toote_hind - allahind_summa
#     print("Allahindlusega summa: ",lõpphind)
# else:
#     print("Palun sisesta kehtiv hind.")
#13 Jalgpalli meeskond
# Küsi kandideerijalt soo
# sugu = input("Sisesta oma sugu (mees/naine): ")
# if sugu == "mees":
#     vanus = int(input("Sisesta oma vanus: "))
#     if 16 <= vanus <= 18:
#         print("Sobite meeskonda!")
#     else:
#         print("Vabandage, kandideerimiseks peab olema 16-18 aastat vana")
# elif sugu == "naine":
#     print("Vabandame, hetkel otsime ainult meeskonda")
# else:
#     print("Palun sisesta kehtiv sugu (mees või naine)")
#14 Busside logistika !!!!
# inimeste_arv = int(input("Sisesta inimeste arv: "))
# bussi_kohtade_arv = int(input("Sisesta bussi kohtade arv: "))
# busside_arv = round(inimeste_arv / bussi_kohtade_arv,0)
# järelejäänud_inimesed = 
# if järelejäänud_inimesed > 0:
#     print("Vaja on",busside_arv+1, " bussi. Viimases bussis on",järelejäänud_inimesed, "inimest")
# else:
#     print("Vaja on",busside_arv, " bussi. Kõik inimesed mahuvad ühte bussi")