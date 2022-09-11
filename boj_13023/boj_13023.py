# 주의 : 한번 검색한 노드에 대한 결과를 삭제해야함.
# 전체 경로에 대해서 검사해야함.
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list() for _ in range(n)]
checked = [False] * n
for i in range(m):
    f_1, f_2 = map(int, input().split())
    graph[f_1].append(f_2)
    graph[f_2].append(f_1)
friends = False

def DFS(depth, cur):
    global friends
    if depth == 5:
        friends = True
        return
    else:
        checked[cur] = True
        for i in graph[cur]:
            if not checked[i]:
                DFS(depth + 1, i)
        checked[cur] = False

for i in range(n):
    DFS(1, i)
    if friends:
        break
if friends:
    print(1)
else:
    print(0)