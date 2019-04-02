#! /usr/bin/env python3


def nextInt():
    num = 0
    while True:
        num += 1
        yield num

if __name__ == '__main__':
    fn = nextInt()
    print(next(fn))
    print(next(fn))
    print(next(fn))
    print(next(fn))
    print(next(fn))