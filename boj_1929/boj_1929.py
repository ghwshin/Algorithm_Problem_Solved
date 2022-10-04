# 에라토스테네스의 체를 사용할 때 n의 제곱근까지만 탐색해야 한다.
import math
m, n = map(int, input().split())
primes = [0] * (n + 1)
for i in range(2, n + 1):
    primes[i] = i

for i in range(2, int(math.sqrt(n)) + 1):
    if primes[i] == 0:
        continue
    else:
        for j in range(2 * i, n + 1, i):
            primes[j] = 0

for i in primes:
    if i != 0 and i >= m:
        print(i)