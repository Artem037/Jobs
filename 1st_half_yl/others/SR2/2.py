import csv

with open('wares.csv', encoding="utf8") as f:
    reader = csv.reader(f, delimiter=';', quotechar='"')
    data = [i for i in reader]

res = []
k = 0

for name, price in data:
    price = int(price)
    if price > 1000:
        res.append('error')
    else:
        k = 1
        print(price)
        if 1000//price > 10:
            res.append([name, 10])
        else:
            res.append([name, 1000//price])
if k:
    print(res[0][1])
    print(sorted(res, key=lambda x: x[1], reverse=True))
else:
    print('error')