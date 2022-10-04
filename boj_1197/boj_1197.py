import sys
from queue import PriorityQueue

input = sys.stdin.readline
V, E = map(int, input().split())
graphq = PriorityQueue()
unionfind = [i for i in range(V + 1)]

for _ in range(E):
    start, end, weight = map(int, input().split())
    graphq.put((weight, start, end))

def find(n):
    if n == unionfind[n]:
        return n
    else:
        unionfind[n] = find(unionfind[n])
        return unionfind[n]

def union(a, b):
    a_p = find(a)
    b_p = find(b)
    if a_p != b_p:
        unionfind[b_p] = a_p

sum_weight = 0
used_edge = 0
while used_edge < V - 1:
    weight, start, end = graphq.get()
    if find(start) != find(end):
        union(start, end)
        sum_weight += weight
        used_edge += 1

print(sum_weight)

