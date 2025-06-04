napis=[]
ciag_instrukcja='0'
ciag_dlugosc=0
poprzednia='0'
naj=0
def przesun_litere(napis, litera):
    for i in range(len(napis)):
        if napis[i] == litera:
            if napis[i] == 'Z':
                napis[i] = 'A'
            else:
                napis[i] = chr(ord(napis[i]) + 1)
            break
    return napis
with open('przyklad1.txt') as plik:
    for instrukcja in plik:
        instrukcja = instrukcja.rstrip().split()
        print(instrukcja)
        if instrukcja[0]==poprzednia:
            ciag_dlugosc+=1
            if ciag_dlugosc>naj:
                naj=ciag_dlugosc
                ciag_instrukcja=poprzednia
        else:
            if ciag_dlugosc>naj:
                naj=ciag_dlugosc
                ciag_instrukcja=poprzednia
            ciag_dlugosc=1
            poprzednia=instrukcja[0]
        if instrukcja[0]=='DOPISZ':
            napis.append(instrukcja[1])
            #ZULAUNTURHNV
        if instrukcja[0]=='USUN':
            napis.pop()
            #ZLAUTURHNV
        if instrukcja[0]=="PRZESUN":
            przesun_litere(napis, instrukcja[1])
            #ALAVTURINV  źle... :(

separator=''
print(separator.join(napis))
#print(len(napis)) #dobrze
print(ciag_instrukcja," - ",  naj)