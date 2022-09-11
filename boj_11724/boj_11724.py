# 주의 : 무방향 그래프이기 때문에 양쪽에 노드를 추가해야함 (인접 그래프)
# dfs를 재귀로 구현해도 무방함
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list() for _ in range(n + 1)]
check = [False] * (n + 1)
for _ in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
stack = []
connect_n = 0

# def DFS(v):
#     check[v] = True
#     for i in graph[v]:
#         if not check[v]:
#             DFS(i)

for i in range(1, n + 1):
    if not check[i]:
        stack.append(i)
        while stack:
            cur = stack.pop()
            check[cur] = True
            for conj in graph[cur]:
                if not check[conj]:
                    stack.append(conj)
        # DFS(i)
        connect_n += 1
print(connect_n)
