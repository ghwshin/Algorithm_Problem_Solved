import heapq, sys
heap = []
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
for _ in range(n):
    command = int(input())
    if command == 0:
        if heap:
            print(str(heapq.heappop(heap)) + "\n")
        else:
            print("0\n")
    else:
        heapq.heappush(heap, command)