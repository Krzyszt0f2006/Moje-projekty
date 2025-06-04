def dodawanie_binarne(a, b):
    if len(a) < len(b):
        a ='0'*(len(b)-len(a))+a
    elif len(b)<len(a):
        b ='0'*(len(a)-len(b))+b
    nadwaga = 0
    wynik=''
    for i in range(len(a)-1,-1,-1):
        suma = int(a[i]) + int(b[i]) + nadwaga
        if suma>1:
            nadwaga = 1
        else:
            nadwaga=0
        wynik=str(suma % 2)+wynik
        #wynik+=str(suma % 2)
        #1%2=1
        #2%2=0
    if nadwaga == 1:
        wynik = '1'+wynik
    return wynik
a='1010' #10
b='10100' #20
print(dodawanie_binarne(a, b))
#11110 to 30
