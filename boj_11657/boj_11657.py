import sys

inf = sys.maxsize

N, M = map(int, input().split())
edge = []
dist = [sys.maxsize] * (N + 1)
for _ in range(M):
    start, end, weight = map(int, input().split())
    edge.append((start, end, weight))


dist[1] = 0

for _ in range(N - 1):
    for start, end, weight in edge:
        if dist[start] != inf and dist[start] + weight < dist[end]:
            dist[end] = dist[start] + weight

cycled = False

for start, end, weight in edge:
    if dist[start] != inf and dist[start] + weight < dist[end]:
        cycled = True

if not cycled:
    for i in range(2, N + 1):
        if dist[i] != inf:
            print(dist[i])
        else:
            print(-1)
else:
    print(-1)