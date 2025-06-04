def rozklad_czynniki_unikalne(n):
    czynniki=[]
    d=2
    while n>1:
        if n%d==0:
            czynniki.append(d)
            while n%d==0:
                n=n//d
        else:
            d+=1
    return czynniki
def rozklad_czynniki(n):
    czynniki=[]
    d=2
    while n>1:
        if n%d==0:
            czynniki.append(d)
            n=n//d
        else:
            d+=1
    return czynniki
print(rozklad_czynniki())