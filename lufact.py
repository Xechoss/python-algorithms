import numpy as np


def backfact(a, b, r):
    n = b.size
    x = np.zeros((n, 1), dtype=np.double)
    y = np.zeros((n, 1), dtype=np.double)
    y[0] = b[r[0]]
    for k in range(1, n):
        y[k] = b[r[k]]-a[k, :k]@y[:k]
    x[n-1] = y[n-1]/a[n-1, n-1]
    for k in range(n-2, -1, -1):
        x[k] = (y[k]-a[k, k+1:]@x[k+1:])/a[k, k]
    return x


def lufact(a, b):
    n = b.size
    r = np.arange(n)
    for p in range(n):
        max_row = np.argmax(np.abs(a[p:, p]))+p
        a[[p, max_row], :] = a[[max_row, p], :]
        r[p], r[max_row] = r[max_row], r[p]
        if a[p, p] < 0:
            print('error！！！')
            break
        for k in range(p+1, n):
            m = a[k, p]/a[p, p]
            a[k, p] = m
            a[k, p+1:] = a[k, p+1:] - m*a[p, p+1:]
    print(a)
    return backfact(a, b, r)


def main():
    n = int(input())
    a = np.zeros((n, n), dtype=np.double)
    for r in range(n):
        a[r, :] = np.array(input().split(), dtype=np.double)
    b = np.zeros((n, 1), dtype=np.double)
    for r in range(n):
        b[r] = np.array(input(), dtype=np.double)
    x = lufact(a, b)
    print(x)


if __name__ == '__main__':
    main()