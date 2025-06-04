najmniejsze=[0, 0]
ile=0
with open('liczby.txt') as plik:
    for liczba in plik:
        liczba=liczba.rstrip()
        if int(liczba)<1000:
            ile+=1
            najmniejsze.append(liczba)
            najmniejsze.pop(0)
print(ile)
print(najmniejsze)
