"""
【问题描述】利用梯形公式和连续增加的[a, b]子区间来求函数f(x)=1/x的积分近似值。
【输入形式】在屏幕上依次输入积分上限、下限和迭代次数。
【输出形式】输出使用递归梯形公式求得的积分近似值。
"""
import numpy as np


def fun(x):  # 需求积分函数
    if x != 0:  # 当x为0时会抛出异常，因此x设不为0
        return 1/x
    return 0


def rectrap(a, b, n):
    # 利用递归公式求t矩阵，公式不好注释，所以这里就没写了
    # 根据公式，推出下面的循环
    m = 1
    h = b-a  # h
    t = np.zeros((n+2, 1), dtype=np.double)  # 声明矩阵
    t[1, :] = h*(fun(a)+fun(b))/2
    for i in range(1, n+1):  # 循环求t矩阵
        m = 2*m
        h = h/2
        s = 0
        for j in range(1, m//2+1):
            x = a+h*(2*j-1)  # x变化
            s += fun(x)
        t[i+1, :] = t[i, :]/2+h*s
    print(t[1:][:])  # 打印t矩阵，不使用0行
    """
【样例1输出】
[[2.4       ]
 [1.86666667]
 [1.68333333]
 [1.62896825]]
    """


def main():
    """
【样例1输入】
1 5 3
    """
    a, b, m = map(int, input().split())  # 输入积分上限、下限和迭代次数
    rectrap(a, b, m)


if __name__ == '__main__':
    main()
    """
【样例1说明】输入：积分上限a为1、下限b为5和迭代次数n为3。输出：T(0)~T(3)的积分近似值。
    """
