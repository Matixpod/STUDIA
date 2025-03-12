
# %% Zad 1
def bomb_has_been_planted(m, time):
    k = []
    for day in range(len(m)):
        if "CT" in m[day]:
            ct = [m[day].index("CT"),day]

        if "B" in m[day]:
            b = [m[day].index("B"),day]

        if "K" in m[day]:
            k = [m[day].index("K"),day]

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
    for day in range(int(math.sqrt(c+1))):
        for j in range(day,int(math.sqrt(c))+1):
            if day**2 + j**2 == c:
                return True       
            elif len(str(day**2 + j**2)) > len(str(c)):
                break

    return False
judgeSquareSum(1000000000)

# %%

import math

def judgeSquareSum(c: int) -> bool:
    for day in range(int(math.isqrt(c)) + 1):
        reminder = c - day**2
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
    def minCostClimbingStairs( cost):
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
    def maxProfitAssignment( difficulty, profit, workers) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        workers.sort()
        
        result = 0
        max_payment = 0
        day = 0
        
        for worker in workers:
            while day < len(jobs) and worker >= jobs[day][0]:
                max_payment = max(max_payment, jobs[day][1])
                day += 1
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
    # day = 0
    # while day < len(nums)-1:
    #     print(nums[day+1] > nums[day])
    #     if nums[day+1] > nums[day]:
    #         result += (nums[day+1] - nums[day])
    #         day+=2
    #     else:
    #         result += nums[day]
    #         day+=1
    # return result

    ans = 0
    for day in range(len(s)):
        if day < len(s) - 1 and dic[s[day]] < dic[s[day+1]]:
            ans -= dic[s[day]]
        else:
            ans += dic[s[day]]
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
    for day in s:
        if day in dic:
            looking_for.append(dic[day])
        elif day in [dic["("], dic["["], dic["{"]] and not looking_for:
            return False
        elif day == looking_for[-1]:
            looking_for.pop()
        else:
            return False

    return not looking_for


isValid("(){}}{")

# %%

def removeElement(nums, val):
    k = 0
    for day in range(len(nums)):
        if nums[day] != val:
            nums[k] = nums[day]
            k += 1

    print(k)

removeElement([0,1,2,2,3,0,4,2],2)

# %%

def generate(numRows):
    x = 1
    result = []
    for day in range(1,numRows+1):
        result.append([x]*day)
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
        for day in range(1,n+1):
            result.append(sum(code2[day:day+k]))
    else:
        k = abs(k)
        for day in range(n):
            result.append(sum(code2[day+n-k:day+n]))
    return result

# def decrypt(code, k):

#     n = len(code)
#     if k == 0:
#         return [0] * n
    
#     result = [0] * n
#     extended_code = code * 2  # Extend the array to handle circular indexing
    
#     if k > 0:
#         for day in range(n):
#             result[day] = sum(extended_code[day+1:day+k+1])  # Sum of the next k numbers
#     else:  # k < 0
#         k = abs(k)
#         for day in range(n):
#             result[day] = sum(extended_code[day+n-k:day+n])  # Sum of the previous k numbers
    
#     return result


decrypt([5,7,1,4],3)

# %%


# def maximumSubarraySum(nums, k):
#     n = len(nums)
#     result = 0
#     for day in range(n-k+1):
#         if len(set(nums[day:day+k])) == k:
#             curr = sum(nums[day:day+k])
#             if curr > result:
#                 result = curr
#     return result
            
# maximumSubarraySum([1,2,2],2)


# def maximumSubarraySum(nums, k):
#     if n < k:
#         return 0
    
#     n = len(nums)
#     total = sum(nums[:k])
#     max_total = total if len(set(nums[:k])) == k else 0

#     for day in range(k,n):
#         total += nums[day] - nums[day - k]
#         if len(set(nums[day-k+1:day+1])) == k:
#             max_total = max(max_total, total)
#     return max_total





def maximumSubarraySum(nums, k):
    n = len(nums)
    if n < k:
        return 0
    freq = {}  
    total = 0
    max_total = 0

    for day in range(k):
        total += nums[day]
        freq[nums[day]] = freq.get(nums[day],0) + 1

    if len(freq) == k:
        max_total = total

    for day in range(k,n):
        total -= nums[day-k]
        if freq[nums[day-k]] == 1:
            del freq[nums[day-k]]
        else:
            freq[nums[day-k]] -= 1
            
        total += nums[day]
        freq[nums[day]] = freq.get(nums[day],0) + 1

        if len(freq) == k:
            max_total = max(max_total,total)
    return max_total




# maximumSubarraySum([1,1,1,7,8,9],3)

# %%
from collections import deque

class Solution:
    def slidingPuzzle(self,board):
        target = "123450"
        start = "".join(str(num) for row in board for num in row)
        visited = set()
        visited.add(start)
        possible_moves = {
            0:[1,3],
            1:[0,2,4],
            2:[1,5],
            3:[0,4],
            4:[1,3,5],
            5:[2,4]
        }

        queue = deque([(start, start.index("0"), 0)])


        while queue:
            print(visited)
            state, index, moves = queue.popleft()

            if state == target:
                return moves

            for move in possible_moves[index]:
                new_state = list(state)
                new_state[move],new_state[index] = new_state[index], new_state[move]
                new_state = "".join(new_state)
                if new_state not in visited:
                    visited.add(new_state)
                    queue.append([new_state, move,moves+1])
        return -1


board = [[4,1,2],[5,0,3]]
solution = Solution()
print(solution.slidingPuzzle(board))

# %%

def findChampion(n, edges):
    defeat_to = {team:[] for team in range(n)}

    for win,lose in edges:
        defeat_to[lose].append(win)

    for day in range(n):
        if defeat_to[day] != []:
            del defeat_to[day]

    if len(defeat_to) != 1:
        return -1
    else:
        return list(defeat_to)[0]




findChampion(3,[[0,1],[1,2]])

# %%
import heapq
def minimumObstacles(start,target,graph):
    obstacles = {node: float('inf') for node in graph}
    obstacles[start] = 0
    priority_queue = [(0, start)]  # Kolejka priorytetowa (odległość, wierzchołek)

    while priority_queue:
        current_obstacles, current_node = heapq.heappop(priority_queue)

        for neighbor,weight in graph[current_node].items():
            distance = current_obstacles + weight
            if distance < obstacles[neighbor]:
                obstacles[neighbor] = distance
                heapq.heappush(priority_queue,(distance,neighbor))
    print(obstacles)



minimumObstacles("A","D",{
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 3},
    'D': {'B': 6, 'C': 3}
})

# %%
import heapq

def shortestPathBinaryMatrix(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
    priority_queue = [(1,0,0)]
    obstacles = [[float('inf')] * cols for _ in range(rows)]
    obstacles[0][0] = 0

    if grid[0][0] == 1 or grid[-1][-1] == 1:
        return -1

    while priority_queue:
        current_obstacles,x,y = heapq.heappop(priority_queue) 
        for dx, dy in directions:
            if (x, y) == (rows - 1, cols - 1):
                return current_obstacles
            nx, ny = dx + x, dy + y
            if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 0:
                new_obstacles = current_obstacles + 1
                if new_obstacles < obstacles[nx][ny]:
                    obstacles[nx][ny] = new_obstacles
                    heapq.heappush(priority_queue,(new_obstacles,nx,ny)) 

    return -1

shortestPathBinaryMatrix([[1,0,0],[1,1,0],[1,1,0]])

# %%
import heapq
def minimumObstacles(grid):
    rows, cols = len(grid), len(grid[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    priority_queue = [(0,0,0)]
    obstacles = [[float('inf')] * cols for _ in range(rows)]
    obstacles[0][0] = 0

    while priority_queue:
        current_obstacles,x,y = heapq.heappop(priority_queue) 
        if (x, y) == (rows - 1, cols - 1):
                return current_obstacles
        for dx, dy in directions:
            nx, ny = dx + x, dy + y
            if 0 <= nx < rows and 0 <= ny < cols:
                new_obstacles = current_obstacles + (1 if grid[nx][ny] == 1 else 0)
                if new_obstacles < obstacles[nx][ny]:
                    obstacles[nx][ny] = new_obstacles
                    heapq.heappush(priority_queue,(new_obstacles,nx,ny)) 



minimumObstacles([[0,1,1],[1,1,0],[1,1,0]])

# %%

class Solution(object):
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)

        return False 
        
# %%
import heapq
def minimumTime(grid):
    rows,cols = len(grid),len(grid[0])
    directions = [(0,1),(1,0),(0,-1),(-1,0)]
    visited = [[False] * cols for _ in range(rows)]
    p_queue = [(0,0,0)]

    if grid[0][1] > 1 and grid[1][0] > 1:
        return -1

    while p_queue:
        current_time,x,y = heapq.heappop(p_queue)

        if (x,y) == (rows-1,cols-1):
            return current_time
        
        if visited[x][y]:
            continue
        visited[x][y] = True
        
        for dx,dy in directions:
            nx,ny = dx + x , dy + y
            
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                wait_time = max(0,grid[nx][ny] - current_time)

                if wait_time % 2 == 1:
                    wait_time += 1
                heapq.heappush(p_queue,(current_time + wait_time + 1,nx,ny))
    return -1

minimumTime([[0,1,3,2],[5,1,2,5],[4,3,8,6]])

# %%
from collections import defaultdict,deque

def validArrangement(pairs):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    start_node = pairs[0][0]

    for start,end in pairs:
        graph[start].append(end)
        out_degree[start] += 1
        in_degree[end] += 1

    for node in graph:
        if out_degree[node] > in_degree[node]:
            start_node = node 
            break

    stack = [start_node]
    path = []

    while stack:
        print(graph)
        print(stack)
        while graph[stack[-1]]:
            next_node = graph[stack[-1]].pop()
            stack.append(next_node)
        path.append(stack.pop())

    path.reverse()
    result = [[path[day], path[day+1]] for day in range(len(path)-1) ]

    return result


validArrangement([[1,3],[1,2],[2,1]])
# validArrangement([[1,3],[3,2],[2,1]])

# %% 
def checkIfExist(s):
    dict = {num:(day,num/2) for day,num in enumerate(s)}
    for num,target in dict.items():
        index,target = target
        if target in (s[:index] + s[index+1:]):
            return True
    return False


            



checkIfExist([15,7,-17,3,15,12])
# %% 

def isPrefixOfWord(sentence, searchWord):
    sentence = sentence.split(" ")
    for day,word in enumerate(sentence):
        if searchWord in word and word.index(searchWord) == 0:
            return day+1
    return -1


isPrefixOfWord("day love eating burger","burg")

# %%
from collections import deque
# def addSpaces(s, spaces):
#     result = []
#     spaces = deque(spaces)
#     day = 0
#     for j,letter in enumerate(s):
#         if spaces and j == spaces[0] + day:
#             result.append(' ')
#             spaces.popleft()
#         result.append(letter)
#     return  "".join(result)



def addSpaces(s, spaces):
    result = []
    last_index = 0
    for space in spaces:
        result.append(s[last_index:space])
        result.append(' ')
        last_index = space
    result.append(s[last_index:])

    return "".join(result)



addSpaces("LeetcodeHelpsMeLearn",[8,13,15])

# %%


def canMakeSubsequence(str1, str2):
    n = len(str1)
    m = len(str2)
    day = 0
    j = 0

    while day < n and j < m:
        if str1[day] == str2[j]:
            j += 1
        elif chr((ord(str1[day]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
            j += 1

        day += 1
    return j == m
        

canMakeSubsequence("zc",'ad')

# %%
import math
import heapq
def pickGifts(gifts, k):
    max_heap = [-gift for gift in gifts]
    heapq.heapify(max_heap)
    for _ in range(k):
        largest = -heapq.heappop(max_heap)
        heapq.heappush(max_heap,-int(math.sqrt(largest)))

    return -sum(max_heap)

pickGifts([25,64,9,4,100],4)

# %%

def findScore(nums):
    result = 0
    dic = {day:num for day,num in enumerate(nums)}
    while dic:
        day = min(dic,key=dic.get)
        result += dic[day]
        for neighbor in [day-1,day,day+1]:
            if neighbor in dic:
                del dic[neighbor]

    return result


import heapq
def findScore(nums):
    result = 0
    heap = [[num, day] for day,num in enumerate(nums)]
    heapq.heapify(heap)
    processed = set()
    while heap:
        num,day = heapq.heappop(heap)
        if day in processed:
            continue
        result += num
        processed.add(day)
        for neighbor in [day-1,day+1]:
            processed.add(neighbor)
    return result





findScore([2,1,3,4,5,2])

# %%

import heapq
def getFinalState(nums, k, multiplier):
    heap = [[num, day] for day,num in enumerate(nums)]
    heapq.heapify(heap)
    for day in range(k):
        current_min,day = heapq.heappop(heap)
        nums[day] = current_min*multiplier
        heapq.heappush(heap,[nums[day],day])

    return nums



getFinalState([1,2],3,4)



# %%
def finalPrices(prices):
    prices2 = prices[:]
    for day in range(0,len(prices)):
        for j in range(day+1,len(prices)):
            if prices[j] <= prices[day]:
                prices2[day] = prices[day] - prices[j]
                break
    return prices2

        
finalPrices([10,1,1,6])





# %%

test = {1,2,3,3}
test2 = (1,2,3,3)
print(*test)
print(*test2)

def build_profile(name,surname,**kwargs):
    kwargs['name'] = name
    kwargs['surname'] = surname
    return kwargs

user1 = build_profile('Mateusz','Podporski',age=21,phone_nr='513236216')
print(user1['name'])




# %%

def findTargetSumWays(nums, target):
    memo = {}
    def recursion(day, current_sum):
        if (day, current_sum) in memo:
            return memo[(day, current_sum)]

        if day == len(nums):
            return 1 if current_sum == target else 0
        
        positive = recursion(day + 1, current_sum + nums[day])
        negative = recursion(day + 1, current_sum - nums[day])

        memo[(day, current_sum)] = positive + negative
        
        return memo[(day, current_sum)]
    
    return recursion(0, 0)  


findTargetSumWays([1,1,1,1,1],3)

# %%

def maxScoreSightseeingPair(values):
    result = 0
    for day,val_i in enumerate(values):
        j = day + 1
        while j < len(values):
            if day < j:
                result = max(result,val_i + values[j] + day - j)
            j += 1
    return result


def maxScoreSightseeingPair(values):
    max_score = 0
    max_val_plus_i = values[0] + 0

    for j in range(1, len(values)):
        max_score = max(max_score, max_val_plus_i + values[j] - j)
        max_val_plus_i = max(max_val_plus_i, values[j] + j)

    return max_score

# maxScoreSightseeingPair([8,1,5,2,6])

# %%
def mincostTickets(days, costs):
    dp = [0] * (days[-1] + 1)
    for day in range(days[-1]+1):
        if day not in days:
            dp[day] = dp[day-1]
        else:
            dp[day] = min(
                dp[day-1] + costs[0],
                dp[max(0,day - 7)] + costs[1],
                dp[max(0,day - 30)] + costs[2]
            )
    return dp[-1]


# from collections import deque
# def mincostTickets(days, costs):
#     last7 = deque()
#     last30 = deque()
#     total_cost = 0

#     for day in days:
#         while last7 and last7[0][0] + 7 <= day:
#             last7.popleft()
#         while last30 and last30[0][0] + 30 <= day:
#             last30.popleft()

#         cost1 = total_cost + costs[0]
#         cost7 = (last7[-1][1] if last7 else 0) + costs[1]
#         cost30 = (last30[-1][1] if last30 else 0) + costs[2]

#         total_cost = min(cost1,cost7,cost30)

#         last7.append((day,total_cost))
#         last30.append((day,total_cost))

#     return total_cost

    

mincostTickets([1,4,6,7,8,20],[2,7,15])
# %%
def waysToSplitArray(nums):
    result = 0
    left = nums[0]
    right = sum(nums) - left

    for i in range(1,len(nums)):
        if left >= right:
            result += 1
        left += nums[i]
        right -= nums[i]

    return result


waysToSplitArray([10,4,-8,7])


# %%

from collections import deque

def coinChange(coins, amount):
    queue = deque([(0,0)])
    visited = set()
    while queue:
        current_count, current_amount = queue.popleft()
        if current_amount == amount:
            return current_count
        for coin in coins:
            next_coin = current_amount + coin
            if next_coin <= amount and next_coin not in visited:
                queue.append((current_count + 1,current_amount + coin))
                visited.add(next_coin)
    return -1


coinChange([1,2,5],100)

# %%
def countPalindromicSubsequence(s):
    visited = {}
    result = set()
    for i in range(len(s)):
        left = s[i]
        if left in visited:
            continue
        visited[left] = True
        for j in range(len(s)-1,i,-1):
            right = s[j]
            if left == right:
                for k in range(i+1,j):
                    result.add(left+s[k]+right)
    return len(result)



def countPalindromicSubsequence(s):
    result = set()
    left_indices = {}
    right_indices = {}

    for i, char in enumerate(s):
        if char not in left_indices:
            left_indices[char] = i
        right_indices[char] = i

    for char in left_indices:
        left = left_indices[char]
        right = right_indices[char]
        if right - left > 1:
            for k in range(left + 1, right):
                result.add((char, s[k], char))

    return len(result)




countPalindromicSubsequence("bbcbaba")

# %%

def stringMatching(words):
    result = []
    for i in range(len(words)):
        for j in range(len(words)):
            if i != j and words[i] in words[j]:
                result.append(words[i])
    return list(set(result))


stringMatching(["leetcoder","leetcode","od","hamlet","am"])

# %%%
def countPrefixSuffixPairs(words):
    global result
    result = 0

    def isPrefixAndSuffix(str1, str2):
        n = len(str1)
        if str1 == str2[:n] and str1 == str2[-n:]:
            global result
            result += 1

    for i in range(len(words)):
        for j in range(i+1,len(words)):
            isPrefixAndSuffix(words[i],words[j])
    return result


countPrefixSuffixPairs(["a","aba","ababa","aa"])


# %%


def ascii_to_letters(ascii_codes):
    letters = [chr(code) for code in ascii_codes]
    return letters

print("".join(ascii_to_letters([78,73,71,71,69,82])))