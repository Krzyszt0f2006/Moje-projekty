def dlugosc(a):
    dlugosc=0
    naj_l='1'
    ciag=0
    poprzednia='1'
    #print(poprzednia)
    for literka in a:
        if literka==poprzednia:
            ciag+=1
            poprzednia=literka
            if ciag>dlugosc:
                dlugosc=ciag
                naj_l=literka
        else:
            ciag=1
            if poprzednia == '1':
                naj_l=literka
                dlugosc=1
            poprzednia=literka
    for i in range(dlugosc):
        print(naj_l, end="")
    print(' ', end='')
    print(dlugosc)

with open('pary.txt') as plik:
    for liczba in plik:
        liczba=liczba.strip().split()
        dlugosc(liczba[1])