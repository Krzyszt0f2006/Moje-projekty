def p(a):
    if a == 1: return False
    if a == 2: return True
    for x in range(2, a):
        if a % x == 0:
            return False
    return True
def suma(a):
    roznica=0
    liczba1=0
    liczba2=0
    for l1 in range(a):
        for l2 in range(a):
            if p(l1) and p(l2):
                if l1+l2==a:
                    abs(l1-l2)>roznica
                    roznica=abs(l1-l2)
                    liczba1=l1
                    liczba2=l2
    print(a, liczba1, liczba2)
    return liczba1, liczba2

with open('pary.txt') as plik:
    for liczba in plik:
        liczba=liczba.strip().split()
        liczba[0]=int(liczba[0])
        if liczba[0]%2==0 and int(liczba[0])>4:
            suma(liczba[0])
        #    print(liczba[0], suma(liczba[0]))
