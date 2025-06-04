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
                if 'BB' in gen:
                    geny.append(gen)
                gen=''
    return geny

with open('dane_geny.txt') as plik:
    for linijka in plik:
        linijka=linijka.rstrip()
        wszystkiegeny.append(znajdz_gen(linijka))
        genotypy.append((linijka))

#Gatunek^ to zbiór osobników o o dlugosci genotypu rownej i
def zad4():
    odporny=0
    silnie_odporny=0
    for i in range(len(genotypy)):
        obecny_genotyp=genotypy[i]
        ile=0
        for gen in wszystkiegeny[i]:
            if gen[::-1] in obecny_genotyp:
                ile+=1
        if ile==len(wszystkiegeny[i]):
            odporny+=1
    for genot in genotypy:
        if genot[::]==genot[::-1]:
            silnie_odporny+=1
    print('odporny - ', odporny, 'silnie odporny - ', silnie_odporny)
zad4()