import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
K = int(input())

def dfs(node):
    global is_bipartite, graph, graph_set, checked
    checked[node] = True
    for i in graph[node]:
        if not checked[i]:
            graph_set[i] = (graph_set[node] + 1) % 2
            dfs(i)
        elif graph_set[i] == graph_set[node]:
            is_bipartite = False


for i in range(K):
    V, E = map(int, input().split())
    graph = [list() for __ in range(V + 1)]
    graph_set = [0] * (V + 1)
    checked = [False] * (V + 1)
    is_bipartite = True
    for j in range(E):
        start, end = map(int, input().split())
        graph[start].append(end)
        graph[end].append(start)

    for k in range(1, V + 1):
        if is_bipartite:
            dfs(k)
        else:
            break
    if is_bipartite:
        print('YES')
    else:
        print('NO')
