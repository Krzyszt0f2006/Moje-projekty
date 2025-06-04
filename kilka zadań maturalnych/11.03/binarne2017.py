dwucyklicze=0
najdluzsze=0
najdluzsza_liczba=0
with open('binarne.txt') as plik:
    for liczba in plik:
        liczba=liczba.rstrip()
        if liczba[0:int(len(liczba) / 2)]==liczba[int(len(liczba)/ 2):]:
            dwucyklicze+=1
            if len(liczba)>najdluzsze:
                najdluzsze=len(liczba)
                najdluzsza_liczba=liczba
print(dwucyklicze, najdluzsze, najdluzsza_liczba)
