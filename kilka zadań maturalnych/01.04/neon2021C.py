napis=[]
slownik={}
def przesun_litere(napis, litera):
    for i in range(len(napis)):
        if napis[i] == litera:
            if napis[i] == 'Z':
                napis[i] = 'A'
            else:
                napis[i] = chr(ord(napis[i]) + 1)
            break
    return napis
with open('instrukcje.txt') as plik:
    for instrukcja in plik:
        instrukcja = instrukcja.rstrip().split()
        print(instrukcja)
        if instrukcja[0]=='DOPISZ':
            if instrukcja[1] not in slownik:
                slownik[instrukcja[1]] = 1
            else:
                slownik[instrukcja[1]] += 1
            napis.append(instrukcja[1])
            #ZULAUNTURHNV
        if instrukcja[0]=='USUN':
            napis.pop()
            #ZLAUTURHNV
        if instrukcja[0]=="PRZESUN":
            przesun_litere(napis, instrukcja[1])
            #ALAVTURINV  chyba dobrze?????

print(max(slownik), slownik[max(slownik)])
#dziala dobrze