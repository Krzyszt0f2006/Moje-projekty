def NWD(a, b):
    while b:
        a, b = b, a % b
    return a

with open("liczby.txt") as plik:
    liczby = [int(linia.strip()) for linia in plik.readlines()]
max_dlugosc = 0
max_poczatek = -1
max_nwd = -1
poczatek = 0
for i in range(2, len(liczby)):
    if NWD(NWD(liczby[i-2], liczby[i-1]), liczby[i]) > 1:
        if i - poczatek > max_dlugosc:
            max_dlugosc = i - poczatek
            max_poczatek = poczatek
            max_nwd = NWD(NWD(liczby[i-2], liczby[i-1]), liczby[i])
    else:
        poczatek = i - 1

print("Pierwsza liczba ciągu:", liczby[max_poczatek])
print("Długość ciągu:", max_dlugosc)
print("Największy wspólny dzielnik:", max_nwd)
