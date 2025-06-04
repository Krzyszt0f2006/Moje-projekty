najmniejszaS1=0
najmniejszaS2=0
najmniejszaS3=0
with open('dane_systemy1.txt') as S1, open('dane_systemy2.txt') as S2, open('dane_systemy3.txt') as S3:
    for pomiar1, pomiar2, pomiar3 in zip(S1, S2, S3):
        pomiar1=pomiar1.rstrip().split()
        pomiar2 = pomiar2.rstrip().split()
        pomiar3 = pomiar3.rstrip().split()
        #S1 to system binarny, S2 system czworkowy, a S3 to system osemkowy
        if int(pomiar1[1])<int(najmniejszaS1):
            najmniejszaS1=pomiar1[1]
        if int(pomiar2[1])<int(najmniejszaS2):
            najmniejszaS2=pomiar2[1]
        if int(pomiar3[1])<int(najmniejszaS3):
            najmniejszaS3=pomiar3[1]
print(najmniejszaS1)
print(bin(int(najmniejszaS2, 4)).replace('0b', ''))
print(bin(int(najmniejszaS3, 8)).replace('0b', ''))

