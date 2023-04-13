def dig(k):
    if k < 10:
        return k
    else:
        return k % 10 + dig(k // 10)


def task():
    h = list(map(int, input().split(" ")))
    m = list(map(int, input().split(" ")))
    r = []
    for a in h:
        sa = dig(a)
        for b in m:
            if sa != dig(b):
                r.append((a, b))
    for (x, y) in sorted(r):
        x, y = str(x), str(y)
        if len(x) == 2 and len(y) == 2:
            print(f'{x}:{y}')
        elif len(x) == 2 and len(y) == 1:
            print(f'{x}:0{y}')
        elif len(x) == 1 and len(y) == 2:
            print(f'0{x}:{y}')
        else:
            print(f'0{x}:0{y}')


task()
