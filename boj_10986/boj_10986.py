import sys
input = sys.stdin.readline

def comb_two(n):
    return (n * (n - 1)) // 2

n, m = map(int, input().split())
arr = list(map(int, input().split()))

mod_arr = [arr[0] % m] * n
num_arr = [0] * m
num_arr[mod_arr[0]] += 1

for i in range(1, n):
    mod_arr[i] = (mod_arr[i - 1] + arr[i]) % m
    num_arr[mod_arr[i]] += 1
re_sum = num_arr[0] + comb_two(num_arr[0])
for i in range(1, m):
    re_sum += comb_two(num_arr[i])
print(re_sum)