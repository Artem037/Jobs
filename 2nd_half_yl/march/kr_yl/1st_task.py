import sys

stars = input().split()
li = [i.strip('\n') for i in sys.stdin]
for row in li:
    max_len = 0
    max_order = []
    row = list(row)
    for i in range(len(row)):
        symb = row[i]
        if symb in stars:
            order = [symb]
            for symb_in_order in row[i + 1:]:
                order.append(symb_in_order)
                if symb_in_order in stars:
                    break
            if len(order) >= max_len:
                max_len = len(order)
                max_order = order
    print(''.join(max_order))
