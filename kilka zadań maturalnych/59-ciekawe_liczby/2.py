ile=0
with open('liczby.txt') as plik:
    for element in plik:
        element=int(element.rstrip())
        odwrocona=int((str(element)[::-1]))
        element=element+odwrocona
        if element==int(str(element)[::-1]):
            ile+=1
print(ile)

