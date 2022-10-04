import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
height = 0
leaf = N

while leaf != 0:
    leaf //= 2
    height += 1

tree_size = pow(2, height + 1)
leaf_start_idx = tree_size // 2 - 1
tree = [0] * (tree_size + 1)

for i in range(leaf_start_idx + 1, leaf_start_idx + N + 1):
    tree[i] = int(input())

def set_tree(i):
    while i != 1:
        tree[i // 2] += tree[i]
        i -= 1
set_tree(tree_size - 1)

def change_value(index, value):
    diff = value - tree[index]
    while index > 0:
        tree[index] += diff
        index //= 2

def get_sum(start, end):
    part = 0
    while start <= end:
        if start % 2 == 1:
            part += tree[start]
            start += 1
        if end % 2 == 0:
            part += tree[end]
            end -= 1
        start //= 2
        end //= 2
    return part

for _ in range(M + K):
    q, start, end = map(int, input().split())
    if q == 1:
        change_value(start + leaf_start_idx, end)
    elif q == 2:
        start += leaf_start_idx
        end += leaf_start_idx
        print(get_sum(start, end))
