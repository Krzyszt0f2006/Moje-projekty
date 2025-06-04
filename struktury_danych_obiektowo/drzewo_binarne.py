class Node:
    def __init__(self, wartosc):
        self.wartosc = wartosc
        self.lewy = None
        self.prawy = None

class DrzewkoBinarne:
    def __init__(self, wartosc_korzenia):
        self.korzen = Node(wartosc_korzenia)

    def dodaj(self, wartosc):
        kolejka = [self.korzen]
        while kolejka:
            biezacy = kolejka.pop(0)

            if biezacy.lewy is None:
                biezacy.lewy = Node(wartosc)
                return
            else:
                kolejka.append(biezacy.lewy)

            if biezacy.prawy is None:
                biezacy.prawy = Node(wartosc)
                return
            else:
                kolejka.append(biezacy.prawy)

    def inorder(self, wezel):   # Left, Node, Right - LNR
        if wezel:
            self.inorder(wezel.lewy)
            print(wezel.wartosc, end=" ")
            self.inorder(wezel.prawy)

    def preorder(self, wezel):  # Node, Left, Right
        if wezel:
            print(wezel.wartosc, end=" ")
            self.inorder(wezel.lewy)
            self.inorder(wezel.prawy)

    def postorder(self, wezel): # Left, Right, Node
        if wezel:
            self.inorder(wezel.lewy)
            self.inorder(wezel.prawy)
            print(wezel.wartosc, end=" ")


db = DrzewkoBinarne(1)
db.dodaj(2)
db.dodaj(3)
db.dodaj(4)
db.dodaj(5)
db.dodaj(6)
db.dodaj(7)
db.inorder(db.korzen)
print()
db.preorder(db.korzen)
print()
db.postorder(db.korzen)