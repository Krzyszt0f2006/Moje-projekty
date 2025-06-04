import  copy
plansza=list()
punkty=((0, -1),(1, -1), (1,0), (1,1), (0, 1), (-1, 1), (-1, 0), (-1, -1))
zadanieA=0
#zadanieB=0
with open('gra.txt') as plik:
    for linijka in plik:
        plansza.append(list(linijka.rstrip()))
        #print(linijka.rstrip())
for i in range(2, 100):
   # robocza=copy.deepcopy(plansza)
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
            if (x==1 and y==18 and i==38):
                zadanieA=komorki
            if (komorki in (2, 3) and plansza[x][y]=='X') or (komorki==3 and plansza[x][y]=='.'):
                plansza[x][y]='X'
                #if i==2:
                #    zadanieB+=1
            else:
                plansza[x][y]='.'
print(zadanieA)
#print(zadanieB)