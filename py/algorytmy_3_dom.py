# %%

def zadanie1(n):
    return 1 if n == 1 else n * (zadanie1(n - 1))

zadanie1(15)
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

zadanie3(42,56)

# %%


def zadanie4(arr):
    curr = arr[0]
    arr_left = []
    arr_right = []
    for i in arr:
        if i < curr:
            arr_left.append(i)
        else:
            arr_right.append(i)
    return arr if arr == arr_left + arr_right else zadanie4(arr_left + arr_right)

zadanie4([6,3,1,7,8,2,5,4])


















