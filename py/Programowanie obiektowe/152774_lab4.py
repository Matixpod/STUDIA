# %% Zadanie 1

class Ssak:
    rodzaj = "Ssak"
    def __init__(self,info):
        self.info = info 

    def ciekawostka(self):
        return self.info
    




class Pies(Ssak):
    rodzaj = "Pies"
    def __init__(self,info):
        super().__init__(info)

    def ciekawostka(self):
        return self.info


class Kot(Ssak):
    rodzaj = "Kot"
    def __init__(self,info):
        super().__init__(info)

    def ciekawostka(self):
        return self.info







s = Ssak("gatunek")
print(s.ciekawostka())
p = Pies("Ma 4 łapy")
print(p.ciekawostka())
k = Kot("Pije mleko")
print(k.ciekawostka())


# %% Zadanie 2




class Zegar:
    def __init__(self):
        self.godzina = 0
        self.minuta = 0
        self.sekunda = 0

    def ustaw_czas(self,godzina,minuta,sekunda):
        self.godzina = godzina
        self.minuta = minuta
        self.sekunda = sekunda

    def __repr__(self):
        return f"{self.godzina:02}:{self.minuta:02}:{self.sekunda:02}"



class Zegar_elektroniczny(Zegar):
    def __init__(self):
        super().__init__()
        self.dni_tygodnia = 0
        self.dzien_miesiaca = 0
        self.miesiac = 0
        self.rok = 0

    def ustaw_czas(self,godzina,minuta,sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok):
        super().ustaw_czas(godzina,minuta,sekunda)
        self.dni_tygodnia = dni_tygodnia
        self.dzien_miesiaca = dzien_miesiaca
        self.miesiac = miesiac
        self.rok = rok

    def __repr__(self):
        return f"{self.godzina:02}:{self.minuta:02}:{self.sekunda:02} {self.dzien_miesiaca}/{self.miesiac}/{self.rok}"




class Zegar_4_wymiar(Zegar_elektroniczny):
    def __init__(self):
        super().__init__()
        self.czas_kwantowy = 0

    def ustaw_czas(self, godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok, czas_kwantowy):
        super().ustaw_czas(godzina, minuta, sekunda, dni_tygodnia, dzien_miesiaca, miesiac, rok)
        self.czas_kwantowy = czas_kwantowy

    def __repr__(self):
        return f"{self.godzina:02}:{self.minuta:02}:{self.sekunda:02} {self.dzien_miesiaca}/{self.miesiac}/{self.rok}  {self.czas_kwantowy}"
    

zegar = Zegar()
zegar.ustaw_czas(12, 30, 0)
print(zegar)
zegar_elektroniczny = Zegar_elektroniczny()
zegar_elektroniczny.ustaw_czas(12, 30, 0, 2, 22, 3, 2023)
print(zegar_elektroniczny)
zegar_czwarty_wymiar = Zegar_4_wymiar()
zegar_czwarty_wymiar.ustaw_czas(12, 30, 0, 2, 22, 3, 2023, 0.5)
print("ZegarCzwartyWymiar:", zegar_czwarty_wymiar)


# %% Zadanie 3





class Ksiazka():
    def __init__(self,tytul, autor, cena):
        self.tytul = tytul
        self.autor = autor
        self.cena = cena

    def __str__(self):
        return f"{self.tytul} {self.autor} {self.cena}" 
    
    def __repr__(self):
        return f"{self.tytul} {self.autor} {self.cena}" 


class Ksiazka_fantasy(Ksiazka):
    def __init__(self, tytul, autor, cena, podgatunek_fantasy):
        super().__init__(tytul,autor,cena)
        self.podgatunek_fantasy = podgatunek_fantasy


class Ksiazka_kryminalna(Ksiazka):
    def __init__(self, tytul, autor, cena, liczba_zabojstw):
        super().__init__(tytul,autor,cena)
        self.liczba_zabojstw = liczba_zabojstw

    
class KsiazkaFantastycznoKryminalna(Ksiazka_fantasy, Ksiazka_kryminalna):
    def __init__(self, tytul, autor, cena, **kwargs):
        super().__init__(tytul, autor, cena, **kwargs)
# Zrobić z użyciem kwargs...



class Biblioteka:


    def __init__(self):
        self.dostepne_ksiazki = []
        self.wypozyczone_ksiazki = {}
    def lista_ksiazek(self):
        return f"Obecnie dostepne ksiazki:\n{self.dostepne_ksiazki}"
    
    def wyswietl_wypozyczone(self):
        return f"Obecnie wypożyczone ksiązki:\n{self.wypozyczone_ksiazki}"
    
    def dodaj_ksiazke(self,ksiazka):
        self.dostepne_ksiazki.append(ksiazka)
        print("książka została dodana do biblioteki")
        
    def wypozycz(self, ksiazka, osoba):
        """Wypożycza książkę osobie."""
        if ksiazka in self.dostepne_ksiazki:
            if osoba in self.wypozyczone_ksiazki:
                self.wypozyczone_ksiazki[osoba].append(ksiazka)
            else:
                self.wypozyczone_ksiazki[osoba] = [ksiazka]
            self.dostepne_ksiazki.remove(ksiazka)
            print(f"Książka '{ksiazka}' została wypożyczona przez {osoba}.")
        else:
            print(f"Książka '{ksiazka}' nie jest dostępna w bibliotece.")

    def zwroc(self, ksiazka, osoba):
        """Zwraca książkę do biblioteki."""
        if osoba in self.wypozyczone_ksiazki and ksiazka in self.wypozyczone_ksiazki[osoba]:
            self.wypozyczone_ksiazki[osoba].remove(ksiazka)
            self.dostepne_ksiazki.append(ksiazka)
            print(f"Książka '{ksiazka}' została zwrócona przez {osoba}.")
        else:
            print(f"Książka '{ksiazka}' nie jest wypożyczona przez {osoba}.")



ksiazka1 = Ksiazka("Dune", "Frank Herbert", 39.99)
ksiazka2 = Ksiazka_fantasy("Władca Pierscieni", "J.R.R. Tolkien", 49.99, "high fantasy")
ksiazka3 = Ksiazka_kryminalna("Zbrodnia i kara", "Fiodor Dostojewski", 29.99, 10)
# ksiazka4 = KsiazkaFantastycznoKryminalna("Miasto Cienia", "Cassandra Clare", 59.99,
# "urban fantasy", 5)

biblioteka = Biblioteka()
biblioteka.dodaj_ksiazke(ksiazka1)
biblioteka.dodaj_ksiazke(ksiazka2)
biblioteka.dodaj_ksiazke(ksiazka3)
biblioteka.lista_ksiazek()

biblioteka.wypozycz(ksiazka1, "Jan Kowalski")
biblioteka.wypozycz(ksiazka2, "Jan Kowalski")
print(biblioteka.lista_ksiazek())
print(biblioteka.wyswietl_wypozyczone())
biblioteka.zwroc(ksiazka2,"Jan Kowalski")
print(biblioteka.wyswietl_wypozyczone())
print(biblioteka.lista_ksiazek())






# %% Zadanie 4

class Furniture:
    def __init__(self, material, size):
        self.__material = material
        self.size = size
    
    def get_material(self):
        return self.__material

    def set_material(self, material):
        self.__material = material
    


class Table(Furniture):
    def __init__(self, material, size, legs):
        super().__init__(material,size)
        self.__legs = legs
    

    @property
    def legs(self):
        return self.__legs

    def set_legs(self,legs):
        self.__legs = legs


class Chair(Furniture):
    def __init__(self, material, size, has_armrests):
        super().__init__(material, size)
        self.__has_armrests = has_armrests

    @property
    def has_armrests(self):
        return self.__has_armrests
    
    @has_armrests.setter
    def has_armrests(self,armrests):
        self.__has_armrests = armrests




table = Table('wood', 'large', 4)
chair = Chair('metal', 'medium', True)

print('Table material:', table.get_material())
table.set_material('plastic')
print('Table material after modification:', table.get_material())
print('Table size:', table.size)
print('Table legs:', table.legs)
table.set_legs(6)
print('Table legs after modification:', table.legs)
print('Chair material:', chair.get_material())
print('Chair has armrests:', chair.has_armrests)
chair.has_armrests = False
print('Chair has armrests after modification:', chair.has_armrests)

