import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
num = list(map(int, input().split()))
count = 0
num.sort()
start_idx = 0
end_idx = n - 1
while start_idx < end_idx:
    if num[start_idx] + num[end_idx] < m:
        start_idx += 1
    elif num[start_idx] + num[end_idx] > m:
        end_idx -= 1
    else:
        count += 1
        start_idx += 1
        end_idx -= 1
print(count)
