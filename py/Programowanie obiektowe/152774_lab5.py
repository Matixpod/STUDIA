# %%
from abc import ABC, abstractmethod
import random
import math


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


class GameObject(ABC):
    def __init__(self, health_points):
        self.health_points = health_points
    
    def is_alive(self):
        return self.health_points > 0
    
    @abstractmethod
    def interact(self, player):
        pass

class Player(GameObject):
    def interact(self, player):
        pass

class Monster(GameObject):
    def interact(self, player):
        player.health_points -= 10
        self.health_points = 0
        print("Gracz zabił potwora.")

class Door(GameObject):
    def interact(self, player):
        print("Gracz przeszedł przez drzwi.")

player = Player(50)
objects = [Monster, Door]

for _ in range(10):
    object_class = random.choices(objects, weights=[7, 3], k=1)[0] 
    game_object = object_class(50)
    game_object.interact(player)
    
    if not player.is_alive():
        print("Gracz został zabity!")
        break



# %% Zadanie 3



class Equation(ABC):
    def __init__(self, nums):
        self.nums = nums
    
    @abstractmethod
    def solve(self):
        pass

class LinearEquation(Equation):
    def __init__(self, nums):
        if len(nums) != 2:
            raise ValueError("Równanie musi mieć 2 liczby")
        super().__init__(nums)
    
    def solve(self):
        a, b = self.nums
        if a == 0:
            print("Brak rozwiązania.")
        else:
            x = -b / a
            print(f"x = {x}")

class QuadraticEquation(Equation):
    def __init__(self, nums):
        if len(nums) != 3:
            raise ValueError("Równanie musi mieć 2 liczby")
        super().__init__(nums)
    
    def solve(self):
        a, b, c = self.nums
        delta = b**2 - 4*a*c
        if delta < 0:
            print("Brak rozwiązania.")
        elif delta == 0:
            x = -b / (2*a)
            print(f"x = {x}")
        else:
            x1 = (-b + math.sqrt(delta)) / (2*a)
            x2 = (-b - math.sqrt(delta)) / (2*a)
            print(f"x1 = {x1}, x2 = {x2}")


eq = LinearEquation([2, 0])
eq.solve()

eq1 = LinearEquation([0, 2])
eq1.solve()

eq2 = QuadraticEquation([1, -5, 6])
eq2.solve()
