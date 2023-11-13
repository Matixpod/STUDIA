import math
import random
# l = []
# l1 = [1,2,3]
# l2 = [4,5,6]

# l3 = l1+l2
# l4 = l2+l1

# print(l3,l4)
# print(len(l3))
# print(l3.index(1))
# print(l3.index(max(l3)))

# print("=====")


# for v1,v2 in zip(l1,l2):
#     print(v1,v2)

# print("=====")

# for i,val in enumerate(l4):
#     print(i,val)


# ZADANIE 1
def zadanie1(x):
    return x**3 - 3*x**2 + 8*x - 2

# print(zadanie1(10))


# ZADANIE 2
def zadanie2(a,b = 0):

    if a == 0:
        if b == 0:
            return "nieskończenie wiele rozwiązań"
        else:
            return "Brak rozwiązań"
    else:
        x = (-b) / a
        return f"Rozwiązanie równania liniowego: {x}"
    

# print(zadanie2(0,2))

# ZADANIE 3
def zadanie3(list1):

    list2 = list1.copy()

    for i,element in enumerate(list2):
        if element % 4 == 0:
            del list2[i]

    list3 = list2.copy()
    j = 1
    for i,element in enumerate(list2):
        if element % 2 != 0:
            list3.insert(i-1+j,-1)
            j += 1
     
    return list3
        

# print(zadanie3([random.randrange(10) for i in range(0,10)]))


# ZADANIE 4
def zadanie4(a = 0,b = 10,n = 10):
    return [random.randrange(a,b+1) for i in range(n)]

# print(zadanie4(0,100,100))

# ZADANIE 5
def zadanie5(n):
    arr = [random.randrange(0,10) for i in range(n)]
    print(arr)
    print(min(arr))
    print(arr.index(max(arr)))
    print(sum(arr))
    print(arr.sorted())
    print(arr.count(3))
    print(set(arr))
    
# zadanie5(10)


# ZADANIE 6
def zadanie6(text):
    arr = []
    for i,val in enumerate(text):
        for j in range(i+1,len(text)):
            arr.append(val+text[j])
    return arr


# print(zadanie6("ABCD"))

# ZADANIE 7
def zadanie7():
    arr1 = [i**3 for i in range(11)]
    print(arr1)
    arr2 = [i**3 for i in range(11) if i**3 % 3 == 0]
    print(arr2)
    arr3 = [i**3 if i % 3 == 0 else i**2 for i in range(11)]
    print(arr3)

# zadanie7()


# ZADANIE 8
def zadanie8():
    arr = [random.randrange(-10,10) for i in range(20)]
    arr = sum([i**2 if i < 0 else 0 for i in arr])
    return arr

# zadanie8()



# ZADANIE 9
def zadanie9(x):
    if type(x) == int:
        return x**2
    else:
        arr = [i**2 for i in x]
        return arr
    
# print(zadanie9([2,4,5,43,4]))


# ZADANIE 10
def zadanie10(x):
    return "".join([chr(i) for i in x])

# print(zadanie10([random.randrange(97,123) for i in range(11)]))


# ZADANIE 11
def zadanie11(arr1, arr2):
    print(set(arr1 + arr2))
    set1 = {i for i in arr1}
    set2 = {i for i in arr2}
    print(set1.intersection(set2))
    print(set1.difference(set2))


# zadanie11([random.randrange(11) for i in range(11)],[random.randrange(11) for i in range(11)])


# ZADANIE 12
def zadanie12():
    słownik = {
        'banana' : 'banan',
        'cherry' : 'wiśnia',
        'apple': 'jabłko',
        'pear': 'gruszka',
        'watermelon': 'arbuz'
    }
    translate = input("Wprowadź słowo: ")
    while translate != "":
        if translate in słownik:
            print(słownik[translate])
        else:
            check = input("Nie ma takiego słowa! Czy chcesz dodać słowo do słownika? [tak/nie]: ")
            if check == "tak":
                translated = input("Podaj tłumaczenie słowa: ")
                słownik[translate] = translated
        translate = input("Wprowadź słowo")
        
        

# zadanie12() 
































