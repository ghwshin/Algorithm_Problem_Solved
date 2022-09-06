# 시간 제한이 1초 이므로, O(N)의 연산이 필요함.
import sys
n = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
stack = []
result = [0] * n
for i in range(n):
    while stack and A[stack[-1]] < A[i]:
        index = stack.pop()
        result[index] = A[i]
    stack.append(i)
while stack:
    index = stack.pop()
    result[index] = -1
for a in result:
    print(a, end=' ')