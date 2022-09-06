# 구간의 합을 구하기 위해서 구간 합 배열이 필요하다.
# 합을 구해야 하는 횟수는 최대 100000번, 수의 개수는 100000이다. 최대 O(n)으로 계산시
# 불가능 함을 확인할 수 있으며, O(1) 알고리즘을 사용해야 한다.
data_n, question_n = map(int, input().split())
data = list(map(int, input().split()))
sum_arr = [0 for i in range(data_n)]
sum_arr[0] = data[0]
for i in range(1, data_n):
    sum_arr[i] = (sum_arr[i - 1] + data[i])
for n in range(question_n):
    start, end = map(int, input().split())
    if start == 1:
        print(sum_arr[end - 1])
    else:
        print(sum_arr[end - 1] - sum_arr[start - 2])