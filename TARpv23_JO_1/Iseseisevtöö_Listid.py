##1 Sõna/Lause
#from string import *
#v=k=m=t=0
#vokaali=["e","u","i","o","ü","õ","a","ö","ä",]
#konsonanti="qwrtpsdfghjklzxcvbnm"
#märkid=punctuation
#lause=input("Kirjuta sõna või lause:\n").lower() #"ABCD!"->"abcd!"
#lause_list=list(lause) #["a","b","c","d","!"]
#for sümbol in lause_list:
#    if sümbol in vokaali:
#        v+=1
#    elif sümbol in konsonanti:
#        k+=1
#    elif sümbol in märkid:
#        m+=1
#    else: #elif sümbol==" ":
#        t+=1
#print("Vokaali: ",v)
#print("Konsonanti: ",k)
#print("Märkid: ",m)
#print("Tühikud: ",t)
#2 Loetelu
#nimed=[]
#for i in range(5):
#    nimi=input("Siseta nimi: ").capitalize()
#    nimed.append(nimi)
#nimed.sort()
#print("Nimed tähestikulises järjekorras:", nimed)
#for n in range(len(nimed)):
#    print(n+1,".",nimed[n],sep="") #sep убирает пробелы между 1. 2. 3.
#print("Viimati lisatud nimi: ",nimi) #последнее имя храниться в переменной nimi
#uued_nimed=[]
#for nimi in nimed:
#    if nimi not in uued_nimed:
#        uued_nimed.append(nimi)
#print(uued_nimed)
#                                                 #uued_nimed=list(set(nimed))
#                                                 #print(uued_nimed)
#uus_nimi=input("Siseta uus nimi: ")
#nimed.append(uus_nimi)
#nimed.sort
#print("Uue nimega nimekiri: ",nimed)
#õpilased=['Juhan','Kati','Mario','Mario','Mati','Mati']
#õpilased=1
#print("Kordusteta nimekiri: ",õpilased)
#vanused=[]
#for i in range(5):
#    vanus=int(input("Siseta vanus: "))
#    vanused.append(vanus) #lisame andmed järjendisse
#maksimum=max(vanused)
#minimum=min(vanused)
#summa=sum(vanused)
#keskmine=summa/len(vanused)
#print("maksimum arv on: ",maksimum,"\nminimum arv on: ",minimum,"\nsumma on: ",summa,"\nkeskmine on: ",keskmine)
##kuva ekraanile nimi koos vanusega
#for i in range(5):
#    print(nimed[i]," on ", vanused[i]," aastat vana")
##3 Tärnid
#from random import *
#arvud=[]
#N=int(input("Mitu rida joonistame? "))
#S=input("Sisesta sümbol: ")
##loendi täitmine
#for p in range(N):
#    arvud.append(randint(1,100))
##diagrammi loomine
#for p in range(N):
#    print(arvud[p]*S)
#4 Postiindex
#postindx=["Tallinn","Narva, Narva-Jõesuu","Kohtla-Järve","Ida-Virumaa, Lääne-Virumaa, Jõgevamaa","Tartu linn","Tartumaa, Põlvamaa, Võrumaa, Valgamaa","Viljandimaa, Järvamaa, Harjumaa, Raplamaa","Pärnumaa","Läänemaa, Hiiumaa, Saaremaa"]
#while True:
#    while True:
#        try:
#            indx=int(input("Siseta index: "))
#            #if 10000<=indx<=99999:
#            indx_elemendide_arv=len(str(indx))
#            if indx_elemendide_arv==5:
#                break
#            else:
#                print("On vaja 5 numbriline arv(index)")
#        except:
#            print("Vale andmetüüp")
#    symbolid=list(str(indx))
#    syml=symbolid[0]
#    print(syml)
#    print(f"Sa elad piirkonnas {Indx[int(symbolid[0])-1]}")
#    if syml==1 and syml=2 and syml==3:
#        print("Оставайтесь дома!")
#    else:
#        print("Носите маски!")
#5 Vahetus
#from random import *
#from string import * 
#rida=[]
#N=randint(2,25)
#for i in range(N):
#    rida.append(choice(ascii_uppercase))
#print(rida)
#kogus=int(input("Mitu elemendi vahetame ome vahel "))
#if len(rida)//2>=kogus:
#    for i in range(kogus):
#        a=rida[i]
#        rida[i]=rida[len(rida)-i-1]
#        rida[len(rida)-1-i]=a
#print(rida)
#6 Бесполезное число
#from random import *
#num=[]
#for i in range(10):
#    arv=randint(1,50)
#    num.append(arv)
#print(num)
#maksimum=max(num)
#print(maksimum)
#d=maksimum/len(num)
#print(d)
#maxindx=num.index(maksimum)
#num[maxindx]=d
#print(num)
#1v for
#from random import *
#from string import *
#from time import sleep
#for i in range(100):
#    print("#",end="")
#    sleep(random())
#print()
#7 Sorteerimine
#num=[]
#for i in range(6):
#    num_ask=int(input("Siseta number: "))
#    num.append(num_ask)
#kahaneva_järgi=sorted(num)
#kasvava_järgi=sorted(num,reverse=True)
#print("kahaneva järgi on: ",kahaneva_järgi)
#print("kasvava järgi on: ",kasvava_järgi)
#8 Võrdsepikkusega elemendid

#9 Nimi kontroll
#try:
    täht=["e","u","i","o","ü","õ","a","ö","ä","q","w","r","t","y","p","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]
    nimi=input("Siseta oma nime: ").lower
    nimi_list=list(nimi)
    for i in nimi_list:
        if nimi 
except ValueError:
    print("Nimi peab koosnema tähtedest.")
#10 

#11

