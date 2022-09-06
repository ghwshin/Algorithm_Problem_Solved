from collections import deque

instr = input().strip()
ex = input().strip()
dq = deque()
val = str()
exsize = len(ex)
for i in range(len(instr)):
    isequal = False
    dq.append(instr[i])
    val += instr[i]
    if len(val) < exsize:
        continue
    elif len(val) > exsize:
        val = val[1:]
    if val == ex:
        for j in range(exsize):
            dq.pop()
        if len(dq) != 0:
            val = str()
            k = len(dq) - exsize
            if k < 0:
                for k in range(len(dq)):
                    val += dq[k]
            else:
                for l in range(exsize):
                    val = dq[len(dq) - 1 - l] + val
                    k -= 1
        else:
            val = str()
if len(dq) == 0:
    print("FRULA")
else:
    while len(dq) != 0:
        print(dq.popleft(), end='')
