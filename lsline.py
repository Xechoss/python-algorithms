"""
【问题描述】根据N个数据点构造最小二乘拟合直线y=ax+b。
【输入形式】在屏幕上依次输入数据点的个数N，和N对数据点的x和y坐标。
【输出形式】输出最小二乘拟合直线y=ax+b和误差。
"""
import numpy as np


def ls_line(x, y):
    xm = np.mean(x)  # 求x，y均根
    ym = np.mean(y)
    sum_x = (x - xm) @ (x - xm)
    sum_xy = (y - ym) @ (x - xm)  # 解方程
    a = sum_xy / sum_x  # 求出a
    b = ym - a * xm  # 根据y=a*x+b；求出b
    return a, b


def main():
    """
    【样例1输入】
    8
    -1 10
    0 9
    1 7
    2 5
    3 4
    4 3
    5 0
    6 -1
    """
    n = int(input())
    x = np.zeros(n, dtype=np.int)  # 初始化x, y
    y = np.zeros(n, dtype=np.int)
    for i in range(n):  # 输入x， y
        p, q = map(int, input().split())
        x[i] = p
        y[i] = q
    a, b = ls_line(x, y)
    """
    【样例1输出】
    y=-1.6071429x+8.6428571
    1.1801937
    【样例1说明】
    输入：有8对数据点，后续每行是一对数据点的x和y坐标。
    输出：最小二乘拟合直线为y=-1.6071429x+8.6428571，
    误差（norm2范数，即欧式距离）为1.1801937（保留小数点后7位有效数字）
    
    """
    print('y=', end='')
    print('%.7f' % a, end='')
    print('x+', end='')
    print('%.7f' % b)
    sumz = 0
    z = x * a + b - y
    for i in range(n):
        sumz += z[i] ** 2
    sum1 = np.sqrt(sumz)  # 求误差
    print('%.7f' % sum1)


if __name__ == '__main__':
    main()
