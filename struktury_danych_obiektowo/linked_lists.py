class Node:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.nastepny = None

class Linkedlist:
    def __init__(self):
        self.head = None

    def append(self, element):
        nowa_noda = Node(element)

        if not self.head:
            self.head = nowa_noda
            return

        biezacy_element = self.head
        while biezacy_element.nastepny:
            biezacy_element = biezacy_element.nastepny
        biezacy_element.nastepny = nowa_noda

    def display(self):
        biezacy = self.head
        while biezacy:
            print(biezacy.wartosc, end=" -> ")
            biezacy = biezacy.nastepny
        print("None")
    def prepend(self,value):
        nowa_noda=Node(value)
        nowa_noda.nastepny=self.head
        self.head=nowa_noda
    def delete(self,value):
        biezacy = self.head
        if self.head.wartosc == value:
            self.head = self.head.nastepny
            return
        czy_znaleziona=False
        while biezacy.nastepny:
            if biezacy.nastepny.wartosc == value:
                biezacy.nastepny = biezacy.nastepny.nastepny
                czy_znaleziona=True
                return
            biezacy = biezacy.nastepny
        if czy_znaleziona==False:
            raise IndexError("Object not found")
    def reverse(self):
        poprzedni = None
        biezacy = self.head
        while biezacy:
            nastepny = biezacy.nastepny
            biezacy.nastepny = poprzedni
            poprzedni = biezacy
            biezacy = nastepny
        self.head = poprzedni
nowa_lista = Linkedlist()
nowa_lista.display()


nowa_lista.append(5)
nowa_lista.append(25)
nowa_lista.append(8)

nowa_lista.display()
print('-')
nowa_lista.prepend(21)
nowa_lista.display()
nowa_lista.delete(5)
nowa_lista.display()
nowa_lista.delete(21)
nowa_lista.display()
nowa_lista.append(25)
nowa_lista.append(8)
nowa_lista.display()
nowa_lista.reverse()
nowa_lista.display()
#nowa_lista.delete(33)