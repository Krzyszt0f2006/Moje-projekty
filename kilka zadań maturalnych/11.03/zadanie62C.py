taka_sama=0
wieksza=0
with open('liczby1.txt') as plik1, open('liczby2.txt') as plik2:
    for liczba1, liczba2 in zip(plik1, plik2):
        liczba1=liczba1.rstrip()
        liczba2=liczba2.rstrip()
        liczba1=int(liczba1, 8)
        liczba2=int(liczba2)
        if liczba1==liczba2:
            taka_sama+=1
        if liczba1>liczba2:
            wieksza+=1
print(taka_sama)
print(wieksza)