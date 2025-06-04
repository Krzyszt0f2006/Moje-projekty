najwieksza=0
with open('binarne.txt') as plik:
    for liczba in plik:
        liczba=liczba.rstrip()
        #liczba=int(liczba, 2)
        #if liczba<=65535:
        #    if liczba>najwieksza:
        #        najwieksza=liczba
        if int(liczba, 2)>najwieksza and int(liczba, 2)<=65535:
            najwieksza=int(liczba, 2)
#print(liczba, str(bin(liczba))[2:])
print(najwieksza, bin(najwieksza)[2:])