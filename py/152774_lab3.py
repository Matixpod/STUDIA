import random
import collections
import itertools
import math

def zadanie1():
    arr = [random.randrange(11) for i in range(51)]
    dict = collections.Counter(arr)    
    return dict.most_common(5)

# print(zadanie1())

def zadanie2(text):
    error = itertools.permutations(text,2)
    test2 = itertools.combinations(text,2)
    print(f"Napis pobrany od użytkownika: {text}")
    print("Permutacje:", " ". join(i[0]+i[1] for i in list(error)))
    print("Kombinacje:", " ". join(i[0]+i[1] for i in list(test2)))


# zadanie2("ABCD")

def zadanie3(a,b):
    arr = []
    sum = 0

    try:
        for i in range(len(a)):
            for i,val in enumerate(a[i]):
                sum += val * b[i]
            arr.append(sum)
            sum = 0
        return arr
    except TypeError as error:
        return "Błąd typu danych, podana macierz zamiast wektora:\n", error


zadanie3([[1, 2, 3],[4, 5, 6],[7, 8, 9]],[6, 4, 2])



# def zadanie4():


def zadanie5(a,b,c):
    delta = b**2 - 4 * a * c

    try:
        x1 = (-b - math.sqrt(delta)) / (2*a)
        x2 = (-b + math.sqrt(delta)) / (2*a)
        if x1 != x2:
            return f"Podane liczby: a = {a}, b = {b}, c = {c} \nx1 = {x1} \nx2 = {x2}\n"
        else:
            return f"Podane liczby: a = {a}, b = {b}, c = {c} \nx1 = {x1}\n"
    except ValueError:
        return f"Podane liczby: a = {a}, b = {b}, c = {c} \nDelta mniejsza od zera brak rozwiązań\n"

# zadanie5(4,4,1)

def zadanie5b():
    check = True
    arr = []
    while len(arr) < 3:
        data = input("Podaj wartosci po spacjach lub w osobnych wierszach: ").split()
        if data == []:
            check = False
            break
        for i in data:
            arr.append(int(i))

    if check == True:
        print(zadanie5(arr[0],arr[1],arr[2]))
        zadanie5b()


# zadanie5b()

def zadanie6(n):
    arr = [i for i in range(1,n)]
    for i,val in enumerate(arr):
        for j in range(i+1,n):
            if arr[j] % val == 0:
                del arr[j]
    print(arr)
                
        
zadanie6(10)













