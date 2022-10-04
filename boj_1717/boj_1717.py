import sys
input = sys.stdin.readline
n, m = map(int, input().split())
union_find = [i for i in range(n + 1)]

def find(n):
    if union_find[n] != n:
        great = find(union_find[n])
        union_find[n] = great
        return great
    else:
        return n

def union(a, b):
    great_a = find(a)
    great_b = find(b)
    if great_a != great_b:
        union_find[great_b] = great_a

def same(a, b):
    great_a = find(a)
    great_b = find(b)
    if great_a == great_b:
        return True
    else:
        return False

for _ in range(m):
    command, a, b = map(int, input().split())
    if command == 0:
        union(a, b)
    else:
        if same(a, b):
            print('YES')
        else:
            print('NO')
