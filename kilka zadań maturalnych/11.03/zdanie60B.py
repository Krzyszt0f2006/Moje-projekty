ile=0
liczby=[]
with open('liczby.txt') as plik:
    for liczba in plik:
        dzielniki=[]
        liczba=liczba.rstrip()
        liczba=int(liczba)
        for i in range(1, liczba+1):
            if liczba%i==0:
                dzielniki.append(i)
        if len(dzielniki)==18:
            liczby.append((liczba, dzielniki))
            ile+=1
for i in liczby:
    print(i)

print(ile)
