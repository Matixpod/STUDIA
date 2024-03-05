import datetime


# %% Zadanie 1

class Punkt_na_plaszczyznie():
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Prosta():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def sprawdz_punkt(self, punkt):
        return punkt.y == self.a * punkt.x + self.b
    
    def miejsce_zerowe(self):
        return -self.b / self.a,0
    

pkt = Punkt_na_plaszczyznie(1,5)

prosta = Prosta(2, 3)

print(prosta.sprawdz_punkt(pkt))
print(prosta.miejsce_zerowe())

# %% Zadanie 2




class Prostokat():
    def __init__(self,p1, p2):
        self.p1 = p1
        self.p2 = p2

    def pole(self):
        a = abs(self.p1.x - self.p2.x)
        b = abs(self.p1.y - self.p2.y)
        print(a*b)

    def obwod(self):
        a = abs(self.p1.x - self.p2.x)
        b = abs(self.p1.y - self.p2.y)
        return (a+b)*2

        
class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Punkt(1, 1)
p2 = Punkt(2, 3)
prostokat = Prostokat(p1,p2)
prostokat.pole()
print(prostokat.obwod())







# %% Zadanie 3


class Note():
    def __init__(self,autor,tresc):
        self.autor = autor
        self.tresc = tresc
        self.data = datetime.datetime.now()

class Notebook():
    def __init__(self):
        self.notes = []
        
    def add_new_note(self,autor,tresc):
        self.notes.append(Note(autor,tresc))

    def add_note(self,notatka):
        self.notes.append(notatka)
    
    def count_notes(self):
        return self.notes.count()
    
    def __str__(self):
        if self.notes == []:
            return "Nie masz notatek!"
        print("Twoje notatki: ")
        return "".join(f'{note.autor}: "{note.tresc}" stworzone dnia {note.data}\n' for note in self.notes)
        

        


Notatnik = Notebook()
Notatnik.add_new_note("Mateusz", "zrób trening")
Notatnik.add_new_note("Mateusz", "zrób trening2")
print(Notatnik)



# %% Zadanie 4

class Pracownik():
    def __init__(self,imie,nazwisko,stanowisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.stanowisko = stanowisko
        self._id = id(self)
        self.__pensja = pensja

    def przedstaw_sie(self):
        return f"Cześc nazywam sie {self.imie} {self.nazwisko} i pracuje na stanowsiku {self.stanowisko} ID {self._id}"
    
    def __zmien_pensje(self,nowa_pensja):
        self.__pensja = nowa_pensja

    def get_pensja(self):
        return f"Twoja pensja wynosi {self.__pensja}"
    
    def podwyzka(self,wartosc):
        self.__zmien_pensje(self.__pensja+wartosc)




osoba = Pracownik("Mateusz", "Podporski", "Szef", 99999)
print(osoba.przedstaw_sie())

print(osoba.get_pensja())
osoba.podwyzka(10000)
print(osoba.get_pensja())




