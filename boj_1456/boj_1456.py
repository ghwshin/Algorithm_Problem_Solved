# n 제곱 값이 너무 커서 overflow 발생 가능성이 있음
# (n ** k)와 b 값을 비교하지 않고, n 과 b / (n ** (k - 1)) 값을 비교한다.
import math
a, b = map(int, input().split())
n = 10000000
p = [0] * (n + 1)
result = 0
for i in range(2, n + 1):
    p[i] = i

for i in range(2, int(math.sqrt(n)) + 1):
    if p[i] == 0:
        continue
    for j in range(2 * i, n + 1, i):
        # 에라토스테네스의 체 적용
        p[j] = 0

for i in range(2, n + 1):
    if p[i] != 0:
        div = p[i]
        while p[i] <= b / div:
            if p[i] >= a / div:
                result += 1
            div *= p[i]
print(result)

