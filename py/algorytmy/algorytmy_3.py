# %%

def zadanie1(n):
    a = 0
    b = 1
    for _ in range(n):
        a,b = b, a + b
    return a

print(zadanie1(6))



def zadanie1b(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return zadanie1b(n-1) + zadanie1b(n-2)

zadanie1b(6)

# %%

def zadanie2(a,x,lewo,prawo):
    if lewo <= prawo:
        mid = (lewo + prawo) // 2
        if a[mid] == x:
            return mid
        elif a[mid] < x:
            return zadanie2(a,x,mid + 1,prawo)
        else:
            return zadanie2(a,x,lewo,mid - 1)
    else:
        return -1

lista = [1,2,3,4,5,6,7,8,9]
cel=4
wynik=zadanie2(lista,cel,0,len(lista)-1)

if wynik != -1:
    print(f'Znaleziono wartość {cel} na indeksie {wynik}.')
else:
    print(f'Wartość {cel} nie została znaleziona.')

# %%

def zadanie3(a,b,c=[]):
    if a == [] and b == []:
        print(c)
        return c

    if not a:
        c.append(b.pop(0))
        zadanie3(a,b,c)

    if not b:
        c.append(a.pop(0))
        zadanie3(a,b,c)
        
    try:
        if b == [] or a[0] < b[0]:
            c.append(a.pop(0))
            zadanie3(a,b,c)
        elif a == [] or a[0] > b[0]:
            c.append(b.pop(0))
            zadanie3(a,b,c)
    except:
        zadanie3(a,b,c)

print(zadanie3([1,2,4],[3,5,7]))


# %%


def zadanie3i(a,b):
    c = []
    while a != [] and b != []:
        if a[0] < b[0]:
            c.append(a.pop(0))
        else:
            c.append(b.pop(0))

    if not a:
        c.append(b.pop(0))
    else:
        c.append(a.pop(0))
    return c



zadanie3i([1,2,5,7],[3,4,6])    

def zadanie3b(arr):
    if len(arr) <= 1:
        return arr
    else:
        mid = len(arr)//2
        left = arr[:mid]
        right = arr[mid:]
        left_sort = zadanie3b(left)
        right_sort = zadanie3b(right)
        return zadanie3i(left_sort,right_sort)



zadanie3b([4,2,1,5,3,345,34,2])


# %%

def zadanie4(n,left,middle,right):
    if n == 1:
        print(f"przenieś dysk 1 z {left} do {right}")
        return
    
    zadanie4(n-1,left,right,middle)
    print(f"przenieś dysk {n} z {left} do {right}")
    zadanie4(n-1,middle,left,right)


zadanie4(5,'A','B','C')








