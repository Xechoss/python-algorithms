import numpy as np
import math


def lagran(x, w):
    n = len(x)
    lr = np.zeros((n, n), dtype=np.float)
    for j in range(n):
        pt = 1
        for k in range(n):
            if k == j:
                continue
            fac = x[j] - x[k]
            pt = np.polymul(pt, np.poly(x[k])) / fac
        lr[j, :] = pt
    w = np.array(w)
    c = w@lr
    print(c)
    print(lr)
    return c


def main():
    a = float(input())
    x = [float(i) for i in input().split()]
    y = []
    for i in x:
        y.append(math.cos(i))
    p = lagran(x, y)
    print('P'+str(len(x)-1)+'('+str(a)+')=', end='')
    print('%.6f' % np.polyval(p, a))


if __name__ == '__main__':
    main()