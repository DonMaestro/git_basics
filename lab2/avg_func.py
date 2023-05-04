#!/usr/bin/env/ python3

def avg(*iterable):
    return sum(iterable) / len(iterable)


def main(args):
    print(args)

    print(avg(1, 2, 3))
    print(avg(1))
    print(avg(1, 2, 3, 4, 5))


if __name__ == '__main__':
    import sys

    main(sys.argv)

