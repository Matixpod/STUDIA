import random
import string

def generator_hasla():
    # Zapytanie o długość hasła
    dlugosc = int(input("Podaj długość hasła: "))

    # Ustawienia dla dodatkowych znaków
    uzyj_duzych_liter = input("Czy chcesz włączyć duże litery? (t/n): ").lower() == 't'
    uzyj_cyfr = input("Czy chcesz włączyć cyfry? (t/n): ").lower() == 't'
    uzyj_znakow_specjalnych = input("Czy chcesz włączyć znaki specjalne? (t/n): ").lower() == 't'

    # Tworzenie puli znaków
    znaki = string.ascii_lowercase  # Małe litery jako domyślny zestaw
    if uzyj_duzych_liter:
        znaki += string.ascii_uppercase
    if uzyj_cyfr:
        znaki += string.digits
    if uzyj_znakow_specjalnych:
        znaki += string.punctuation

    # Generowanie hasła
    haslo = ''.join(random.choice(znaki) for _ in range(dlugosc))

    print("Wygenerowane hasło:", haslo)

# Uruchomienie generatora
generator_hasla()

# Testowanie
# 1. OK
# 2. OK
# 3. OK
# 4. OK
# 5. OK
# 6. OK
# 7. OK
# 8. OK
# 9. Program nie obsługuje błędnych danych wejściowych (np. ujemnej długości hasła, niepoprawnych znaków) nie prosi o podanie prawidłowych.
# 10. Program ignoruje błędne znaki wejściowe przy pytaniach i kontynuuje działanie z domyślną wartością "nie".









