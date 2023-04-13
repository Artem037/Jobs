import argparse
import os

parser = argparse.ArgumentParser()

parser.add_argument("source", type=str)
parser.add_argument("receiver", type=str)
parser.add_argument('--upper', action="store_true")
parser.add_argument('--lines', type=int)

args = parser.parse_args()
data = []

if os.path.exists(args.source):
    with open(args.source, 'r', encoding='utf-8') as f:
        data = [i.rsplit('\n')[0] for i in f]

if not args.lines or args.lines > len(data):
    args.lines = len(data)
    text = ''.join(data[:args.lines])
else:
    if len(data) >= args.lines:
        data = data[:args.lines]

with open(args.receiver, 'w', encoding='utf-8') as f:
    if args.upper:
        data = [i.upper() for i in data]
    for i in data:
        f.write(i + '\n')
