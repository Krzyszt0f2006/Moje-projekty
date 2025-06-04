ciagi=[]
nieparzyste=[]
suma_przedzialow=[]
with open('przedzialy.txt') as plik:
    for element in plik:
        element=element.rstrip()
        ciagi.append(element)
        print(element)

    for i in range(len(ciagi)):
        element=ciagi[i]
        #print(element)
        ujemna=1
        ujemna2=1
        p_otwarty=True
        k_otwarty=True
        p_liczby=[]
        k_liczby=[]
        #poczatek
        paczatek=True
        koniec=False
        for cyfra in element:
            if paczatek:
                if cyfra=="<":
                    p_otwarty=False
                if cyfra.isdigit():
                    p_liczby.append(cyfra)
                if cyfra=="-":
                    ujemna=-1
                if cyfra==",":
                    koniec=True
                    paczatek=False
            if koniec:
                if cyfra==">":
                    k_otwarty=False
                if cyfra.isdigit():
                    k_liczby.append(cyfra)
                if cyfra=="-":
                    ujemna2=-1
                if cyfra==",":
                    paczatek=False
        liczba1=int("".join(p_liczby))*ujemna
        liczba2=int("".join(k_liczby))*ujemna2
        #print(liczba1)
        #print(liczba2)
        if p_otwarty:
            p_otwarty=1
        else:
            p_otwarty=0
        if k_otwarty:
            k_otwarty=0
        else:
            k_otwarty=1
        ile=0
        for i in range(liczba1+p_otwarty,liczba2+k_otwarty):
            ile+=i
        suma_przedzialow.append(ile)
print(suma_przedzialow)