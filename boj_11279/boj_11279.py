from heapq import heappop, heappush
import sys
input = sys.stdin.readline
print = sys.stdout.write
h = []
N = int(input())
for _ in range(N):
    c = int(input())
    if c == 0:
        if h:
            r = heappop(h)
            print(f"{r[1]}\n")
        else:
            print(f"0\n")
    else:
        heappush(h, (-c, c))
