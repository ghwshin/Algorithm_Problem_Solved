import math
Min, Max = map(int, input().split())
checked = [False] * (Max - Min + 1)

for i in range(2, int(math.sqrt(Max) + 1)):
    powered = i * i
    start = int(Min / powered)
    if Min % powered != 0:
        start += 1
    for j in range(start, int(Max / powered) + 1):
        checked[int((j * powered) - Min)] = True
count = 0
for i in range(0, Max - Min + 1):
    if not checked[i]:
        count += 1
print(count)