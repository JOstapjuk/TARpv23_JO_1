##1 Sõna/Lause
from string import *
v=k=m=t=0
vokaali=["e","u","i","o","ü","õ","a","ö","ä",]
konsonanti="qwrtpsdfghjklzxcvbnm"
märkid=punctuation
lause=input("Kirjuta sõna või lause:\n").lower() #"ABCD!"->"abcd!"
lause_list=list(lause) #["a","b","c","d","!"]
for sümbol in lause_list:
   if sümbol in vokaali:
       v+=1
   elif sümbol in konsonanti:
       k+=1
   elif sümbol in märkid:
       m+=1
   else: #elif sümbol==" ":
       t+=1
print("Vokaali: ",v)
print("Konsonanti: ",k)
print("Märkid: ",m)
print("Tühikud: ",t)
#2 Loetelu
nimed=[]
for i in range(5):
   nimi=input("Siseta nimi: ").capitalize()
   nimed.append(nimi)
nimed.sort()
print("Nimed tähestikulises järjekorras:", nimed)
for n in range(len(nimed)):
   print(n+1,".",nimed[n],sep="") #sep убирает пробелы между 1. 2. 3.
print("Viimati lisatud nimi: ",nimi) #последнее имя храниться в переменной nimi
uued_nimed=[]
for nimi in nimed:
   if nimi not in uued_nimed:
       uued_nimed.append(nimi)
print(uued_nimed)
                                                #uued_nimed=list(set(nimed))
                                                #print(uued_nimed)
uus_nimi=input("Siseta uus nimi: ")
nimed.append(uus_nimi)
nimed.sort
print("Uue nimega nimekiri: ",nimed)
õpilased=['Juhan','Kati','Mario','Mario','Mati','Mati']
õpilased=1
print("Kordusteta nimekiri: ",õpilased)
vanused=[]
for i in range(5):
   vanus=int(input("Siseta vanus: "))
   vanused.append(vanus) #lisame andmed järjendisse
maksimum=max(vanused)
minimum=min(vanused)
summa=sum(vanused)
keskmine=summa/len(vanused)
print("maksimum arv on: ",maksimum,"\nminimum arv on: ",minimum,"\nsumma on: ",summa,"\nkeskmine on: ",keskmine)
#kuva ekraanile nimi koos vanusega
for i in range(5):
   print(nimed[i]," on ", vanused[i]," aastat vana")
##3 Tärnid
from random import *
arvud=[]
N=int(input("Mitu rida joonistame? "))
S=input("Sisesta sümbol: ")
#loendi täitmine
for p in range(N):
   arvud.append(randint(1,100))
#diagrammi loomine
for p in range(N):
   print(arvud[p]*S)
#4 Postiindex
postindx=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
while True:
   while True:
       try:
           indx=int(input("Siseta index: "))
           #if 10000<=indx<=99999:
           indx_elemendide_arv=len(str(indx))
           if indx_elemendide_arv==5:
               break
           else:
               print("On vaja 5 numbriline arv(index)")
       except:
           print("Vale andmetüüp")
   symbolid=list(str(indx))
   syml=symbolid[0]
   print(syml)
   print(f"Sa elad piirkonnas {Indx[int(symbolid[0])-1]}")
   if syml==1 and syml=2 and syml==3:
       print("Оставайтесь дома!")
   else:
       print("Носите маски!")
#5 Vahetus
from random import *
from string import * 
rida=[]
N=randint(2,25)
for i in range(N):
   rida.append(choice(ascii_uppercase))
print(rida)
kogus=int(input("Mitu elemendi vahetame ome vahel "))
if len(rida)//2>=kogus:
   for i in range(kogus):
       a=rida[i]
       rida[i]=rida[len(rida)-i-1]
       rida[len(rida)-1-i]=a
print(rida)
#6 Бесполезное число
from random import *
num=[]
for i in range(10):
   arv=randint(1,50)
   num.append(arv)
print(num)
maksimum=max(num)
print(maksimum)
d=maksimum/len(num)
print(d)
maxindx=num.index(maksimum)
num[maxindx]=d
print(num)
1v for
from random import *
from string import *
from time import sleep
for i in range(100):
   print("#",end="")
   sleep(random())
print()
#7 Sorteerimine
num=[]
for i in range(6):
   num_ask=int(input("Siseta number: "))
   num.append(num_ask)
kahaneva_järgi=sorted(num)
kasvava_järgi=sorted(num,reverse=True)
print("kahaneva järgi on: ",kahaneva_järgi)
print("kasvava järgi on: ",kasvava_järgi)
#8 Võrdsepikkusega elemendid


#9 Nimi kontroll
nimi_list=[]
nimi = input("Sisesta oma nimi: ")
nimi_list.append(nimi)

if nimi.isalpha():
    print("Tere, ", nimi.capitalize())

    num_tähed = len(nimi)
    print("Tähtede arv teie nimes: ", num_tähed)

    vokaalid = 0
    konsonandid = 0
    for letter in nimi.lower():
        if letter in 'euioüõaöä':
            vokaalid += 1
        elif letter.isalpha():
            konsonandid += 1 
else:
    print("Nimi peab sisaldama ainult tähti.")
    

    print("Vokaalide arv teie nimes: ", vokaalid)
    print("Konsonantide arv teie nimes:", konsonandid)
    
sümbolid = sorted(nimi.lower())

unikaalsed_tähted = sorted(set(sümbolid))
print("Sinu nimetähed tähestikulises järjekorras: ", unikaalsed_tähted)
#10 

#11

#12
from random import *
numbers = []
for i in range(10):
    numbers.append(randint(1, 100))
print("Lähtenimekiri:", numbers)
min_väärtus = min(numbers)
max_väärtus = max(numbers)
numbers[0] = min_väärtus
numbers[-1] = max_väärtus

print("Loetelu pärast minimaalse ja maksimaalse väärtuse asendamist:", numbers)

#13
euroopa_pealinnad = ["Pariis","London","Berliin","Madrid","Rooma","Amsterdam","Tallinn","Stockholm","Oslo","Riga"]
euroopa_pealinnad.sort()

index = 1
for i in euroopa_pealinnad:
    print(f"{index}. {i}")
    index += 1
    
uus_pealinnad = []
for _ in range(2):
    pealinn = input("Sisesta uue Euroopa pealinna nimi: ")
    uus_pealinnad.append(pealinn)

euroopa_pealinnad.extend(uus_pealinnad)

euroopa_pealinnad.sort()

print("Uuendatud järjestus: ")
index = 1
for i in euroopa_pealinnad:
    print(f"{index}. {i}")
    index += 1
    
kokku_pealinnad = len(euroopa_pealinnad)
print(f"Meie edetabelis on {kokku_pealinnad} Euroopa pealinnad.")

#14
from random import *

vastused = ["Jah, kindlasti!", "Jah!", "Võib-olla!", "Ei!"]

print("Teid tervitab programm 'Maagiline pall 8'")
print("Küsi jah/ei küsimus ja ma annan sulle vastuse.")

while True:
    küsimus = input("Esitage oma küsimus (kui soovite programmi töö lõpetada, kirjutage 'stop'): ")

    if küsimus.lower() == "stop":
        print("Head päeva!")
        break

    vastus = choice(vastused) # https://www.w3schools.com/python/ref_random_choice.asp -ссылка с которой я узнала эту функцию
    print("Vastus:", vastus)

#16
jarjend = ["kodu", "taldrik", "coca-cola", "pall", "õpik", "telefon", "arvuti", "pilt"]

otsingusona = input("Sisesta otsitav sõna: ")

if otsingusona in jarjend:
   print(f"See sõna nimekirjas on")
else:
   print("Seda sõna nimekirjas ei ole")

17 Kasino
from time import sleep
from random import choice, random

num = ["1", "2", "3", "4", "5", "6"]
mängija_pank = 100
print("Tere tulemast kasiinosse! Teie eesmärk on ära arvata arv 1 kuni 6.")

while True:
    if mängija_pank <= 0:
        print("Teil on raha otsas. Mäng on läbi!")
        break

    print(f"Teil on {mängija_pank} münte.")

    while True:
        panus = input("Kui palju sa tahad panustada? ")
        if panus.isdigit():
            panus = int(panus)
            if 0 < panus <= mängija_pank:
                break
            else:
                print("Palun sisestage number 1 kuni", mängija_pank)
        else:
            print("Palun sisestage terve positiivne arv.")

    kasiino_näitas = choice(num)
    for i in range(10):
        print("*", end="")
        sleep(random())
    print("\nKasiino viskas kondi välja.")

    while True:
        mängija_valik = input("Vali number 1 kuni 6: ")
        if mängija_valik.isdigit():
            mängija_valik = int(mängija_valik)
            if 1 <= mängija_valik <= 6:
                break
            else:
                print("Palun vali arv 1 kuni 6.")
        else:
            print("Palun sisestage täisarv.")

    if mängija_valik == int(kasiino_näitas):
        print("Palju õnne! Sa võitsid", panus * 2, "münt!")
        mängija_pank += panus
    else:
        print("Kahjuks sa kaotasid", panus, "münt.")
        mängija_pank -= panus

    mängida_uuesti = input("Tahad veel mängida? (jah/ei): ")
    if mängida_uuesti.lower() != 'jah':
        print("Aitäh mängu eest! Teie lõpppank on", mängija_pank, "münt.")
        break
