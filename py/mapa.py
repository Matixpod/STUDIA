

# sourcery skip: remove-redundant-if
lista = ['tekst',65,"tekst2"]

tekst = "tekst"
tekst2 = 'inny tekst'

krotka = ('tekst', 65)

krotka = tuple(lista)

sprawdzenie = 65 in krotka

słownik = {
        'klucz1': 'wartość1',
        'klucz2': 2
            }


słownik['klucz1'] = 'zmieniona wartość'

słownik['klucz3'] = 'nowa wartość'
warunek = 0
# for element in lista:

# for i in range(5):

age = 20

if age < 18:
    print("Jesteś niepełnoletni")
elif age >= 18 and age < 65:
    print("Jesteś dorosły")
else:
    print("Jesteś senior")




def nazwa_funkcji(argumenty):
    # Kod funkcji
    return wynik

# %%

def przywitanie(imie, wiek):
    print(f"Witaj, {imie}! Masz {wiek} lat.")

przywitanie("Anna", 30)  # Argumenty pozycyjne
przywitanie(wiek=25, imie="Tomek")  # Argumenty nazwane