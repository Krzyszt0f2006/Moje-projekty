import math
temperatury1=[]
temperatury2=[]
temperatury3=[]
zegary=[]
zegary2=[]
zegary3=[]
# S1 to system binarny, S2 system czworkowy, a S3 to system osemkowy
with open("dane_systemy1.txt") as S1:
    with open("dane_systemy2.txt") as S2:
        with open("dane_systemy3.txt") as S3:
            for linijka1 in S1:
                zegar, temperatura = linijka1.strip().split()
                zegary.append(int(zegar, 2))
                temperatury1.append(int(temperatura, 2))

            for linijka2 in S2:
                zegar, temperatura = linijka2.strip().split()
                zegary2.append(int(zegar, 4))
                temperatury2.append(int(temperatura, 4))

            for linijka3 in S3:
                zegar, temperatura = linijka3.strip().split()
                zegary3.append(int(zegar, 8))
                temperatury3.append(int(temperatura, 8))
naj_skok_temperatury=[]
for i in range(len(temperatury1)):
    for j in range(i + 1, len(temperatury1)):
        r_ij = (temperatury1[i] - temperatury1[j])**2
        naj_skok_temperatury.append(math.ceil(r_ij/abs(i-j)))
print(max(naj_skok_temperatury))