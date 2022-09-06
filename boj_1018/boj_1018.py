n, m = input().split(' ')
n = int(n)
m = int(m)
chess = list()
for _ in range(n):
    chess.append(input())

chess_w = list()
for i in range(8):
    if i % 2 == 1:
        chess_w.append("BWBWBWBW")
    else:
        chess_w.append("WBWBWBWB")

chess_b = list()
for i in range(8):
    if i % 2 == 1:
        chess_b.append("WBWBWBWB")
    else:
        chess_b.append("BWBWBWBW")

min_sq = 9999999999
for i in range(n):
    if i + 8 > n:
        break
    for j in range(m):
        if j + 8 > m:
            break
        min_tmp_w = 0
        min_tmp_b = 0
        comp_i = 0
        comp_j = 0
        for k in range(i, i + 8):
            comp_j = 0
            for l in range(j, j + 8):
                if chess[k][l] != chess_w[comp_i][comp_j]:
                    min_tmp_w += 1
                if chess[k][l] != chess_b[comp_i][comp_j]:
                    min_tmp_b += 1
                comp_j += 1
            comp_i += 1
        min_sq = min(min_tmp_b, min_tmp_w, min_sq)


print(min_sq)