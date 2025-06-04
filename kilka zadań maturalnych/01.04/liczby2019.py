ile=0
import math
def czy_wielkorotnosc(a):
    i=round(math.log(a, 3))
    print(i)
    if 3**i==a:
        return True
    return False
with open('liczby.txt') as plik:
    for liczba in plik:
        liczba=int(liczba.strip())
        if czy_wielkorotnosc(liczba):
            ile+=1
print(ile)
