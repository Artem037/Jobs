import argparse

parser = argparse.ArgumentParser()
parser.add_argument("args", nargs='*', type=str)
parser.add_argument("--sort", action="store_true")

args = parser.parse_args()

list1 = [i.split("=") for i in args.args]

res = {}
res1 = {}
k = ''
for key, value in list1:
    res[key] = value

if args.sort:
    for key, value in sorted([[key, res[key]] for key in res.keys()], key=lambda x: x[0]):
        print(f'Key: {key} Value: {res[key]}')
else:
    for key in res.keys():
        print(f'Key: {key} Value: {res[key]}')
