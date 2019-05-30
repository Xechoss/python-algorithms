"""
【问题描述】考虑[0.0,1.2]内的函数y=f(x)=cos(x)。利用多个（2,3,4等）节点构造拉格朗日插值多项式。
【输入形式】在屏幕上依次输入在区间[0.0,1.2]内的一个值x*，构造插值多项式后求其P(x*)值，和多个节点的x坐标。
【输出形式】输出插值多项式系数矩阵，拉格朗日系数多项式矩阵和P(x*)值（保留小数点后6位有效数字）
"""
import numpy as np
import math


def lagran(x, w):
    n = len(x)
    lr = np.zeros((n, n), dtype=np.float)
    for j in range(n):
        pt = 1
        for k in range(n):
            if k == j:
                continue
            fac = x[j] - x[k]
            pt = np.polymul(pt, np.poly1d([1.0, -x[k]])) / fac
        lr[j, :] = pt
    w = np.array(w)
    c = w@lr
    print(c)
    print(lr)
    return c


def main():
    """
    【样例1输入】
    0.3
    0 1.2
    """
    a = float(input())
    x = [float(i) for i in input().split()]
    y = []
    for i in x:
        y.append(math.cos(i))
    p = lagran(x, y)
    print('P'+str(len(x)-1)+'('+str(a)+')=', end='')
    print('%.6f' % np.polyval(p, a))
    """
    【样例1输出】
    [-0.53136854  1.        ]
    [[-0.83333333  1.        ]
    [ 0.83333333  0.        ]]
    P1(0.3)=0.840589
    """


if __name__ == '__main__':
    main()