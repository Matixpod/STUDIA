# %%
import itertools
import math
import random
import collections
# %%


def zadanie1():
    arr = [random.randrange(11) for _ in range(51)]
    dict = collections.Counter(arr)
    return dict.most_common(5)

print(zadanie1())

# %% 


def zadanie2(text):
    error = itertools.permutations(text,3)
    test2 = itertools.combinations(text,3)
    print(f"Napis pobrany od użytkownika: {text}")
    print("Permutacje:", " ". join(i[0]+i[1]+i[2] for i in list(error)))
    print("Kombinacje:", " ". join(i[0]+i[1]+i[2] for i in list(test2)))

zadanie2("ABC")
# %%

def zadanie3(a):
    if len(a) != 2:
        raise ValueError('Wprowadzona macierz o złym wymiarze! \nWprowadź macierz o wymiarze 2x2.')
    return a[0][0] * a[1][1] - a[1][0] * a[0][1]


zadanie3([[1,2]])
# %%


def zadanie5(a,b,c):
    delta = b**2 - 4 * a * c

    try:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        return f"{x1} {x2}\n" if x1 != x2 else f"{x1}\n"
    except ValueError:
        return f"\n"


def zadanie5b():
    with open('G:/Users/mateu/Pulpit/Github/STUDIA/pliki_do_zadan/equations.txt','r') as file:
        with open('G:/Users/mateu/Pulpit/Github/STUDIA/pliki_do_zadan/equations_results.txt','w') as file2:
            for i in file:
                nums = i.split()
                file2.write(zadanie5(int(nums[0]),int(nums[1]),int(nums[2])))

zadanie5b()
# %%

def zadanie6(n):
    if n <= 1 or  (n != 2 and n % 2 == 0):
        return 'nie jest liczba pierwsza'
    else:
        for i in range(int(math.sqrt(n)), 4, -2):
            if n % i == 0:
                return 'nie jest liczba pierwsza'
    return 'jest liczba pierwsza'




def zadanie6b(n=30):
    if n == 0:
        arr = [0]
    else:
        arr = [0,1]
        arr.extend(arr[i-1] + arr[i-2] for i in range(2, n + 1))
    
    for i in arr:
        print(f'Liczba {i} {zadanie6(i)}')

zadanie6b()