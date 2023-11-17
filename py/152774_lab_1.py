import math
import random

# ZADANIE 1
def zadanie1():
    arr = [1, 1.5, "tekst"]
    print(arr)

# zadanie1()

# ZADANIE 2
def zadanie2():
    num1 = int(input("Podaj liczbe 1"))
    num2 = int(input("Podaj liczbe 2"))
    print(num1 * num2)
    if num2 == 0:
        print("nie mozna dzielic przez 0")
    else:
        print(num1 / num2)

# zadanie2()

# ZADANIE 3
def zadanie3():
    num = int(input("Podaj liczbe: "))
    if num % 2 == 0:
        print(num / 2)
    else:
        print(num**3)

# zadanie3()

# ZADANIE 4
def zadanie4():
    print(f'"Hello, { input("Podaj imie")}!"')

# zadanie4()


# ZADANIE 5
def zadanie5():
    r = float(input("Podaj dlugosc r"))
    h = float(input("Podaj dlugosc h"))

    print(h * math.pi * r ** 2)


# zadanie5()


# ZADANIE 6
def zadanie6():
    for i in range(5):
        print(i)
    for i in range(5, 11):
        print(i)
    for i in range(0,10,3):
        print(i)
    for i in range(0,-10,-2):
        print(i)


# zadanie6()


# ZADANIE 7
def zadanie7():
    arr = []
    while True:
        word = input("Wpisz słowo")
        if word == "koniec":
            break
        arr.append(word)

    print(arr)

# zadanie7()


# ZADANIE 8
def zadanie8():
    arr = [5,3,2,2,213,123,3,23,-123,2]
    maks = arr[0]
    maks_i = 0
    mini = arr[0]
    mini_i = 0

    for i,num in enumerate(arr):
        if num > maks:
            maks = num
            maks_i = i
        if num < mini:
            mini = num
            mini_i = i
    print("Najwieksza wartość: ", maks , "pod indeksem: ", maks_i)
    print("Najmniejsza wartość: ", mini , "pod indeksem: ", mini_i)

# zadanie8()

# ZADANIE 9
def zadanie9():
    a = float(input("Podaj bok a: "))
    b = float(input("Podaj bok b: "))
    c = float(input("Podaj bok c: "))
    a,b,c = a**2,b**2,c**2

    if a + b == c or a + c == b or b + c == a:
        print("Trojkat jest prostokatny")
    else:
        print("Trojkat nie jest prostokatny")

# zadanie9()



# ZADANIE 10
def zadanie10():
    check = 0
    pkt1 = [1,2]
    pkt2 = [3,1]
    pkt3 = [int(input("współrzędna 1")), int(input("współrzędna 2"))]
    if pkt2[0] >= pkt3[0] >= pkt1[0] or pkt1[0] >= pkt3[0] >= pkt2[0]:
        check += 1



    if pkt2[1] >= pkt3[1] >= pkt1[0] or pkt1[0] >= pkt3[1] >= pkt2[1]:
        check += 1
    if check == 2:
        print ("Punkt znajduje sie w środku")
    else:
        print("Punkt nie leży w środku")

# zadanie10()


# ZADANIE 11
def zadanie11():
    num = int(input("Podaj liczbe"))
    sum = 0
    while num > 0:
        sum += num % 10
        num //= 10
    print(sum)

# zadanie11()



# ZADANIE 12
def zadanie12():
    text = input("Napisz cos: ")
    print(len(text))
    print(text[3])
    print(text[-2])
    print(text[:11])
    print(text[:-5])
    print(text[5:-5])
    text = text[::-1]
    text = text[slice(0,-1,2)]
    print(text)

# zadanie12()


# ZADANIE 13
def zadanie13():
    text = input("Podaj tekst: ")
    text = "".join(text.split(" "))
    text2 = ""
    for i in range(len(text),0,-1):
        text2 += text[i-1]

    if text2 == text:
        print("Tekst jest palindromem")
    else:
        print("Tekst nie jest palindromem")

# zadanie13()

# ZADANIE 14
def zadanie14():
    text = input("Podaj tekst: ")
    text = text.split()
    for i in range(1, len(text), 2):
        text[i] = text[i].replace("a","A")
        text[i-1] = text[i-1].capitalize()
    text = " ".join(text)
    print(text)


# zadanie14()

# ZADANIE 15
def zadanie15(n):
    if n == 0:
        arr = [0]
    else:
        arr = [0,1]
        for i in range(2, n + 1):
            arr.append(arr[i-1] + arr[i-2])

    print(arr)


# zadanie15(999)


# ZADANIE 16
def zadanie16():
    arr1 = [1, 4, 3, 5, 2]
    arr2 = [4, 2, 1, 5, 3]
    arr = list(zip(arr1,arr2))
    print("Lista 1: ", arr1)
    print("Lista 2: ", arr2)
    print("Wynik działania programu:")
    for item in arr:
        if item[0] != item[1]:
            print(item[0], " + ", item[1], " = ", item[0] + item[1])
        else:
            print(item[0], " * ", item[1], " = ", item[0] * item[1])
            

# zadanie16()


# ZADANIE 17
def zadanie17():
    arr = ["apple","orange", "apple", "cherry","ala", "banana","aaaaaaaa","ads"]
    for i,word in enumerate(arr):
        try:
            if word[i] == "a":
                print(i , word, " <--")
            else:
                print(i , word)
        
        except:
            print(i , word)


# zadanie17()


# ZADANIE 18
def zadanie18():
    rng = random.randrange(1000)
    while True:
        guess = int(input("Zgadnij liczbe: "))
        if guess == rng:
            print("Wygrałeś!")
            break
        elif guess < rng:
            print("Twoja liczba jest mniejsza od szukanej")
        else:
            print("Twoja liczba jest większa niż szukana")

            
# zadanie18()


# ZADANIE 19
def zadanie19():
    arr = [random.randrange(10) for _ in range(10)]
    result = {}
    count = 0
    for num in arr:
        for num2 in arr:
            if num == num2:
                count += 1
        result[num] = count
        count = 0
    print(result)


# zadanie19()


# ZADANIE 20
def zadanie20():
    while True:
        text = input('Podaj "polecenie" i "jakieś słowa"')
        if text == "":
            break
        words = text.split()
        command = words[0].lower()
        text = ' '.join(words[1:])
        if command == "lower":
            print(text.lower())
        elif command == "upper":
            print(text.upper())
        elif command == "title":
            print(text.title())
        elif command == "reversed":
            print(text[::-1])
        else:
            print("Nieznane polecenie")
        


# zadanie20()




