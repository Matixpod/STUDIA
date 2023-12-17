# %%
from collections import deque
# %%

def zadanie1(napis):
    s = deque()
    for sym in napis:
        if sym == '[':
            s.append('[')
        elif sym == ']':
            if len(s) == 0:
                return False
            sym2 = s.pop()
            if  sym2 != '[':
                return False

        if sym == "(":
            s.append(sym)
        elif sym == ")":
            if len(s) == 0:
                return False
            sym2 = s.pop()
            if  sym2 != '(':
                return False


    return len(s) == 0
    
zadanie1('a = [(3, 5), (2, 5), (2, 9)]')



# %%%%%
def zadanie2_wersja_1(arr):
    arr_deque = deque(arr)
    stack_left = deque()
    stack_right = deque()
    max_val = max(arr_deque)
    min_val = min(arr_deque)

    max_i = arr_deque.index(max_val)
    min_i = arr_deque.index(min_val)

    stack_left.append(arr_deque[min_i])
    stack_right.append(arr_deque[max_i])
    arr_deque.remove(min_val)
    arr_deque.remove(max_val)

    stack_left.append(arr_deque.popleft())

    while len(arr_deque) > 0:
        element = arr_deque.popleft()
        if element < stack_left[-1]:
            stack_right.append(stack_left.pop())
            stack_left.append(element)
        else:
            counter = 0
            while element > stack_right[-1]:
                stack_left.append(stack_right.pop())
                counter += 1
            stack_right.append(element)
            for _ in range(counter):
                stack_right.append(stack_left.pop())
            

    while stack_left:
        stack_right.append(stack_left.pop())
        
    return list(stack_right)

print(zadanie2_wersja_1([900,5,2,16,9,6,3678,10,2,3]))

# %%

def zadanie2_wersja_2(arr):
    arr_deque = deque(arr)
    stack_left = deque()
    stack_right = deque()

    while arr_deque:
        element = arr_deque.popleft()
        if not stack_left or element <= stack_left[-1]:
            stack_left.append(element)
        else:
            while stack_left and element > stack_left[-1]:
                stack_right.append(stack_left.pop())
            stack_left.append(element)
            while stack_right:
                stack_left.append(stack_right.pop())
            
    return list(stack_left)



print(zadanie2_wersja_2([9,5,2,1,9,6,3,10,2,3]))

# %%


def zadanie3(line):
    line = deque(line)
    exit = deque()
    while line:
        name, send = line.popleft()
        if send == True:
            send = False
            line.append((name, send))
        elif send == False:
            exit.append((name, send))

    return line,exit



zadanie3([('Grażyna', True),('Laura', False),('Bartek', False),('Andrzej', True),('Wiesiek', False)])