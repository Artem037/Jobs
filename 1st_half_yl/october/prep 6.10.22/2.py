with open('boat_suits.txt', 'rt') as f:
    read_data = f.read().split('\n')
color = read_data[1]
people = read_data[4:-1]
k = 0
summ = 0
p_res = []
for i in people:
    name, color1, count = i.split()
    if color1 == color:
        k += 1
        p_res.append(name)
        summ += int(count)
p_res1 = [len(i) for i in p_res]
print(p_res[sorted(list(p_res1.index(max(p_res1))))[0]])
with open('colored_dress.txt', 'wt') as f:
    f.write(f'{str(k)}\n')
    f.write(f'{max(sorted(p_res))}\n')
    f.write(str(summ))
