# N을 최대한 분할 하면 다음과 같다.
# ex) 15 = 1 + 2 + 3 + 4 + 5
# 하지만 위의 분할에서 부분을 더하면 또 다른 분할이 된다. ex) 15 = 6 + 7
# 따라서 15까지의 배열을 만들어 두개의 포인터를 만들고
# start_idx => 연속된 자연수에서 삭제
# end_idx => 현재 연속된 범위를 확장
n = int(input())
re_sum = 1
count = 1
start_idx = 1
end_idx = 1
while end_idx != n:
    if re_sum == n:
        end_idx += 1
        count += 1
        re_sum += end_idx
    elif re_sum > n:
        re_sum -= start_idx
        start_idx += 1
    else:
        end_idx += 1
        re_sum += end_idx
print(count)