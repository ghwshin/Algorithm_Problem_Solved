# BFS로 풀이해보기
# BFS의 특징은 여러 경로로 도달할 때, 최단 경로를 보장 할 수 있음
# depth를 계속해서 저장하면 알수있다!
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
maze = [[0] * m for _ in range(n)]
result = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
checked = [([False] * m) for _ in range(n)]

for i in range(n):
    line = list(input())
    for j in range(m):
        maze[i][j] = int(line[j])

def BFS(node):
    global result
    q = deque()
    q.append(node)
    checked[node[0]][node[1]] = True
    while q:
        cur = q.popleft()
        for i in range(4):
            next_x = cur[0]+dx[i]
            next_y = cur[1]+dy[i]
            if next_x >= 0 and next_y >= 0 and next_x < n and next_y < m:
                if maze[next_x][next_y] >= 1 and checked[next_x][next_y] == False:
                    checked[next_x][next_y] = True
                    maze[next_x][next_y] = maze[cur[0]][cur[1]] + 1
                    q.append((next_x, next_y))

BFS((0, 0))
print(maze[n-1][m-1])
