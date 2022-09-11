# 단계별로 생각해보자!
# 백트래킹 문제이며, dfs로 해결 가능함
import sys
print = sys.stdout.write
n = int(input())
def prime_detect(num):
    for i in range(2, (num // 2 + 1)):
        if num % i == 0:
            return False
    return True

def DFS(num, pos):
    if pos == n:
        print(str(num) + "\n")
    else:
        for i in range(1, 10, 2):
            next_num = num * 10 + i
            if prime_detect(next_num):
                DFS(next_num, pos + 1)
DFS(2, 1)
DFS(3, 1)
DFS(5, 1)
DFS(7, 1)
