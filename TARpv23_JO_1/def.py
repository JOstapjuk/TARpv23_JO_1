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
while True:
    arv1=int(input("Siseta arv number 1: "))
    arv2=int(input("Siseta arv number 2: "))
    operatsion=input("Millist funktsiooni soovite kasutada? + / - / * / / /")
    result=arithmetic(arv1,arv2,operatsion)
    print(result)