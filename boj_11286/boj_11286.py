# 시간 제한 1초
import heapq
import sys
input = sys.stdin.readline
print = sys.stdout.write
hq = []
n = int(input())
for _ in range(n):
    command = int(input())
    if command == 0:
        if hq:
            print(str(heapq.heappop(hq)[1]) + '\n')
        else:
            print('0\n')
    else:
        heapq.heappush(hq, (abs(command), command))
