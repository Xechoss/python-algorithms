"""
【问题描述】考虑[0,4]内的函数y=f(x)=cos(x)。利用多个（2,3,4等）节点构造牛顿插值多项式。
【输入形式】在屏幕上依次输入在区间[0,4]内的一个值x*，构造插值多项式后求其P(x*)值，和多个节点的x坐标。
【输出形式】输出牛顿插值多项式系数向量，差商矩阵和P(x*)值（保留小数点后6位有效数字）。
"""
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
    print(d)
    c = d[n-1, n-1]
    for i in range(n-1, 0, -1):
        c = np.polymul(c, np.poly1d([1.0, -x[i]]))
        m = len(c)
        c[m-1] += d[i, i]
    return c


def main():
    """
    【样例1输入】
    0.3
    0 1 2 3 4
    """
    a = float(input())
    x = [float(i) for i in input().split()]
    y = []
    for i in x:
        y.append(math.cos(i))
    p = new_poly(x, y)
    print(p)
    print('%.6f' % np.polyval(p, a))
    """
    【样例1输出】
          4          3          2
-0.01466 x + 0.2345 x - 0.8493 x + 0.1697 x + 1
[[ 1.          0.          0.          0.          0.        ]
 [ 0.54030231 -0.45969769  0.          0.          0.        ]
 [-0.41614684 -0.95644914 -0.24837572  0.          0.        ]
 [-0.9899925  -0.57384566  0.19130174  0.14655916  0.        ]
 [-0.65364362  0.33634888  0.45509727  0.08793184 -0.01465683]]
P4(0.3)=0.980699
    """


if __name__ == '__main__':
    main()