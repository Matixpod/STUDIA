# %%
import random

# %% Zmienne
num = 69
float = 3.23
bool = True
strng = "Hello World!"
arr = [69, 3.23, True, "Hello World"]

print(num,float,bool,arr)

# %%
l = []
l1 = [1,2,3]
l2 = [4,5,6]

l3 = l1+l2
l4 = l2+l1

print(l3,l4)
print(len(l3))
print(l3.index(1))
print(l3.index(max(l3)))

print("=====")


for v1,v2 in zip(l1,l2):
    print(v1,v2)

print("=====")

for i,val in enumerate(l4):
    print(i,val)


# %%
def sumka(num):
    suma = 0
    while num > 0:
        suma += num % 10
        num //= 10
    return suma

sumka(1234)

# %%
arr = ['lol', 'test','tekst','dupa']

print(" ".join(arr))

# %%

def interdiff(arr1, arr2):
    print(set(arr1 + arr2))
    set1 = {i for i in arr1}
    set2 = {i for i in arr2}
    print(set1.intersection(set2))
    print(set1.difference(set2))


interdiff([random.randrange(11) for i in range(11)],[random.randrange(11) for i in range(11)])

# %%


def lambdos():
    
    print(lambda x,y: f"siema to jakas liczba {x+y}")
    print(print(x(34,12)))


lambdos()

# %%

def test(n):

    return lambda x: x*n


test(2)(5)