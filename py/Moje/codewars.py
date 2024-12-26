
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

# %%


# def maximumSubarraySum(nums, k):
#     n = len(nums)
#     result = 0
#     for i in range(n-k+1):
#         if len(set(nums[i:i+k])) == k:
#             curr = sum(nums[i:i+k])
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

#     for i in range(k,n):
#         total += nums[i] - nums[i - k]
#         if len(set(nums[i-k+1:i+1])) == k:
#             max_total = max(max_total, total)
#     return max_total





def maximumSubarraySum(nums, k):
    n = len(nums)
    if n < k:
        return 0
    freq = {}  
    total = 0
    max_total = 0

    for i in range(k):
        total += nums[i]
        freq[nums[i]] = freq.get(nums[i],0) + 1

    if len(freq) == k:
        max_total = total

    for i in range(k,n):
        total -= nums[i-k]
        if freq[nums[i-k]] == 1:
            del freq[nums[i-k]]
        else:
            freq[nums[i-k]] -= 1
            
        total += nums[i]
        freq[nums[i]] = freq.get(nums[i],0) + 1

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

    for i in range(n):
        if defeat_to[i] != []:
            del defeat_to[i]

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
    result = [[path[i], path[i+1]] for i in range(len(path)-1) ]

    return result


validArrangement([[1,3],[1,2],[2,1]])
# validArrangement([[1,3],[3,2],[2,1]])

# %% 
def checkIfExist(arr):
    dict = {num:(i,num/2) for i,num in enumerate(arr)}
    for num,target in dict.items():
        index,target = target
        if target in (arr[:index] + arr[index+1:]):
            return True
    return False


            



checkIfExist([15,7,-17,3,15,12])
# %% 

def isPrefixOfWord(sentence, searchWord):
    sentence = sentence.split(" ")
    for i,word in enumerate(sentence):
        if searchWord in word and word.index(searchWord) == 0:
            return i+1
    return -1


isPrefixOfWord("i love eating burger","burg")

# %%
from collections import deque
# def addSpaces(s, spaces):
#     result = []
#     spaces = deque(spaces)
#     i = 0
#     for j,letter in enumerate(s):
#         if spaces and j == spaces[0] + i:
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
    i = 0
    j = 0

    while i < n and j < m:
        if str1[i] == str2[j]:
            j += 1
        elif chr((ord(str1[i]) - ord('a') + 1) % 26 + ord('a')) == str2[j]:
            j += 1

        i += 1
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
    dic = {i:num for i,num in enumerate(nums)}
    while dic:
        i = min(dic,key=dic.get)
        result += dic[i]
        for neighbor in [i-1,i,i+1]:
            if neighbor in dic:
                del dic[neighbor]

    return result


import heapq
def findScore(nums):
    result = 0
    heap = [[num, i] for i,num in enumerate(nums)]
    heapq.heapify(heap)
    processed = set()
    while heap:
        num,i = heapq.heappop(heap)
        if i in processed:
            continue
        result += num
        processed.add(i)
        for neighbor in [i-1,i+1]:
            processed.add(neighbor)
    return result





findScore([2,1,3,4,5,2])

# %%

import heapq
def getFinalState(nums, k, multiplier):
    heap = [[num, i] for i,num in enumerate(nums)]
    heapq.heapify(heap)
    for i in range(k):
        current_min,i = heapq.heappop(heap)
        nums[i] = current_min*multiplier
        heapq.heappush(heap,[nums[i],i])

    return nums



getFinalState([1,2],3,4)



# %%
def finalPrices(prices):
    prices2 = prices[:]
    for i in range(0,len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] <= prices[i]:
                prices2[i] = prices[i] - prices[j]
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
    def recursion(i, current_sum):
        if (i, current_sum) in memo:
            return memo[(i, current_sum)]

        if i == len(nums):
            return 1 if current_sum == target else 0
        
        positive = recursion(i + 1, current_sum + nums[i])
        negative = recursion(i + 1, current_sum - nums[i])

        memo[(i, current_sum)] = positive + negative
        
        return memo[(i, current_sum)]
    
    return recursion(0, 0)  


print(findTargetSumWays([1,1,1,1,1],3))