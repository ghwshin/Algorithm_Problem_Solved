n, m = map(int, input().split())
lec = list(map(int, input().split()))

start = 0 # 최소 인덱스
end = 0 # 최대 인덱스
for i in lec:
    if start < i:
        start = i
    end += i

while start <= end:
    mid = (start + end) // 2
    sum = 0
    cnt = 0
    for i in range(n):
        if sum + lec[i] > mid:
            # 블루레이 수를 증가시킴
            cnt += 1
            sum = 0
        sum += lec[i]
    if sum != 0:
        # 마지막에 남은 합이 있으면 카운트 증가
        cnt += 1
    if cnt > m:
        # 이진 탐색 : 오른쪽 탐색
        start = mid + 1
    else:
        # 이진 탐색 : 왼쪽 탐색
        end = mid - 1
print(start)