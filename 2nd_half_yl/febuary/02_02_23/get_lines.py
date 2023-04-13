import argparse


def count_lines(path):
    try:
        with open(path) as f:
            print('alr')
            return sum(1 for _ in f)
    except Exception:
        return 0


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", default='')
    sp = parser.parse_args()
    print(count_lines(sp.file))
