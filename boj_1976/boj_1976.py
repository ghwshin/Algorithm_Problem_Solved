N = int(input())
M = int(input())
parent = [i for i in range(1, N + 1)]
parent.insert(0, 0)
mat = [[0 for j in range(N + 1)] for i in range(N + 1)]

def find(n):
    if n == parent[n]:
        return n
    else:
        parent[n] = find(parent[n])
        return parent[n]

def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

for i in range(1, N + 1):
    mat[i] = list(map(int, input().split()))
    mat[i].insert(0, 0)

r = list(map(int, input().split()))
r.insert(0, 0)

for i in range(1, N + 1):
    for j in range(1, N + 1):
        if mat[i][j] == 1:
            union(i, j)

idx = find(r[1])
is_correct = True
for i in range(2, len(r)):
    if idx != find(r[i]):
        is_correct = False
        break

if is_correct:
    print('YES')
else:
    print('NO')







