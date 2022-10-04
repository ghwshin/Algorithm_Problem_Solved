equation = list(map(str, input().split('-')))
result = 0
def sum(plus):
    sum = 0
    tmp = plus.split('+')
    for i in tmp:
        sum += int(i)
    return sum

for i in range(len(equation)):
    tmp = sum(equation[i])
    if i == 0:
        result += tmp
    else:
        result -= tmp

print(result)
