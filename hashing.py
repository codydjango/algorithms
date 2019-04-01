#! /usr/bin/env python3

if __name__ == '__main__':
    arr = ['test_{0}'.format(i) for i in range(100000)]
    machines = {}
    mod = 7
    for a in arr:
        machines.setdefault(hash(a) % mod, []).append(a)

    for (k,v) in machines.items():
        print(k, len(v))