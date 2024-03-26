# %%
from abc import abstractmethod

# %% Zadanie 1
class Transport:
    def __init__(self, start, koniec, ładunek):
        self.start = start
        self.koniec = koniec
        self.ładunek = ładunek

    @abstractmethod
    def transportuj(self,nowy_koniec):
        self.koniec = nowy_koniec

    def get_start(self):
        return self.start
    
    def get_koniec(self):
        return self.koniec
    
    def get_ładnuek(self):
        return self.ładunek
    




class Samolot(Transport):
    def __init__(self, start, koniec, ładunek, ilosc_pasazerow, ilosc_bagazy):
        super().__init__(start,koniec,ładunek)
        self.ilosc_pasazerow = ilosc_pasazerow
        self.ilosc_bagazy = ilosc_bagazy

    def transportuj(self, nowy_koniec):
        print(f"Samolot startuje z {self.start} do miejsca {self.koniec}")
        print(f"Na pokładzie znajduje sie {self.ilosc_pasazerow} pasażerów i {self.ilosc_bagazy} bagazy")
        self.start = self.koniec
        super().transportuj(nowy_koniec)

    def __str__(self):
        return f"Informacje:\n start: {self.start}\n koniec: {self.koniec}\n ładunek: {self.ładunek}\n\n" 

class Statek(Transport):
    def __init__(self, start, koniec, ładunek, rodzaj_ładunku, ilosc_kontenerów):
        super().__init__(start,koniec,ładunek)
        self.rodzaj_ładunku = rodzaj_ładunku
        self.ilosc_kontenerów = ilosc_kontenerów

    def transportuj(self, nowy_koniec):
        print(f"Statek wypływa z {self.start} do {self.koniec}")
        print(f"Na statku znajduje sie {self.ilosc_kontenerów} kontenerów z zawartoscia typu {self.rodzaj_ładunku}")
        self.start = self.koniec
        super().transportuj(nowy_koniec)

    def __str__(self):
        return f"Informacje:\n start: {self.start}\n koniec: {self.koniec}\n ładunek: {self.ładunek}\n\n" 


class Ciezarowka(Transport):
    def __init__(self, start, koniec, ładunek, ilosc_palet, typ_ladunku):
        super().__init__(start,koniec,ładunek)
        self.ilosc_palet = ilosc_palet
        self.typ_ladunku = typ_ladunku

    def transportuj(self, nowy_koniec):
        print(f"Ciężarówka wyrusza ze {self.start} do {self.koniec}")
        print(f"Ciężarówka przewozi {self.ilosc_palet} palet o typie {self.typ_ladunku}")
        self.start = self.koniec
        super().transportuj(nowy_koniec)

    def __str__(self):
        return f"Informacje:\n start: {self.start}\n koniec: {self.koniec}\n ładunek: {self.ładunek}\n\n" 



statek = Statek("Gdansk", "New York", "kontenery", "Towar A", 100)

statek.transportuj("Hamburg")
print(statek)


# %% Zadanie 2





