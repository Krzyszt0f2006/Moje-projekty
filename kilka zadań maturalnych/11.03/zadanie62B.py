liczby = []
with open('liczby2.txt') as plik2:
    for liczba2 in plik2:
        liczba2=liczba2.rstrip()
        liczba2=int(liczba2)
        liczby.append(liczba2)
najdluzszy_ciag = 0
poprzedni_ciag = 0
ostatni = 0

for i in range(1, len(liczby)):
    if liczby[i - 1] < liczby[i]:
        najdluzszy_ciag += 1
    else:
        if najdluzszy_ciag > poprzedni_ciag:
            poprzedni_ciag = najdluzszy_ciag
            ostatni = i - 1
        najdluzszy_ciag = 0

print(poprzedni_ciag + 1)
print(liczby[ostatni - poprzedni_ciag])