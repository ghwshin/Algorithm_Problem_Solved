import sys
import heapq
inf = sys.maxsize

input = sys.stdin.readline
n, m, k = map(int, input().split())
graph = [list() for _ in range(n + 1)]

dist = [[inf] * k for _ in range(n + 1)]

for i in range(m):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))

# start 1
q = [(0, 1)]
dist[1][0] = 0

while q:
    cur_weight, node = heapq.heappop(q)
    for next in graph[node]:
        next_node = next[0]
        next_weight = next[1]
        next_dist = cur_weight + next_weight
        if dist[next_node][k - 1] > next_dist:
            dist[next_node][k - 1] = next_dist
            dist[next_node].sort()
            heapq.heappush(q, (next_dist, next_node))

for i in range(1, n + 1):
    if dist[i][k - 1] == inf:
        print(-1)
    else:
        print(dist[i][k - 1])