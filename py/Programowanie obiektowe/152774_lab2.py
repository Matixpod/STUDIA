import datetime
import matplotlib.pyplot as plt


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
    
    def graph(self):
        plt.plot([self.p1.x, self.p2.x, self.p2.x, self.p1.x, self.p1.x],
                 [self.p1.y, self.p1.y, self.p2.y, self.p2.y, self.p1.y])

        plt.scatter([self.p1.x,self.p2.x], [self.p1.y,self.p2.y])
        plt.grid()
        plt.show()

        
class Punkt():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p1 = Punkt(1, 1)
p2 = Punkt(2, 3)
prostokat = Prostokat(p1,p2)
prostokat.pole()
prostokat.graph()
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

# %% Zadanie 5
class Player():
    def __init__(self, nick):
        self.nick = nick
        self.__health = 100
        self._score = 0
        self.lvl = 0


    def attack(self,enemy):
        print(f">>> Atakujesz gracza {enemy.nick} za 10 obrażeń\n")
        enemy.__health -= 10

        if enemy.__health <= 0:
            self._score += 100
            print(f"!!!Pokonałeś {enemy.nick} zyskujesz 100xp!!!\n")


    def heal(self):
        print(f">>> Leczysz sie za 15 pkt zdrowia\n")
        self.__health += 15
        if self.__health > 100:
            self.__health = 100

    def _get_health(self):
        return self.__health
    
    def _set_health(self,value):
        self.__health = value

    def __str__(self):
        return f"Nick: {self.nick}\nŻycie: {self.__health}\nScore: {self._score}\n"
    
    
    @property
    def level(self):
        self.lvl = (self._score // 100) + 1
        return f"Poziom gracza {self.nick}: {self.lvl}"
    
    @level.setter
    def level(self, value):
        pass



player1 = Player("John")
player2 = Player("Mike")
print(player1)
print(player2)
player2.attack(player1)
player2.attack(player1)
player1.attack(player2)
player1.attack(player2)
player1.attack(player2)
player1.attack(player2)
player1.attack(player2)
player1.attack(player2)
player1.attack(player2)
player1.attack(player2)
player1.attack(player2)
player1.attack(player2)
player1.heal()
# player2._set_health(100)

print(player1.level)
print(player1)
print(player2)













