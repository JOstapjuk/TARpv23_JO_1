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
vanused=["14","16","19","10","24","10"]
kokku_vanused=len(vanused)
#keskmine_vanused=sum(vanused)/kokku_vanused