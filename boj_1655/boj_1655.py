import heapq, sys
input = sys.stdin.readline
print = sys.stdout.write
N = int(input())
h = []
start = int(input())
print(str(start) + "\n")
heapq.heappush(h, start)
for _ in range(1, N):
    num = int(input())
    heapq.heappush(h, num)
    length = len(h)
    if length % 2 != 0:
        print(str(h[length // 2 - 1]) + "\n")
    else:
        print(str(h[length // 2 - 1]) + "\n")