# 오일러 피 함수 구하기
import math
n = int(input())
result = n
for i in range(2, int(math.sqrt(n) + 1)):
    if n % i == 0:
        result -= (result / i)
        while n % i == 0:
            n /= i
if n > 1:
    # 남은 소인수 처리
    result -= (result / n)
print(int(result))