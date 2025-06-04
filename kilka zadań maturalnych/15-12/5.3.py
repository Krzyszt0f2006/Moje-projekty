znalezione=[]
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
            godziny="0"
        else:
            #godziny=int(godziny)
            pass
        czasy=[1111,2222,3333,4444]
        czy_palindrom=True
        sekundy=""
        sekundy+=str(sek1)
        sekundy+=str(sek2)
        if sekundy!=godziny[::-1]:
            czy_palindrom=False
        minuty=""
        minuty+=str(min1)
        minuty+=str(min2)
        if minuty!=minuty[::-1]:
            czy_palindrom=False
        wykonywanie=False
        if int(godziny)==12 and int(minuty)<=15:
            wykonywanie=True
            if int(minuty)==15 and int(sekundy)>0:
                wykonywanie=False
        if wykonywanie:
            znalezione.append([int(godziny),int(minuty),int(sekundy)])
            #print(f"{godziny}:{min1}{min2}:{sek1}{sek2}")
#print(znalezione)
dobrane=[]
for i in range(len(znalezione)):
    if znalezione.count(znalezione[i])>=3:
        if znalezione[i] not in dobrane:
            dobrane.append(znalezione[i])
for element1 in dobrane:
    print(f"{element1[0]}:{element1[1]}:{element1[2]}")