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
print(oblicz_moc(678))
print(oblicz_moc(1991))
