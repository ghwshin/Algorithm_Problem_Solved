import sys
from queue import PriorityQueue
input = sys.stdin.readline

q = PriorityQueue()
n = int(input())
for _ in range(n):
    times = list(map(int, input().split()))
    q.put((times[1], times[0]))
    # (종료시간, 시작시간)
max_meeting = 1
cur = q.get()
cur_start = cur[1]
cur_end = cur[0]
while q.qsize() > 0:
    cur = q.get()
    start = cur[1]
    end = cur[0]
    if cur_end <= start:
        cur_start = cur[1]
        cur_end = cur[0]
        max_meeting += 1
print(max_meeting)