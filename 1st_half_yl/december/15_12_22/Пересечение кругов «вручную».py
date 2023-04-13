from math import sqrt

x1, y1, r1 = input().split()
x2, y2, r2 = input().split()
x1, y1, r1, x2, y2, r2 = int(x1), int(y1), int(r1), int(x2), int(y2), int(r2)
distance = sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
if distance <= r1 + r2:
    print('YES')
else:
    print('NO')
