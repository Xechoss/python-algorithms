"""
【问题描述】使用动态规划算法解0-1背包问题，具体来说就是，依据递归式，按照顺序求得子问题，
            使得选择合适物品装入背包可使这些物品的重量总和不超过背包容量，且价值总和最大。
【输入形式】在屏幕上输入背包容量、物品数量、每件物品价值和重量。
【输出形式】最优解时所选物品编号。
"""
import numpy as np


def knapsack(v, w, c, n, m):
    jm = min(w[n]-1, c)
    for j in range(jm+1):
        m[n][j] = 0
    for j in range(w[n], c+1):
        m[n][j] = v[n]
    for i in range(n-1, -1, -1):
        jm = min(w[i]-1, c)
        for j in range(jm+1):
            m[i][j] = m[i+1][j]
        for k in range(w[i], c+1):
            m[i][j] = max(m[i+1][j], m[i+1][j-w[i]]+v[i])
    m[1][c] = m[2][c]
    if c > w[1]:
        m[1][c] = max(m[1][c], m[2][c-w[1]]+v[1])


def traceback(m, w, c, n, x):
    for i in range(0, n):
        if m[i][c] == m[i+1][c]:
            x[i] = 0
        else:
            x[i] = 1
            c -= w[i]
    if m[n][c] >= 0:
        x[n] = 1
    else:
        x[n] = 0


def main():
    """
    【样例输入】
10
5
6 3 5 4 6
2 2 6 5 4
    """
    c = int(input())
    n = int(input())
    w = [int(i) for i in input().split()]
    v = [int(i) for i in input().split()]
    m = np.zeros((n, c+1), dtype=np.int)
    x = np.zeros(n, dtype=np.int)
    knapsack(v, w, c, n-1, m)
    traceback(m, w, c, n-1, x)
    for i in range(n):
        if x[i] > 0:
            print(i+1, end=' ')


if __name__ == '__main__':
    main()
