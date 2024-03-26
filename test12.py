def infinite_recursion():
    infinite_recursion()

try:
    infinite_recursion()
except RecursionError:
    print("Przepełnienie stosu!")