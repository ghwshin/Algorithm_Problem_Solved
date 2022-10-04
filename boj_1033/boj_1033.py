# dfs로 최소 공배수를 찾아 계산하기
n = int(input())
l = [[] for _ in range(n)]
checked = [False] * n
lcm = 1
mass = [0] * n

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def dfs(node):
    checked[node] = True
    for i in l[node]:
        next_node = i[0]
        if not checked[next_node]:
            mass[next_node] = mass[node] * i[2] // i[1]
            dfs(next_node)

for i in range(n - 1):
    a, b, p, q = map(int, input().split())
    l[a].append((b, p, q))
    l[b].append((a, q, p))
    lcm *= (p * q // gcd(p, q))

mass[0] = lcm
dfs(0)
mass_gcd = mass[0]
for i in range(1, n):
    mass_gcd = gcd(mass_gcd, mass[i])
for i in range(n):
    print(mass[i] // mass_gcd, end=' ')