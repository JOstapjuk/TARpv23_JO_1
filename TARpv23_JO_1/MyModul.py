def Summa(arv1:int,arv2:int,arv3=0)->int:
    """ Funktsioon tagastab kolme arvu summa
    Summa(arv1,arv2,arv3)

    :param int arv1: Arv1 sisestab kasutaja
    :param int arv2: Arv2 sisestab kasutaja
    :param int arv3: Vaikimisi arv3 võrdub nulliga
    :rtype: int
    """
    s=arv1+arv2+arv3
    return s

def typeControl() -> any:
    """ Funktsioon kontrollib, millist tüüpi andmed on
        typeControl()
    :rtype: any
    """
    int_1=input("Sisetage andmed")
    try:
        
        return int(int_1)
    except :
        try:
            return float(int_1)
        except:
            return str(int_1)

def arithmetic(arv1:float,arv2:float,operatsion:str)->any:
    """ 3 argumenti: esimesed 2 on numbrid, kolmas on operatsioon, mis tuleb teha nende kohal. 
        arithmetic=(arv1,arv2,operatsion)

        :param float arv1: Arv1 sisestab kasutaja
        :param float arv2: Arv2 sisestab kasutaja
        :param str operatsion: Operatsion sisestab kasutaja + / - / * / "/" /
        :rtype: any

    """
    if operatsion == "+":
        return arv1 + arv2
    elif operatsion == "-":
        return arv1 - arv2
    elif operatsion == "*":
        return arv1 * arv2
    elif operatsion== "/":
        if arv2 !=0:
            return arv1 / arv2
        else:
            return "Nulli ei saa jagada"
    else:
        return "Tundmatu operatsioon"

def is_year_leap(year:int)->bool:
    """ Funktsioon otsustab kas aasta on liigaasta või ei ole
    Tagastab True kui liigasta ja False kui on tavaline aasta 

    :param int year: Aasta sisestab kasutaja
    :rtype: bool
    """
    if year%4==0 and year%100!=0:
        return True
    else:
        return False

from math import *
def square(külg:float)->any:
    """ Funktsioon tagastab 3 värtusi ümbermõt,pindala ja diagonaal
    Tagastab S,P,d

    :param float külg: Ruudukülg sisetab kasutaja
    :rtype: any
    """
    S=külg**2
    P=4*külg
    d=külg*sqrt(2)
    return S,P,d
#4
def season(a:int)->str:
    """ Funktsioon tagastab aastaaega nimi (talv, kevad, suvi или sügis)

    :param int a: Kuu sisetab kasutaja
    :rtype: str
    """
    while True:
        if a>0 and a<13:
            break
        else:
            try:
                a=int(input("Ainult 1-12!\nSiseta veel kord number: "))
            except:
                print("Viga andmetüübiga")
    if a==12 or a==1 or a==2:
        s="Talv"
    elif a>2 and a<6:
        s="Kevad"
    elif a in range(6,9,1):
        s="Suvi"
    elif 9<=a<=11:
        s="Sügis"
    return s

#5
def bank()