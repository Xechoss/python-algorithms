import numpy as np


def traceback(i, j, s):
    if i == j:
        print('A' + str(i), end='')
    else:
        print('(', end='')
        traceback(i, int(s[i][j]), s)
        traceback(int(s[i][j] + 1), j, s)
        print(')', end='')


def matrix_chain(p, n, m, s):
    for i in range(n):
        m[i][i] = 0
    for r in range(2, n+1):
        for i in range(1, n-r+1):
            j = i+r-1
            m[i][j] = m[i+1][j]+p[i-1]*p[i]*p[j]
            s[i][j] = i
            for k in range(i+1, j):
                t = m[i][k]+m[k+1][j]+p[i-1]*p[k]*p[j]
                if t < m[i][j]:
                    m[i][j] = t
                    s[i][j] = k


def main():
    n = int(input())
    n = n+1
    p = np.array(input().split(), dtype=np.int)
    m = np.zeros((n, n), dtype=np.int)
    s = np.zeros((n, n), dtype=np.int)
    matrix_chain(p, n, m, s)
    print(m[1:, 1:])
    print(s[1:, 1:])
    traceback(1, n-1, s)


if __name__ == '__main__':
    main()