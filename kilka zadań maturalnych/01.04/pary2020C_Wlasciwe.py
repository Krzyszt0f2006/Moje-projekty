wynik='a'
def wartosc(a):
    suma=0
    for literka in a:
        literka=int(ord(literka))
        suma+=literka
    if suma==312:
        global wynik
        wynik=a
    return suma
tab=[]
with open('pary.txt') as plik:
    for liczba in plik:
        liczba=liczba.strip().split()
        if int(liczba[0])==len(liczba[1]):
            liczba[0]=int(liczba[0])
            tab.append(liczba)
#posortowanie tablicy
print(tab)
for element in tab:
    if element[0]>3:
        tab.remove(element)
print(tab)
print('Teraz tylko ktora ma mniejsza wartosc')
for element in tab:
    element[1]=wartosc(element[1])
#    print(element[1])
print(tab)
for element in tab:
    if element[1]>312:
        tab.remove(element)
print(tab)
print(tab[2])
tab[2][1]=wynik
print(tab[2])