import math
#ZAD 1
przyklad1 = math.e
print(przyklad1**10)
przyklad2=(math.log(5+(math.sin(8))**2))**(1/6)
print(przyklad2)
print(math.floor(3.55))
print(math.ceil(4.80))
#ZAD 2
imie="BARTŁOMIEJ"
nazwisko="LIS"
print(imie.capitalize()+ " " + nazwisko.capitalize())
#ZAD 3
piosenka="la la la la la la la la"
print(piosenka.count("la"))
#ZAD 4
print(imie[1]+" "+imie[len(imie)-1])
#ZAD 5 i 6
slowa="Urodzony Polakiem jednak to przez mój wybór zostałem kierowcą tira"
liczba=3912.123567
liczba16=0xd0cd
print(slowa.split())
print(slowa)
print(liczba)
print(hex(liczba16))
#ZAD 7
sporty=["piłka nożna", "koszykówka","siatkówka"]
sporty.reverse()
sporty.extend(["golf", "hokej", "łyżwiarstwo"])
print(sporty)
#ZAD 8
skroty={"zw":"zaraz wracam","jj":"już jestem","kc":"kocham cię","cze":"cześć"}
print(skroty)
#ZAD 9
slownik={"GOTHIC":["RPG","SINGLEPLAYER","2001"],"DAWN OF WAR":["STRATEGIA","SINGLEPLAYER/MULTIPLAYER","2004"],"DRUG DEALER SIMULATOR":["SYMULATOR","SINGLEPLAYER",'2020']}
print(len(slownik))
#ZAD 10
zdanie=input()
print(zdanie.count("a"))
#ZAD 11
print("PODAJ a: ")
a=input()
a=int(a)
print("PODAJ b: ")
b=input()
b=int(b)
print("PODAJ c: ")
c=input()
c=int(c)
if(a>b and a>c):
    print("Najwieksza jest liczba "+str(a))
elif(b>a and b>c):
    print("Najwieksza jest liczba "+str(b))
else:
    print("Najwieksza jest liczba "+str(c))
#ZAD 12
rozneliczby=[1,2.5,3,4.5,5,6.5,7,8]
for i in range(len(rozneliczby)):
    print(rozneliczby[i]**2)
#ZAD 13
parzyste=[]
liczbap=""
licznik=0
while licznik!=10:
    liczbap=input()
    liczbap=int(liczbap)
    if(liczbap%2==0 and liczbap!=0):
        parzyste.append(liczbap)
    licznik+=1
print(parzyste)