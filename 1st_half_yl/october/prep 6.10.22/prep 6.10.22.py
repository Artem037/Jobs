class ZeroDivisionError(Exception):
    pass


class NotEnoughError(Exception):
    pass


def stubborness(*data):
    res = []
    for i in data:
        st = i[0]
        if len(i) < 2:
            raise NotEnoughError('Not enough values')
        if min(list(i[1:])) == 0:
            raise ZeroDivisionError('Cannot be divided by zero')
        if st % min(list(i[1:])) == 0 and st % max(list(i[1:])) == 0:
            res.append(st)
    if not res:
        raise IndexError('Empty Return Error')
    return sorted(list(set(res)))


data = [(8, 2, 16), (14, 6, 1, 7, 14), (6, 9), (8, 1, 8)]
print(*stubborness(*data))

# data = [(12, 6, 2), (14, 6, 0, 12), (10, 9, 5, 5, 13, 5, 5)]
# print(*stubborness(*data))

# data = [(7, 3), (14, 28, 2), (11,)]
# print(*stubborness(*data))

# data = [(2, 3, 7)]
# print(*stubborness(*data))