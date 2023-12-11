# %%

def zadanie1(n):
    return 1 if n == 1 else n * (zadanie1(n - 1))

print(zadanie1(15))
# %%


def zadanie2(n):
    print(n)
    if n in [1, 0]:
        return n
    elif n % 2 == 0:
        return zadanie2(n//2)
    else:
        return zadanie2((3*n + 1))
    
zadanie2(13)

# %%



def zadanie3(a,b):
    return a if b == 0 else zadanie3(b, a % b)

print(zadanie3(42,56))

# %%


def zadanie4(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return zadanie4(left) + middle + zadanie4(right)

print(zadanie4([6,3,1,7,8,2,5,4]))


















