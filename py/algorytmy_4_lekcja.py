# %%
import collections
import math
import random
# %%
def zadanie1(napis):
    s = collections.deque()
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
    s = collections.deque()
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
    print(processes[0])




processes = [
        ('git status', 25),
        ('python calculations.py', 534),
        ('gcc main.c', 1348),
        ('screenshot', 105)
        ]

zadanie3(processes, n=4, p=0.2, max_time=1000)

# %%

import random
from collections import deque

def scheduler(processes, n, p, max_time):
    completed_processes = []
    remaining_processes = []
    processes_queue = deque(processes)

    time = 0
    while processes_queue and time < max_time:
        current_process, duration = processes_queue.popleft()
        while duration > 0 and time < max_time:
            if duration >= n:
                duration -= n
            else:
                duration = 0

            if duration == 0:
                completed_processes.append(current_process)
            else:
                if random.random() < p:
                    duration += random.randint(0, 100)

            time += n

    while processes_queue:
        remaining_processes.append(processes_queue.popleft()[0])

    return f'Zakończone procesy: {completed_processes} \nPozostałe procesy: {remaining_processes}'

processes = [
    ('git status', 25),
    ('python calculations.py', 534),
    ('gcc main.c', 1348),
    ('screenshot', 105)
]

result = scheduler(processes, n=4, p=0.2, max_time=1000)
print(result)










