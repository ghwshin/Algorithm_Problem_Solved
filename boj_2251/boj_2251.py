from collections import deque

bucket = list(map(int, input().split()))
# C는 결과
# A : 0, B : 1, C : 2
s = [0, 0, 1, 1, 2, 2]
r = [1, 2, 0, 2, 0, 1]
checked = [[False for i in range(201)] for j in range(201)]
result = [False] * 201

def BFS():
    q = deque()
    # (A, B) 초기화
    q.append((0, 0))
    checked[0][0] = True
    result[bucket[2]] = True
    while q:
        cur = q.popleft()
        cur_a = cur[0]
        cur_b = cur[1]
        cur_c = bucket[2] - cur_b - cur_a
        for k in range(6):
            next_b = [cur_a, cur_b, cur_c]
            next_b[r[k]] += next_b[s[k]]
            next_b[s[k]] = 0
            # 물 초과
            if next_b[r[k]] > bucket[r[k]]:
                # 초과량을 보낸 애에게 다시 넣고, 최대치로 만듬
                next_b[s[k]] = next_b[r[k]] - bucket[r[k]]
                next_b[r[k]] = bucket[r[k]]
            # 방문한 노드가 아니면 다시 큐에 넣음
            if not checked[next_b[0]][next_b[1]]:
                checked[next_b[0]][next_b[1]] = True
                q.append((next_b[0], next_b[1]))
                if next_b[0] == 0:
                    result[next_b[2]] = True

BFS()
for i in range(len(result)):
    if result[i]:
        print(i, end=' ')