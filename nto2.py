n = int(input())
m = int(input())
stations = [input() for i in range(m)]
k = int(input())
visits = [input() for i in range(k)]

all_stat = {}
all_visit = {}

res = 0

for i in stations:
    if i[0] in all_stat.keys():
        all_stat[i[0]].append(i[2:])
    else:
        all_stat[i[0]] = [i[2:]]
for i in visits:
    if i[0] in all_visit.keys():
        all_visit[i[0]].append(i[2:])
    else:
        all_visit[i[0]] = [i[2:]]

for i in range(n):
    for j in all_visit[str(i+1)]:
        print(len(all_visit[str(i+1)]))
        d_v, m_v, y_v = j.split('.')
        d_s, m_s, y_s = all_stat[str(i+1)][all_visit[str(i+1)].index(j)].split('.')
        d_v, m_v, y_v = int(d_v), int(m_v), int(y_v)
        # print(d_v, m_v, y_v)
        d_s, m_s, y_s = int(d_s), int(m_s), int(y_s)
        # print(d_s, m_s, y_s)
        if y_v >= y_s:
            if m_v >= m_s:
                if d_v >= d_s:
                    res += 1
                    # print('d')
                break
            # print('m')
            break
        # print('y')
        break
# print(res)