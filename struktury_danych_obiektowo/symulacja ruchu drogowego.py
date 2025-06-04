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
            print(biezacy.wartosc.name, end=" -> ")
            biezacy = biezacy.nastepny
        print("None")

    def prepend(self, value):
        nowa_noda = Node(value)
        nowa_noda.nastepny = self.head
        self.head = nowa_noda

    def delete(self, value):
        biezacy = self.head
        if self.head.wartosc == value:
            self.head = self.head.nastepny
            return
        czy_znaleziona = False
        while biezacy.nastepny:
            if biezacy.nastepny.wartosc == value:
                biezacy.nastepny = biezacy.nastepny.nastepny
                czy_znaleziona = True
                return
            biezacy = biezacy.nastepny
        if not czy_znaleziona:
            raise IndexError("nie znaleziono obiektu")

    def reverse(self):
        poprzedni = None
        biezacy = self.head
        while biezacy:
            nastepny = biezacy.nastepny
            biezacy.nastepny = poprzedni
            poprzedni = biezacy
            biezacy = nastepny
        self.head = poprzedni


class PriorityQueue:
    def __init__(self):
        self.kolejka_drogowa = Linkedlist()

    def enqueue(self, pojad):
        if not self.kolejka_drogowa.head or self.kolejka_drogowa.head.wartosc.priority < pojad.priority:
            self.kolejka_drogowa.prepend(pojad)
        else:
            obecny = self.kolejka_drogowa.head
            while obecny.nastepny and obecny.nastepny.wartosc.priority >= pojad.priority:
                obecny = obecny.nastepny
            nowa_noda = Node(pojad)
            nowa_noda.nastepny = obecny.nastepny
            obecny.nastepny = nowa_noda

    def dequeue(self):
        if self.kolejka_drogowa.head:
            wartosc = self.kolejka_drogowa.head.wartosc
            self.kolejka_drogowa.head = self.kolejka_drogowa.head.nastepny
            return wartosc
        return None

    def display(self):
        self.kolejka_drogowa.display()



class Vehicle:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

    def pojazd_pokaz(self):
        print(f' Imie: {self.name} Priorytet: {self.priority}')

class TrafficManager:
    def __init__(self):
        self.Kolejka_priorytetowa = PriorityQueue()

    def dodaj_pojazd(self, pojazd):
        self.Kolejka_priorytetowa.enqueue(pojazd)
        print(f" {pojazd.name} {pojazd.priority}) dodany")

    def process_vehicle(self):
        #4.process_vehicle() – Przetwarza kolejny pojazd z kolejki priorytetowej (tzn. pojazd o najwyższym priorytecie). Pojazd ten zostaje usunięty z kolejki i uznany za przepuszczony.
        pojazd = self.Kolejka_priorytetowa.dequeue()
        if pojazd:
            print(f"{pojazd.name} (Priorytet : {pojazd.priority})")
        else:
            print("nie ma takiego pojazdu")

    def pokaz_kolejke(self):
         self.Kolejka_priorytetowa.display()

    # def pokaz_kolejke(self):
    #     biezacy = self. head
    #     while biezacy:
    #         print(biezacy.wartosc, end=" -> ")
    #         biezacy = biezacy.nastepny
    #     print("None")
skrzyzowanie=TrafficManager()
karetka=Vehicle('Karetka',3)
karetka.pojazd_pokaz()
skrzyzowanie.pokaz_kolejke()
skrzyzowanie.dodaj_pojazd(karetka)

skrzyzowanie.pokaz_kolejke()

