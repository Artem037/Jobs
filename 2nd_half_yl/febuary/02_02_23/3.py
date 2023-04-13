import argparse

parser = argparse.ArgumentParser()

parser.add_argument("source", type=str)
parser.add_argument("receiver", type=str)
parser.add_argument('--upper', action="store_true")
parser.add_argument('--lines', type=int)

args = parser.parse_args()

with open(args.source, 'r', encoding='utf-8') as f:
    data = [i.rsplit('\n')[0] for i in f]

if args.lines:
    if len(data) >= args.lines:
        data = data[:args.lines]

with open(args.receiver, 'w', encoding='utf-8') as f:
    if args.upper:
        data = [i.upper() for i in data]
    f.write('\n'.join(data))
