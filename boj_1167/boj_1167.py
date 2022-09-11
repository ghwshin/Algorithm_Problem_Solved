# 트리의 지름 구하기의 아이디어
# 트리에서의 임의의 한 노드에서 가장 거리가 먼 노드는 트리의 지름의 두 노드 중 하나이다.
# 문제를 잘읽으세요. -> 분명히 노드를 순서대로 입력을 준다고 안했음
import sys
from collections import deque

input = sys.stdin.readline
v = int(input())
tree = [list() for _ in range(v + 1)]
for i in range(1, v+1):
    line = list(map(int, input().split(' ')))
    cur = 0
    for j in range(1, len(line) - 1, 2):
        # 주의!
        tree[line[0]].append((line[j], line[j + 1]))
checked = [False] * (v + 1)
distance = [0] * (v + 1)

def bfs(node):
    best_node = node
    max_dist = 0
    checked[node] = True
    q = deque()
    q.append(node)
    while q:
        cur = q.popleft()
        for t_node in tree[cur]:
            if not checked[t_node[0]]:
                checked[t_node[0]] = True
                distance[t_node[0]] = distance[cur] + t_node[1]
                if max_dist < distance[t_node[0]]:
                    max_dist = distance[t_node[0]]
                    best_node = t_node[0]
                q.append(t_node[0])
    return best_node, max_dist

first_best, first_max = bfs(1)
checked = [False] * (v + 1)
distance = [0] * (v + 1)
final_best, final_max = bfs(first_best)
print(final_max)

