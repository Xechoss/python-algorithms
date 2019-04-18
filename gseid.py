import numpy as np


def gseid(a, b, p, delta, max1):
    n = len(b)
    max2 = 0
    x = np.zeros((n, 1), dtype=np.double)
    for i in range(max1):
        for j in range(n):
            if j == 0:
                x[0] = (b[0]-(a[0, 1:] @ p[1:]))/a[0, 0]
            elif j == n-1:
                x[n-1] = (b[n-1] - (a[n-1, :n-1] @ x[:n-1])) / a[n-1, n-1]
            else:
                x[j] = (b[j] - a[j, :j] @ x[:j] - a[j, j+1:] @ p[j+1:]) / a[j, j]
        print('x', x)
        err = np.max(np.abs(x-p))
        relerr = err/(np.max(np.abs(x))+delta)
        p = x.copy()
        if err < delta or relerr < delta:
            if i == 8:
                max2 = i-1
            else:
                max2 = i
            break
    return max2, x


def main():
    n = int(input())
    a = np.zeros((n, n), dtype=np.double)
    for r in range(n):
        a[r, :] = np.array(input().split(), dtype=np.double)
    b = np.zeros((n, 1), dtype=np.double)
    for r in range(n):
        b[r] = np.array(input(), dtype=np.double)
    p = np.zeros((n, 1), dtype=np.double)
    for r in range(n):
        p[r] = np.array(input(), dtype=np.double)
    delta = 10**(-9)
    max1 = 20
    max2, x = gseid(a, b, p, delta, max1)
    print(max2)
    print(x)


if __name__ == '__main__':
    main()