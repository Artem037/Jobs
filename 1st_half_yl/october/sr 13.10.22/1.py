alp = 'abcdefghijklmnopqrstuvwxyz'
k = 0
bad = []
with open('castle.txt', 'r', encoding='utf8') as f:
    data = ''.join(f.read().strip())
for i in data:
    if i != ' ':
        if data.index(i) < len(data) - 1:
            if alp.find(i.lower()) > alp.find(data[data.index(i) + 1].lower()):
                bad.append(data[data.index(i) + 1])
                k = 1
        else:
            if k:
                bad.append(i)
with open('verdict.txt', 'w', encoding='utf8') as f:
    if k:
        f.write(''.join(bad))
    else:
        f.write('OKAY')
