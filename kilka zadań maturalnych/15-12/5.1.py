wiersz=1
with open('rejestrator.txt') as plik:
    for element in plik:
        element=element.rstrip()
        godz1= element[0:4]
        #print(godz1)
        godz1=int(godz1, 2)
        #print(godzina)
        godz2= element[4:8]
        #print(godz2)
        godz2=int(godz2, 2)
        min1=element[8:12]
        #print(min1)
        min1=int(min1,2)
        min2=element[12:16]
        min2=int(min2,2)
        sek1=element[16:20]
        sek1=int(sek1,2)
        sek2=element[20:24]
        sek2=int(sek2,2)
        #(element)
        godziny=""
        godziny += str(godz1)
        godziny += str(godz2)
        if godziny=='24':
            godziny=0
        else:

            godziny=int(godziny)
        czasy=[1111,2222,3333,4444]
        if wiersz in czasy:
            print(f"{godziny}:{min1}{min2}:{sek1}{sek2}")
        wiersz+=1

