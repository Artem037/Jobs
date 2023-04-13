class FewArgumentsError(Exception):
    pass


class AttributeError(Exception):
    pass


class EmptyResultError(Exception):
    pass


def most_wonderful_flavors(*data, criterion='beroha'):
    res = []
    if len(data) < 2:
        raise FewArgumentsError('Too few flavors')
    if len(criterion) < 2:
        raise AttributeError('Value is too small')
    for i in data:
        for j in i:
            if i.find(j) < len(i) - 1:
                if criterion.find(j + i[i.find(j) + 1]) != -1:
                    res.append(i)
                    break
    if not res:
        raise EmptyResultError('Result is empty')
    return sorted(res)


args = ['violets', 'lemon zest', 'liquid chocolate']
criterion = "ytrewq"
print(most_wonderful_flavors(*args, criterion=criterion))
