niepoprawny=0
zegar=12
with open('dane_systemy1.txt') as S1, open('dane_systemy2.txt') as S2, open('dane_systemy3.txt') as S3:
    for pomiar1, pomiar2, pomiar3 in zip(S1, S2, S3):
        pomiar1=pomiar1.rstrip().split()
        pomiar2 = pomiar2.rstrip().split()
        pomiar3 = pomiar3.rstrip().split()
        #S1 to system binarny, S2 system czworkowy, a S3 to system osemkowy
        if zegar!=int(pomiar1[0], 2) and zegar!=int(pomiar2[0], 4) and zegar!=int(pomiar3[0], 8):
            niepoprawny+=1
        zegar+=24
print(niepoprawny)