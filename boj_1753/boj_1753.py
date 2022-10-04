import sys
from queue import PriorityQueue
input = sys.stdin.readline

inf = sys.maxsize

V, E = map(int, input().split())
graph = [list() for _ in range(V + 1)]
start_vertex = int(input())
dist = [inf] * (V + 1)
dist[start_vertex] = 0
q = PriorityQueue()

for i in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

checked = [False] * (V + 1)
# (distance, vertex)
q.put((0, start_vertex))

while q.qsize() > 0:
    cur = q.get()
    cur_vertex = cur[1]
    cur_mindist = cur[0]
    if checked[cur_vertex]:
        continue
    checked[cur_vertex] = True
    for node in graph[cur_vertex]:
        next_vertex = node[0]
        next_weight = node[1]
        next_mindist = dist[next_vertex]
        if dist[next_vertex] > cur_mindist + next_weight:
            dist[next_vertex] = cur_mindist + next_weight
            q.put((dist[next_vertex], next_vertex))

for i in range(1, V + 1):
    if checked[i]:
        print(dist[i])
    else:
        print("INF")