# %%
import time

# %%
begin = time.time()
cache = {}
def fibo_cache(n):
    if n in cache:
        result = cache[n]
    elif n == 0:
        result = 0
    elif n == 1:
        result = 1
    else:
        result = fibo_cache(n-1) + fibo_cache(n-2)
    cache[n] = result
    return result


print(fibo_cache(320))
end = time.time()
print(f"Czas wykonania wersji cache: {end - begin:0.9f}s.")

# %%
begin = time.time()

def fibo_r(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibo_r(n-1) + fibo_r(n-2)

# print(fibo_r(320))
end = time.time()
print(f"Czas wykonania wersji rekurencyjnej: {end - begin:0.9f}s.")

# %%

begin = time.time()
def fibo_t(n):
    if n == 0:
        arr = [0]
    else:
        arr = [0,1]
        arr.extend(arr[i-1] + arr[i-2] for i in range(2, n + 1))
    return arr[-1]


print(fibo_t(320))
end = time.time()
print(f"Czas wykonania wersji z tablicą: {end - begin:0.9f}s.")

# %%
begin = time.time()

def fibo(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a



print(fibo(320))
end = time.time()
print(f"Czas wykonania wersji ze zmiennymi: {end - begin:0.9f}s.")

# %%
database = {}
def interfejs():
    while True:
        action = input("(a) Utwórz konto \n(b) Zaloguj się \n(c) Zakończ program: ")
        if action == "c":
            break
        elif action == "a":
            login = input("Podaj login")
            pswd = input("Podaj hasło")
            database[login] = djb2(pswd)
        elif action == "b":
            login = input("Podaj login")
            pswd = input("Podaj hasło")

            if database[login] == djb2(pswd):
                print(f"Witaj {login} zostałes zalogowany!")
            else:
                print("Wprowadziles niepoprawny login lub haslo.")
        else:
            print("Niepoprawne wprowadzenie, spróbuj ponownie")



interfejs()

def djb2(key):
    h = 5381
    for c in key:
        h += h * 33 + ord(c)
    return h


# %%

def create_hash_table(n, m):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def next_prime(num):
        while not is_prime(num):
            num += 1
        return num

    size = next_prime(m * n)
    hash_table = [None] * size
    return hash_table



def insert_into_hash_table(T,key,value):
    idx = hash(key) % len(T)
    if T[idx] is None or T[idx][0] == key:
        T[idx] = (key, value)
        return T

    for idx in range(len(T) - 1):
        if T[idx] is None or T[idx][0] == key:
            T[idx] = (key, value)
            return T

    raise Exception("Nie udało sie dodać klucz-wartość do tablicy hash")


def print_hash_table(n, m, key, value):
    T = create_hash_table(n,m)
    print(f"Tablica mieszająca o długości {len(T)}:")
    for i,val in enumerate(insert_into_hash_table(T,key,value)):
        print(i,val)


print_hash_table(4,5,"banan",12)