napis=[]

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
        if instrukcja[0] == 'DOPISZ':
            napis.append(instrukcja[1])
        elif instrukcja[0] == 'USUN':
            if len(napis) > 0:
                napis.pop()
        elif instrukcja[0] == "PRZESUN":
            napis = przesun_litere(napis, instrukcja[1])
        elif instrukcja[0] == 'ZMIEN':
            if len(napis) > 0:
                napis[-1] = instrukcja[1]
#wreszcie dobrze
separator = ''
print(separator.join(napis))
