import sys
n = int(input())
m = int(input())
inf = sys.maxsize

graph = [[inf for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(1, n + 1):
    graph[i][i] = 0

for i in range(m):
    start, end, cost = map(int, input().split())
    if graph[start][end] > cost:
        graph[start][end] = cost

for k in range(1, n + 1):
    for s in range(1, n + 1):
        for e in range(1, n + 1):
            graph[s][e] = min(graph[s][e], graph[s][k] + graph[k][e])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == inf:
            print(0, end=' ')
        else:
            print(graph[i][j], end=' ')
    print()
