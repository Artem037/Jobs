a = input().split(' -> ')
names = [a.index(input()) for i in range(int(input()))]
for i in range(len(names)):
    if names[i] == 0:
        print(' -> '.join([a[0], a[1]]))
    elif names[i] == len(a) - 1:
        print(' -> '.join([a[-2], a[-1]]))
    else:
        print(' -> '.join([a[names[i] - 1], a[names[i]], a[names[i] + 1]]))
