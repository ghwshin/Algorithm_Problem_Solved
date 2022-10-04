import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
graph = [list() for _ in range(N + 1)]
hack = [0] * (N + 1)
checked = [False] * (N + 1)

for _ in range(M):
    start, end = map(int, input().split())
    graph[start].append(end)

def bfs(node):
    q = deque()
    q.append(node)
    checked[node] = True
    while q:
        cur = q.popleft()
        for i in graph[cur]:
            if not checked[i]:
                hack[i] += 1
                checked[i] = True
                q.append(i)


for i in range(1, N + 1):
    checked = [False] * (N + 1)
    bfs(i)

max_hack = max(hack)
for i in range(1, N + 1):
    if hack[i] == max_hack:
        print(i, end=' ')