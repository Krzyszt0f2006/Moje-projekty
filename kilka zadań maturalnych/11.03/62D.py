zlicz=0
zlicz_osemkow=0
with open('liczby2.txt') as plik2:
    for liczba2 in plik2:
        liczba2=liczba2.rstrip()
        zlicz+=int(liczba2.count('6'))
        liczba2=str(oct(int(liczba2)))
        zlicz_osemkow+=int(liczba2.count('6'))
print(zlicz)
print(zlicz_osemkow)

