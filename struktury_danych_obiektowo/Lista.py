class Lista:
    def __init__(self):
        self.dane = []
        self.dlugosc = 0
        self.realna_dlugosc=0
        for i in range(10):
            self.dane.append(None)
            self.realna_dlugosc+=1

    def append(self, wartosc):
        dodano=False
        for i in range(self.realna_dlugosc-1):
            if self.dane[i]==None:
                self.dane[i]=wartosc
                self.dlugosc += 1
                dodano=True
                break
        if dodano==False:
            for i in range(self.realna_dlugosc):
                self.dane.append(None)
                self.realna_dlugosc+=1
            self.dane[self.dlugosc]=wartosc
            self.dlugosc+=1
            print('przedluzono Liste')
    def get(self, index):
        if 0 <= index < self.dlugosc:
            return self.dane[index]
        else:
            raise IndexError("Index out of range")

    def insert(self, wartosc, index):
        if index < 0 or self.dlugosc <= index:
            raise IndexError("Index out of range")
        else:
            self.dane = self.dane[:index] + [wartosc] + self.dane[index:]
    def remove(self,element):
        znalezione=False
        #musisz znaleźć index elementu
        for i in range(self.dlugosc):
            if self.dane[i]==element:
                znaleziony_indeks=i
                znalezione=True
        if znalezione==True:
            self.dane=self.dane[:znaleziony_indeks-1]+self.dane[znaleziony_indeks+1:]
            self.dlugosc-=1
        else:
            raise IndexError("Object not found")
    def display(self):
        print(self.dane[:self.dlugosc])

mojaLista = Lista()
mojaLista.append(10)
mojaLista.append(20)
mojaLista.display()
print(mojaLista.get(1))
#print(mojaLista.get(3))
class Stos:
    def __init__(self):
        self.dane=[]
        self.dlugosc=0
    def push(self,obiekt):
        self.dane.insert(0,obiekt)
        self.dlugosc+=1
    def pop(self,indeks):
        if indeks>self.dlugosc-1:
            #print('not enough elements in stack')
            raise ValueError('not enough elements in stack')
        else:
            for i in range(0,indeks+1):
                self.dane.pop(0)
                self.dlugosc-=1
    def display(self):
        print(self.dane)
    def isEmpty(self):
        if self.dlugosc!=0:
            return True
        else:
            return False

mojStos=Stos()
mojStos.push(1)
mojStos.push(29)
mojStos.display()
mojStos.push('www')
mojStos.display()
mojStos.pop(0)
mojStos.display()
#######
class Queue:
    def __init__(self):
        self.dane=[]
        self.dlugosc=0
        #enqueue i dequeue
    def enqueue(self, object):
        self.dane.append(object)
        self.dlugosc+=1
    def dequeue(self, index):
        if index>self.dlugosc-1:
            raise ValueError('not enough elements in stack')
        else:
            for i in range(index+1):
                self.dane.pop(0)
                self.dlugosc+=1
    def display(self):
        print(self.dane)
    def isEmpty(self):
        if self.dlugosc!=0:
            return True
        else:
            return False
print('Kolejka')
kolejka=Queue()
kolejka.enqueue(1)
kolejka.enqueue(37)
kolejka.enqueue(29301)
kolejka.display()
#kolejka.dequeue(5)
kolejka.display()
print('Testy listy')
nowa_lista=Lista()
nowa_lista.display
for i in range(13):
    nowa_lista.append(i)
    if i==6:
        nowa_lista.display()
nowa_lista.display()
nowa_lista.insert(21,6)
nowa_lista.display()
nowa_lista.remove(21)
nowa_lista.display()