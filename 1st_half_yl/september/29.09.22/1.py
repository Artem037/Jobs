from random import choice

with open('lines.txt', 'r') as f:
    data = f.read()
if data:
    print(choice(data.split('\n')))
