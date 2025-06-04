anagramy=[]
nie_ma=[]
with open("anagramy.txt") as plik:
    for element in plik:
        element=element.rstrip
        anagramy.append(element)
def anagram(slowo):
    tab=[]
    for litera in slowo:
        tab.append(litera)
    return sorted(tab)
ile=0
print(anagramy)
for i in range(len(anagramy)):
    ile=0
    for j in range(len(anagramy)):
        if j!=i:
            if anagram(anagramy[i])==anagram(anagramy[j]):
                ile+=1
    if ile==0:
        print(anagram[i])