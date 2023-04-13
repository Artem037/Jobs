n = int(input())
all = [input().split() for i in range(n)]
axis = []
first = 0
second = 0
third = 0
fourth = 0
for i in all:
    x, y = int(i[0]), int(i[1])
    if not x or not y:
        axis.append([x, y])
    elif x > 0 and y > 0:
        first += 1
    elif x < 0 and y > 0:
        second += 1
    elif x < 0 and y < 0:
        third += 1
    else:
        fourth += 1
for i in axis:
    print(f'({i[0]}, {i[1]})')
print(f'I:{first}, II:{second}, III:{third}, IV:{fourth}.')
