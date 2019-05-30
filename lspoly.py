"""
【问题描述】根据N个数据点构造最小二乘多项式拟合
【输入形式】在屏幕上依次输入数据点的个数N，和N对数据点的x和y坐标
【输出形式】输出最小二乘多项式和误差
"""
import numpy as np


def ls_poly(x, y):
    n = len(x)
    f = np.zeros((n, 3), dtype=np.float)
    for i in range(3):
        f[:, i] = x**i  # 初始化f
    a = np.transpose(f)@f
    b = np.transpose(f)@y
    c = np.linalg.inv(a)@b
    c = np.flipud(c)
    return c


def main():
    """
【样例1输入】
4
-3 3
0 1
2 1
4 3
    """
    n = int(input())
    x = np.zeros(n, dtype=np.float)  # 初始化x, y
    y = np.zeros(n, dtype=np.float)
    for i in range(n):  # 输入x， y
        p, q = map(float, input().split())
        x[i] = p
        y[i] = q
    c = ls_poly(x, y)
    print(c)
    sumz = 0
    z = 0
    for i in range(3):
        z += c[i]*x**(2-i)
    for i in range(n):
        sumz += (z[i]-y[i])**2
    sum1 = np.sqrt(sumz)  # 求误差
    print('%.7f' % sum1)
    """
【样例1输出】
[0.17846248 -0.19249542  0.85051861]
0.2445252
    """


if __name__ == '__main__':
    main()
"""
【样例1说明】输入：有4对数据点，后续每行是一对数据点的x和y坐标。
输出：最小二乘多项式为y=0.17846248x**2-0.19249542x+0.85051861，
误差（norm2范数，即欧式距离）为0.2445252（保留小数点后7位有效数字）
"""
