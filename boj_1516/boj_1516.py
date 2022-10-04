# 위상 정렬
from collections import deque
N = int(input())
graph = [list() for _ in range(N + 1)]
time = [0] * (N + 1)
indegree = [0] * (N + 1)
min_time = [0] * (N + 1)

for i in range(1, N + 1):
    inp = list(map(int, input().split()))
    time[i] = inp[0]
    indg = 0
    for j in range(1, len(inp) - 1):
        graph[inp[j]].append(i)
        indg += 1
    indegree[i] += indg

q = deque()

for i in range(1, N + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    cur = q.popleft()
    for next in graph[cur]:
        indegree[next] -= 1
        min_time[next] = max(min_time[next], min_time[cur] + time[cur])
        if indegree[next] == 0:
            q.append(next)

for i in range(1, N + 1):
    print(min_time[i] + time[i])
