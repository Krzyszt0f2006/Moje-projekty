def nwd(a, b):
    while b!=0:
        a, b = b, a % b
    return a
najwieksza=0
liczby=[]
w_pierwsze=[]
with open('liczby.txt') as plik:
    for liczba in plik:
        dzielniki=[]
        liczba=liczba.rstrip()
        liczba=int(liczba)
        liczby.append(liczba)
#print(liczby)
for i in range(len(liczby)):
    pierwsze = True
    for j in range(200):
        if i != j and nwd(liczby[i], liczby[j]) > 1:
            pierwsze = False
    if pierwsze and liczby[i] > najwieksza:
        najwieksza=liczby[i]
print(najwieksza)
