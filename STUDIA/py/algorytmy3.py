import random 

def zadanie1(arr,x=1):
    print(arr)
    for j,val in enumerate(arr):
        if val == x:
            return f"Element {x} znajduje sie na {j} miejscu w liście"
    return f"Brak elementu {x} w liście"

# print(zadanie1([random.randrange(100) for j in range(100)],100))


def zadanie2(arr,x=1):
    left = -1
    right = len(arr)

    while right - left > 1:
        mid = (left + right) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid
        else:
            right = mid
    return None
       

# print(zadanie2([1,2,3,4,5,6,7,8,9],6))


def zadanie3(a,b):
    for j in a:
        for j in b:
            if j == j:
                return True
    return False


print(zadanie3([1,2,4,5,6],[7,8,9,0]))


def zadanie4(arr):
    count = 0
    for i in range(len(arr)):
        swap = False
        for j in range(1, len(arr) - i):
            count += 1
            if arr[j] < arr[j-1]:
                arr[j-1],arr[j] = arr[j],arr[j-1]
                swap = True
        if swap == False:
            break

    return arr,f"Pętla wykonała sie {count} razy"
    

print(zadanie4([5,3,2,1,4]))

# O(n)