def funcSort(x):
    return x[2]


cond = input()
points = input()
res = []
with open(cond, 'r', encoding='utf8') as f:
    data = f.read().split('\n')
    st, nd = data[0], data[1]
with open(points, 'r', encoding='utf8') as f:
    data = [i.split() for i in f.read().strip().split('\n')]
for i in data:
    x, y = int(i[0]), int(i[1])
    if eval(st) and eval(nd):
        res.append((x, y, (x ** 2 + y ** 2) ** 0.5))
res_1 = sorted(res, key=funcSort)
with open('answer.txt', 'w', encoding='utf8') as f:
    for i in res_1:
        if res_1.index(i) < len(res) - 1:
            f.write(f'({i[0]}, {i[1]}, {i[2]})\n')
        else:
            f.write(f'({i[0]}, {i[1]}, {i[2]})')
