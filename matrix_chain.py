"""
【问题描述】使用动态规划算法解矩阵连乘问题，具体来说就是，
依据其递归式自底向上的方式进行计算，在计算过程中，保存已子问题答案，
每个子问题只解决一次，在后面计算需要时只要简单查一下得到其结果，
从而避免大量的重复计算，最终得到多项式时间的算法。
【输入形式】在屏幕上输入矩阵连乘个数，和第1个矩阵的行数和第1个矩阵到第n个矩阵的列数，各数间都以一个空格分隔。
【输出形式】矩阵m，其中m(i,j)中存放的是：计算A[i:j](其中1<=i<=j<=n)所需的最少数乘次数。
矩阵s，其中s[i][j]记录了断开的位置，即最优的加括号方式应为(A[i:s[i][j]])*(A[s[i][j]+1:j])。
矩阵连乘A1...An的最优计算次序。
【样例输入】
 6
 30 35 15 5 10 20 25
【样例输出】
 [[    0 15750  7875  9375 11875 15125]
 [    0     0  2625  4375  7125 10500]
 [    0     0     0   750  2500  5375]
 [    0     0     0     0  1000  3500]
 [    0     0     0     0     0  5000]
 [    0     0     0     0     0     0]]
 [[0 1 1 3 3 3]
 [0 0 2 3 3 3]
 [0 0 0 3 3 3]
 [0 0 0 0 4 5]
 [0 0 0 0 0 5]
 [0 0 0 0 0 0]]
 ((A1(A2A3))((A4A5)A6))
【样例说明】
 输入：矩阵连乘个数为6，第1个矩阵的行数和第1个矩阵到第n个矩阵的列数，以空格分隔。
 输出：矩阵m，s，和矩阵连乘的最优计算次序。
"""
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
