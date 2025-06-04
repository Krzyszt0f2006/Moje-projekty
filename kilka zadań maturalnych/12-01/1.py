def sum_pairs(ints, s):
    print(ints,s)
    indexy=[]  #odwrocone indexy jako [j,i]
    for i in range(len(ints)):
        for j in range(len(ints)):
            if ints[i]+ints[j]==s and i!=j:
                znajduje=False
                for m in range(len(indexy)):
                    w=[j,i]
                    #print(f"w przed sortowaniem {w}")
                    w=sorted(w)
                    if w==(sorted(indexy[m])):
                        #print(w, indexy[m])
                        znajduje=True
                        w=None
                        break
                if znajduje==False:
                    indexy.append([j,i])
    if len(indexy)>0:
        indexy=sorted(indexy)
        print(indexy)
        a=indexy[0][1]
        b=indexy[0][0]
        indexy=None
        print(f"posortowame{indexy}")
        print(f"wynik {[ints[a],ints[b]]}")
        return [ints[a],ints[b]]
    return None
    #szukanie takiej ppary liczby od lewej strony ktora =s
print(sum_pairs([11, 3, 7, 5],         10))
#print(sum_pairs([20, -13, 40], -7))
print(sum_pairs([10, 5, 2, 3, 7, 5], 10))





def sum_pairs1(liczby, suma):
    sprawdzone = {}
    for i, liczba in enumerate(liczby):
        element = suma - liczba
        if element in sprawdzone:
            return [element, liczba]
        sprawdzone[liczba] = i
    return None