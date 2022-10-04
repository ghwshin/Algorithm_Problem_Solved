import sys, heapq
input = sys.stdin.readline
n = int(input())
nums = []
for i in range(n):
    heapq.heappush(nums, int(input()))

result = 0
while len(nums) > 1:
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)
    result += (first + second)
    heapq.heappush(nums, first + second)

print(result)