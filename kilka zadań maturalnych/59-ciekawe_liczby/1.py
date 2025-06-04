import time
czas_1=time.time()
def rozklad_czynniki_unikalne(n):
    czynniki=[]
    d=2
    while n>1:
        if n%d==0:
            if len(czynniki)>=3 or d%2==0:
                return [0]
            czynniki.append(d)
            while n%d==0:
                n=n//d
        else:
            d+=1
    return czynniki
ile=0
with open('liczby.txt') as plik:
    for element in plik:
        element=int(element.rstrip())
        rozklad=rozklad_czynniki_unikalne(element)
        if len(rozklad)==3:
            ile+=1
print("wynik : ",ile)
czas2=time.time()
print("czas : ",czas2-czas_1)