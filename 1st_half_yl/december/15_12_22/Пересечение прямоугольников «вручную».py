x1, y1, w1, h1 = input().split()
x2, y2, w2, h2 = input().split()
x1, y1, w1, h1, x2, y2, w2, h2 = int(x1), int(y1), int(w1), int(h1), int(x2), int(y2), int(w2), int(h2)

dist1 = [x1 + w1, y1 + h1]
dist2 = [x2 + w2, y2 + h2]

if (x1 <= dist2[0] <= dist1[0] and y1 <= dist2[1] <= dist1[1]) or x1 == dist2[0] or y1 == dist2[1] or (
        x2 <= dist1[0] <= dist2[0] and y2 <= dist1[1] <= dist2[1]) or x2 == dist1[0] or y2 == dist1[1]:
    print('YES')
else:
    print('NO')
