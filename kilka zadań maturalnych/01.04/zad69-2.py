wszystkiegeny=[]
genotypy=[]
def znajdz_gen(linijka):
    geny=[]
    koncowa=0
    for a in range(len(linijka)-1):
        if linijka[a]=="A" and linijka[a+1]=="A":
            gen=''
            if a>=koncowa:
                b=a
                for b in range(a, len(linijka)-1):
                    if(linijka[b] == "B" and linijka[b + 1] == "B"):
                        koncowa=b
                        gen+="BB"
                        break
                    else:
                        gen+=linijka[b]
                if gen.find("BB")>0:
                    geny.append(gen)
                gen=''
    return geny

with open('dane_geny.txt') as plik:
    for linijka in plik:
        linijka=linijka.rstrip()
        wszystkiegeny.append(znajdz_gen(linijka))
        genotypy.append((linijka))

#Gatunek^ to zbiór osobników o o dlugosci genotypu rownej i
def zad2():
    licznik=0
    for geny in wszystkiegeny:
        for gen in geny:
            if gen.find("BCDDC")>-1:
                licznik+=1
                break
    return licznik
najdluzsza=0
print(zad2())
#dobrze - 8 