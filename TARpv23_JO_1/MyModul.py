﻿def Summa(arv1:int,arv2:int,arv3=0)->int:
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