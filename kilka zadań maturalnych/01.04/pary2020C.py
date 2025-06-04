wynik='a'
def wartosc(a):
    suma=0
    for literka in a:
        literka=int(ord(literka))
        suma+=literka
    if suma==312:
        wynik=a
    return suma

tab=[]
with open('przyklad.txt') as plik:
    for liczba in plik:
        liczba=liczba.strip().split()
        if int(liczba[0])==len(liczba[1]):
            liczba[0]=int(liczba[0])
            tab.append(liczba)
#posortowanie tablicy
print(tab)
for element in tab:
    if element[0]>6:
        tab.remove(element)
print(tab)
print('Teraz tylko ktora ma mniejsza wartosc')
if wartosc(tab[0][1])<wartosc(tab[1][1]):
    print(tab[0])
else:
    print(tab[1])
#Dostosowac program do pliku pary
print('-------------------------------------------------')
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
tab[2][1]=wynik`
print(tab[2])