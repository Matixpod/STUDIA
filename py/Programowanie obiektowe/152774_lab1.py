# %%
import math


# %% Zadanie 1
class Samochod():

    def __init__(self,marka,model,rok_produkcji,predkosc_maksymalna):
        self.marka = marka
        self.model = model
        self.rok_produkcji = rok_produkcji
        self.predkosc_maksymalna = predkosc_maksymalna



    def jedz(self,droga):
        print(f"{self.marka} {self.model} {self.rok_produkcji} jedzie po drodze z prędkością {self.predkosc_maksymalna} km/h.")
        if  self.predkosc_maksymalna - droga.maksymalna_predkosc > 0:
            print(f"Przekraczasz prędkość o {self.predkosc_maksymalna - droga.maksymalna_predkosc} km/h.")
        else:
            print("Jedziesz zgodnie z przepisami")


    def __del__(self):
        return "Samochód został zniszczony"
    



class Droga():
    def __init__(self,rodzaj,maksymalna_predkosc):
        self.rodzaj = rodzaj
        self.maksymalna_predkosc = maksymalna_predkosc


moj_samochod = Samochod("Ferrari", "250 GTO", 2019, 200)
moja_droga = Droga("Autostrada", 140)
moj_samochod.jedz(moja_droga)


# %% Zadanie 2

class Konto_Bankowe():
    def __init__(self, numer_konta, imie, nazwisko, saldo):
        self.numer_konta = numer_konta
        self.imie = imie
        self.nazwisko = nazwisko
        self.saldo = saldo



    def wplata(self):
        print(f"Twoje saldo wynosi {self.saldo}")
        pieniadze = float(input("Podaj kwotę wpłaty: "))
        self.saldo = self.saldo + pieniadze
        print(f"Wplata zostala wykonana saldo wynosi {self.saldo}")
    
    def wyplata(self):
        print(f"Twoje saldo wynosi {self.saldo}")
        pieniadze = float(input("Ile chcesz wypłacić?"))
        if pieniadze <= self.saldo:
            self.saldo = self.saldo - pieniadze
            print(f"Wyplata zostala wykonana saldo wynosi {self.saldo}")

        else:
            print(f"Masz za mało pieniedzy na koncie!")

    def __del__():
        return "Obiekt został zniszczony"



moje_konto = Konto_Bankowe("123456789", "Jan", "Kowalski", 1000.0)
moje_konto.wplata()
moje_konto.wyplata()






# %% Zadanie 3

class Energia_Odnawialna():
    def __init__(self,nazwa,moc,lokacja):
        self.nazwa = nazwa
        self.moc = moc
        self.lokacja = lokacja

    def get_info(self):
        return f"Źródło: {self.nazwa}, Moc: {self.moc} Watt, Lokalizacja: {self.lokacja}"


    def __add__(self,other):
        zrodlo = f"{self.nazwa}, {other.nazwa}"
        moc = self.moc + other.moc
        lokacja = f"{self.lokacja}, {other.lokacja}"
        return Energia_Odnawialna(zrodlo, moc, lokacja)
elektrownia_wiatrowa = Energia_Odnawialna("Wiatr", 50, "Niemcy")
elektrowania_sloneczna = Energia_Odnawialna("Slonce", 30, "Polska")

print(elektrownia_wiatrowa.get_info())
print(elektrowania_sloneczna.get_info())
elektrowania_hybrydowa = elektrownia_wiatrowa + elektrowania_sloneczna
print(elektrowania_hybrydowa.get_info())
# %% Zadanie 4

class Fraction():
    def __init__(self, a, b):
        dzielnik = math.gcd(a,b)
        self.licznik = int(a / dzielnik)
        self.mianownik = int (b / dzielnik)

    def __repr__(self):
        return f"{self.licznik}/{self.mianownik}"
    
    def __str__(self):
        if self.licznik > self.mianownik:
            calosc = self.licznik // self.mianownik
            self.licznik = self.licznik % self.mianownik
            if self.licznik == 0:
                return f"{calosc}"
            else:
                return f"{calosc} {self.licznik}/{self.mianownik}"
        else:
            return f"{self.licznik}/{self.mianownik}"


    def __add__(self,other):
        nowy_licznik = (self.licznik * other.mianownik) + (other.licznik * self.mianownik)
        nowy_mianownik = self.mianownik * other.mianownik
        return Fraction(nowy_licznik,nowy_mianownik)
    
    def __sub__(self,other):
        nowy_licznik = (self.licznik * other.mianownik) - (other.licznik * self.mianownik)
        nowy_mianownik = self.mianownik * other.mianownik
        return Fraction(nowy_licznik,nowy_mianownik)
    
    def __mul__(self, other):
        nowy_licznik = self.licznik * other.licznik
        nowy_mianownik = self.mianownik * other.mianownik
        return Fraction(nowy_licznik,nowy_mianownik)


    def __truediv__(self,other):
        nowy_licznik = self.licznik * other.mianownik
        nowy_mianownik = self.mianownik * other.licznik
        return Fraction(nowy_licznik,nowy_mianownik)

    def __abs__(self):
        return Fraction(abs(self.licznik), self.mianownik)
    
    def __eq__(self, other):
        return self.licznik == other.licznik and self.mianownik == other.mianownik

    def __ne__(self, other):
        return not self.licznik == other.licznik and self.mianownik == other.mianownik

    def __lt__(self, other):
        return self.licznik/self.mianownik < other.licznik/other.mianownik

    def __le__(self, other):
        return self.licznik/self.mianownik < other.licznik/other.mianownik or self.licznik == other.licznik and self.mianownik == other.mianownik

    def __gt__(self, other):
        return self.licznik/self.mianownik > other.licznik/other.mianownik

    def __ge__(self, other):
        return self.licznik/self.mianownik > other.licznik/other.mianownik or self.licznik == other.licznik and self.mianownik == other.mianownik
        


    def __float__(self):
        return float(self.licznik/self.mianownik)
    
    def __int__(self):
        return int(self.licznik/self.mianownik)
    
    def __bool__(self):
        return bool(self.licznik/self.mianownik)

    def __round__(self,digits):
        return round(self.licznik/self.mianownik, digits)



f = Fraction(3, 4)
print(f)

print(Fraction(2, 4) + Fraction(4, 4))
print(Fraction(2, 4) - Fraction(4, 4))
print(Fraction(1, 2) * Fraction(3, 4))
print(Fraction(4, 5) / Fraction(3, 7))
print(abs(Fraction(-69,13)))

print(Fraction(3, 7) == Fraction(6, 14))
print(Fraction(3, 7) != Fraction(6, 14))
print(Fraction(3, 7) < Fraction(6, 14))
print(Fraction(3, 7) <= Fraction(6, 14))
print(Fraction(3, 7) > Fraction(6, 14))
print(Fraction(3, 7) >= Fraction(6, 14))

print(float(Fraction(1, 3)))
print(int(Fraction(2, 4)))
print(bool(Fraction(2, 4)))

print(round(Fraction(1, 3),2))







