najwieksza=0
najmniejsza=741240
with open('liczby1.txt') as plik1, open('liczby2.txt') as plik2:
    for liczba1, liczba2 in zip(plik1, plik2):
        liczba1=liczba1.rstrip()
        liczba2=liczba2.rstrip()
        liczba1 = int(liczba1)
        if liczba1>najwieksza:
            najwieksza=liczba1
        if liczba1<najmniejsza:
            najmniejsza=liczba1
print(najwieksza)
print(najmniejsza)