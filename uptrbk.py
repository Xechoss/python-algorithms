import numpy as np


def backsub(a, b):
    n = b.size
    x = np.zeros([n, 1], dtype=np.double)
    x[n-1] = b[n-1]/a[n-1, n-1]
    for k in range(n-2, -1, -1):
        x[k] = (b[k]-a[k, k+1:] @ x[k+1:])/a[k, k]
    return x


def uptrai(a, b):
    N = b.size
    aug = np.hstack((a, b))
    for p in range(N):
        max_row = np.argmax(np.abs(aug[p:, p]))+p
        aug[[p, max_row], :] = aug[[max_row, p], :]
        if aug[p, p] == 0:
            break
        for k in range(p+1, N):
            m = aug[k, p]/aug[p, p]
            aug[k, p] = 0
            aug[k, p+1:] = aug[k, p+1:]-m*aug[p, p+1:]
    x = backsub(aug[:, :-1], aug[:, -1])
    print(x)


def main():
    n = input()
    n = int(n)
    a = np.zeros((n, n), dtype=np.double)
    for r in range(n):
        a[r, :] = np.array(input().split(), dtype=np.double)
    b = np.zeros((n, 1), dtype=np.double)
    for r in range(n):
        b[r] = np.array(input(), dtype=np.double)
    uptrai(a, b)


if __name__ == '__main__':
    main()