# 퀵 정렬로 풀이
# sort 써도댐
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
A = list(map(int, input().split()))

def quickSort(S, E, K):
    global A
    # 재귀 탈출 조건 : start < end
    if S < E:
        pivot = partition(S, E)
        if pivot == K: # pivot이 K번째 위치 : 찾음 (정렬 완료)
            return
        elif K < pivot: # 왼쪽 정렬
            quickSort(S, pivot - 1, K)
        else: # 오른쪽 정렬
            quickSort(pivot + 1, E, K)
def partition(S, E):
    global A
    # 분할할 갯수가 두개?
    if S + 1 == E:
        if A[S] > A[E]:
            A[S], A[E] = A[E], A[S]
        return E

    M = (S + E) // 2 # pivot은 중앙으로 잡기
    A[S], A[M] = A[M], A[S] # pivot switching (앞으로)
    pivot = A[S]
    i = S + 1
    j = E

    while i <= j: # i == j 일때까지!
        while pivot < A[j] and j > 0:
            j -= 1
        while pivot > A[i] and i < len(A) - 1:
            i += 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    A[S] = A[j]
    A[j] = pivot
    return j
quickSort(0, N - 1, K - 1)
print(A[K - 1])