import numpy as np


def lcs_length(m, n, x, y, c, b):
    for i in range(m+1):
        c[i][0] = 0
    for j in range(n+1):
        c[0][j] = 0
    for i in range(1, m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1]+1
                b[i][j] = 1
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i][j] = 2
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 3
    print(c)


def lcs(i, j, x, b):
    if i == -1 or j == -1:
        return
    if b[i][j] == 1:
        lcs(i-1, j-1, x, b)
        print(x[i-1], end='')
    elif b[i][j] == 2:
        lcs(i-1, j, x, b)
    else:
        lcs(i, j-1, x, b)


def main():
    x = np.array(input().split())
    y = np.array(input().split())
    m = len(x)
    n = len(y)
    c = np.zeros((m+1, n+1), dtype=np.int)
    b = np.zeros((m+1, n+1), dtype=np.int)
    lcs_length(m, n, x, y, c, b)
    lcs(m, n, x, b)


if __name__ == '__main__':
    main()