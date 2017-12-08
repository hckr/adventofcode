#!/usr/bin/env python3

rows = []

try:
    while True:
        rows.append([ int(x) for x in input().split() ])
except EOFError:
    pass

###

def s1_row_val(r):
    return max(r) - min(r)

def s2_row_val(r):
    r_len = len(r)
    for i, a in enumerate(r):
        for i2 in range(i + 1, r_len):
            b = r[i2]
            if a % b == 0:
                return int(a / b)
            if b % a == 0:
                return int(b / a)
    return None

###

s1 = 0
s2 = 0

for r in rows:
    s1 += s1_row_val(r)
    s2 += s2_row_val(r)

print(s1)
print(s2)
