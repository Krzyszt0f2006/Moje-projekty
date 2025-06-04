niepoprawne=0
najkrotszy=0
with open('binarne.txt') as plik:
    for liczba in plik:
        liczba=liczba.rstrip()
        for i in range(int(len(liczba)/4)):
            if (int(liczba[i*4:i*4+4], 2)) > 9:
                niepoprawne+=1
                if najkrotszy==0:
                    najkrotszy=len(liczba)
                else:
                    if int(najkrotszy)>len(liczba):
                        najkrotszy=len(liczba)
                break
print(niepoprawne, najkrotszy)