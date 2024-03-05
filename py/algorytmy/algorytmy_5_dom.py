# %%
import random
import string
from builtins import hash

# %%
def zadanie1():
    with open(r'..\pliki_do_zadan\wsb_pliki\pg11.txt',encoding="utf8") as file:
        counter = {}
        for line in file:
            words = line.split()
            for word in words:
                word = word.lower()
                if word not in counter:
                    counter[word] = 0
                else:
                    counter[word] += 1
        counter = sorted(counter.items(), key=lambda x: x[1],reverse=True)     
        print(counter[:10])


zadanie1()

# %%%%%

def zadanie2(n):
    if n <= 1:
        return None
    cache = {}

    for i in range(1,n):
        num = i
        steps = 1
        while i != 1:
            if i in cache:
                steps += cache[i] - 1
                break
            steps += 1
            i = i // 2 if i % 2 == 0 else 3 * i + 1
        cache[num] = steps
    print(max(cache, key=cache.get))

zadanie2(1000000)

# %%


def djb2(key):
    h = 5381
    for c in key:
        h += h * 33 + ord(c)
    return h % 997

def zadanie3(target,lenght = 8):

    while True:
        combination = ''.join(random.choice(string.ascii_lowercase) for _ in range(lenght))
        hash = djb2(combination)
        if hash == target:
            return combination


zadanie3(42) 

# %%


def pobierz(T, key):
    idx = djb2(key) % len(T)
    
    if T[idx] and T[idx][0] == key:
        return T[idx][1]
    
    for i in range(len(T)):
        current_idx = (idx + i) % len(T)
        
        if not T[current_idx]:
            return None
        
        if T[current_idx][0] == key:
            return T[current_idx][1]
    
    print("Błąd: Klucz nie znaleziony")
    return None

arr = [None] * 10
arr[djb2("klucz") % len(arr)] = ("klucz", "wartosc")

wynik = pobierz(arr, "klucz")
print(wynik)




