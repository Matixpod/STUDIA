
# %% Zad 1
def bomb_has_been_planted(m, time):
    k = []
    for i in range(len(m)):
        if "CT" in m[i]:
            ct = [m[i].index("CT"),i]

        if "B" in m[i]:
            b = [m[i].index("B"),i]

        if "K" in m[i]:
            k = [m[i].index("K"),i]

    steps_needed = max([abs(ct[0]-b[0]),abs(ct[1]-b[1])])
    if k:
        steps_needed2 = max([abs(ct[0]-k[0]),abs(ct[1]-k[1])]) + max([abs(b[0]-k[0]),abs(b[1]-k[1])])
        # print(ct,b,k)
        print(steps_needed2,"ilosc krokow z kitem")
    print(steps_needed, "ilosc krokow bez kitu")
    return bool(k and time - steps_needed2 >= 5 or time - steps_needed >= 10)
        

# %% Zad 2






map1 = [
        ["CT", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "0"],
        ["0", "0", "0", "0", "0", "0", "B"]
    ]

map5 = [
    ["0", "0", "0", "0", "0", "0"],
    ["CT", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "B"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "K", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"],
    ["0", "0", "0", "0", "0", "0"]
]
        

print(bomb_has_been_planted(map1,13))
print(bomb_has_been_planted(map5, 13))


# %%
import math
def judgeSquareSum(c: int) -> bool:
    for i in range(int(math.sqrt(c+1))):
        for j in range(i,int(math.sqrt(c))+1):
            if i**2 + j**2 == c:
                return True       
            elif len(str(i**2 + j**2)) > len(str(c)):
                break

    return False
judgeSquareSum(1000000000)

# %%

import math

def judgeSquareSum(c: int) -> bool:
    for i in range(int(math.isqrt(c)) + 1):
        reminder = c - i**2
        if is_squere(reminder):
            return True
    return False

def is_squere(n: int) -> bool:
    sqrt_n = math.isqrt(n)
    return sqrt_n * sqrt_n == n

# Testowanie
judgeSquareSum(5)
# %%

class Solution:
    def minCostClimbingStairs(self, cost):
        cost.append("end")
        if cost[1] < cost[0]:
            cost = cost[1:]


        step_cost = 0

        while len(cost) > 1:
            print(len(cost))
            print(cost[0])
            cost = cost[1:]



Solution().minCostClimbingStairs([10,15,20])


# %%

class Solution:
    def maxProfitAssignment(self, difficulty, profit, workers) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        workers.sort()
        
        result = 0
        max_payment = 0
        i = 0
        
        for worker in workers:
            while i < len(jobs) and worker >= jobs[i][0]:
                max_payment = max(max_payment, jobs[i][1])
                i += 1
            result += max_payment
        

        
        return result
    

    
print(Solution().maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))