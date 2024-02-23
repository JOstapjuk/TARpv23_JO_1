from MyModul import * #Summa as s
#1
#b=int(input("Siseta arv2: "))
#summa_3=Summa(3,b,int(input("Kolmas arv: ")))
#summa_31=Summa(100,100)

#print(summa_3)
#print(summa_31)
#2
#value=input("Siseta number: ")
#value_control=typeControl(value) 
#print(value_control)
#(1)
#while True:
#    arv1=int(input("Siseta arv number 1: "))
#    arv2=int(input("Siseta arv number 2: "))
#    operatsion=input("Millist funktsiooni soovite kasutada? + / - / * / / /")
#    result=arithmetic(arv1,arv2,operatsion)
#    print(result)
#(2)
#while True:
#    try:
#        aasta=int(input("Siseta aasta number: "))
#        break
#    except:
#        print("Viga")
#a=is_year_leap(aasta)
#print(a)
#(3)
#while True:
#    try:
#        a=int(input("Siseta külg: "))
#        break
#    except:
#        print("Viga")
#S,P,d=square(a)
#print(f"S={S}, P={P}, d={d}")
#(4)
while True:
    try:
        kuu=int(input("kuu number: "))
        break
    except:
        print("Viga")
a=season(kuu)
print(a)