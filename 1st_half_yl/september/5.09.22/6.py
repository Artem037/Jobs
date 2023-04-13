import sys

word = input()
data = list(map(str.strip, sys.stdin))
n = 0
res = []

for i in data:
    k = 1
    word1 = list(word)
    for j in i:
        if j not in word1:
            k = 0
        else:
            word1.remove(j)
    if k:
        n += 1
        res.append(i)
print(n)
for i in res:
    print(i)
