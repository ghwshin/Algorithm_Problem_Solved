n = int(input())
stack = []
next_num = 1
result = ""
for i in range(n):
    current_num = int(input())
    if next_num <= current_num:
        for j in range(next_num, current_num + 1):
            stack.append(j)
            result += "+"
        next_num = stack[-1] + 1
        stack.pop()
        result += "-"
    else:
        if not stack or stack[-1] < current_num:
            result = "NO"
            break
        else:
            while stack[-1] != current_num:
                stack.pop()
                result += "-"
            stack.pop()
            result += "-"
if result == "NO":
    print(result)
else:
    for ch in result:
        print(ch)