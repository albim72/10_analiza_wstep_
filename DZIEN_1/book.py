class Book(object):
    # definicja stanu - konstruktor klasy
    # def __new__(cls, *args, **kwargs):
    #     return super().__new__(Book)
    def __init__(self,id,tytul,autor,wydawnictwo,cena=30):
        self.idbook = id
        self.tytul = tytul
        self.autor = autor
        self.cena = cena
        self.wyd = wydawnictwo
        self.oprawa = "miękka"
        self.info()

    def __repr__(self):
        return f"książka: {self.tytul}, autor: {self.autor}, oprawa: {self.oprawa}"

    def info(self):
        print("Utworzenie nowej książki - obiekt klasy Book")

    def rabat(self,procent):
        return self.cena * procent/100


#utworzenie obieektu klasy Book
bk = Book(45,"Poradnik początkująego biegacza - wyd I","Michał Stec","abc",56)
print(bk)
print(bk.tytul)
print(bk.wyd)
print(f"rabat wynosi: {bk.rabat(25)} zł")
