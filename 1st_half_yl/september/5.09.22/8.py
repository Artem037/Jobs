a = int(input())
data = []
res = []
for i in range(a):
    data += [input().split()]
le, r, t, b = data[0], data[0], data[0], data[0]
minx, maxx, miny, maxy = int(data[0][0]), int(data[0][0]), int(data[0][1]), int(data[0][1])
for x, y in data:
    x, y = int(x), int(y)
    if abs(x) > abs(y):
        print(f'({x}, {y})')
    if x < minx:
        le = [str(x), str(y)]
        minx = x
    if x > maxx:
        r = [str(x), str(y)]
        maxx = x
    if y < miny:
        b = [str(x), str(y)]
        miny = y
    if y > maxy:
        t = [str(x), str(y)]
        maxy = y
print(f'left: ({", ".join(le)})')
print(f'right: ({", ".join(r)})')
print(f'top: ({", ".join(t)})')
print(f'bottom: ({", ".join(b)})')
