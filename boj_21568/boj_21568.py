# 현재 채점은 불가능
# 확장 유클리드 호제법을 사용
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def gcd_ex(a, b):
    result = [1, 0]
    if b == 0:
        return result
    q = a // b
    xy = gcd_ex(b, a % b)
    result[0] = xy[1]
    result[1] = xy[0] - xy[1] * q
    return result

A, B, C = map(int, input().split())
a_b_gcd = gcd(A, B)
if C % a_b_gcd != 0:
    print(-1)
else:
    K = C // a_b_gcd
    xy = gcd_ex(A, B)
    print(xy[0] * K, end=' ')
    print(xy[1] * K)

