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
eesnimi=input("Mis on sinu nimi? ").capitalize()
print("Tere",eesnimi)
if eesnimi=="Juku":
    print("Lähme kinno")
    vanus=int(input("Kui vana sa oled? "))
    if  vanus<0 or vanus>100:
        tulemus="viga andmetega"
    elif vanus<6:
        tulemus="Sinu pilet on tasuta"
    elif vanus<=14:
        tulemus="Sinu pilet on lastepilet"
    elif vanus<=65:
        tulemus="Sinu pilet on täispilet"
    elif vanus<=100:
        tulemus="sinu pilet on sooduspilet"
    print(tulemus) #Ilus ja õige vastus!"Vale vanus" või "On vaja osta"
else:
    print("Ma ootan Jukut")