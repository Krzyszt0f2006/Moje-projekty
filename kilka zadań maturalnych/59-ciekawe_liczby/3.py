def mnozenie_cyfr(liczba):
    wynik=1
    liczba=str(liczba)
    for element1 in liczba:
        wynik=int(element1)*wynik
    return wynik
def oblicz_moc(n):
    moc=0
    while len(str(n))>1:
        moc+=1
        n=mnozenie_cyfr(n)
    return moc
slownik = {
    '1': 1,
    '2': 0,
    '3': 2,
    '4': 0,
    '5': 1,
    '6': 0,
    '7': 0,
    '8': 0
}
max_1=0
min_1=9999999
with open('liczby.txt') as plik:
    for element in plik:
        element=int(element.rstrip())
        moc=oblicz_moc(element)
        print(element, moc)
        for klucz in slownik:
            if str(moc)==klucz:
                slownik[klucz]+=1
        if moc==1:
            if element<min_1:
                min_1=element
            if element>max_1:
                max_1=element
for klucz in slownik:
    print(f"Dla mocy {klucz} ilosc wystapien wynosi {slownik[klucz]}. ")
print("Maksymalna liczba o mocy 1 : ", max_1)
print("Minimalna liczba o mocy 1 : ", min_1)