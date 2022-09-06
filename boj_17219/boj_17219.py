import sys
t = input().split()
n = int(t[0])
m = int(t[1])
password = dict()
for i in range(n):
    t = sys.stdin.readline().split()
    password[t[0]] = t[1]
for i in range(m):
    a = sys.stdin.readline().rstrip()
    print(password[a])