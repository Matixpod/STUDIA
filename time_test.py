import time
import matplotlib.pyplot as plt
import random
import heapq

def maxScoreSightseeingPair(values):
    max_score = 0
    max_val_plus_i = values[0] + 0

    for j in range(1, len(values)):
        max_score = max(max_score, max_val_plus_i + values[j] - j)
        max_val_plus_i = max(max_val_plus_i, values[j] + j)

    return max_score

def finalPrices(prices):
    prices2 = prices[:]
    for i in range(0,len(prices)):
        for j in range(i+1,len(prices)):
            if prices[j] <= prices[i]:
                prices2[i] = prices[i] - prices[j]
                break
    return prices2


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



def checkIfExist(arr):
    dict = {num:(i,num/2) for i,num in enumerate(arr)}
    for num,target in dict.items():
        index,target = target
        if target in (arr[:index] + arr[index+1:]):
            return True
    return False


data_sizes = [100, 1000, 10000, 100000]
times = []

for size in data_sizes:
    values = [random.randint(1, 10000) for _ in range(size)]
    start_time = time.time()
    checkIfExist(values)
    end_time = time.time()
    times.append(end_time - start_time)

plt.plot(data_sizes, times, marker='o')
plt.xlabel('Data Size')
plt.ylabel('Time (s)')
plt.title('Time Complexity of your function')
plt.grid(True)
plt.show()