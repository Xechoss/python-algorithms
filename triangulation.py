import numpy as np
import math
global weight
weight = None


def w(i, j, k):
    global weight
    return weight[i][j]+weight[j][k]+weight[i][k]


def min_weight(n, t, s):
    for i in range(n):
        t[i][i] = 0
    for r in range(2, n + 1):
        for i in range(1, n - r + 1):
            j = i + r - 1
            t[i][j] = t[i + 1][j] + w(i - 1, i, j)
            s[i][j] = i
            for k in range(i + 1, j):
                u = t[i][k] + t[k + 1][j] + w(i - 1, k, j)
                if u < t[i][j]:
                    t[i][j] = u
                    s[i][j] = k
    print('s', s)


def create_weight(p, n):
    global weight
    for i in range(n):
        weight[i][i] = 0
    for i in range(n+1):
        for j in range(i+1, n):
            weight[i][j] = math.sqrt((p[i, :1]-p[j, :1])**2+(p[i, 1:]-p[j, 1:])**2)
    print('w',weight)


def traceback(i, j, s):
    if i == j:
        return
    else:
        traceback(i, int(s[i][j]), s)
        traceback(int(s[i][j] + 1), j, s)
        print(str(i-1)+str(int(s[i][j]))+str(j))


def main():
    n = int(input())
    p = np.zeros((n, 2), dtype=np.int)
    for i in range(n):
        p[i, :] = np.array(input().split(), dtype=np.int)
    global weight
    weight = np.zeros((n, n), dtype=np.double)
    t = np.zeros((n, n), dtype=np.double)
    s = np.zeros((n, n), dtype=np.double)
    create_weight(p, n)
    min_weight(n, t, s)
    traceback(1, n-1, s)


if __name__ == '__main__':
    main()
