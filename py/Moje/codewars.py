
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
    

    
# print(Solution().maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]))

# %%

def romanToInt(s):
    dic = {"I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000,
    }
    # result = 0
    # nums = [dic[letter] for letter in s]
    # nums.append(0)
    # i = 0
    # while i < len(nums)-1:
    #     print(nums[i+1] > nums[i])
    #     if nums[i+1] > nums[i]:
    #         result += (nums[i+1] - nums[i])
    #         i+=2
    #     else:
    #         result += nums[i]
    #         i+=1
    # return result

    ans = 0
    for i in range(len(s)):
        if i < len(s) - 1 and dic[s[i]] < dic[s[i+1]]:
            ans -= dic[s[i]]
        else:
            ans += dic[s[i]]
    return ans


print(romanToInt("MCMXCIV"))

# %%

def isValid(s):
    dic = {
        "(":")",
        "[":"]",
        "{":"}"
    }

    looking_for = []
    for i in s:
        if i in dic:
            looking_for.append(dic[i])
        elif i in [dic["("], dic["["], dic["{"]] and not looking_for:
            return False
        elif i == looking_for[-1]:
            looking_for.pop()
        else:
            return False

    return not looking_for


isValid("(){}}{")

# %%

def removeElement(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1

    print(k)

removeElement([0,1,2,2,3,0,4,2],2)

# %%

def generate(numRows):
    x = 1
    result = []
    for i in range(1,numRows+1):
        result.append([x]*i)
        if len(result) > 2:
            for j in range(1,len(result) - 1):
                result[-1][j] = result[-2][j-1] + result[-2][j]


    return result

        

generate(5)
# %%

def decrypt(code, k):
    code2 = code*2
    result = []
    n = len(code)
    if k == 0:
        return [0]*n
    elif k > 0:
        for i in range(1,n+1):
            result.append(sum(code2[i:i+k]))
    else:
        k = abs(k)
        for i in range(n):
            result.append(sum(code2[i+n-k:i+n]))
    return result

# def decrypt(code, k):

#     n = len(code)
#     if k == 0:
#         return [0] * n
    
#     result = [0] * n
#     extended_code = code * 2  # Extend the array to handle circular indexing
    
#     if k > 0:
#         for i in range(n):
#             result[i] = sum(extended_code[i+1:i+k+1])  # Sum of the next k numbers
#     else:  # k < 0
#         k = abs(k)
#         for i in range(n):
#             result[i] = sum(extended_code[i+n-k:i+n])  # Sum of the previous k numbers
    
#     return result


decrypt([5,7,1,4],3)


