import sys
from queue import PriorityQueue
input = sys.stdin.readline
positive = PriorityQueue()
minus = PriorityQueue()
zeros = 0
result = 0
n = int(input())
for _ in range(n):
    cur = int(input())
    # 양수, 음수의 우선순위 큐를 두어 내림차순 정렬
    if cur > 0:
        positive.put((-cur, cur))
    elif cur < 0:
        minus.put(cur)
    else:
        zeros += 1
while minus.qsize() > 1:
    tmp = minus.get() * minus.get()
    result += tmp
if minus.qsize() == 1 and zeros == 0:
    # 음수가 하나 남고, 0이 존재하면 음수를 무시한다.
    # 0이 없으면 결과값에 음수를 추가한다.
    result += minus.get()
while positive.qsize() > 1:
    first = positive.get()
    second = positive.get()
    # 둘 중에 하나가 1이면 묶으면 안된다.
    if first[1] == 1 or second[1] == 1:
        positive.put(first)
        positive.put(second)
        break
    else:
        result += (first[1] * second[1])
while positive.qsize():
    result += positive.get()[1]
print(result)
