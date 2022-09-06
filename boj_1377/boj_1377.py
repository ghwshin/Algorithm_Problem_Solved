# 오름차순 버블 정렬
# 한번도 안바뀌는 상태여야 한다. (내부 swap이 일어나지 않을때까지 몇번 내부 for문이 동작하는가?)
# 정렬 전과 정렬 후의 인덱스 차이를 확인하면 이동 거리가 나온다.
# 이동 거리가 가장 큰 것을 확인하면 내부 for문의 최대 횟수를 확인할 수 있다.
import sys
input = sys.stdin.readline
N = int(input())
l = []
for i in range(N):
    l.append((int(input()), i))
s_l = sorted(l)
max_idx = 0
for i in range(N):
    max_idx = max(max_idx, (s_l[i][1] - i))
print(max_idx + 1)