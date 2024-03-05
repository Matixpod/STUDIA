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



elektrownia_wiatrowa = Energia_Odnawialna("Wiatr", 50, "Niemcy")
elektrowania_sloneczna = Energia_Odnawialna("Slonce", 30, "Polska")



# %%

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
        nowy_mianownik = self.mianownik * other.mianownik
        nowy_licznik1 = self.licznik * other.mianownik
        nowy_licznik2 = other.licznik * self.mianownik
        print(f"{nowy_licznik1}/{nowy_mianownik} + {nowy_licznik2}/{nowy_mianownik}")
        

f = Fraction(3, 4)
print(f)

Fraction(1, 4) + Fraction(2, 4)







