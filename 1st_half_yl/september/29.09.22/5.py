with open('price.txt', 'r', encoding='utf8') as f:
    data = [i.split('\t') for i in ''.join(f.read()).split('\n')]
summ = 0
if data:
    for i in data:
        summ += (int(i[1]) * float(i[2]))
print(summ)
