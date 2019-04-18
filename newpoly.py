import numpy as np
import math


def new_poly(x, y):
    n = len(x)
    d = np.zeros((n, n), dtype=np.float)
    d[:, 0] = y
    for i in range(1, n):
        for j in range(i, n):
            fac = x[j] - x[j-i]
            d[j, i] = (d[j, i-1]-d[j-1, i-1])/fac
    c = d[n-1, n-1]
    for i in range(n-1, 0, -1):
        c = np.polymul(c, np.poly1d([1, -x[i]]))
        m = len(c)
        c[m-1] += d[i, i]
    return c


def main():
    a = float(input())
    x = [float(i) for i in input().split()]
    y = []
    for i in x:
        y.append(math.cos(i))
    p = new_poly(x, y)
    print(p)
    print('%.6f' % np.polyval(p, a))


if __name__ == '__main__':
    main()