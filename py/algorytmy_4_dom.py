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
     
              
    if len(s) == 0:
        return True
    else:
        return False
    
zadanie1('a = [(3, 5), (2, 5), (2, 9)]')


# %%%%%

def zadanie2(arr):
    stack_left = deque()
    stack_right = deque()
    stack_left.append(arr.pop(arr.index(min(arr))))
    stack_right.append(arr.pop(arr.index(max(arr))))
    stack_left.append(arr.pop(0))

    for num in arr:
        num2 = stack_left.pop()
        if num2 > num:
            stack_right.append(num2)
            stack_left.append(num)
        else:
            while num2 < num:
                stack_left.append(num2)
                num2 = stack_right.pop()
            if num2 == num:
                stack_right.append(num)
                stack_right.append(num2)
            stack_right.append(num)

    while stack_left:
        stack_right.append(stack_left.pop())
    return stack_right


zadanie2([9,5,2,1,9,6,3])















