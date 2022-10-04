import sys
input = sys.stdin.readline
t = int(input())
def gcd(a, b):
    if a < b:
        a, b = b, a
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
for _ in range(t):
    A, B = map(int, input().split())
    ggcd = gcd(A, B)
    print(ggcd * (A // ggcd) * (B // ggcd))
    # (a * b / 최대공약수)