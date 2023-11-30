# %%
import random
# %%
def zadanie1(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

print(zadanie1([random.randrange(100) for _ in range(10)]))
# Złożoność obliczeniowa tego algorytmu to O(n) ponieważ długość wykonywania funkcji zależy od długości wprowadzonej listy
# %%

def zadanie2(arr):
    for i in range(1,len(arr)):
        x = 0
        while arr[i-1-x] > arr[i - x] and i - x != 0:
            arr[i-1-x],arr[i-x] = arr[i-x],arr[i-x-1]
            x+=1
    return arr

print(zadanie2([random.randrange(100) for _ in range(10)]))
# Złożoność obliczeniowa tego algorytmu to O(n^2) ponieważ mamy pętle zagnieżdżoną w pętli co oznacza że pętle sie wykonają w najgorszym przypadku w liczbie dlugości funkcji do kwadratu
# %%

def zadanie3(s1,s2):
    counter = 0
    for letter1 in s2:
        for letter2 in s1:
            if letter1 == letter2:
                counter += 1
    print(counter)

zadanie3('ala ma kota', 'aoiuye')
# Złożoność obliczeniowa tego algorytmu to O(n*m) ponieważ mamy 2 pętle o różnych długościach które są zagnieżdżone w sobie co oznacza że w najgorszym przypadku petla wykona sie w dlugość 1 ciagu znaków * 2 ciągu znaków
# %%

def zadanie4(arr):
    n = len(arr)
    mid = n // 2
    if n % 2 == 0:
        return (arr[mid - 1] + arr[mid]) / 2
    else:
        return arr[mid]

print(zadanie4([1,2,3,4,5,6,7,8,9,10]))
# Złożoność tego algorytmu to O(1) ponieważ funkcja zawsze sprawdza tylko 2 środkowe elementy listy