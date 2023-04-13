arr = input()
last = ""
arrow = ""
res = []
for j in range(len(arr)):
    check = 0
    i = arr[j]
    if i == ">" and "<" in arrow:
        res.append(arrow[:-1])
        arrow = arrow[-1]
        arrow += i
        check = 1
    if j == len(arr) - 1:
        arrow += i
        res.append(arrow)
    if last == ">" and i == "<":
        last = i
        res.append(arrow)
        arrow = i
    elif last == "-" and i == "<":
        last = i
        res.append(arrow)
        arrow = i
    elif last == ">" and i == "-":
        last = i
        res.append(arrow)
        arrow = i
    else:
        if check == 0:
            last = str(i)
            arrow += str(i)
for i in res:
    print(i)
