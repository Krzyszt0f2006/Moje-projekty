with open('dane_geny.txt') as plik:
    dane=[linijka.strip() for linijka in plik]
print(dane)
gatunki={}
#Gatunek^ to zbiór osobników o o dlugosci genotypu rownej i
def znajdowanie_genotypow(genotyp):
    geny=[]
    litery=genotyp[0]
    #for litera in genotyp:
lista_dlugosci=[]
for slowo in dane:
    lista_dlugosci.append(len(slowo))
def dlugosc(a):
    ile=0
    for zmienna in lista_dlugosci:
        if zmienna==a:
            ile+=1
    return ile
najdluzsza=0
for zmienna in lista_dlugosci:
        if dlugosc(zmienna)>najdluzsza:
            najdluzsza=dlugosc(zmienna)
print(len(set(lista_dlugosci)))
print(najdluzsza)