def silnia(a):
    wartosc=1
    for i in range(1, a+1):
        wartosc=wartosc*i
    return wartosc
def suma_cyfr(b):
    suma = 0
    while b > 0:
        suma +=silnia(b % 10)
        b //= 10
    return suma
#print(suma_cyfr(12))
#print(silnia(4))
with open('liczby.txt') as plik:
    for liczba in plik:
        liczba=int(liczba.strip())
        if suma_cyfr(liczba)==liczba:
            print(liczba)