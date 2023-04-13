import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--movie", choices=['melodrama', 'football', 'other'], type=str, default='other')
parser.add_argument("--barbie", metavar="arg", type=int, default=50)
parser.add_argument("--cars", metavar="arg", type=int, default=50)

args = parser.parse_args()

if args.barbie > 100 or args.barbie < 0:
    args.barbie = 50

if args.cars > 100 or args.cars < 0:
    args.cars = 50

if args.movie == 'melodrama':
    m = 0
elif args.movie == 'football':
    m = 100
elif args.movie == 'other':
    m = 50

boy = int((100 - args.barbie + args.cars + m) / 3)
girl = 100 - boy

print('boy:', boy)
print('girl:', girl)
