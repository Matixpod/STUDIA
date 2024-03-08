# %%
import random
from collections import deque
import math
# %%
def zadanie1(napis):
    s = deque()
    for sym in napis:
        print(s)
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
        

zadanie1('((2 + 5) * (2 + 3)) / 2')

# %%


def zadanie2(napis):
    s = deque()
    napis = napis.split()
    for sym in napis:
        try:
            sym = float(sym)
            s.append(sym)
        except:

            print(s,sym)
            num = s.popleft()
            while len(s) != 0:
                if sym == '+':
                    num += s.pop()
                elif sym == '-':
                    num -= s.pop()
                elif sym == '*':
                    num *= s.pop()
                elif sym == '/':
                    num /= s.pop()
            s.append(num)
            print(num)
           

zadanie2('2 7 + 3 / 14 3 - 4 * + 2 /')
# %%


def zadanie3(processes, n, p, max_time):
    completed_processes = []
    processes_queue = deque(processes)
    time = 0
    while processes_queue and time <= max_time:
        name, duration = processes_queue.popleft()
        if duration > n:
            duration -= n
            if random.random() < p:
                duration += random.randrange(0,100)
            processes_queue.append((name, duration))
        else:
            duration = 0
            completed_processes.append(name)

        time += n
    return f'Zakończone procesy: {completed_processes} \nPozostałe procesy: {processes_queue}'
    

processes = [
        ('git status', 150),
        ('python calculations.py', 230),
        ('gcc main.c', 130),
        ('screenshot', 100)
        ]

print(zadanie3(processes, n=10, p=0.2, max_time=1000))

# %%











