import math
n = int(input())
# 주의!! n 이상의 펠린드롬 수를 찾지만, 입력이 1000000까지 일뿐, 출력은 넘을 수 있다.
l = 1100000
p = [0] * (l + 1)
for i in range(2, l + 1):
    p[i] = i

for i in range(2, int(math.sqrt(l)) + 1):
    if p[i] == 0:
        continue
    for j in range(2 * i, l + 1, i):
        p[j] = 0

for i in range(n, l + 1):
    str_num = p[i]
    if str_num == 0:
        continue
    str_num = str(str_num)
    start = 0
    end = len(str_num) - 1
    is_pelin = True
    while start <= end:
        if str_num[start] != str_num[end]:
            is_pelin = False
            break
        start += 1
        end -= 1
    if is_pelin:
        print(str_num)
        break
