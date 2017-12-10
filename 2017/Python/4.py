#!/usr/bin/env python3

passphrases = []

try:
    while True:
        passphrases.append(input())
except EOFError:
    pass

s1 = 0
for passphrase in passphrases:
    words = set()
    for word in passphrase.split():
        if word in words:
            break
        words.add(word)
    else:
        s1 += 1

s2=0
for passphrase in passphrases:
    words = set()
    for word in passphrase.split():
        if any(len(word) == len(w) and all(l in w for l in word) for w in words):
            break
        words.add(word)
    else:
        s2 += 1

print(s1)
print(s2)
