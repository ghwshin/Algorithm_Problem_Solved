# O(nlogn)의 알고리즘이 필요하다.
# 분할 후 병합시 몇번 swap되는가?
import sys
input = sys.stdin.readline
print = sys.stdout.write
result = 0

def merge_sort(start, end):
    global tmp, N, result
    # 더 분할 할 수 없음
    if end - start < 1:
        return
    mid = int(start + (end - start) / 2)
    merge_sort(start, mid)
    merge_sort(mid + 1, end)
    # 끝까지 분할 되고 난 뒤에 임시 배열에 배정
    for i in range(start, end + 1):
        tmp[i] = A[i]
    cur = start
    idx_1 = start
    idx_2 = mid + 1
    while idx_1 <= mid and idx_2 <= end:
        if tmp[idx_1] > tmp[idx_2]:
            A[cur] = tmp[idx_2]
            # 병합 정렬시 뒤쪽이 더 크면 앞쪽으로 병합되는 과정에서
            # 얼마만큼 이동했는지가 swap의 횟수가 됨
            result += idx_2 - cur
            cur += 1
            idx_2 += 1
        else:
            A[cur] = tmp[idx_1]
            cur += 1
            idx_1 += 1
    while idx_1 <= mid:
        A[cur] = tmp[idx_1]
        cur += 1
        idx_1 += 1
    while idx_2 <= end:
        A[cur] = tmp[idx_2]
        cur += 1
        idx_2 += 1

N = int(input())
A = [0] + list(map(int, input().split()))
tmp = [0] * (N + 1)
merge_sort(1, N)
print(str(result))
