import  copy
plansza=list()
punkty=((0, -1),(1, -1), (1,0), (1,1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
zadanieC=0
zywe=0
with open('gra.txt') as plik:
    for linijka in plik:
        plansza.append(list(linijka.rstrip()))
        #print(linijka.rstrip())
for i in range(2, 100):
    robocza=copy.deepcopy(plansza)
    ile_zywych=0
    for x in range(12):
        for y in range(20):
            komorki=0
            for a in punkty:
                b=a[0]+y
                c=a[1]+x
                if c>11:
                    c=0
                elif c<0:
                    x=11
                if b>19:
                    b=0
                elif b<0:
                    b=19
                if plansza[c][b]=='X':
                    komorki+=1
            if (komorki in (2, 3) and plansza[x][y]=='X') or (komorki==3 and plansza[x][y]=='.'):
                robocza[x][y]='X'
                ile_zywych+=1
                #if i==2:
                    #zadanieB+=1
            else:
                robocza[x][y]='.'
    if robocza==plansza:
        if zadanieC==0:
            zadanieC=i
            zywe=ile_zywych
    plansza=copy.deepcopy(robocza)
print(zadanieC)
print(zywe)