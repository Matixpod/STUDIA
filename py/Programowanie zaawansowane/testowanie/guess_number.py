import random

def zgadnij_liczbe():
    # Pobranie maksymalnego zakresu od użytkownika
    max_liczba = int(input("Podaj maksymalną liczbę dla zakresu zgadywania: "))

    # Losowanie liczby w zakresie od 0 do max_liczba
    liczba_do_zgadniecia = random.randint(0, max_liczba)

    # Inicjalizacja zmiennej liczącej próby
    proby = 0
    odgadnieta = False

    print(f"Zgadnij liczbę od 0 do {max_liczba}!")

    # Pętla zgadywania
    while not odgadnieta:
        proby += 1
        guess = int(input("Podaj swoją liczbę: "))

        if guess < liczba_do_zgadniecia:
            print("Za mało! Spróbuj wyżej.")
        elif guess > liczba_do_zgadniecia:
            print("Za dużo! Spróbuj niżej.")
        else:
            print(f"Brawo! Zgadłeś liczbę {liczba_do_zgadniecia} w {proby} próbach.")
            odgadnieta = True

        print()

# Uruchomienie gry
zgadnij_liczbe()

# Testowanie
# 1. OK
# 2. OK
# 3. OK
# 4. OK
# 5. OK
# 6. OK
# 7. OK
# 8. Brak komunikatu o błędzie (należy dodać ewentualność)
# 9. OK
# 10. Nie można podac przedzialu zaczynajacego sie nie od 0 ponieważ uzytkownik moze podac jedynie górną granice.
# 11. Brak komunikatu o błędzie (należy dodać ewentualność)








