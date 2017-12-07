#!/usr/bin/env python3
d = input()
l = len(d)

s1 = 0
for i in range(l):
    if d[i] == d[(i + 1) % l]:
        s1 += int(d[i])
print(s1)

s2 = 0
for i in range(l):
    if d[i] == d[(i + int(l / 2)) % l]:
        s2 += int(d[i])
print(s2)
