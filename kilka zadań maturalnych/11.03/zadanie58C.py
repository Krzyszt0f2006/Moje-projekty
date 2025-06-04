rekordS1=0
rekordS2=11
rekordS3=5
rekord=1
czy_rekord=False
with open('dane_systemy1.txt') as S1, open('dane_systemy2.txt') as S2, open('dane_systemy3.txt') as S3:
    for pomiar1, pomiar2, pomiar3 in zip(S1, S2, S3):
        pomiar1=pomiar1.rstrip().split()
        pomiar2 = pomiar2.rstrip().split()
        pomiar3 = pomiar3.rstrip().split()
        czy_rekord=False
        #S1 to system binarny, S2 system czworkowy, a S3 to system osemkowy
        if int(pomiar1[1])>int(rekordS1):
            rekordS1=pomiar1[1]
            czy_rekord=True
        if int(pomiar2[1])>int(rekordS2):
            rekordS2=pomiar2[1]
            czy_rekord=True
        if int(pomiar3[1])>int(rekordS3):
            rekordS3=pomiar3[1]
            czy_rekord=True
        if czy_rekord==True:
            rekord+=1
print(rekord)
