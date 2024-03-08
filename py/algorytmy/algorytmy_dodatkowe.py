def metoda_Babilonska(s):
    x = [s / 2]
    n = 0

    while abs(x[n-1] - x[n]) > 0.1 or n < 1:
        x.append((x[n] + s/x[n])/2)
        n += 1
    print(x[-1])

# metoda_Babilonska(125348)


def druga_najwieksza(arr):
    max_num = arr[0]
    second_max = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
        if num < second_max:
            second_max = num
    for num2 in arr:
        if num2 > second_max and num2 < max_num:
            second_max = num2
    print(second_max)


# druga_najwieksza([4,1,2,1,2,4])


def collatz(n):
    if n == 1:
        print(n)

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        print(n)
    

# collatz(11)

def zadanie5():
    arr = input("Podaj liczby po spacji: ").split()
    count = 0
    for num in arr:
        if int(num) % 2 == 0:
            count += 1
    if count == len(arr):
        print("Wszystkie liczby są parzyste")
    else:
        print("Nie wszystkie liczby są parzyste")

# zadanie5()

def zadanie6(arr):
    check = True
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            check = False
            break

    if check == True:
        print("Jest posortowana")
    else:
        print("Nie jest posortowana")

# zadanie6([1, 2, 3, 4, 7])


def zadanie7():
    arr1 = [1, 2, 5, 7]
    arr2 = [3,4,6]
    arr = []
    while arr1 != [] and arr2 != []:
        if arr1[0] < arr2[0]:
            arr.append(arr1.pop(0))
        else:
            arr.append(arr2.pop(0))

    if not arr1:
        arr.append(arr2.pop(0))
    else:
        arr.append(arr1.pop(0))
    print(arr)

# zadanie7()