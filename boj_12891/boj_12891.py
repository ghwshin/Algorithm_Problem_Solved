# A, C, G, T
import sys
input = sys.stdin.readline

def acgt_cal(string):
    acgt = [0] * 4
    for s in string:
        if s == 'A':
            acgt[0] += 1
        elif s == 'C':
            acgt[1] += 1
        elif s == 'G':
            acgt[2] += 1
        else:
            acgt[3] += 1
    return acgt

def acgt_valid(char):
    if char == 'A':
        return 0
    elif char == 'C':
        return 1
    elif char == 'G':
        return 2
    else:
        return 3

s, p = map(int, input().split())
input_str = input()
# a, c, g, t
dna = list(map(int, input().split()))
n = len(input_str) - 1
count = 0

start_idx = 0
end_idx = p - 1
cur_dna = acgt_cal(input_str[start_idx:end_idx+1])

while end_idx < n:
    if dna[0] <= cur_dna[0] and dna[1] <= cur_dna[1] and dna[2] <= cur_dna[2] and dna[3] <= cur_dna[3]:
        count += 1
    cur_dna[acgt_valid(input_str[start_idx])] -= 1
    start_idx += 1

    end_idx += 1
    if end_idx < n:
        cur_dna[acgt_valid(input_str[end_idx])] += 1
print(count)
