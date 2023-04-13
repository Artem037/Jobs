import json
import requests
import datetime

date_inp, time_inp = input().split()
date_inp = date_inp.split('/')
time_inp = time_inp.split(':')

with open('rita.json', 'r', encoding='utf-8') as file:
    templates = json.load(file)

resp = requests.get(f'http://{templates["host"]}:{templates["port"]}')

data = resp.json()
good_dates = []
res = []
for sl_got in data:
    year, month, day = sl_got['date'].split('/')
    hour, minute = sl_got['time'].split(':')
    event = sl_got['event']
    participants = sl_got['participants']

    date1 = datetime.datetime(int(date_inp[0]), int(date_inp[1]), int(date_inp[2]), int(time_inp[0]), int(time_inp[1]))
    date2 = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute))

    if date2 >= date1:
        res.append([event, participants])
res.sort(key=lambda x: x[1], reverse=True)
print(res[0][0], str(res[0][1]))
