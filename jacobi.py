import numpy as np


def jacobi(a, b, p, delta, max1):
    n = len(b)
    x = np.zeros((n, 1), dtype=np.double)
    for i in range(max1):
        for j in range(n):
            x[j] = (b[j]-(a[j, :] @ p[:]-a[j][j]*p[j]))/a[j, j]
        err = np.max(np.abs(x-p))
        relerr = err/(np.max(np.abs(x))+delta)
        p = x.copy()
        if err < delta or relerr < delta:
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
    max2, x = jacobi(a, b, p, delta, max1)
    print(max2)
    print(x)


if __name__ == '__main__':
    main()