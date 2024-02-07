from audioop import reverse
from random import * 
nimed=["Mati","Meelis","Kati","Mati"]
while True:
    print("**************")
    v=input("N-näita andmed\nL-lisada andmeid\nK-andmete kustutamine\nH-andmete haldus\nI-positsiooni otsing\n")
    if v=="N":
        v=input("Kas juhslik nimi(j) või terve loetelu(t)?")
        if v=="t":
            print(nimed)
        elif v=="j":
            print(choice(nimed))
    elif v=="L":
        v=input("Kas nimekirja lõppu(l) või positsionile(p)?")
        if v=="l":
            nimi=input("Sisesta nimi: ")
            nimed.append(nimi)
        elif v=="p":
            nimi=input("Sisesta nimi: ")
            ind=int(input("Mis kohale: "))
            nimed.insert(ind-1,nimi)
    elif v=="K":
        v=input("Kas nimi järgi(n), indeksi järgi(i) või kõike nimed(k)?")
        if v=="i":
            ind=int(input("Sisesta indeks: "))
            nimed.pop(ind-1)
        elif v=="k":
            nimed.clear()
        elif v=="n":
            nimi=input("Sisesta nimi: ")
            mitu=nimed.count(nimi)
            if mitu>0:
                if mitu>1:
                    ind=-1
                    indlist=[]
                    for e in nimed:
                        ind+=1
                        if e==nimi:
                            indlist.append(ind)
                    print(indlist)
                    v=int(input("Mis index?"))
                    nimed.pop(v)
                else:
                    nimed.remove(nimi)
            else:
                print(nimi," ei ole loetelus")
    elif v=="H":
        v=input("Sorteerimine(s), kopeerimine(k) või ümber pööramine(p)")
        if v=="s":
            v=int(input("A-z(1) või Z-a?(2)"))
            if v==1:
                nimed.sort()
            elif v==2:
                nimed.sort(reverse=True)
        elif v=="k":
            nimed.copy()
        elif v=="p":
            nimed.reverse()
    elif v=="I":
        nimi=input("Siseta nimi: ")
        mitu=nimed.count(nimi)
        print("Kui palju inimesi selle nimega: ",mitu)
        if mitu>1:
            indeks=[]
            sindeks=-1
            for i in range(mitu):
                sindex=nimed.index(nimi,sindex+1)
                indeks.append(sindex)
             print("Mis nende indeks on: ",indeks)
        else:
            indeks=nimed.index(nimi)
            print("Mis tema indeks on: ",indeks)
        print("Mis tema/nende indeks on: ",ind)