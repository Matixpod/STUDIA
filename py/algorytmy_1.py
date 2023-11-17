def zadanie1():
    num1 = int(input("Podaj liczbe"))
    if num1 % 3 == 0 and num1 % 5 ==0:
        print(f"{num1} jest podzielne przez 3 i 5")
    elif num1 % 3 ==0:
        print(f"{num1} jest podzielne przez 3")
    elif num1 % 5 == 0:
        print(f"{num1} jest podzielne przez 5")
    else:
        print(f"{num1} nie jest podzialne przez 3 ani 5")


# zadanie1()

def zadanie2():
    a = int(input("Podaj a0"))
    r = int(input("Podaj r"))
    n = int(input("Podaj n"))
    i = 0
    suma = 0
    while i < n:
        suma += a
        a += r
        i += 1
    print(suma)

# zadanie2()

def zadanie3():
    arr = input("podaj liczby po spacji").split()
    arr = [int(i) for i in arr]
    iloczyn = 1
    suma = 0
    for i in arr:
        iloczyn *= i
        suma += i
    print(iloczyn, suma)


# zadanie3()

def zadanie4():
    a = int(input("podaj a"))
    b = int(input("podaj b"))
    x = (-b) / a
    print(f"Rozwiązanie równania liniowego: {x}")

# zadanie4()

def zadanie5():
    n = int(input("podaj liczbe"))
    check = all(n % i != 0 for i in range(2, n))
    if check:
        print(f"Liczba {n} jest liczbą pierwszą")
    else:
        print(f"Liczba {n} nie jest liczbą pierwszą")

zadanie5()

