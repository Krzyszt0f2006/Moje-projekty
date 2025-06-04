def wartosc(a):
    suma=0
    for literka in a:
        literka=int(ord(literka))
        suma+=literka
    return suma
print(wartosc('asd'))